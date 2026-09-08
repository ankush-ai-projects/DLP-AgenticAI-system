"""Shared rate limiter for brute-force protection.

Login and registration are the two endpoints an attacker can hammer
without needing a valid token first, so they're the ones that need a
limit. Keyed by client IP; swap `key_func` for a header-based key if this
sits behind a proxy that doesn't forward the real client IP.
"""
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.core.config import settings

limiter = Limiter(key_func=get_remote_address)

AUTH_RATE_LIMIT = (
    f"{settings.AUTH_RATE_LIMIT_ATTEMPTS}/{settings.AUTH_RATE_LIMIT_WINDOW_SECONDS}seconds"
)
