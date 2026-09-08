"""
app/api/v1/endpoints/scan.py

Auth + File Upload dono complete.

Flow:
  POST /scans/pii     → JWT token verify → real user_id → detect → DB save
  POST /scans/upload  → JWT token verify → file read → detect → DB save
  GET  /scans/{id}    → JWT token verify → apna scan fetch karo
  GET  /scans/history → JWT token verify → apne saare scans
"""

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session               import get_db
from app.schemas.detection_schema import ScanRequest, ScanResponse
from app.detection.hybrid_engine  import engine
from app.detection.risk_scorer    import assign_risk_levels, build_risk_summary
from app.detection.masker         import mask_text
from app.repositories.scan_repo   import ScanRepository
from app.core.dependencies        import get_current_user
from app.models.user              import User

router = APIRouter(prefix="/scans", tags=["scans"])


# ── 1. Text scan — Auth protected ────────────────────────────────────
@router.post("/pii", response_model=ScanResponse)
async def scan_for_pii(
    payload:      ScanRequest,
    db:           Session = Depends(get_db),
    current_user: User    = Depends(get_current_user),  # ← JWT se real user
):
    """
    Text scan karo — result DB mein save hoga.

    Auth flow:
    - Request mein Authorization: Bearer <token> hona chahiye
    - get_current_user() token decode karta hai
    - real user_id milta hai — user_id=1 hardcoded nahi

    Detection flow:
    - Hybrid engine (Regex + NLP) text scan karta hai
    - Risk scorer severity assign karta hai
    - Masker PII hide karta hai
    - DB mein save hota hai current user ke saath
    """
    repo = ScanRepository(db)

    # Real user_id use karo — hardcoded nahi
    scan = repo.create_scan(
        user_id  = current_user.id,
        filename = "text_scan",
    )

    try:
        repo.mark_in_progress(scan.id)

        findings     = engine.detect(payload.text)
        findings     = assign_risk_levels(findings)
        risk_summary = build_risk_summary(findings)
        masked       = mask_text(payload.text, findings)

        repo.save_results(
            scan_id      = scan.id,
            findings     = findings,
            risk_summary = risk_summary,
            masked_text  = masked,
        )

        return ScanResponse(
            total_findings = len(findings),
            risk_summary   = risk_summary,
            findings       = findings,
            masked_text    = masked,
        )

    except Exception as e:
        repo.mark_failed(scan.id, str(e))
        raise HTTPException(status_code=500, detail=str(e))


# ── 2. File upload scan — Auth protected ─────────────────────────────
@router.post("/upload", response_model=ScanResponse)
async def upload_and_scan(
    file:         UploadFile = File(...),
    db:           Session    = Depends(get_db),
    current_user: User       = Depends(get_current_user),
):
    """
    File upload karke scan karo.

    Supported formats:
    - PDF  → pdfplumber se text extract hota hai
    - CSV  → saari rows ka text scan hota hai
    - TXT  → seedha decode hota hai

    Flow:
    1. File read karo
    2. Format ke hisaab se text extract karo
    3. Hybrid engine se scan karo
    4. DB mein save karo — filename aur user_id ke saath
    """
    repo = ScanRepository(db)

    scan = repo.create_scan(
        user_id  = current_user.id,
        filename = file.filename,
    )

    try:
        repo.mark_in_progress(scan.id)

        # File content read karo
        content = await file.read()

        # File type se text extract karo
        text = _extract_text(file.filename, content)

        if not text.strip():
            raise ValueError("File mein koi readable text nahi mila.")

        # Detection pipeline
        findings     = engine.detect(text)
        findings     = assign_risk_levels(findings)
        risk_summary = build_risk_summary(findings)
        masked       = mask_text(text, findings)

        repo.save_results(
            scan_id      = scan.id,
            findings     = findings,
            risk_summary = risk_summary,
            masked_text  = masked,
        )

        return ScanResponse(
            total_findings = len(findings),
            risk_summary   = risk_summary,
            findings       = findings,
            masked_text    = masked,
        )

    except Exception as e:
        repo.mark_failed(scan.id, str(e))
        raise HTTPException(status_code=500, detail=str(e))


# ── 3. Scan by ID ─────────────────────────────────────────────────────
@router.get("/{scan_id}")
async def get_scan_result(
    scan_id:      int,
    db:           Session = Depends(get_db),
    current_user: User    = Depends(get_current_user),
):
    """
    Scan ID se result fetch karo.
    Sirf apna scan dekh sakte ho — dusre ka nahi.
    """
    repo = ScanRepository(db)
    scan = repo.get_by_id(scan_id)

    if not scan:
        raise HTTPException(status_code=404, detail="Scan nahi mila.")

    # Sirf apna scan — security check
    if scan.user_id != current_user.id:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail      = "Yeh scan tumhara nahi hai.",
        )

    return {
        "id":          scan.id,
        "filename":    scan.filename,
        "status":      scan.status,
        "risk_level":  scan.risk_level,
        "findings":    scan.findings,
        "masked_text": scan.scan_result,
        "created_at":  str(scan.created_at),
    }


# ── 4. User scan history ──────────────────────────────────────────────
@router.get("/history/me")
async def get_my_scans(
    db:           Session = Depends(get_db),
    current_user: User    = Depends(get_current_user),
):
    """
    Apne saare scans — latest pehle.
    Token se automatically current user ka history milta hai.
    """
    repo  = ScanRepository(db)
    scans = repo.get_by_user_id(user_id=current_user.id, limit=50)

    return {
        "user_id": current_user.id,
        "total":   len(scans),
        "scans": [
            {
                "id":         s.id,
                "filename":   s.filename,
                "status":     s.status,
                "risk_level": s.risk_level,
                "created_at": str(s.created_at),
            }
            for s in scans
        ],
    }


# ── Helper: file se text extract ──────────────────────────────────────
def _extract_text(filename: str, content: bytes) -> str:
    """
    File type dekh ke appropriate extractor use karo.

    PDF:  pdfplumber — page by page text nikalta hai
    CSV:  csv reader — saari cells ka text
    TXT:  seedha UTF-8 decode
    """
    name = (filename or "").lower()

    if name.endswith(".pdf"):
        try:
            import pdfplumber
            import io
            pages = []
            with pdfplumber.open(io.BytesIO(content)) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        pages.append(text)
            return "\n".join(pages)
        except ImportError:
            raise ValueError("PDF support ke liye: pip install pdfplumber")

    elif name.endswith(".csv"):
        import csv
        import io
        rows = []
        reader = csv.reader(
            io.StringIO(content.decode("utf-8", errors="ignore"))
        )
        for row in reader:
            rows.append(" ".join(row))
        return "\n".join(rows)

    else:
        return content.decode("utf-8", errors="ignore")
