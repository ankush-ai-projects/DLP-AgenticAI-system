"""Persistent short-term memory of past scan outcomes, keyed by asset.

This gives the planner cross-scan context (e.g. "last scan on this asset
found 12 CRITICAL findings in the billing table") without re-scanning or
re-reading full history. Only compact summaries are stored -- never raw
findings or PII -- so this stays safe to feed back into an LLM prompt.
"""
from sqlalchemy import Column, DateTime, Integer, JSON, String
from datetime import datetime, timezone

from app.models.base import Base


class ScanMemory(Base):
    """One compact summary row per completed scan, for planner recall."""

    __tablename__ = "scan_memory"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, index=True, nullable=False)
    asset_type = Column(String(50), nullable=False)
    scan_id = Column(Integer, nullable=True)
    highest_risk = Column(String(20), nullable=True)  # low/medium/high/critical
    entity_type_counts = Column(JSON, default=dict)   # {"CREDIT_CARD": 3, "SSN": 1}
    verified_finding_count = Column(Integer, default=0)
    planner_source = Column(String(30), nullable=True)  # llm | deterministic_fallback
    created_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
