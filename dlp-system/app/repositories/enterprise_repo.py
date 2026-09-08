"""Persistence boundary for enterprise assets and agentic scan runs."""
from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session

from app.models.enterprise import (
    AgentRun,
    AgenticScan,
    AgenticScanStatus,
    Asset,
    AssetType,
    AuditEvent,
    HumanReview,
    ReviewStatus,
    RunStatus,
    SensitiveFinding,
)
from app.schemas.enterprise import AssetCreate


class EnterpriseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_asset(self, owner_id: int, payload: AssetCreate) -> Asset:
        asset = Asset(owner_id=owner_id, **payload.model_dump())
        self.db.add(asset)
        self.db.commit()
        self.db.refresh(asset)
        return asset

    def create_assets(self, owner_id: int, payloads: list[AssetCreate]) -> list[Asset]:
        """Create a database selection atomically."""
        assets = [Asset(owner_id=owner_id, **payload.model_dump()) for payload in payloads]
        self.db.add_all(assets)
        self.db.commit()
        for asset in assets:
            self.db.refresh(asset)
        return assets

    def existing_database_names(
        self,
        owner_id: int,
        *,
        platform: str,
        host: str,
        port: int,
        database_names: list[str],
    ) -> set[str]:
        """Return databases already registered for the same server and owner."""
        rows = (
            self.db.query(Asset.database_name)
            .filter(
                Asset.owner_id == owner_id,
                Asset.asset_type == AssetType.DATABASE,
                Asset.platform == platform,
                Asset.host == host,
                Asset.port == port,
                Asset.database_name.in_(database_names),
            )
            .all()
        )
        return {str(row[0]) for row in rows if row[0] is not None}

    def get_asset(self, asset_id: int, owner_id: int) -> Asset | None:
        return self.db.query(Asset).filter(Asset.id == asset_id, Asset.owner_id == owner_id).first()

    def list_assets(self, owner_id: int) -> list[Asset]:
        return self.db.query(Asset).filter(Asset.owner_id == owner_id).order_by(Asset.created_at.desc()).all()

    def create_scan(self, *, user_id: int, asset_id: int, goal: str, initial_state: dict[str, Any]) -> AgenticScan:
        scan = AgenticScan(
            user_id=user_id,
            asset_id=asset_id,
            goal=goal,
            status=AgenticScanStatus.CREATED,
            workflow_state=initial_state,
        )
        self.db.add(scan)
        self.db.commit()
        self.db.refresh(scan)
        return scan

    def get_scan(self, scan_id: int, user_id: int | None = None) -> AgenticScan | None:
        query = self.db.query(AgenticScan).filter(AgenticScan.id == scan_id)
        if user_id is not None:
            query = query.filter(AgenticScan.user_id == user_id)
        return query.first()

    def save_workflow(self, scan: AgenticScan, state: dict[str, Any]) -> AgenticScan:
        scan.status = AgenticScanStatus(state["status"])
        scan.plan = state.get("plan", {})
        scan.workflow_state = state
        scan.summary = state.get("report") or state.get("risk_summary") or {}
        scan.iteration_count = state.get("iteration_count", 0)
        scan.approval_required = state.get("approval_required", False)
        errors = state.get("errors", [])
        scan.error_message = errors[-1].get("message") if errors else None
        self._replace_findings(scan.id, state.get("verified_findings", []))
        self._append_events(scan.id, state.get("events", []))
        self.db.commit()
        self.db.refresh(scan)
        return scan

    def _replace_findings(self, scan_id: int, findings: list[dict[str, Any]]) -> None:
        self.db.query(SensitiveFinding).filter(SensitiveFinding.scan_id == scan_id).delete()
        for finding in findings:
            self.db.add(
                SensitiveFinding(
                    scan_id=scan_id,
                    entity_type=finding["entity_type"],
                    masked_value=finding["masked_value"],
                    confidence=str(finding["confidence"]),
                    source=finding["source"],
                    risk_level=finding["risk_level"],
                    location=finding.get("location", {}),
                )
            )

    def _append_events(self, scan_id: int, events: list[dict[str, Any]]) -> None:
        existing = self.db.query(AgentRun).filter(AgentRun.scan_id == scan_id).count()
        for event in events[existing:]:
            status_value = event.get("status", "completed")
            run_status = RunStatus.BLOCKED if status_value == "blocked" else (
                RunStatus.FAILED if status_value == "failed" else RunStatus.COMPLETED
            )
            self.db.add(
                AgentRun(
                    scan_id=scan_id,
                    agent_name=event["agent"],
                    action=event["action"],
                    status=run_status,
                    output_summary=event.get("summary", {}),
                )
            )
            self.db.add(
                AuditEvent(
                    scan_id=scan_id,
                    actor=f"agent:{event['agent']}",
                    event_type=event["action"],
                    payload={"status": event.get("status"), **event.get("summary", {})},
                )
            )

    def ensure_pending_review(self, scan_id: int, reason: str) -> HumanReview:
        review = self.db.query(HumanReview).filter(
            HumanReview.scan_id == scan_id, HumanReview.status == ReviewStatus.PENDING
        ).first()
        if review:
            return review
        review = HumanReview(scan_id=scan_id, status=ReviewStatus.PENDING, reason=reason)
        self.db.add(review)
        self.db.commit()
        self.db.refresh(review)
        return review

    def decide_review(self, scan_id: int, *, user_id: int, approved: bool, note: str) -> HumanReview:
        review = self.db.query(HumanReview).filter(
            HumanReview.scan_id == scan_id, HumanReview.status == ReviewStatus.PENDING
        ).first()
        if not review:
            raise ValueError("Pending review not found")
        review.status = ReviewStatus.APPROVED if approved else ReviewStatus.REJECTED
        review.decision_by = user_id
        review.decision_note = note
        self.db.commit()
        self.db.refresh(review)
        return review
