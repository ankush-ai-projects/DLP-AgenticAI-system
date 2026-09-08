"""
app/detection/risk_scorer.py

Entity type + confidence ke basis pe risk level assign karta hai.
Logic:
  - AADHAAR / PAN / CREDIT_CARD = high-value data → threshold kam
  - PERSON / ADDRESS = medium sensitivity
  - EMAIL / PHONE = lower sensitivity
"""

from typing import List
from app.schemas.detection_schema import DetectionFinding

# Entity sensitivity and detector confidence are separate concepts. A highly
# confident email match is still not as severe as a validated payment card.
BASE_RISK = {
    "CREDIT_CARD": "critical",
    "AADHAAR": "high",
    "PAN": "high",
    "ADDRESS": "medium",
    "PHONE": "medium",
    "PERSON": "medium",
    "EMAIL": "low",
}
RISK_ORDER = ["low", "medium", "high", "critical"]


def _get_risk_level(entity_type: str, confidence: float) -> str:
    base = BASE_RISK.get(entity_type, "medium")
    if confidence < 0.50:
        return "low"
    if confidence < 0.75:
        return RISK_ORDER[max(0, RISK_ORDER.index(base) - 1)]
    return base


def assign_risk_levels(findings: List[DetectionFinding]) -> List[DetectionFinding]:
    """
    Har finding ko risk level assign karo.
    In-place modify karta hai aur return karta hai.
    """
    for f in findings:
        f.risk_level = _get_risk_level(f.entity_type, f.confidence)
    return findings


def build_risk_summary(findings: List[DetectionFinding]) -> dict:
    """
    Ek scan ke saare findings ka risk summary banao.
    Frontend dashboard ke liye useful.
    """
    summary = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    entity_counts = {}

    for f in findings:
        level = f.risk_level or "low"
        summary[level] = summary.get(level, 0) + 1
        entity_counts[f.entity_type] = entity_counts.get(f.entity_type, 0) + 1

    return {
        "by_level":       summary,
        "by_entity_type": entity_counts,
        "total":          len(findings),
        "has_critical":   summary["critical"] > 0,
    }
