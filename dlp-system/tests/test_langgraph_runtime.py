"""Integration contracts for checkpointed LangGraph orchestration."""
from __future__ import annotations

import pytest

pytest.importorskip("langgraph")

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

from app.agents.critic import CriticAgent
from app.agents.risk_policy import RiskPolicyAgent
from app.agents.state import WorkflowState
from app.workflows.langgraph_runtime import build_langgraph


class _Planner:
    calls = 0

    def run(self, state):
        self.calls += 1
        state.status = "planning"
        state.plan = {"read_only": True, "planner_source": "test"}
        state.event("planner", "create_plan", "completed")
        return state


class _Scanner:
    def __init__(self, *, fail_once=False, critical=False):
        self.fail_once = fail_once
        self.critical = critical
        self.calls = 0

    def run(self, state, progress_callback=None):
        self.calls += 1
        if self.fail_once and self.calls == 1:
            raise ConnectionError("temporary scanner failure")
        count = 7 if self.critical else 1
        state.findings = [
            {
                "entity_type": "CREDIT_CARD" if self.critical else "EMAIL",
                "masked_value": f"masked-{index}",
                "confidence": 0.99,
                "source": "test",
                "risk_level": "critical" if self.critical else "low",
                "location": {"row_number": index},
            }
            for index in range(count)
        ]
        state.status = "scanning"
        state.event("database_scan", "scan_database", "completed")
        return state


class _Reporter:
    def run(self, state):
        state.report = {"risk": state.risk_summary, "policy": state.policy_decision}
        state.status = "completed"
        state.event("reporting", "generate_report", "completed")
        return state


class _Supervisor:
    def __init__(self, scanner):
        self.planner = _Planner()
        self.database = scanner
        self.system = scanner
        self.critic = CriticAgent()
        self.risk = RiskPolicyAgent()
        self.reporting = _Reporter()


def _state(scan_id: int, *, review: bool = True) -> dict:
    return WorkflowState(
        scan_id=scan_id,
        goal="Scan the test database for sensitive data",
        asset={"name": "test", "asset_type": "database", "platform": "sqlite"},
        requested_entities=["CREDIT_CARD", "EMAIL"],
        require_human_review_for_critical=review,
        thread_id=f"dlp-scan-{scan_id}",
    ).model_dump(mode="json")


def test_graph_replans_after_recoverable_specialist_failure():
    scanner = _Scanner(fail_once=True)
    supervisor = _Supervisor(scanner)
    graph = build_langgraph(supervisor, InMemorySaver())

    result = graph.invoke(
        _state(101), config={"configurable": {"thread_id": "dlp-scan-101"}}
    )

    assert result["status"] == "completed"
    assert scanner.calls == 2
    assert supervisor.planner.calls == 2
    assert result["retry_count"] == 1


def test_graph_interrupts_and_resumes_same_checkpoint():
    graph = build_langgraph(_Supervisor(_Scanner(critical=True)), InMemorySaver())
    config = {"configurable": {"thread_id": "dlp-scan-202"}}

    paused = graph.invoke(_state(202), config=config)
    assert paused["approval_required"] is True
    assert paused["__interrupt__"]

    completed = graph.invoke(
        Command(resume={"approved": True, "note": "Reviewed by analyst"}),
        config=config,
    )
    assert completed["status"] == "completed"
    assert completed["human_decision"] == "approved"
    assert completed["policy_decision"]["review_note"] == "Reviewed by analyst"
