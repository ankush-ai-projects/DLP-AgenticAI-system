"""Deterministic validators used after pattern and NLP detection."""
from __future__ import annotations

import re


def digits_only(value: str) -> str:
    return re.sub(r"\D", "", value)


def luhn_valid(value: str) -> bool:
    digits = digits_only(value)
    if not 13 <= len(digits) <= 19 or len(set(digits)) == 1:
        return False
    total = 0
    parity = len(digits) % 2
    for index, char in enumerate(digits):
        number = int(char)
        if index % 2 == parity:
            number *= 2
            if number > 9:
                number -= 9
        total += number
    return total % 10 == 0


def pan_valid(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", value.strip().upper()))


def aadhaar_shape_valid(value: str) -> bool:
    digits = digits_only(value)
    return len(digits) == 12 and digits[0] in "23456789"
