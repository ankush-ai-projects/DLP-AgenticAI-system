"""Pre-execution guardrails for goals and agent plans."""
from __future__ import annotations

import re
from typing import Any


FORBIDDEN_GOAL_PATTERNS = [
    r"\b(drop|truncate|delete|update|insert|alter)\s+(table|database|from|into)\b",
    r"\b(rm\s+-rf|format\s+[a-z]:|del\s+/[fsq])\b",
    r"ignore\s+(all\s+)?previous\s+instructions",
]


def validate_goal(goal: str) -> str:
    normalized = " ".join(goal.strip().split())
    for pattern in FORBIDDEN_GOAL_PATTERNS:
        if re.search(pattern, normalized, re.IGNORECASE):
            raise ValueError("The scan goal requests a prohibited or destructive operation")
    return normalized


def validate_plan(plan: dict[str, Any], asset_type: str) -> dict[str, Any]:
    allowed_tools = {
        "database": {"test_connection", "discover_schema", "scan_database", "verify", "risk", "report"},
        "system": {"check_path", "discover_files", "scan_system", "verify", "risk", "report"},
    }
    tools = plan.get("tools")
    if not isinstance(tools, list) or not tools:
        raise ValueError("Plan requires a non-empty tools list")
    invalid = set(tools) - allowed_tools[asset_type]
    if invalid:
        raise ValueError(f"Plan contains non-allowlisted tools: {sorted(invalid)}")
    plan["read_only"] = True
    return plan
