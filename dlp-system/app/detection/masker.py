"""
app/detection/masker.py

Detected PII ko text mein mask karta hai before display.
Architecture doc mein: "4111-XXXX-XXXX-9012 — obfuscated before any display"
"""

from typing import List
from app.schemas.detection_schema import DetectionFinding


# ── Masking rules per entity type ────────────────────────────────────
def _mask_value(entity_type: str, value: str) -> str:
    """
    Entity type ke hisaab se appropriate masking apply karo.
    """
    if entity_type == "AADHAAR":
        # Sirf last 4 digits dikhao: XXXX XXXX 9012
        parts = value.split()
        if len(parts) == 3:
            return f"XXXX XXXX {parts[-1]}"
        return "XXXX XXXX XXXX"

    elif entity_type == "PAN":
        # Middle hide karo: ABXXX1234F
        if len(value) == 10:
            return f"{value[:2]}XXXXX{value[7:]}"
        return "XXXXXXXXXX"

    elif entity_type == "CREDIT_CARD":
        # Industry standard: first 4 + last 4
        digits = value.replace("-", "").replace(" ", "")
        if len(digits) >= 8:
            return f"{digits[:4]}-XXXX-XXXX-{digits[-4:]}"
        return "XXXX-XXXX-XXXX-XXXX"

    elif entity_type == "EMAIL":
        # user@domain.com → u***@domain.com
        if "@" in value:
            local, domain = value.split("@", 1)
            masked_local = local[0] + "***" if local else "***"
            return f"{masked_local}@{domain}"
        return "***@***.***"

    elif entity_type == "PHONE":
        # +91-9876543210 → +91-XXXXX43210
        digits_only = "".join(filter(str.isdigit, value))
        if len(digits_only) >= 4:
            return "XXXXX" + digits_only[-4:]
        return "XXXXXXXXXX"

    elif entity_type == "PERSON":
        # Rahul Sharma → R***** S*****
        words = value.split()
        return " ".join(w[0] + "*" * (len(w) - 1) if w else "" for w in words)

    elif entity_type == "ADDRESS":
        # Partial masking
        words = value.split()
        if len(words) <= 3:
            return "*" * len(value)
        # First word raho, baaki mask
        return words[0] + " " + "X" * (len(value) - len(words[0]) - 1)

    else:
        # Generic masking
        return "*" * len(value)


def mask_value(entity_type: str, value: str) -> str:
    """Public single-value masking API used by scanners and reports."""
    return _mask_value(entity_type, value)


def mask_text(original_text: str, findings: List[DetectionFinding]) -> str:
    """
    Original text mein saare findings ko mask karo.
    Position-based replacement — overlapping findings handle hoti hain.

    Args:
        original_text: Original scan text
        findings:      Hybrid engine ke findings (with positions)

    Returns:
        Masked text string
    """
    if not findings:
        return original_text

    # Position ke basis pe sort karo (reverse order — end se start)
    # Taaki positions shift na ho jab replace karte hain
    sortable = [
        f for f in findings
        if f.start_pos is not None and f.end_pos is not None
    ]
    sortable.sort(key=lambda f: f.start_pos, reverse=True)  # type: ignore

    result = original_text
    for f in sortable:
        masked_val = _mask_value(f.entity_type, f.value)
        result = result[: f.start_pos] + masked_val + result[f.end_pos :]

    return result
