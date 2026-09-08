"""Regex Pattern Detector - Enhanced pattern detection"""
import re
from typing import List, Dict


class RegexDetector:
    """Detect sensitive patterns using regex"""

    @staticmethod
    def find_credit_cards(text: str) -> List[Dict]:
        """Find credit card numbers"""
        pattern = r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b"
        return RegexDetector._extract_matches(text, pattern, "CREDIT_CARD")

    @staticmethod
    def find_ssn(text: str) -> List[Dict]:
        """Find SSN numbers"""
        pattern = r"\b\d{3}-\d{2}-\d{4}\b"
        return RegexDetector._extract_matches(text, pattern, "SSN")

    @staticmethod
    def find_emails(text: str) -> List[Dict]:
        """Find email addresses"""
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        return RegexDetector._extract_matches(text, pattern, "EMAIL")

    @staticmethod
    def find_phone_numbers(text: str) -> List[Dict]:
        """Find phone numbers"""
        pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
        return RegexDetector._extract_matches(text, pattern, "PHONE")

    @staticmethod
    def _extract_matches(text: str, pattern: str, match_type: str) -> List[Dict]:
        """Extract regex matches from text"""
        matches = []
        for match in re.finditer(pattern, text):
            matches.append(
                {
                    "type": match_type,
                    "value": match.group(),
                    "start": match.start(),
                    "end": match.end(),
                }
            )
        return matches
