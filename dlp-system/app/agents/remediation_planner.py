"""Bounded AI planner for file-level DLP remediation."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from app.ai.model_client import ModelClient, build_model_client


ALLOWED_ACTIONS = {"mask", "redact", "encrypt", "delete"}
REDACTION_FORMATS = {".pdf", ".docx"}


class RemediationPlannerAgent:
    """Recommend an action without ever receiving raw sensitive values."""

    name = "remediation_planner"

    def __init__(self, model_client: ModelClient | None = None):
        self.model_client = model_client or build_model_client()

    def plan(
        self,
        *,
        file_path: str,
        findings: list[dict[str, Any]],
        requested_action: str | None,
        reason: str,
    ) -> dict[str, Any]:
        deterministic = self._deterministic_plan(
            file_path=file_path,
            findings=findings,
            requested_action=requested_action,
            reason=reason,
        )
        safe_findings = [
            {
                "entity_type": item.get("entity_type"),
                "masked_value": item.get("masked_value"),
                "risk_level": item.get("risk_level"),
                "confidence": item.get("confidence"),
            }
            for item in findings[:250]
        ]

        try:
            candidate = self.model_client.generate_json(
                system=(
                    "You are a bounded DLP remediation planner. Return JSON only. "
                    "Choose exactly one allowed action. You receive masked metadata only. "
                    "Never request raw PII, credentials, shell commands, paths outside the "
                    "supplied file, or bypass of human approval. Delete always requires admin."
                ),
                user=json.dumps(
                    {
                        "file_extension": Path(file_path).suffix.lower(),
                        "masked_findings": safe_findings,
                        "requested_action": requested_action,
                        "business_reason": reason,
                        "allowed_actions": sorted(ALLOWED_ACTIONS),
                        "fallback": deterministic,
                    }
                ),
            )
            action = str(candidate.get("recommended_action", "")).lower()

            if action not in ALLOWED_ACTIONS:
                raise ValueError("Model recommended an unsupported action")

            if requested_action and action != requested_action:
                action = requested_action

            return {
                **deterministic,
                "recommended_action": action,
                "reason": str(candidate.get("reason") or deterministic["reason"])[:1000],
                "confidence": min(1.0, max(0.0, float(candidate.get("confidence", 0.85)))),
                "planner_source": "llm",
                "admin_required": action == "delete",
            }
        except Exception:
            return deterministic

    @staticmethod
    def _deterministic_plan(
        *,
        file_path: str,
        findings: list[dict[str, Any]],
        requested_action: str | None,
        reason: str,
    ) -> dict[str, Any]:
        extension = Path(file_path).suffix.lower()
        risks = Counter(str(item.get("risk_level", "low")).lower() for item in findings)
        entities = Counter(str(item.get("entity_type", "UNKNOWN")) for item in findings)

        if requested_action:
            action = requested_action.lower()
            if action not in ALLOWED_ACTIONS:
                raise ValueError("Unsupported remediation action")
        elif extension in REDACTION_FORMATS:
            action = "redact"
        else:
            action = "mask"

        recommendation_reason = reason.strip() or (
            f"{len(findings)} verified findings were detected in a {extension or 'file'} asset. "
            f"The bounded policy selected {action} while preserving an encrypted backup."
        )

        return {
            "recommended_action": action,
            "reason": recommendation_reason[:1000],
            "confidence": 0.95,
            "planner_source": "deterministic_fallback",
            "approval_required": True,
            "admin_required": action == "delete",
            "entity_counts": dict(entities),
            "risk_counts": dict(risks),
            "safety_controls": [
                "allowlist_validation",
                "sha256_precondition",
                "encrypted_backup",
                "human_approval",
                "atomic_write",
                "verification_rescan",
                "audit_event",
            ],
        }
