"""Short-term cross-scan memory for the planner.

Agentic (as opposed to purely reactive) planning benefits from knowing what
happened last time this asset was scanned. ScanMemoryStore persists a small,
PII-free summary after every scan and lets the planner recall the last N
summaries for the same asset before it plans the next one.
"""
from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session

from app.agents.state import WorkflowState
from app.models.memory import ScanMemory


class ScanMemoryStore:
    def __init__(self, db: Session):
        self.db = db

    def recall(self, asset_id: int, limit: int = 3) -> list[dict[str, Any]]:
        """Return the last `limit` scan summaries for this asset, newest first."""
        rows = (
            self.db.query(ScanMemory)
            .filter(ScanMemory.asset_id == asset_id)
            .order_by(ScanMemory.created_at.desc())
            .limit(limit)
            .all()
        )
        return [
            {
                "scan_id": row.scan_id,
                "highest_risk": row.highest_risk,
                "entity_type_counts": row.entity_type_counts or {},
                "verified_finding_count": row.verified_finding_count,
                "planner_source": row.planner_source,
                "created_at": row.created_at.isoformat(),
            }
            for row in rows
        ]

    def remember(self, asset_id: int, state: WorkflowState) -> ScanMemory:
        """Persist a compact summary of a just-completed scan."""
        counts: dict[str, int] = {}
        for finding in state.verified_findings:
            entity_type = finding.get("entity_type", "UNKNOWN")
            counts[entity_type] = counts.get(entity_type, 0) + 1

        row = ScanMemory(
            asset_id=asset_id,
            asset_type=state.asset.get("asset_type", "unknown"),
            scan_id=state.scan_id,
            highest_risk=state.risk_summary.get("level"),
            entity_type_counts=counts,
            verified_finding_count=len(state.verified_findings),
            planner_source=state.plan.get("planner_source"),
        )
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return row


def summarize_for_prompt(memories: list[dict[str, Any]]) -> str:
    """Render recalled memory as a short, prompt-safe context string.

    Only counts and risk labels ever appear here -- never raw values -- so
    this is safe to pass to an LLM even though it is "memory of a scan".
    """
    if not memories:
        return "No prior scans recorded for this asset."
    lines = []
    for memory in memories:
        top_entities = ", ".join(
            f"{k}={v}" for k, v in sorted(
                memory["entity_type_counts"].items(), key=lambda kv: -kv[1]
            )[:3]
        ) or "none"
        lines.append(
            f"- scan {memory['scan_id']}: risk={memory['highest_risk']}, "
            f"verified_findings={memory['verified_finding_count']}, top_entities=({top_entities})"
        )
    return "Prior scans on this asset (most recent first):\n" + "\n".join(lines)
