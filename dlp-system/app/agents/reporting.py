from __future__ import annotations

from app.agents.state import WorkflowState
from app.rag.policy_retriever import PolicyRetriever


class ReportingAgent:
    name = "reporting"

    def __init__(self, retriever: PolicyRetriever | None = None):
        self.retriever = retriever or PolicyRetriever()

    def run(self, state: WorkflowState) -> WorkflowState:
        state.status = "reporting"
        level = state.risk_summary.get("level", "low")
        total = state.risk_summary.get("total_findings", 0)
        policy_context = self.retriever.retrieve(
            " ".join([level, *state.risk_summary.get("by_entity", {}).keys(), "remediation policy"])
        )
        state.report = {
            "title": f"DLP scan report: {state.asset['name']}",
            "executive_summary": (
                f"The scan found {total} verified sensitive-data occurrences. "
                f"The overall risk level is {level}."
            ),
            "asset": {
                "name": state.asset["name"],
                "type": state.asset["asset_type"],
                "platform": state.asset["platform"],
            },
            "coverage": state.scan_stats,
            "risk": state.risk_summary,
            "policy": state.policy_decision,
            "findings": state.verified_findings,
            "errors": state.errors,
            "recommendations": self._recommendations(level),
            "policy_evidence": policy_context,
        }
        state.status = "completed" if not state.errors else "partially_completed"
        state.event(self.name, "generate_report", "completed", final_status=state.status)
        return state

    @staticmethod
    def _recommendations(level: str) -> list[str]:
        recommendations = ["Review access permissions and retain only required sensitive data."]
        if level in {"high", "critical"}:
            recommendations.extend(
                [
                    "Apply encryption or tokenization to confirmed sensitive fields.",
                    "Restrict access and open a tracked remediation item.",
                    "Re-scan after remediation and compare results.",
                ]
            )
        return recommendations
