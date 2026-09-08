"""Scan Database Model"""
from sqlalchemy import Column, String, Integer, ForeignKey, JSON, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum

from app.models.base import BaseModel


class ScanStatus(str, enum.Enum):
    """Scan status"""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed" 
    FAILED = "failed"


class Scan(BaseModel):
    """Scan model for DLP operations""" 

    __tablename__ = "scans"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=True)
    status = Column(SQLEnum(ScanStatus), default=ScanStatus.PENDING)
    findings = Column(JSON, nullable=True)
    risk_level = Column(String(20), nullable=True)  # Low, Medium, High, Critical
    scan_result = Column(Text, nullable=True)
    error_message = Column(String(500), nullable=True)

    # Relationships
    user = relationship("User", back_populates="scans")
