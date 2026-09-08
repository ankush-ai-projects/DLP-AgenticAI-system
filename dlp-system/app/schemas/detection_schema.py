"""
app/schemas/detection_schema.py

Ek "finding" ka structure — har detected entity yaise dikhti hai.
Yeh model pure project mein use hota hai.
"""

from pydantic import BaseModel, Field
from typing import Optional, List


class DetectionFinding(BaseModel):
    entity_type: str = Field(
        description="PERSON | ADDRESS | AADHAAR | PAN | CREDIT_CARD | EMAIL | PHONE"
    )
    value: str = Field(
        description="Actual detected text (masking ke baad obfuscated hoga)"
    )
    confidence: float = Field(
        ge=0.0, le=1.0,
        description="0.0 to 1.0 — kitna sure hai model"
    )
    source: str = Field(
        description="'regex' | 'nlp' | 'both'"
    )
    start_pos: Optional[int] = Field(
        default=None,
        description="Character start position in original text"
    )
    end_pos: Optional[int] = Field(
        default=None,
        description="Character end position in original text"
    )
    risk_level: Optional[str] = Field(
        default=None,
        description="'low' | 'medium' | 'high' | 'critical'"
    )


class ScanRequest(BaseModel):
    text: str = Field(
        description="Scan karne wala text",
        min_length=1,
        max_length=50000
    )


class ScanResponse(BaseModel):
    total_findings: int
    risk_summary: dict
    findings: List[DetectionFinding]
    masked_text: str
