"""
test_pipeline.py — DLP pipeline end-to-end test
Run karo: python test_pipeline.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# ── Imports ───────────────────────────────────────────────────────────
try:
    from app.detection.hybrid_engine import engine
    from app.detection.risk_scorer   import assign_risk_levels, build_risk_summary
    from app.detection.masker        import mask_text
    print("[OK] All imports successful\n")
except ImportError as e:
    print(f"[ERROR] Import failed: {e}")
    print("  Check karo: detection_schema.py, hybrid_engine.py, nlp_detector.py sab hain?")
    sys.exit(1)

# ── Test cases ────────────────────────────────────────────────────────
TEST_CASES = [
    {
        "name": "Test 1 — Mixed PII",
        "text": (
            "Customer Rahul Sharma with Aadhaar 2345 6789 0123 "
            "and PAN ABCDE1234F lives at Sector 14, Gurgaon. "
            "Contact: rahul.sharma@gmail.com, 9876543210."
        ),
    },
    {
        "name": "Test 2 — Credit card",
        "text": "Transaction on card 4111111111111111 by Priya Singh was declined.",
    },
    {
        "name": "Test 3 — Clean text (koi PII nahi)",
        "text": "Please review the quarterly sales report for Q3 2024.",
    },
    {
        "name": "Test 4 — Multiple persons",
        "text": (
            "Joint account of Suresh Patel and Meena Patel. "
            "Email: suresh@hdfc.co.in. Address: MG Road, Bangalore."
        ),
    },
    {
        "name": "Test 5 — Aadhaar + PAN",
        "text": "Linking Aadhaar 3456 7890 1234 with PAN XYZAB6543W is pending.",
    },
]


def run_tests():
    print("=" * 60)
    print("  DLP Pipeline — End to End Test")
    print("=" * 60)

    total_pass = 0
    total_fail = 0

    for tc in TEST_CASES:
        print(f"\n{'─'*60}")
        print(f"  {tc['name']}")
        print(f"  Input : {tc['text'][:80]}{'...' if len(tc['text']) > 80 else ''}")

        try:
            # Pipeline
            findings     = engine.detect(tc["text"])
            findings     = assign_risk_levels(findings)
            risk_summary = build_risk_summary(findings)
            masked       = mask_text(tc["text"], findings)

            if findings:
                print(f"\n  Findings ({len(findings)}):")
                for f in findings:
                    print(
                        f"    [{f.risk_level.upper():8}] "
                        f"{f.entity_type:12} | "
                        f"conf={f.confidence:.2f} | "
                        f"src={f.source:5} | "
                        f'"{f.value}"'
                    )
            else:
                print(f"\n  Findings: None detected")

            print(f"\n  Risk    : {risk_summary['by_level']}")
            print(f"  Masked  : {masked[:80]}{'...' if len(masked) > 80 else ''}")
            total_pass += 1

        except Exception as e:
            print(f"\n  [FAIL] Error: {e}")
            import traceback
            traceback.print_exc()
            total_fail += 1

    print(f"\n{'='*60}")
    print(f"  Results: {total_pass} passed, {total_fail} failed")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    run_tests()
