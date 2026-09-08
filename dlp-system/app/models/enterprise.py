"""Enterprise asset, agentic scan, review, and audit models."""
from __future__ import annotations

import enum

from sqlalchemy import Boolean, Column, Enum as SQLEnum, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class AssetType(str, enum.Enum):
    DATABASE = "database"
    SYSTEM = "system"


class AgenticScanStatus(str, enum.Enum):
    CREATED = "created"
    PLANNING = "planning"
    CONNECTING = "connecting"
    DISCOVERING = "discovering"
    SCANNING = "scanning"
    VERIFYING = "verifying"
    RISK_ANALYSIS = "risk_analysis"
    AWAITING_REVIEW = "awaiting_review"
    REPORTING = "reporting"
    COMPLETED = "completed"
    PARTIALLY_COMPLETED = "partially_completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class RunStatus(str, enum.Enum):
    STARTED = "started"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"


class ReviewStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class Asset(BaseModel):
    __tablename__ = "assets"

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    tenant_key = Column(String(80), nullable=False, default="default", index=True)
    name = Column(String(120), nullable=False)
    asset_type = Column(SQLEnum(AssetType), nullable=False, index=True)
    platform = Column(String(40), nullable=False)
    host = Column(String(255), nullable=True)
    port = Column(Integer, nullable=True)
    database_name = Column(String(255), nullable=True)
    root_path = Column(String(1000), nullable=True)
    secret_ref = Column(String(255), nullable=True)
    config = Column(JSON, nullable=False, default=dict)
    is_active = Column(Boolean, nullable=False, default=True)

    scans = relationship("AgenticScan", back_populates="asset")


class AgenticScan(BaseModel):
    __tablename__ = "agentic_scans"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False, index=True)
    goal = Column(Text, nullable=False)
    status = Column(SQLEnum(AgenticScanStatus), nullable=False, default=AgenticScanStatus.CREATED)
    plan = Column(JSON, nullable=False, default=dict)
    workflow_state = Column(JSON, nullable=False, default=dict)
    summary = Column(JSON, nullable=False, default=dict)
    iteration_count = Column(Integer, nullable=False, default=0)
    approval_required = Column(Boolean, nullable=False, default=False)
    error_message = Column(Text, nullable=True)

    asset = relationship("Asset", back_populates="scans")
    runs = relationship("AgentRun", back_populates="scan", cascade="all, delete-orphan")
    reviews = relationship("HumanReview", back_populates="scan", cascade="all, delete-orphan")
    sensitive_findings = relationship("SensitiveFinding", back_populates="scan", cascade="all, delete-orphan")


class AgentRun(BaseModel):
    __tablename__ = "agent_runs"

    scan_id = Column(Integer, ForeignKey("agentic_scans.id"), nullable=False, index=True)
    agent_name = Column(String(80), nullable=False, index=True)
    action = Column(String(120), nullable=False)
    status = Column(SQLEnum(RunStatus), nullable=False, default=RunStatus.STARTED)
    input_summary = Column(JSON, nullable=False, default=dict)
    output_summary = Column(JSON, nullable=False, default=dict)
    duration_ms = Column(Integer, nullable=True)
    error_message = Column(Text, nullable=True)

    scan = relationship("AgenticScan", back_populates="runs")


class HumanReview(BaseModel):
    __tablename__ = "human_reviews"

    scan_id = Column(Integer, ForeignKey("agentic_scans.id"), nullable=False, index=True)
    status = Column(SQLEnum(ReviewStatus), nullable=False, default=ReviewStatus.PENDING)
    reason = Column(Text, nullable=False)
    decision_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    decision_note = Column(Text, nullable=True)

    scan = relationship("AgenticScan", back_populates="reviews")


class SensitiveFinding(BaseModel):
    __tablename__ = "sensitive_findings"

    scan_id = Column(Integer, ForeignKey("agentic_scans.id"), nullable=False, index=True)
    entity_type = Column(String(60), nullable=False, index=True)
    masked_value = Column(String(255), nullable=False)
    confidence = Column(String(20), nullable=False)
    source = Column(String(40), nullable=False)
    risk_level = Column(String(20), nullable=False, index=True)
    location = Column(JSON, nullable=False, default=dict)

    scan = relationship("AgenticScan", back_populates="sensitive_findings")


class AuditEvent(BaseModel):
    __tablename__ = "audit_events"

    scan_id = Column(Integer, ForeignKey("agentic_scans.id"), nullable=True, index=True)
    actor = Column(String(120), nullable=False)
    event_type = Column(String(120), nullable=False, index=True)
    payload = Column(JSON, nullable=False, default=dict)
