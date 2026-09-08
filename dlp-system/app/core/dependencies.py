"""
app/core/dependencies.py

Yeh file FastAPI ka dependency injection use karti hai.
Har protected endpoint mein Depends(get_current_user) lagao —
FastAPI automatically token verify karega aur user return karega.

Flow:
  Request aata hai JWT token ke saath (Authorization header)
       ↓
  get_current_user() call hota hai automatically
       ↓
  Token decode hota hai → user_id nikalta hai
       ↓
  DB se user fetch hota hai
       ↓
  Endpoint ko real User object milta hai

TEMPORARY (settings.SKIP_AUTH): jab true hai, upar wala poora token flow
skip ho jaata hai aur ek single "dev user" (DB mein auto-create/reuse)
har request ke liye return hota hai -- bina login ke saare scans
(DB scanner, system scanner) chalte hain. Set SKIP_AUTH=false env var
(ya .env se hatao) taaki wapas real JWT-based login required ho jaaye.
"""

import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.core.security import decode_token
from app.models.user import User
from app.repositories.user_repo import UserRepository

# auto_error=False -- with SKIP_AUTH on, requests won't carry a token at
# all, and OAuth2PasswordBearer's default behavior is to raise 401 itself
# before get_current_user() below ever runs. With SKIP_AUTH off, missing
# tokens are still rejected -- just explicitly, in get_current_user().
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login", auto_error=False
)

_DEV_USER_USERNAME = "dev-user"
_DEV_USER_EMAIL = "dev-user@local.invalid"


def _get_or_create_dev_user(db: Session) -> User:
    """Single shared user used for every request while SKIP_AUTH=true.

    Created once, reused after -- has a random unguessable password since
    nothing ever logs in as this user through /auth/login; it exists only
    so downstream code that expects a real `User` (created_by fields,
    audit events, etc.) keeps working unchanged.
    """
    repo = UserRepository(db)
    user = repo.get_by_username(_DEV_USER_USERNAME)
    if user:
        return user

    return repo.create_user(
        username=_DEV_USER_USERNAME,
        email=_DEV_USER_EMAIL,
        password=secrets.token_urlsafe(32),
        full_name="Development User (SKIP_AUTH enabled)",
    )


def get_current_user(
    token: str | None = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """
    JWT token se current user nikalo.
    Har protected endpoint mein yeh automatically call hota hai.

    Agar token:
    - Missing hai     → 401 Unauthorized
    - Expired hai     → 401 Unauthorized
    - User nahi mila  → 401 Unauthorized
    - Inactive user   → 400 Bad Request
    """
    if settings.SKIP_AUTH:
        return _get_or_create_dev_user(db)

    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail      = "Token invalid ya expired hai. Dobara login karo.",
        headers     = {"WWW-Authenticate": "Bearer"},
    )

    if not token:
        raise credentials_exception

    # Token decode karo
    payload = decode_token(token)
    if not payload:
        raise credentials_exception

    # user_id nikalo token se
    user_id: int = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    # DB se user fetch karo
    repo = UserRepository(db)
    user = repo.get_by_id(int(user_id))
    if not user:
        raise credentials_exception

    # Active hai ya nahi check karo
    if not user.is_active:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail      = "User inactive hai.",
        )

    return user


def get_current_admin(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Sirf admin users ke liye — role check karta hai.
    Admin-only endpoints mein use karo.
    """
    if current_user.role != "admin":
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail      = "Admin access chahiye.",
        )
    return current_user
