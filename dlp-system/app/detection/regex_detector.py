"""
app/detection/regex_detector.py  —  Layer 1

Structured PII detect karta hai: Aadhaar, PAN, Credit Card, Email, Phone.
Pattern match = high confidence (0.92-0.97).
"""

import re
from typing import List
from app.schemas.detection_schema import DetectionFinding

# ── Patterns ──────────────────────────────────────────────────────────
PATTERNS = {
    "AADHAAR": (
        r"\b[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}\b",
        0.97,
    ),
    "PAN": (
        r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b",
        0.97,
    ),
    "CREDIT_CARD": (
        r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b",
        0.95,
    ),
    "EMAIL": (
        r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b",
        0.95,
    ),
    "PHONE": (
        r"\b(?:\+91[\-\s]?)?[6-9][0-9]{9}\b",
        0.92,
    ),
}


def run_regex_detection(text: str) -> List[DetectionFinding]:
    """
    Text mein saare structured PII patterns dhundho.
    Returns: list of DetectionFinding
    """
    findings: List[DetectionFinding] = []

    for entity_type, (pattern, base_confidence) in PATTERNS.items():
        for match in re.finditer(pattern, text):
            findings.append(
                DetectionFinding(
                    entity_type=entity_type,
                    value=match.group(),
                    confidence=base_confidence,
                    source="regex",
                    start_pos=match.start(),
                    end_pos=match.end(),
                    risk_level=None,
                )
            )

    return findings
