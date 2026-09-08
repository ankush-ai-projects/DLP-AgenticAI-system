"""Application constants"""

# Scan Status
SCAN_STATUS_PENDING = "pending"
SCAN_STATUS_IN_PROGRESS = "in_progress"
SCAN_STATUS_COMPLETED = "completed"
SCAN_STATUS_FAILED = "failed"

# User Roles
ROLE_ADMIN = "admin"
ROLE_USER = "user"
ROLE_AUDITOR = "auditor"

# DLP Patterns
DLP_PATTERNS = {
    "CREDIT_CARD": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "PHONE": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
}

# File Upload Settings
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
ALLOWED_EXTENSIONS = {".pdf", ".txt", ".docx", ".xlsx", ".csv"}
