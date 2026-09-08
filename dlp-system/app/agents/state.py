"""Shared, serializable workflow state for every specialist agent."""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class WorkflowState(BaseModel):
    scan_id: int | None = None
    goal: str
    asset: dict[str, Any]
    requested_entities: list[str]
    file_extensions: list[str] | None = None
    batch_size: int = 1000
    row_limit: int = 5000
    require_human_review_for_critical: bool = True
    dry_run: bool = True
    status: str = "created"
    plan: dict[str, Any] = Field(default_factory=dict)
    findings: list[dict[str, Any]] = Field(default_factory=list)
    verified_findings: list[dict[str, Any]] = Field(default_factory=list)
    scan_stats: dict[str, Any] = Field(default_factory=dict)
    risk_summary: dict[str, Any] = Field(default_factory=dict)
    policy_decision: dict[str, Any] = Field(default_factory=dict)
    report: dict[str, Any] = Field(default_factory=dict)
    file_hashes: dict[str, str] = Field(default_factory=dict)
    errors: list[dict[str, Any]] = Field(default_factory=list)
    events: list[dict[str, Any]] = Field(default_factory=list)
    retry_count: int = 0
    iteration_count: int = 0
    approval_required: bool = False
    human_decision: str | None = None
    last_error: dict[str, Any] | None = None
    runtime: str = "langgraph"
    thread_id: str | None = None
    memory_context: str = ""

    def event(self, agent: str, action: str, status: str, **summary: Any) -> None:
        self.events.append(
            {"agent": agent, "action": action, "status": status, "summary": summary}
        ) 