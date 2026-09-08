"""
app/detection/nlp_detector.py  —  Layer 2

Trained custom NER model use karta hai unstructured text se
PERSON, ADDRESS, AADHAAR, PAN, EMAIL, PHONE detect karne ke liye.

Model load hota hai ek baar startup pe — har request pe reload nahi.
"""

try:
    import spacy
except ImportError:  # Regex-only mode remains available in minimal deployments.
    spacy = None
from pathlib import Path
from typing import List
from app.schemas.detection_schema import DetectionFinding

# ── Model path ────────────────────────────────────────────────────────
# Pehle custom trained model try karo,
# agar nahi mila toh spaCy ka default English model fallback
CUSTOM_MODEL_PATH = Path("models/trained/dlp_ner_model")
FALLBACK_MODEL    = "en_core_web_sm"

# ── NLP confidence map ────────────────────────────────────────────────
# Custom trained labels ke liye confidence scores
LABEL_CONFIDENCE = {
    "PERSON":      0.80,
    "ADDRESS":     0.75,
    "AADHAAR":     0.90,
    "PAN":         0.90,
    "CREDIT_CARD": 0.88,
    "EMAIL":       0.92,
    "PHONE":       0.85,
    # spaCy default labels jo hum rakhenge
    "GPE":         0.70,  # cities/countries → ADDRESS ke roop mein treat
    "LOC":         0.70,
    "ORG":         0.65,
}

# spaCy ke default labels → DLP labels mapping
SPACY_REMAP = {
    "GPE": "ADDRESS",
    "LOC": "ADDRESS",
}

# DLP ke liye relevant labels (baaki ignore)
RELEVANT_LABELS = set(LABEL_CONFIDENCE.keys())


def _load_model():
    """
    Model load karo — custom trained pehle, fallback baad mein.
    Module-level variable isliye ki sirf ek baar load ho.
    """
    if spacy is None:
        return None
    if CUSTOM_MODEL_PATH.exists():
        print(f"[NLP] Custom trained model load ho raha hai: {CUSTOM_MODEL_PATH}")
        return spacy.load(str(CUSTOM_MODEL_PATH))
    else:
        print(f"[NLP] Custom model nahi mila. Fallback: {FALLBACK_MODEL}")
        print(f"      Train karne ke liye: python training/train_model.py")
        return spacy.load(FALLBACK_MODEL)


# ── Module-level model load (ek baar) ─────────────────────────────────
try:
    _nlp = _load_model()
except (OSError, RuntimeError):
    _nlp = None


def run_nlp_detection(text: str) -> List[DetectionFinding]:
    """
    Trained NER model se text mein named entities dhundho.

    Args:
        text: Scan karne wala raw text

    Returns:
        List of DetectionFinding — sirf relevant DLP entities
    """
    findings: List[DetectionFinding] = []

    if _nlp is None:
        return findings
    doc = _nlp(text)

    for ent in doc.ents:
        label = ent.label_

        # Irrelevant labels skip karo
        if label not in RELEVANT_LABELS:
            continue

        # spaCy default labels ko DLP labels pe remap karo
        dlp_label  = SPACY_REMAP.get(label, label)
        confidence = LABEL_CONFIDENCE.get(label, 0.70)

        findings.append(
            DetectionFinding(
                entity_type=dlp_label,
                value=ent.text,
                confidence=confidence,
                source="nlp",
                start_pos=ent.start_char,
                end_pos=ent.end_char,
                risk_level=None,
            )
        )

    return findings


def reload_model():
    """
    Naya model train karne ke baad hot-reload ke liye.
    Call karo: from app.detection.nlp_detector import reload_model; reload_model()
    """
    global _nlp
    _nlp = _load_model()
    print("[NLP] Model reloaded successfully.")
