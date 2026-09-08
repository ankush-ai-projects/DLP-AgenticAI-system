"""Risk Engine - Core DLP pattern detection and risk calculation"""
import re
from typing import Dict, List
from app.core.constants import DLP_PATTERNS


class RiskEngine:
    """Engine for detecting sensitive patterns and calculating risk"""

    def __init__(self):
        self.patterns = DLP_PATTERNS
        self.severity_scores = {
            "CREDIT_CARD": 10,
            "SSN": 9,
            "EMAIL": 2,
            "PHONE": 3,
        }

    def analyze(self, content: str) -> Dict:
        """Analyze content for sensitive patterns"""
        findings = {}

        for pattern_name, pattern in self.patterns.items():
            matches = re.finditer(pattern, content)
            pattern_findings = []

            for match in matches:
                pattern_findings.append(
                    {
                        "match": match.group(),
                        "position": match.start(),
                        "severity": self._get_severity(pattern_name),
                    }
                )

            if pattern_findings:
                findings[pattern_name] = pattern_findings

        return findings

    def _get_severity(self, pattern_name: str) -> str:
        """Get severity level for a pattern"""
        score = self.severity_scores.get(pattern_name, 1)

        if score >= 8:
            return "CRITICAL"
        elif score >= 5:
            return "HIGH"
        elif score >= 3:
            return "MEDIUM"
        else:
            return "LOW"

    def calculate_risk_level(self, findings: Dict) -> str:
        """Calculate overall risk level based on findings"""
        if not findings:
            return "LOW"

        max_severity = 0
        for pattern_findings in findings.values():
            for finding in pattern_findings:
                severity = self.severity_scores.get(
                    self._find_pattern_name(finding), 1
                )
                max_severity = max(max_severity, severity)

        if max_severity >= 8:
            return "CRITICAL"
        elif max_severity >= 5:
            return "HIGH"
        elif max_severity >= 3:
            return "MEDIUM"
        else:
            return "LOW"

    def _find_pattern_name(self, finding: Dict) -> str:
        """Find pattern name from finding"""
        # This is a helper method - would need additional context in real implementation
        return "UNKNOWN"
