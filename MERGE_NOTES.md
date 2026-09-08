# Current Project + Agentic Remediation

This package preserves the uploaded current project and its root `main.py`.
Only the file-remediation workflow and live scan-content metrics were merged.

## New files

- `dlp-frontend-new/src/components/RemediationWorkspace.jsx`
- `dlp-frontend-new/src/components/RemediationWorkspace.css`
- `dlp-system/app/models/remediation.py`
- `dlp-system/app/schemas/remediation.py`
- `dlp-system/app/agents/remediation_planner.py`
- `dlp-system/app/tools/remediation_tools.py`
- `dlp-system/app/services/remediation_service.py`
- `dlp-system/app/api/v1/endpoints/remediation.py`
- `dlp-system/alembic/versions/20260818_0002_file_remediation.py`
- `dlp-system/tests/test_remediation_tools.py`
- `REMEDIATION_GUIDE.md`

## Existing files updated

- Scan result/status UI: remediation panel and live files/tables/bytes metrics.
- System/DB scanner tools: progress callbacks and scanned-byte counters.
- API/model registries: remediation endpoints and model registration.
- Configuration/dependencies: remediation backup settings and PDF support.

## Local setup

From the project root:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r .\dlp-system\requirements.txt
python -m uvicorn main:app --reload --port 8001
```

In a second terminal:

```powershell
cd .\dlp-frontend-new
npm install
npm run dev
```

Copy the three `REMEDIATION_*` values from `dlp-system/.env.example` into
your existing `dlp-system/.env`. Keep the remediation key private.
