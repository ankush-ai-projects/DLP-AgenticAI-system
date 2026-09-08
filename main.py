"""Local-dev convenience entrypoint: `python main.py` from the repo root.

The actual FastAPI app is assembled in `dlp-system/app/main.py`, which is
also what Docker/production point at (`uvicorn app.main:app`, run with
`dlp-system/` as the working directory -- see docker/Dockerfile). This
file's only job is to make `dlp-system/app` importable when running from
the repo root without Docker, then re-export `app` unchanged so both
entrypoints are the same code path -- there is no second app assembly to
drift out of sync.
"""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
BACKEND_ROOT = PROJECT_ROOT / "dlp-system"

if not BACKEND_ROOT.is_dir():
    raise RuntimeError(f"Backend directory not found: {BACKEND_ROOT}")

backend_path = str(BACKEND_ROOT)

if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from app.main import app  # noqa: E402 -- import must follow the sys.path insert above

__all__ = ["app"]


if __name__ == "__main__":
    import uvicorn

    from app.core.config import settings

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8001,
        reload=settings.DEBUG,
    )
