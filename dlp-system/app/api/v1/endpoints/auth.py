"""
app/api/v1/endpoints/auth.py

Login aur Register endpoints.

Flow:
  Register → user banao DB mein (password hash hota hai)
  Login    → username/password verify karo → JWT token return karo
  Token    → baaki saare endpoints mein use hoga
"""

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session        import get_db
from app.core.security     import verify_password, create_access_token
from app.core.config       import settings
from app.core.rate_limit   import limiter, AUTH_RATE_LIMIT
from app.schemas.user      import UserCreate, Token
from app.repositories.user_repo import UserRepository
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=201)
@limiter.limit(AUTH_RATE_LIMIT)
async def register(
    request: Request,
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    """
    Naya user register karo.

    Flow:
    1. Username/email already exist karta hai? → error
    2. Password hash karo (bcrypt)
    3. DB mein save karo
    4. Token return karo — seedha login ho jaata hai
    """
    repo = UserRepository(db)

    # Username already exist karta hai?
    if repo.get_by_username(user_data.username):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail      = "Username already registered hai.",
        )

    # Email already exist karta hai?
    if repo.get_by_email(user_data.email):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail      = "Email already registered hai.",
        )

    # User banao
    user = repo.create_user(
        username  = user_data.username,
        email     = user_data.email,
        password  = user_data.password,
        full_name = getattr(user_data, 'full_name', None),
    )

    # Token banao — seedha login
    token = create_access_token(
        data           = {"sub": str(user.id)},
        expires_delta  = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return {
        "message":      "User registered successfully!",
        "access_token": token,
        "token_type":   "bearer",
        "user_id":      user.id,
        "username":     user.username,
    }


@router.post("/login", response_model=Token)
@limiter.limit(AUTH_RATE_LIMIT)
async def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    Login karo — JWT token milega.

    Flow:
    1. Username se user dhundho DB mein
    2. Password verify karo (bcrypt compare)
    3. JWT token banao — user_id embed hota hai
    4. Token return karo

    Yeh token baaki endpoints mein use karo:
    Authorization: Bearer <token>
    """
    repo = UserRepository(db)

    # User dhundho
    user = repo.get_by_username(form_data.username)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail      = "Username ya password galat hai.",
            headers     = {"WWW-Authenticate": "Bearer"},
        )

    # Password verify karo
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail      = "Username ya password galat hai.",
            headers     = {"WWW-Authenticate": "Bearer"},
        )

    # Active hai?
    if not user.is_active:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail      = "Account inactive hai.",
        )

    # JWT token banao
    token = create_access_token(
        data          = {"sub": str(user.id)},
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return {
        "access_token": token,
        "token_type":   "bearer",
    }


@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user),
):
    """
    Return the authenticated user's profile.
    """
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "role": current_user.role.value if hasattr(current_user.role, "value") else current_user.role,
    }
