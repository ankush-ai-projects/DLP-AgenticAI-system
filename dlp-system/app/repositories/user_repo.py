"""
app/repositories/user_repo.py

User DB operations yahan hain.
Auth endpoint aur dependencies yahan se user fetch karte hain.
"""

from sqlalchemy.orm import Session
from typing import Optional
from app.models.user import User
from app.core.security import hash_password


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, username: str) -> Optional[User]:
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def list_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.db.query(User).order_by(User.created_at.desc()).offset(skip).limit(limit).all()

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
        full_name: str = None,
    ) -> User:
        """
        Naya user banao — password hash karke save karo.
        Plain password kabhi DB mein save nahi hota.
        """
        user = User(
            username        = username,
            email           = email,
            hashed_password = hash_password(password),
            full_name       = full_name,
            is_active       = True,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active
