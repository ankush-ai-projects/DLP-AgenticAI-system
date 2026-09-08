"""Scan Service - Business logic for DLP scanning"""
from sqlalchemy.orm import Session
from typing import Dict, List

from app.models.scan import Scan, ScanStatus
from app.schemas.scan import ScanCreate
from app.repositories.scan_repo import ScanRepository
from app.services.risk_engine import RiskEngine


class ScanService:
    """Service for scan operations"""

    def __init__(self, db: Session):
        self.db = db
        self.repo = ScanRepository(db)
        self.risk_engine = RiskEngine()

    def create_scan(self, scan_data: ScanCreate) -> Scan:
        """Create a new scan"""
        db_scan = Scan(
            user_id=scan_data.user_id, filename=scan_data.filename, status=ScanStatus.PENDING
        )
        return self.repo.create(db_scan)

    def start_scan(self, scan_id: int, file_content: str) -> Scan:
        """Start scanning a file"""
        scan = self.repo.get_by_id(scan_id)
        if not scan:
            return None

        # Update status
        scan.status = ScanStatus.IN_PROGRESS
        self.db.commit()

        # Analyze content
        findings = self.risk_engine.analyze(file_content)
        risk_level = self.risk_engine.calculate_risk_level(findings)

        # Update scan results
        scan.findings = findings
        scan.risk_level = risk_level
        scan.status = ScanStatus.COMPLETED

        return self.repo.update(scan, {})

    def get_scan_by_id(self, scan_id: int) -> Scan:
        """Get scan by ID"""
        return self.repo.get_by_id(scan_id)

    def list_scans_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Scan]:
        """List all scans for a user"""
        return (
            self.db.query(Scan)
            .filter(Scan.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
