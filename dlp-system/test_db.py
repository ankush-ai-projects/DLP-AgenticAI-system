from app.repositories.scan_repo import ScanRepository
from app.db.session import get_db

print("Functions check:")
print("create_scan:", hasattr(ScanRepository, 'create_scan'))
print("save_results:", hasattr(ScanRepository, 'save_results'))
print("mark_failed:", hasattr(ScanRepository, 'mark_failed'))

db = next(get_db())
repo = ScanRepository(db)
scan = repo.create_scan(user_id=1, filename="test_scan")
print("Scan ID:", scan.id)
print("Status:", scan.status)