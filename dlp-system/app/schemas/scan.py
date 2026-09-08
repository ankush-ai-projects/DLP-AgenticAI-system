"""Scan Pydantic schemas"""
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

from app.schemas.common import TimestampedSchema


class ScanBase(BaseModel):
    """Base scan schema"""

    filename: str
    user_id: int


class ScanCreate(ScanBase):
    """Scan creation schema"""

    pass


class ScanResult(TimestampedSchema):
    """Scan result schema"""

    id: int
    user_id: int
    filename: str
    status: str
    findings: Optional[Dict[str, Any]] = None
    risk_level: Optional[str] = None
    scan_result: Optional[str] = None

    class Config:
        from_attributes = True


class Finding(BaseModel):
    """Individual finding schema"""

    pattern_type: str
    match: str
    location: int
    severity: str
