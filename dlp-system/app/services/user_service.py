"""User Service - Business logic for users"""
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password
from app.repositories.user_repo import UserRepository


class UserService:
    """Service for user operations"""

    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepository(db)

    def create_user(self, user_data: UserCreate) -> User:
        """Create a new user"""
        # Hash password
        hashed_password = hash_password(user_data.password)

        # Create user object
        db_user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
            full_name=user_data.full_name,
        )

        return self.repo.create(db_user)

    def get_user_by_id(self, user_id: int) -> User:
        """Get user by ID"""
        return self.repo.get_by_id(user_id)

    def get_user_by_username(self, username: str) -> User:
        """Get user by username"""
        return self.db.query(User).filter(User.username == username).first()

    def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        """Update user information"""
        user = self.get_user_by_id(user_id)
        if not user:
            return None

        update_data = user_data.dict(exclude_unset=True)
        return self.repo.update(user, update_data)

    def list_users(self, skip: int = 0, limit: int = 100) -> list:
        """List all users"""
        return self.repo.get_all(skip=skip, limit=limit)
