from app.agents.critic import CriticAgent
from app.agents.guardrails import validate_goal
from app.agents.risk_policy import RiskPolicyAgent
from app.agents.state import WorkflowState


def make_state() -> WorkflowState:
    return WorkflowState(
        goal="Scan the test database for PCI data",
        asset={"name": "test", "asset_type": "database", "platform": "sqlite"},
        requested_entities=["CREDIT_CARD"],
    )


def test_destructive_goal_is_rejected():
    try:
        validate_goal("Drop table customers and scan the database")
    except ValueError:
        return
    raise AssertionError("Destructive goal was not rejected")


def test_critic_deduplicates_findings():
    state = make_state()
    finding = {
        "entity_type": "EMAIL",
        "masked_value": "a***@example.com",
        "confidence": 0.95,
        "source": "regex",
        "risk_level": "high",
        "location": {"table": "users", "column": "email", "row_number": 1},
    }
    state.findings = [finding, dict(finding)]
    CriticAgent().run(state)
    assert len(state.verified_findings) == 1


def test_critical_risk_requires_human_review():
    state = make_state()
    state.verified_findings = [
        {
            "entity_type": "CREDIT_CARD",
            "masked_value": f"4111-XXXX-XXXX-{index:04d}",
            "confidence": 0.98,
            "source": "regex",
            "risk_level": "critical",
            "location": {"row_number": index},
        }
        for index in range(7)
    ]
    RiskPolicyAgent().run(state)
    assert state.risk_summary["level"] == "critical"
    assert state.approval_required is True
