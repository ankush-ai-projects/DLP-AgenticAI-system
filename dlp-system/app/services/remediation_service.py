"""Application service for AI-planned, human-approved file remediation."""

from __future__ import annotations

import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sqlalchemy.orm import Session

from app.agents.remediation_planner import RemediationPlannerAgent
from app.models.enterprise import AgenticScan, AuditEvent
from app.models.remediation import (
    RemediationAction,
    RemediationJob,
    RemediationStatus,
)
from app.models.user import User, UserRole
from app.repositories.enterprise_repo import EnterpriseRepository
from app.schemas.remediation import RemediationPlanRequest
from app.tools.filesystem_tools import file_sha256, validate_allowed_path
from app.tools.remediation_tools import execute_file_remediation


remediation_logger = logging.getLogger("sentineldlp.remediation")


def _normalise_path(value: str) -> str:
    return os.path.normcase(os.path.abspath(os.path.expanduser(value)))


def _status_value(value: Any) -> str:
    return value.value if hasattr(value, "value") else str(value)


class RemediationService:
    def __init__(
        self,
        db: Session,
        planner: RemediationPlannerAgent | None = None,
    ):
        self.db = db
        self.scan_repo = EnterpriseRepository(db)
        self.planner = planner or RemediationPlannerAgent()

    def plan(self, user: User, payload: RemediationPlanRequest) -> RemediationJob:
        scan = self.scan_repo.get_scan(payload.scan_id, user.id)

        if scan is None:
            raise ValueError("Scan not found")

        asset_type = _status_value(scan.asset.asset_type) if scan.asset else ""

        if asset_type != "system":
            raise ValueError("File remediation is available only for system scans")

        try:
            file_path = validate_allowed_path(payload.file_path)
        except FileNotFoundError as error:
            raise ValueError("Selected remediation file no longer exists") from error

        if not file_path.is_file():
            raise ValueError("Selected remediation target is not a file")

        findings = self._file_findings(scan, file_path, payload.finding_indexes)

        if not findings:
            raise ValueError("No verified findings belong to the selected file")

        remediation_logger.info(
            "REMEDIATION_PLAN_REQUEST scan_id=%s user_id=%s file=%s "
            "requested_action=%s findings=%s",
            scan.id,
            user.id,
            file_path.name,
            payload.requested_action or "ai_recommendation",
            len(findings),
        )

        expected_hash = self._expected_hash(scan, file_path, findings)
        current_hash = file_sha256(file_path)

        if expected_hash and current_hash != expected_hash:
            raise ValueError(
                "File changed after scanning. Run a fresh scan before remediation."
            )

        planner_output = self.planner.plan(
            file_path=str(file_path),
            findings=findings,
            requested_action=payload.requested_action,
            reason=payload.reason,
        )
        action = RemediationAction(planner_output["recommended_action"])
        entity_types = sorted(
            {str(item.get("entity_type", "UNKNOWN")) for item in findings}
        )
        preview = {
            "file_name": file_path.name,
            "file_type": file_path.suffix.lower(),
            "file_size_bytes": file_path.stat().st_size,
            "affected_findings": len(findings),
            "entity_types": entity_types,
            "masked_examples": [
                {
                    "entity_type": item.get("entity_type"),
                    "masked_value": item.get("masked_value"),
                    "risk_level": item.get("risk_level"),
                }
                for item in findings[:20]
            ],
            "changes_source_file": True,
            "encrypted_backup_created": True,
            "verification_rescan": action in {
                RemediationAction.MASK,
                RemediationAction.REDACT,
            },
        }
        job = RemediationJob(
            scan_id=scan.id,
            user_id=user.id,
            file_path=str(file_path),
            original_sha256=current_hash,
            action=action,
            status=RemediationStatus.AWAITING_APPROVAL,
            entity_types=entity_types,
            finding_indexes=payload.finding_indexes,
            planner_output=planner_output,
            preview=preview,
            approval_required=True,
            admin_required=action == RemediationAction.DELETE,
        )
        self.db.add(job)
        self.db.flush()
        self._audit(
            scan.id,
            user,
            "remediation_plan_created",
            {
                "job_id": job.id,
                "action": action.value,
                "file_sha256": current_hash,
                "planner_source": planner_output.get("planner_source"),
                "affected_findings": len(findings),
            },
        )
        self.db.commit()
        self.db.refresh(job)
        remediation_logger.info(
            "REMEDIATION_PLAN_CREATED scan_id=%s job_id=%s action=%s "
            "file=%s findings=%s planner=%s approval_required=true",
            scan.id,
            job.id,
            action.value,
            file_path.name,
            len(findings),
            planner_output.get("planner_source", "bounded"),
        )
        return job

    def decide(
        self,
        job_id: int,
        user: User,
        *,
        approved: bool,
        note: str,
    ) -> RemediationJob:
        job = self.get(job_id, user.id)

        if job is None:
            raise ValueError("Remediation job not found")

        if job.status != RemediationStatus.AWAITING_APPROVAL:
            raise ValueError("Remediation job is not awaiting approval")

        if job.admin_required and user.role != UserRole.ADMIN:
            raise PermissionError("Delete remediation requires an administrator")

        job.approved_by = user.id
        job.approval_note = note
        job.approved_at = datetime.now(timezone.utc)
        job.approval_required = False

        if not approved:
            job.status = RemediationStatus.REJECTED
            self._audit(
                job.scan_id,
                user,
                "remediation_rejected",
                {"job_id": job.id, "action": job.action.value, "note": note},
            )
            self.db.commit()
            self.db.refresh(job)
            remediation_logger.info(
                "REMEDIATION_REJECTED scan_id=%s job_id=%s action=%s "
                "file=%s user_id=%s",
                job.scan_id,
                job.id,
                job.action.value,
                Path(job.file_path).name,
                user.id,
            )
            return job

        job.status = RemediationStatus.EXECUTING
        self._audit(
            job.scan_id,
            user,
            "remediation_approved",
            {"job_id": job.id, "action": job.action.value, "note": note},
        )
        self.db.commit()

        remediation_logger.info(
            "REMEDIATION_EXECUTING scan_id=%s job_id=%s action=%s "
            "file=%s user_id=%s",
            job.scan_id,
            job.id,
            job.action.value,
            Path(job.file_path).name,
            user.id,
        )

        try:
            execution_result = execute_file_remediation(
                job_id=job.id,
                file_path=job.file_path,
                expected_sha256=job.original_sha256,
                action=job.action.value,
                entity_types=set(job.entity_types or []),
            )
            job.encrypted_backup_path = str(
                execution_result.pop("encrypted_backup_path")
            )
            job.output_path = execution_result.get("output_path")
            job.result = execution_result
            job.status = RemediationStatus.COMPLETED
            job.executed_at = datetime.now(timezone.utc)
            job.error_message = None
            self._audit(
                job.scan_id,
                user,
                "remediation_completed",
                {
                    "job_id": job.id,
                    "action": job.action.value,
                    "verified": execution_result.get("verified"),
                    "replacements": execution_result.get("replacements"),
                    "output_sha256": execution_result.get("output_sha256"),
                },
            )
            remediation_logger.info(
                "REMEDIATION_COMPLETED scan_id=%s job_id=%s action=%s "
                "file=%s verified=%s replacements=%s",
                job.scan_id,
                job.id,
                job.action.value,
                Path(job.file_path).name,
                execution_result.get("verified"),
                execution_result.get("replacements", 0),
            )
        except Exception as error:
            job.status = RemediationStatus.FAILED
            job.error_message = str(error)
            self._audit(
                job.scan_id,
                user,
                "remediation_failed",
                {
                    "job_id": job.id,
                    "action": job.action.value,
                    "error_type": type(error).__name__,
                    "message": str(error),
                },
            )
            remediation_logger.exception(
                "REMEDIATION_FAILED scan_id=%s job_id=%s action=%s "
                "file=%s error_type=%s message=%s",
                job.scan_id,
                job.id,
                job.action.value,
                Path(job.file_path).name,
                type(error).__name__,
                str(error),
            )

        self.db.commit()
        self.db.refresh(job)
        return job

    def get(self, job_id: int, user_id: int) -> RemediationJob | None:
        return (
            self.db.query(RemediationJob)
            .filter(RemediationJob.id == job_id, RemediationJob.user_id == user_id)
            .first()
        )

    def list(self, user_id: int, scan_id: int | None = None) -> list[RemediationJob]:
        query = self.db.query(RemediationJob).filter(
            RemediationJob.user_id == user_id
        )

        if scan_id is not None:
            query = query.filter(RemediationJob.scan_id == scan_id)

        return query.order_by(RemediationJob.created_at.desc()).limit(200).all()

    @staticmethod
    def _file_findings(
        scan: AgenticScan,
        file_path: Path,
        selected_indexes: list[int],
    ) -> list[dict[str, Any]]:
        state = scan.workflow_state or {}
        findings = state.get("verified_findings") or state.get("findings") or []
        target_path = _normalise_path(str(file_path))
        indexed = [
            (index, finding)
            for index, finding in enumerate(findings)
            if _normalise_path(str((finding.get("location") or {}).get("path", "")))
            == target_path
        ]

        if selected_indexes:
            allowed = set(selected_indexes)
            indexed = [item for item in indexed if item[0] in allowed]

        return [finding for _, finding in indexed]

    @staticmethod
    def _expected_hash(
        scan: AgenticScan,
        file_path: Path,
        findings: list[dict[str, Any]],
    ) -> str | None:
        finding_hash = next(
            (
                (item.get("location") or {}).get("sha256")
                for item in findings
                if (item.get("location") or {}).get("sha256")
            ),
            None,
        )

        if finding_hash:
            return str(finding_hash)

        file_hashes = (scan.workflow_state or {}).get("file_hashes") or {}
        target = _normalise_path(str(file_path))

        return next(
            (
                str(value)
                for key, value in file_hashes.items()
                if _normalise_path(str(key)) == target
            ),
            None,
        )

    def _audit(
        self,
        scan_id: int,
        user: User,
        event_type: str,
        payload: dict[str, Any],
    ) -> None:
        self.db.add(
            AuditEvent(
                scan_id=scan_id,
                actor=f"user:{user.id}:{user.username}",
                event_type=event_type,
                payload=payload,
            )
        )
