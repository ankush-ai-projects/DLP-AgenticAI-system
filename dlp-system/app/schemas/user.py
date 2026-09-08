"""User Pydantic schemas"""
from pydantic import BaseModel, EmailStr
from typing import Optional

from app.schemas.common import TimestampedSchema


class UserBase(BaseModel):
    """Base user schema"""

    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """User creation schema"""

    password: str


class UserUpdate(BaseModel):
    """User update schema"""

    full_name: Optional[str] = None
    email: Optional[EmailStr] = None


class User(TimestampedSchema, UserBase):
    """User response schema"""

    id: int
    is_active: bool
    role: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    """JWT token schema"""

    access_token: str
    token_type: str = "bearer"
