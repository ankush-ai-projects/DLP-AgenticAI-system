"""Reproducible entity-level evaluation helpers."""
from __future__ import annotations

from collections import defaultdict
from typing import Iterable


def classification_metrics(
    expected: Iterable[set[str]], predicted: Iterable[set[str]]
) -> dict[str, dict[str, float]]:
    counts = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0})
    for truth, guess in zip(expected, predicted):
        for label in truth & guess:
            counts[label]["tp"] += 1
        for label in guess - truth:
            counts[label]["fp"] += 1
        for label in truth - guess:
            counts[label]["fn"] += 1
    result = {}
    for label, value in counts.items():
        precision = value["tp"] / max(1, value["tp"] + value["fp"])
        recall = value["tp"] / max(1, value["tp"] + value["fn"])
        f1 = 2 * precision * recall / max(1e-12, precision + recall)
        result[label] = {
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            **value,
        }
    return result


def log_to_mlflow(metrics: dict[str, dict[str, float]], run_name: str = "dlp-evaluation") -> bool:
    try:
        import mlflow
    except ImportError:
        return False
    with mlflow.start_run(run_name=run_name):
        for label, values in metrics.items():
            for name in ("precision", "recall", "f1"):
                mlflow.log_metric(f"{label.lower()}_{name}", values[name])
    return True
