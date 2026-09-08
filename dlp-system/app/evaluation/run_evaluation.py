"""Run the hybrid detector against a labeled golden set and report metrics.

Usage:
    python -m app.evaluation.run_evaluation
    python -m app.evaluation.run_evaluation --golden-set app/evaluation/golden_set.json --log-mlflow

This closes the "Independent precision/recall/F1 evaluation" item the
README lists as pending for the hybrid detector milestone. It is a real
measurement against hand-labeled expected entities, not a demo -- results
are written to evaluation_report.json so they can be quoted with a number
attached instead of "the detector works well".
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from app.detection.hybrid_engine import HybridDetectionEngine
from app.evaluation.metrics import classification_metrics, log_to_mlflow


def load_golden_set(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate(golden_set: list[dict]) -> dict:
    engine = HybridDetectionEngine()
    expected: list[set[str]] = []
    predicted: list[set[str]] = []

    per_sample: list[dict] = []
    for sample in golden_set:
        findings = engine.detect(sample["text"])
        found_types = {f.entity_type for f in findings}
        expected_types = set(sample["expected_entity_types"])

        expected.append(expected_types)
        predicted.append(found_types)
        per_sample.append(
            {
                "id": sample.get("id"),
                "expected": sorted(expected_types),
                "predicted": sorted(found_types),
                "missed": sorted(expected_types - found_types),
                "extra": sorted(found_types - expected_types),
            }
        )

    metrics = classification_metrics(expected, predicted)
    return {"metrics": metrics, "samples": per_sample}


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the hybrid PII/PCI detector.")
    parser.add_argument(
        "--golden-set",
        default=str(Path(__file__).parent / "golden_set.json"),
    )
    parser.add_argument(
        "--output",
        default="evaluation_report.json",
    )
    parser.add_argument("--log-mlflow", action="store_true")
    args = parser.parse_args()

    golden_set = load_golden_set(Path(args.golden_set))
    report = evaluate(golden_set)

    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Evaluated {len(golden_set)} labeled samples.")
    for label, values in report["metrics"].items():
        print(
            f"  {label:<15} precision={values['precision']:.3f} "
            f"recall={values['recall']:.3f} f1={values['f1']:.3f} "
            f"(tp={values['tp']} fp={values['fp']} fn={values['fn']})"
        )

    if args.log_mlflow:
        logged = log_to_mlflow(report["metrics"], run_name="dlp-detector-eval")
        print("Logged to MLflow." if logged else "mlflow not installed -- skipped.")

    print(f"Full report: {args.output}")


if __name__ == "__main__":
    main()
