"""Privacy-preserving wrapper around the hybrid detection engine."""
from __future__ import annotations

from typing import Any

from app.detection.hybrid_engine import engine
from app.detection.masker import mask_value
from app.detection.risk_scorer import assign_risk_levels


def detect_masked(text: str, location: dict[str, Any]) -> list[dict[str, Any]]:
    findings = assign_risk_levels(engine.detect(text))
    safe: list[dict[str, Any]] = []
    for finding in findings:
        safe.append(
            {
                "entity_type": finding.entity_type,
                "masked_value": mask_value(finding.entity_type, finding.value),
                "confidence": round(finding.confidence, 4),
                "source": finding.source,
                "risk_level": finding.risk_level or "low",
                "location": location,
            }
        )
    return safe
