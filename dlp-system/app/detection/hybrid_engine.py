"""
app/detection/hybrid_engine.py  —  Layer 3  (Main Engine)

Yeh class dono layers ko combine karti hai:
1. Regex findings (Layer 1) + NLP findings (Layer 2) merge karo
2. Overlapping findings deduplicate karo
3. Agar dono ne same cheez pakdi toh confidence boost karo
4. Final scored list return karo

Iska output Risk Scorer aur Data Masker ko jaata hai.
"""

from typing import List, Tuple
from app.schemas.detection_schema import DetectionFinding
from app.detection.regex_detector import run_regex_detection
from app.detection.nlp_detector   import run_nlp_detection
from app.detection.validators import aadhaar_shape_valid, luhn_valid, pan_valid


# Overlap threshold: kitne characters overlap ho toh same entity maano
OVERLAP_THRESHOLD = 3


class HybridDetectionEngine:
    """
    Singleton pattern — FastAPI startup pe ek baar initialize karo.
    """

    def detect(self, text: str) -> List[DetectionFinding]:
        """
        Main entry point.

        Args:
            text: Raw input text

        Returns:
            Deduplicated, confidence-scored findings list
        """
        # ── Layer 1: Regex ─────────────────────────────────────────────
        regex_findings = run_regex_detection(text)

        # ── Layer 2: NLP/NER ───────────────────────────────────────────
        nlp_findings = run_nlp_detection(text)

        # ── Layer 3: Merge + Deduplicate ───────────────────────────────
        merged  = self._merge_findings(regex_findings, nlp_findings)
        scored  = self._apply_confidence_boost(merged)
        scored  = self._apply_deterministic_validation(scored)

        # Confidence ke basis pe sort karo (highest first)
        scored.sort(key=lambda f: f.confidence, reverse=True)

        return scored

    def _apply_deterministic_validation(
        self, findings: List[DetectionFinding]
    ) -> List[DetectionFinding]:
        validated: List[DetectionFinding] = []
        for finding in findings:
            if finding.entity_type == "CREDIT_CARD" and not luhn_valid(finding.value):
                continue
            if finding.entity_type == "PAN" and not pan_valid(finding.value):
                continue
            if finding.entity_type == "AADHAAR" and not aadhaar_shape_valid(finding.value):
                continue
            validated.append(finding)
        return validated

    # ── Private methods ───────────────────────────────────────────────

    def _merge_findings(
        self,
        regex_findings: List[DetectionFinding],
        nlp_findings:   List[DetectionFinding],
    ) -> List[DetectionFinding]:
        """
        Dono layers ke findings combine karo.
        Overlapping findings ko ek mein merge karo — source='both'.
        """
        merged: List[DetectionFinding] = []
        used_nlp_indices = set()

        for rf in regex_findings:
            overlapping_nlp = self._find_overlapping(rf, nlp_findings, used_nlp_indices)

            if overlapping_nlp is not None:
                idx, nf = overlapping_nlp
                used_nlp_indices.add(idx)

                # Dono ne pakda — merge karo
                # Regex wala value/position zyada accurate hota hai
                rf.source     = "both"
                rf.confidence = min(1.0, max(rf.confidence, nf.confidence) + 0.10)
                merged.append(rf)
            else:
                merged.append(rf)

        # Remaining NLP findings jo regex ne nahi pakde
        for i, nf in enumerate(nlp_findings):
            if i not in used_nlp_indices:
                merged.append(nf)

        return merged

    def _find_overlapping(
        self,
        target:          DetectionFinding,
        candidates:      List[DetectionFinding],
        already_used:    set,
    ) -> Tuple[int, DetectionFinding] | None:
        """
        target ke saath overlap karne wala first candidate dhundho.
        """
        if target.start_pos is None or target.end_pos is None:
            return None

        for i, c in enumerate(candidates):
            if i in already_used:
                continue
            if c.start_pos is None or c.end_pos is None:
                continue

            # Character-level overlap check
            overlap_start = max(target.start_pos, c.start_pos)
            overlap_end   = min(target.end_pos,   c.end_pos)
            overlap_len   = overlap_end - overlap_start

            if overlap_len >= OVERLAP_THRESHOLD:
                return (i, c)

        return None

    def _apply_confidence_boost(
        self,
        findings: List[DetectionFinding],
    ) -> List[DetectionFinding]:
        """
        source ke basis pe final confidence adjust karo.
        """
        for f in findings:
            if f.source == "both":
                # Dono layers agree — extra boost
                f.confidence = min(1.0, f.confidence + 0.05)
            # regex aur nlp ke base confidence already set hain detectors mein

        return findings


# ── Module-level singleton ─────────────────────────────────────────────
# FastAPI app mein: `from app.detection.hybrid_engine import engine`
engine = HybridDetectionEngine()
