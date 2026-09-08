"""Bounded supervisor for the production-safe multi-agent workflow."""
from __future__ import annotations

import time

from app.agents.critic import CriticAgent
from app.agents.database_agent import DatabaseScanAgent
from app.agents.planner import PlannerAgent
from app.agents.reporting import ReportingAgent
from app.agents.risk_policy import RiskPolicyAgent
from app.agents.state import WorkflowState
from app.agents.system_agent import SystemScanAgent
from app.core.config import settings
from app.core.secrets import SecretProvider
from app.observability.metrics import AGENT_DURATION, SCANS_TOTAL


class SupervisorAgent:
    name = "supervisor"

    def __init__(self, *, secret_provider: SecretProvider | None = None):
        self.planner = PlannerAgent()
        self.database = DatabaseScanAgent(secret_provider)
        self.system = SystemScanAgent()
        self.critic = CriticAgent()
        self.risk = RiskPolicyAgent()
        self.reporting = ReportingAgent()

    def _timed(self, agent_name: str, fn, *args) -> None:
        start = time.monotonic()
        try:
            fn(*args)
        finally:
            AGENT_DURATION.labels(agent=agent_name).observe(time.monotonic() - start)

    def run(self, state: WorkflowState) -> WorkflowState:
        try:
            state.iteration_count += 1
            if state.iteration_count > settings.MAX_AGENT_ITERATIONS:
                raise RuntimeError("Maximum agent iterations exceeded")
            self._timed("planner", self.planner.run, state)
            specialist = self.database if state.asset["asset_type"] == "database" else self.system
            specialist_name = "database_agent" if specialist is self.database else "system_agent"
            self._timed(specialist_name, specialist.run, state)
            self._timed("critic", self.critic.run, state)
            self._timed("risk_policy", self.risk.run, state)
            if state.approval_required:
                state.status = "awaiting_review"
                state.event(self.name, "pause_for_human_review", "blocked", reason="critical_risk")
                SCANS_TOTAL.labels(asset_type=state.asset["asset_type"], status="awaiting_review").inc()
                return state
            self._timed("reporting", self.reporting.run, state)
            SCANS_TOTAL.labels(asset_type=state.asset["asset_type"], status=state.status).inc()
            return state
        except Exception as exc:
            failed_stage = state.status
            state.status = "failed"
            state.errors.append({"stage": failed_stage, "error": type(exc).__name__, "message": str(exc)})
            state.event(self.name, "workflow", "failed", error_type=type(exc).__name__)
            SCANS_TOTAL.labels(asset_type=state.asset.get("asset_type", "unknown"), status="failed").inc()
            return state

    def resume_after_review(self, state: WorkflowState, approved: bool) -> WorkflowState:
        if state.status != "awaiting_review":
            raise ValueError("Scan is not waiting for review")
        state.human_decision = "approved" if approved else "rejected"
        state.approval_required = False
        state.policy_decision["human_decision"] = state.human_decision
        if approved:
            state.event(self.name, "human_review", "completed", decision="approved")
            self._timed("reporting", self.reporting.run, state)
        else:
            state.policy_decision["action"] = "rejected_by_human"
            state.event(self.name, "human_review", "completed", decision="rejected")
            self._timed("reporting", self.reporting.run, state)
        SCANS_TOTAL.labels(asset_type=state.asset["asset_type"], status=state.status).inc()
        return state

