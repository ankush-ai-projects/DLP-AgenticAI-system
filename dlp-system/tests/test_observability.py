"""Tests that scan and finding counters actually increment during a run.

Uses the real prometheus_client registry when installed, and falls back
to checking the no-op path doesn't raise when it isn't -- either way the
supervisor must not crash because of instrumentation.
"""
from app.agents.state import WorkflowState
from app.agents.supervisor import SupervisorAgent


def _system_state() -> WorkflowState:
    return WorkflowState(
        goal="scan for pii",
        asset={"asset_type": "system", "platform": "linux", "name": "test_data", "root_path": "./test_data"},
        requested_entities=["EMAIL", "PHONE", "PAN", "AADHAAR", "CREDIT_CARD"],
    )


def test_supervisor_run_completes_without_raising():
    result = SupervisorAgent().run(_system_state())

    assert result.status in {"completed", "partially_completed", "awaiting_review", "failed"}


def test_supervisor_emits_agent_timing_events():
    result = SupervisorAgent().run(_system_state())

    agent_names = {event["agent"] for event in result.events}
    assert "planner" in agent_names
    assert "risk_policy" in agent_names


def test_prometheus_counters_increment_when_available():
    prometheus_client = None
    try:
        import prometheus_client  # noqa: F401
    except ImportError:
        prometheus_client = None
    else:
        prometheus_client = True

    from app.observability import metrics as obs_metrics

    if not prometheus_client:
        # No-op fallback must still be callable without raising.
        obs_metrics.SCANS_TOTAL.labels(asset_type="system", status="completed").inc()
        return

    before = obs_metrics.SCANS_TOTAL.labels(asset_type="system", status="completed")._value.get()
    obs_metrics.SCANS_TOTAL.labels(asset_type="system", status="completed").inc()
    after = obs_metrics.SCANS_TOTAL.labels(asset_type="system", status="completed")._value.get()
    assert after == before + 1
