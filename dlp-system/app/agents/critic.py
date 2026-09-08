"""Deterministic critic that validates, deduplicates, and calibrates findings."""
from __future__ import annotations

from app.agents.state import WorkflowState


class CriticAgent:
    name = "critic"

    def run(self, state: WorkflowState) -> WorkflowState:
        state.status = "verifying"
        unique: dict[tuple, dict] = {}
        rejected = 0
        for finding in state.findings:
            if not 0.0 <= float(finding.get("confidence", 0)) <= 1.0:
                rejected += 1
                continue
            location = finding.get("location", {})
            key = (
                finding.get("entity_type"),
                finding.get("masked_value"),
                location.get("path"),
                location.get("schema"),
                location.get("table"),
                location.get("column"),
                location.get("row_number"),
            )
            previous = unique.get(key)
            if previous is None or finding["confidence"] > previous["confidence"]:
                unique[key] = finding
        state.verified_findings = list(unique.values())
        state.event(
            self.name,
            "verify_findings",
            "completed",
            accepted=len(state.verified_findings),
            rejected=rejected,
            duplicates_removed=len(state.findings) - rejected - len(state.verified_findings),
        )
        return state
