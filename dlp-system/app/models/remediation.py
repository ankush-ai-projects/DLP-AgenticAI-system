"""Persistent file-remediation jobs and their approval state."""

from __future__ import annotations

import enum

from sqlalchemy import Boolean, Column, DateTime, Enum as SQLEnum, ForeignKey, Integer, JSON, String, Text

from app.models.base import BaseModel


class RemediationAction(str, enum.Enum):
    MASK = "mask"
    REDACT = "redact"
    ENCRYPT = "encrypt"
    DELETE = "delete"


class RemediationStatus(str, enum.Enum):
    AWAITING_APPROVAL = "awaiting_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"


class RemediationJob(BaseModel):
    __tablename__ = "remediation_jobs"

    scan_id = Column(Integer, ForeignKey("agentic_scans.id"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    file_path = Column(String(1000), nullable=False, index=True)
    original_sha256 = Column(String(64), nullable=False)
    action = Column(SQLEnum(RemediationAction), nullable=False, index=True)
    status = Column(
        SQLEnum(RemediationStatus),
        nullable=False,
        default=RemediationStatus.AWAITING_APPROVAL,
        index=True,
    )
    entity_types = Column(JSON, nullable=False, default=list)
    finding_indexes = Column(JSON, nullable=False, default=list)
    planner_output = Column(JSON, nullable=False, default=dict)
    preview = Column(JSON, nullable=False, default=dict)
    approval_required = Column(Boolean, nullable=False, default=True)
    admin_required = Column(Boolean, nullable=False, default=False)
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    approval_note = Column(Text, nullable=True)
    approved_at = Column(DateTime, nullable=True)
    executed_at = Column(DateTime, nullable=True)
    encrypted_backup_path = Column(String(1000), nullable=True)
    output_path = Column(String(1000), nullable=True)
    result = Column(JSON, nullable=False, default=dict)
    error_message = Column(Text, nullable=True)
