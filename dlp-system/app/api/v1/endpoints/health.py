"""Health Check Endpoints.

Two separate endpoints because they answer different questions for an
orchestrator (Docker healthcheck, Kubernetes liveness/readiness probes):

- /health       -- "is the process alive" -- must stay fast and dependency-
                   free, or a slow DB briefly makes the orchestrator kill a
                   perfectly healthy process.
- /health/ready -- "can this instance actually serve traffic" -- checks the
                   database connection so a load balancer can route around
                   an instance that's up but can't reach its DB.
"""
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    """Liveness probe. No dependency checks -- must always be cheap."""
    return {"status": "healthy"}


@router.get("/health/ready")
async def readiness_check(db: Session = Depends(get_db)):
    """Readiness probe. Returns HTTP 503 if the DB is unreachable, so a
    load balancer or Kubernetes readiness probe (which key off status code,
    not body content) correctly routes traffic away from this instance."""
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ready", "database": "ok"}
    except Exception as exc:  # noqa: BLE001 -- any DB failure means "not ready"
        return JSONResponse(
            status_code=503,
            content={"status": "not_ready", "database": f"unreachable: {type(exc).__name__}"},
        )
