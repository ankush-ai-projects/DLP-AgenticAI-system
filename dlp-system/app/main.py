"""FastAPI application factory.

This is the actual importable entrypoint (`app.main:app`) that the
Dockerfile and any WSGI/ASGI host should point at. Previously the only
`main.py` lived at the repo root, outside this package, and did sys.path
surgery to import `app.*` -- that only worked when running from the repo
root directly (`python main.py`) and had no bearing on the Docker image,
where `app/` is copied to `/app/app/` and `uvicorn app.main:app` was being
invoked against a module that did not exist. That repo-root main.py now
just re-exports `app` from here for local-dev convenience.
"""
from __future__ import annotations

import logging
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.api.v1.api_router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.rate_limit import limiter
from app.db.session import engine
from app.middleware.logging_middleware import LoggingMiddleware
from app.models.base import Base
from app.workflows.langgraph_runtime import (
    close_langgraph_runtime,
    get_langgraph_runtime,
)

setup_logging()
logger = logging.getLogger(__name__)


def _validate_production_safety() -> None:
    """Fail fast on the two most common "worked in dev, insecure in prod"
    misconfigurations, instead of silently starting up unsafe.

    Both checks are gated on `settings.is_production` so local dev and CI
    (which reasonably use the insecure defaults) are unaffected.
    """
    if not settings.is_production:
        return

    problems = []
    if settings.has_insecure_secret_key:
        problems.append(
            "SECRET_KEY is the insecure default (or under 32 chars). "
            "Set a real random SECRET_KEY (e.g. `openssl rand -hex 32`)."
        )
    if "*" in settings.ALLOWED_ORIGINS:
        problems.append(
            "ALLOWED_ORIGINS contains '*' in production. Browsers reject "
            "wildcard origins on credentialed requests anyway, and it "
            "defeats CORS entirely for this API's cookie/token auth. "
            "Set explicit origin(s), e.g. https://app.example.com."
        )
    if settings.SKIP_AUTH:
        problems.append(
            "SKIP_AUTH is true in production. This disables login "
            "entirely and serves every request as a single shared dev "
            "user -- set SKIP_AUTH=false before deploying."
        )
    if settings.SYSTEM_SCAN_ALLOW_ANY_PATH:
        problems.append(
            "SYSTEM_SCAN_ALLOW_ANY_PATH is true in production. This "
            "allows a scan against any filesystem path with no "
            "allowlist at all -- set it to false and configure "
            "SYSTEM_SCAN_ALLOWED_ROOTS with specific real paths before "
            "deploying."
        )
    if problems:
        raise RuntimeError(
            "Refusing to start in production with unsafe configuration:\n- "
            + "\n- ".join(problems)
        )


_validate_production_safety()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown."""

    Base.metadata.create_all(bind=engine)
    get_langgraph_runtime()

    logger.info("Application started (environment=%s)", settings.ENVIRONMENT)

    yield

    close_langgraph_runtime()

    logger.info("Application shutting down")


app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    lifespan=lifespan,
    # Don't expose interactive API docs in production -- they're a free
    # map of every endpoint/schema for an attacker, and there's no
    # reason an internal-tool DLP API needs them public.
    docs_url="/docs" if not settings.is_production else None,
    redoc_url="/redoc" if not settings.is_production else None,
    openapi_url="/openapi.json" if not settings.is_production else None,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)
app.include_router(api_router)


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """Catch anything that escapes every route handler.

    Without this, FastAPI's default behavior for an uncaught exception is
    a bare 500 with (in some configurations) a raw traceback -- fine for
    local dev, a real information disclosure risk in production. This logs
    the full exception server-side with a request ID for correlation, and
    returns only that request ID to the client.
    """
    request_id = str(uuid.uuid4())
    logger.exception(
        "Unhandled exception on %s %s [request_id=%s]",
        request.method,
        request.url.path,
        request_id,
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Internal server error.",
            "request_id": request_id,
        },
    )


@app.get("/")
async def root():
    """Return the API health message."""

    return {
        "message": "DLP System API",
    }