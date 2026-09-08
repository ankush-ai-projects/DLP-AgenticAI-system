# Agentic File Remediation

SentinelDLP supports four bounded system-file actions:

- `mask`: replaces verified raw values with entity-aware masked values.
- `redact`: replaces verified raw values with `[REDACTED]` or permanent PDF redactions.
- `encrypt`: creates a Fernet-encrypted `.dlp.enc` container and removes the source after backup.
- `delete`: admin-only removal with an encrypted recovery copy retained for the configured period.

## Safety workflow

```text
Verified scan findings
-> masked-metadata AI/deterministic plan
-> preview
-> human approval
-> allowlist + SHA-256 precondition
-> encrypted backup
-> bounded file tool
-> verification re-scan
-> audit event
```

The planner never receives raw PII/PCI values. The executor detects raw values only inside the
local process and never persists them in the remediation job or audit event.

## Configuration

Add these values to `dlp-system/.env`:

```env
SYSTEM_SCAN_ALLOWED_ROOTS=D:\pii_pci_all_files
REMEDIATION_BACKUP_ROOT=D:\DLP\remediation_backups
REMEDIATION_MASTER_KEY=replace-with-a-separate-long-random-remediation-key
REMEDIATION_DELETE_RETENTION_DAYS=30
```

Keep `REMEDIATION_MASTER_KEY` in a secret manager for production. Changing the key makes existing
encrypted backups unrecoverable.

## API

```text
POST /api/v1/remediations/plan
GET  /api/v1/remediations?scan_id={scan_id}
GET  /api/v1/remediations/{job_id}
POST /api/v1/remediations/{job_id}/decision
```

Delete approval requires a user whose role is `admin`. Mask, redact and encrypt require the scan
owner's explicit approval.

## Supported formats

- Text: TXT, CSV, JSON, XML, LOG
- Office: DOCX, XLSX
- PDF: requires `PyMuPDF`

Mask/redact performs an automatic verification scan. If sensitive values remain, the encrypted
backup is restored and the job is marked failed.
