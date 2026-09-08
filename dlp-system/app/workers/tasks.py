"""Celery tasks for resumable agentic scan execution."""
from app.workers.celery_app import celery_app
from app.db.session import SessionLocal
from app.services.agentic_scan_service import AgenticScanService


@celery_app.task
def scan_file_task(scan_id: int, file_path: str):
    """Compatibility task; scans now run through the agentic workflow."""
    return run_agentic_scan_task(scan_id)


@celery_app.task
def generate_report_task(scan_id: int):
    """Return the persisted report for an agentic scan."""
    db = SessionLocal()
    try:
        scan = AgenticScanService(db).repo.get_scan(scan_id)
        if not scan:
            raise ValueError("Scan not found")
        return scan.summary or {}
    finally:
        db.close()


@celery_app.task
def cleanup_old_scans_task():
    """Safe default: retain records until a retention policy is configured."""
    return {"deleted": 0, "reason": "retention policy not configured"}


@celery_app.task(
    bind=True,
    autoretry_for=(ConnectionError, TimeoutError),
    retry_backoff=True,
    retry_jitter=True,
    max_retries=3,
    name="dlp.run_agentic_scan",
)
def run_agentic_scan_task(self, scan_id: int):
    db = SessionLocal()
    try:
        scan = AgenticScanService(db).execute(scan_id)
        return {
            "scan_id": scan.id,
            "status": scan.status.value if hasattr(scan.status, "value") else str(scan.status),
        }
    finally:
        db.close()
