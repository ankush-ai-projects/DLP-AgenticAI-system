"""Tests for cross-scan memory: recall before planning, remember after completion."""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app.models  # noqa: F401 -- registers ScanMemory on Base.metadata
from app.agents.memory import ScanMemoryStore, summarize_for_prompt
from app.agents.state import WorkflowState
from app.models.base import Base


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    yield session
    session.close()


def _state_with_findings(entity_types: list[str], risk_level: str, scan_id: int) -> WorkflowState:
    return WorkflowState(
        scan_id=scan_id,
        goal="scan",
        asset={"asset_type": "database", "platform": "mysql", "name": "billing"},
        requested_entities=entity_types,
        verified_findings=[{"entity_type": t} for t in entity_types],
        risk_summary={"level": risk_level},
        plan={"planner_source": "deterministic_fallback"},
    )


def test_recall_empty_for_unseen_asset(db_session):
    assert ScanMemoryStore(db_session).recall(asset_id=1) == []


def test_remember_then_recall_round_trip(db_session):
    store = ScanMemoryStore(db_session)
    state = _state_with_findings(["EMAIL", "EMAIL", "PAN"], "high", scan_id=42)

    store.remember(asset_id=1, state=state)
    memories = store.recall(asset_id=1)

    assert len(memories) == 1
    assert memories[0]["scan_id"] == 42
    assert memories[0]["highest_risk"] == "high"
    assert memories[0]["entity_type_counts"] == {"EMAIL": 2, "PAN": 1}
    assert memories[0]["verified_finding_count"] == 3


def test_recall_is_scoped_per_asset(db_session):
    store = ScanMemoryStore(db_session)
    store.remember(asset_id=1, state=_state_with_findings(["EMAIL"], "low", scan_id=1))
    store.remember(asset_id=2, state=_state_with_findings(["CREDIT_CARD"], "critical", scan_id=2))

    assert len(store.recall(asset_id=1)) == 1
    assert len(store.recall(asset_id=2)) == 1
    assert store.recall(asset_id=1)[0]["highest_risk"] == "low"
    assert store.recall(asset_id=2)[0]["highest_risk"] == "critical"


def test_recall_respects_limit_and_recency(db_session):
    store = ScanMemoryStore(db_session)
    for scan_id in range(1, 6):
        store.remember(asset_id=1, state=_state_with_findings(["EMAIL"], "low", scan_id=scan_id))

    recent = store.recall(asset_id=1, limit=2)
    assert len(recent) == 2
    assert recent[0]["scan_id"] == 5  # newest first


def test_summarize_for_prompt_handles_empty_memory():
    assert summarize_for_prompt([]) == "No prior scans recorded for this asset."


def test_summarize_for_prompt_never_leaks_raw_values(db_session):
    """Memory summaries are counts and labels only -- never raw PII values."""
    store = ScanMemoryStore(db_session)
    state = _state_with_findings(["EMAIL", "CREDIT_CARD"], "critical", scan_id=1)
    state.verified_findings = [
        {"entity_type": "EMAIL", "value": "someone@example.com"},
        {"entity_type": "CREDIT_CARD", "value": "4111111111111111"},
    ]
    store.remember(asset_id=1, state=state)
    summary = summarize_for_prompt(store.recall(asset_id=1))

    assert "someone@example.com" not in summary
    assert "4111111111111111" not in summary
    assert "EMAIL" in summary and "CREDIT_CARD" in summary
