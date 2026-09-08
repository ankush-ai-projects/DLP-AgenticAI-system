"""Validated API contracts for file-level remediation."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


RemediationActionValue = Literal["mask", "redact", "encrypt", "delete"]


class RemediationPlanRequest(BaseModel):
    scan_id: int = Field(gt=0)
    file_path: str = Field(min_length=1, max_length=1000)
    requested_action: RemediationActionValue | None = None
    finding_indexes: list[int] = Field(default_factory=list, max_length=1000)
    reason: str = Field(default="", max_length=1000)


class RemediationDecisionRequest(BaseModel):
    approved: bool
    note: str = Field(min_length=3, max_length=1000)


class RemediationJobResponse(BaseModel):
    id: int
    scan_id: int
    file_path: str
    action: str
    status: str
    entity_types: list[str]
    planner_output: dict[str, Any]
    preview: dict[str, Any]
    approval_required: bool
    admin_required: bool
    output_path: str | None = None
    result: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
