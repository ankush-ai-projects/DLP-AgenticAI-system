"""Logging Middleware"""
import logging
import re
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)
SCAN_POLL_PATH = re.compile(r"^/api/v1/agentic-scans/\d+$")


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log HTTP requests and responses"""

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        is_poll_request = (
            request.method == "GET"
            and SCAN_POLL_PATH.fullmatch(request.url.path)
        )
        log_request = logger.debug if is_poll_request else logger.info

        log_request(
            "HTTP request method=%s path=%s",
            request.method,
            request.url.path,
            extra={"client_ip": request.client.host if request.client else "unknown"},
        )

        try:
            response = await call_next(request)
        except Exception:
            logger.exception(
                "HTTP request failed method=%s path=%s",
                request.method,
                request.url.path,
            )
            raise

        # Log response
        duration = time.time() - start_time
        log_response = logger.debug if is_poll_request else logger.info
        log_response(
            "HTTP response method=%s path=%s status=%s duration=%.2fs",
            request.method,
            request.url.path,
            response.status_code,
            duration,
        )

        return response
