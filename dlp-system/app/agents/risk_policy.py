"""Deterministic risk scoring and policy decision agent."""
from __future__ import annotations

from collections import Counter

from app.agents.state import WorkflowState
from app.observability.metrics import FINDINGS_TOTAL


ENTITY_WEIGHTS = {
    "CREDIT_CARD": 10,
    "AADHAAR": 9,
    "PAN": 8,
    "ADDRESS": 5,
    "PHONE": 4,
    "EMAIL": 3,
    "PERSON": 2,
}


class RiskPolicyAgent:
    name = "risk_policy"

    def run(self, state: WorkflowState) -> WorkflowState:
        state.status = "risk_analysis"
        counts = Counter(finding["entity_type"] for finding in state.verified_findings)
        raw_score = sum(ENTITY_WEIGHTS.get(entity, 2) * min(count, 10) for entity, count in counts.items())
        score = min(100, raw_score)
        if score >= 70:
            level = "critical"
        elif score >= 40:
            level = "high"
        elif score >= 15:
            level = "medium"
        else:
            level = "low"
        action = {
            "critical": "review_required",
            "high": "alert",
            "medium": "monitor",
            "low": "allow",
        }[level]
        state.risk_summary = {
            "score": score,
            "level": level,
            "total_findings": len(state.verified_findings),
            "by_entity": dict(counts),
        }
        for entity, count in counts.items():
            FINDINGS_TOTAL.labels(entity_type=entity, risk=level).inc(count)
        state.approval_required = bool(
            state.require_human_review_for_critical and level == "critical"
        )
        state.policy_decision = {
            "action": action,
            "dry_run": state.dry_run,
            "approval_required": state.approval_required,
            "enforcement_performed": False,
        }
        state.event(
            self.name,
            "calculate_risk",
            "completed",
            score=score,
            level=level,
            policy_action=action,
        )
        return state
