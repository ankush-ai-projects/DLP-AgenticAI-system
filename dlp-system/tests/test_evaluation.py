"""Tests for the golden-set evaluation harness."""
from app.evaluation.metrics import classification_metrics
from app.evaluation.run_evaluation import evaluate, load_golden_set
from pathlib import Path


GOLDEN_SET_PATH = Path(__file__).resolve().parents[1] / "app" / "evaluation" / "golden_set.json"


def test_golden_set_loads_and_is_non_empty():
    golden_set = load_golden_set(GOLDEN_SET_PATH)
    assert len(golden_set) > 5
    for sample in golden_set:
        assert "text" in sample
        assert "expected_entity_types" in sample


def test_evaluate_produces_metrics_for_every_seen_label():
    golden_set = load_golden_set(GOLDEN_SET_PATH)
    report = evaluate(golden_set)

    assert "metrics" in report and "samples" in report
    assert len(report["samples"]) == len(golden_set)
    # regex-backed entity types should hit perfect precision/recall on this
    # hand-labeled set since every sample uses well-formed values
    for label in ("EMAIL", "PHONE", "PAN", "AADHAAR", "CREDIT_CARD"):
        assert label in report["metrics"]
        assert report["metrics"][label]["f1"] == 1.0


def test_invalid_luhn_card_is_correctly_rejected():
    golden_set = load_golden_set(GOLDEN_SET_PATH)
    report = evaluate(golden_set)
    sample = next(s for s in report["samples"] if s["id"] == "invalid_luhn_card_should_be_rejected")
    assert sample["predicted"] == []
    assert sample["expected"] == []


def test_classification_metrics_basic_precision_recall():
    expected = [{"A", "B"}, {"A"}]
    predicted = [{"A"}, {"A", "C"}]
    metrics = classification_metrics(expected, predicted)

    assert metrics["A"]["tp"] == 2
    assert metrics["A"]["precision"] == 1.0
    assert metrics["A"]["recall"] == 1.0
    assert metrics["B"]["fn"] == 1
    assert metrics["C"]["fp"] == 1
