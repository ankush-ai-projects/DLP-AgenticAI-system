"""User Database Model"""
from sqlalchemy import Column, String, Boolean, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum

from app.models.base import BaseModel
from app.core.constants import ROLE_USER


class UserRole(str, enum.Enum):
    """User roles"""

    ADMIN = "admin"
    USER = "user"
    AUDITOR = "auditor"


class User(BaseModel):
    """User model"""

    __tablename__ = "users"

    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    role = Column(SQLEnum(UserRole), default=UserRole.USER)

    # Relationships
    scans = relationship("Scan", back_populates="user")
