"""User Endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import User
from app.core.dependencies import get_current_admin, get_current_user
from app.models.user import User as UserModel, UserRole
from app.repositories.user_repo import UserRepository

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    """Get user by ID"""
    is_admin = current_user.role == UserRole.ADMIN or str(current_user.role) == "admin"
    if current_user.id != user_id and not is_admin:
        raise HTTPException(status_code=403, detail="You can only view your own profile")
    user = UserRepository(db).get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/")
async def list_users(
    db: Session = Depends(get_db),
    current_admin: UserModel = Depends(get_current_admin),
):
    """List all users"""
    return UserRepository(db).list_users(skip=0, limit=100)
