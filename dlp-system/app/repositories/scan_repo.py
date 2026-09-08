"""Scan Repository - Database abstraction for scans"""
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import Optional, List
from app.models.scan import Scan, ScanStatus


class ScanRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, scan: Scan) -> Scan:
        self.db.add(scan)
        self.db.commit()
        self.db.refresh(scan)
        return scan

    def get_by_id(self, scan_id: int) -> Optional[Scan]:
        return self.db.query(Scan).filter(Scan.id == scan_id).first()

    def update(self, scan: Scan, update_data: dict) -> Scan:
        for field, value in update_data.items():
            if hasattr(scan, field):
                setattr(scan, field, value)
        self.db.commit()
        self.db.refresh(scan)
        return scan

    def delete(self, scan_id: int) -> bool:
        scan = self.get_by_id(scan_id)
        if scan:
            self.db.delete(scan)
            self.db.commit()
            return True
        return False

    def get_by_user_id(self, user_id: int, skip: int = 0, limit: int = 100) -> list:
        return (
            self.db.query(Scan)
            .filter(Scan.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    # ── DLP functions ─────────────────────────────────────────────────

    def create_scan(self, user_id: int, filename: str, file_path: Optional[str] = None) -> Scan:
        """
        Naya scan record PENDING status ke saath banao.
        Endpoint pe request aate hi sabse pehle yeh call hota hai.
        DB mein ek row insert hoti hai — baad mein update hogi.
        """
        scan = Scan(
            user_id   = user_id,
            filename  = filename,
            file_path = file_path,
            status    = ScanStatus.PENDING,
        )
        return self.create(scan)

    def mark_in_progress(self, scan_id: int) -> Optional[Scan]:
        """
        Detection engine shuru hone pe status update karo.
        Isse pata chalta hai scan chal raha hai — stuck nahi hai.
        """
        scan = self.get_by_id(scan_id)
        if scan:
            return self.update(scan, {"status": ScanStatus.IN_PROGRESS})
        return None

    def save_results(self, scan_id: int, findings: list, risk_summary: dict, masked_text: str) -> Optional[Scan]:
        """
        Detection complete hone pe sab DB mein save karo.
        findings → JSONB column mein store hoga
        risk_level → sabse high risk jo mila
        scan_result → masked text
        status → completed
        """
        scan = self.get_by_id(scan_id)
        if not scan:
            return None

        return self.update(scan, {
            "status":      ScanStatus.COMPLETED,
            "findings":    _serialize_findings(findings),
            "risk_level":  _get_overall_risk(findings),
            "scan_result": masked_text,
        })

    def mark_failed(self, scan_id: int, error: str) -> Optional[Scan]:
        """
        Koi error aaye toh FAILED mark karo.
        Error message DB mein save hoga debugging ke liye.
        """
        scan = self.get_by_id(scan_id)
        if scan:
            return self.update(scan, {
                "status":        ScanStatus.FAILED,
                "error_message": error[:500],
            })
        return None

    def get_by_user_scans(self, user_id: int, limit: int = 20) -> List[Scan]:
        """User ke saare scans — latest pehle."""
        return (
            self.db.query(Scan)
            .filter(Scan.user_id == user_id)
            .order_by(desc(Scan.created_at))
            .limit(limit)
            .all()
        )


# ── Helpers ───────────────────────────────────────────────────────────

def _serialize_findings(findings: list) -> list:
    result = []
    for f in findings:
        result.append({
            "entity_type": f.entity_type,
            "value":       f.value,
            "confidence":  round(float(f.confidence), 4),
            "source":      f.source,
            "start_pos":   f.start_pos,
            "end_pos":     f.end_pos,
            "risk_level":  f.risk_level,
        })
    return result


def _get_overall_risk(findings: list) -> str:
    priority = {"critical": 4, "high": 3, "medium": 2, "low": 1}
    best = "low"
    for f in findings:
        level = f.risk_level or "low"
        if priority.get(level, 0) > priority.get(best, 0):
            best = level
    return best