"""User-scoped dashboard analytics for system and database scans."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timedelta, timezone
from typing import Any, Literal

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload

from app.core.dependencies import get_current_user
from app.db.session import get_db
from app.models.enterprise import AgenticScan, AgenticScanStatus, Asset, AssetType
from app.models.user import User


router = APIRouter(prefix="/dashboard", tags=["dashboard"])

TERMINAL_STATUSES = {
    AgenticScanStatus.COMPLETED.value,
    AgenticScanStatus.PARTIALLY_COMPLETED.value,
    AgenticScanStatus.AWAITING_REVIEW.value,
    AgenticScanStatus.FAILED.value,
    AgenticScanStatus.CANCELLED.value,
}

RISK_ORDER = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}


def enum_value(value: Any) -> str:
    """Return the serialized value for either an Enum or a plain string."""
    return value.value if hasattr(value, "value") else str(value)


def scan_findings(scan: AgenticScan) -> list[dict[str, Any]]:
    """Return persisted verified findings, with workflow-state fallback."""
    if scan.sensitive_findings:
        return [
            {
                "entity_type": finding.entity_type,
                "risk_level": finding.risk_level,
                "masked_value": finding.masked_value,
            }
            for finding in scan.sensitive_findings
        ]

    workflow_state = scan.workflow_state or {}
    verified = workflow_state.get("verified_findings") or []
    detected = workflow_state.get("findings") or []
    report_findings = (workflow_state.get("report") or {}).get("findings") or []

    return verified or report_findings or detected


def highest_risk(findings: list[dict[str, Any]], workflow_state: dict) -> str:
    """Resolve the highest finding risk for one scan."""
    configured_level = (workflow_state.get("risk_summary") or {}).get("level")
    levels = [
        str(finding.get("risk_level", "low")).lower()
        for finding in findings
    ]

    if configured_level:
        levels.append(str(configured_level).lower())

    return max(levels or ["low"], key=lambda level: RISK_ORDER.get(level, 0))


def iso_datetime(value: datetime | None) -> str | None:
    """Serialize database datetimes consistently."""
    if value is None:
        return None

    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)

    return value.isoformat()


@router.get("/summary")
def dashboard_summary(
    asset_type: Literal["system", "database"] = Query(default="system"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Aggregate all persisted scan results for one dashboard type."""
    selected_type = AssetType(asset_type)
    scans = (
        db.query(AgenticScan)
        .join(Asset, AgenticScan.asset_id == Asset.id)
        .options(
            joinedload(AgenticScan.asset),
            joinedload(AgenticScan.sensitive_findings),
        )
        .filter(
            AgenticScan.user_id == current_user.id,
            Asset.asset_type == selected_type,
        )
        .order_by(AgenticScan.updated_at.desc())
        .all()
    )

    status_counts: Counter[str] = Counter()
    entity_counts: Counter[str] = Counter()
    risk_counts: Counter[str] = Counter(
        {"critical": 0, "high": 0, "medium": 0, "low": 0}
    )
    findings_by_scan: dict[int, list[dict[str, Any]]] = {}

    for scan in scans:
        status_counts[enum_value(scan.status)] += 1
        findings = scan_findings(scan)
        findings_by_scan[scan.id] = findings

        for finding in findings:
            entity_type = str(finding.get("entity_type") or "UNKNOWN").upper()
            risk_level = str(finding.get("risk_level") or "low").lower()
            entity_counts[entity_type] += 1
            risk_counts[risk_level] += 1

    total_findings = sum(entity_counts.values())
    incidents = risk_counts["critical"] + risk_counts["high"]
    monitored_assets = len({scan.asset_id for scan in scans})
    active_scans = sum(
        count
        for status, count in status_counts.items()
        if status not in TERMINAL_STATUSES
    )

    today = datetime.now(timezone.utc).date()
    trend_dates = [today - timedelta(days=offset) for offset in range(6, -1, -1)]
    trend_counts = {trend_date: 0 for trend_date in trend_dates}

    for scan in scans:
        if enum_value(scan.status) not in TERMINAL_STATUSES or scan.updated_at is None:
            continue

        scan_date = scan.updated_at.date()
        if scan_date in trend_counts:
            trend_counts[scan_date] += len(findings_by_scan[scan.id])

    recent_scans = []
    for scan in scans[:8]:
        findings = findings_by_scan[scan.id]
        workflow_state = scan.workflow_state or {}
        recent_scans.append(
            {
                "scan_id": scan.id,
                "asset_name": scan.asset.name if scan.asset else "Unknown asset",
                "platform": scan.asset.platform if scan.asset else "unknown",
                "status": enum_value(scan.status),
                "data_found": len(findings),
                "risk_level": highest_risk(findings, workflow_state),
                "error": scan.error_message,
                "updated_at": iso_datetime(scan.updated_at),
            }
        )

    return {
        "asset_type": asset_type,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "metrics": {
            "total_findings": total_findings,
            "incidents": incidents,
            "total_scans": len(scans),
            "completed_scans": status_counts[AgenticScanStatus.COMPLETED.value],
            "partial_scans": status_counts[
                AgenticScanStatus.PARTIALLY_COMPLETED.value
            ],
            "failed_scans": status_counts[AgenticScanStatus.FAILED.value],
            "active_scans": active_scans,
            "monitored_assets": monitored_assets,
        },
        "risk_counts": {
            level: risk_counts[level]
            for level in ("critical", "high", "medium", "low")
        },
        "entity_counts": [
            {"entity_type": entity_type, "count": count}
            for entity_type, count in entity_counts.most_common()
        ],
        "status_counts": dict(status_counts),
        "findings_trend": [
            {
                "date": trend_date.isoformat(),
                "label": trend_date.strftime("%d %b"),
                "value": trend_counts[trend_date],
            }
            for trend_date in trend_dates
        ],
        "recent_scans": recent_scans,
    }  