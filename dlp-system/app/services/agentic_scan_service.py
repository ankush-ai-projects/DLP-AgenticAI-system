"""Application service connecting persistence to the agent runtime."""

from __future__ import annotations

import logging
import time

from sqlalchemy.orm import Session

from app.agents.memory import ScanMemoryStore, summarize_for_prompt
from app.agents.state import WorkflowState
from app.models.enterprise import AgenticScan
from app.repositories.enterprise_repo import EnterpriseRepository
from app.schemas.enterprise import ScanGoalRequest
from app.workflows.langgraph_runtime import (
    LangGraphRuntime,
    get_langgraph_runtime,
)

_TERMINAL_STATUSES = {"completed", "failed"}
scan_logger = logging.getLogger("sentineldlp.scan")


def _progress_percent(stats: dict) -> int:
    """Return a safe progress percentage for lifecycle logging."""
    try:
        return max(0, min(100, int(stats.get("progress_percent", 0))))
    except (TypeError, ValueError):
        return 0


def asset_to_state(asset) -> dict:
    """Convert a persisted asset into workflow state."""
    asset_type = (
        asset.asset_type.value
        if hasattr(asset.asset_type, "value")
        else str(asset.asset_type)
    )

    return {
        "id": asset.id,
        "name": asset.name,
        "asset_type": asset_type,
        "platform": asset.platform,
        "host": asset.host,
        "port": asset.port,
        "database_name": asset.database_name,
        "root_path": asset.root_path,
        "secret_ref": asset.secret_ref,
        "config": asset.config or {},
    }


class AgenticScanService:
    """Create, execute and review agentic DLP scans."""

    def __init__(
        self,
        db: Session,
        runtime: LangGraphRuntime | None = None,
    ):
        self.db = db
        self.repo = EnterpriseRepository(db)
        self.runtime = runtime or get_langgraph_runtime()

    def create(
        self,
        user_id: int,
        payload: ScanGoalRequest,
    ) -> AgenticScan:
        """Create the initial persisted scan state."""
        asset = self.repo.get_asset(
            payload.asset_id,
            user_id,
        )

        if not asset:
            raise ValueError("Asset not found")

        prior_memories = ScanMemoryStore(self.db).recall(asset.id)

        state = WorkflowState(
            goal=payload.goal,
            asset=asset_to_state(asset),
            requested_entities=payload.entities,
            file_extensions=payload.file_extensions,
            batch_size=payload.batch_size,
            row_limit=payload.sample_limit_per_table,
            require_human_review_for_critical=(
                payload.require_human_review_for_critical
            ),
            dry_run=payload.dry_run,
            memory_context=summarize_for_prompt(prior_memories),
        )

        scan = self.repo.create_scan(
            user_id=user_id,
            asset_id=asset.id,
            goal=payload.goal,
            initial_state=state.model_dump(
                mode="json",
            ),
        )

        state.scan_id = scan.id
        scan.workflow_state = state.model_dump(
            mode="json",
        )

        self.db.commit()

        asset_type = (
            asset.asset_type.value
            if hasattr(asset.asset_type, "value")
            else str(asset.asset_type)
        )
        scan_logger.info(
            "SCAN_CREATED scan_id=%s type=%s host=%s target=%s entities=%s",
            scan.id,
            asset_type,
            asset.host or "local",
            asset.root_path if asset_type == "system" else asset.database_name,
            ",".join(payload.entities),
        )

        return scan

    def execute(
        self,
        scan_id: int,
        user_id: int | None = None,
    ) -> AgenticScan:
        """Execute and persist every workflow stage."""
        started_at = time.monotonic()
        scan = self.repo.get_scan(
            scan_id,
            user_id,
        )

        if not scan:
            raise ValueError("Scan not found")

        state = WorkflowState.model_validate(
            scan.workflow_state,
        )

        state.scan_id = scan.id
        last_logged_stage: str | None = None
        last_logged_progress = -5

        scan_logger.info(
            "SCAN_STARTED scan_id=%s type=%s host=%s runtime=langgraph",
            scan.id,
            state.asset.get("asset_type", "unknown"),
            state.asset.get("host") or "local",
        )

        def persist_progress(
            progress_state: WorkflowState,
        ) -> None:
            nonlocal last_logged_progress, last_logged_stage
            self.repo.save_workflow(
                scan,
                progress_state.model_dump(
                    mode="json",
                ),
            )
            stats = progress_state.scan_stats or {}
            progress = _progress_percent(stats)
            progress_bucket = progress - (progress % 5)
            stage = progress_state.status
            stage_changed = stage != last_logged_stage
            progress_changed = progress_bucket >= last_logged_progress + 5

            if stage_changed or progress_changed or progress == 100:
                scan_logger.info(
                    "SCAN_PROGRESS scan_id=%s stage=%s progress=%s%% "
                    "files=%s/%s tables=%s/%s rows=%s bytes=%s "
                    "findings=%s errors=%s",
                    scan.id,
                    stage,
                    progress,
                    stats.get("files_processed", stats.get("files_scanned", 0)),
                    stats.get("total_files", stats.get("files_discovered", 0)),
                    stats.get("tables_processed", stats.get("tables_scanned", 0)),
                    stats.get("total_tables", stats.get("tables_discovered", 0)),
                    stats.get("rows_scanned", 0),
                    stats.get("bytes_processed", stats.get("bytes_scanned", 0)),
                    len(progress_state.findings),
                    len(progress_state.errors),
                )
                last_logged_stage = stage
                last_logged_progress = max(last_logged_progress, progress_bucket)

        if hasattr(
            self.runtime,
            "invoke_with_progress",
        ):
            result = self.runtime.invoke_with_progress(
                state,
                persist_progress,
            )
        else:
            result = self.runtime.invoke(state)

        saved = self.repo.save_workflow(
            scan,
            result.model_dump(mode="json"),
        )

        if result.approval_required:
            self.repo.ensure_pending_review(
                scan.id,
                "Critical risk requires analyst approval",
            )
        elif result.status in _TERMINAL_STATUSES:
            ScanMemoryStore(self.db).remember(scan.asset_id, result)

        scan_logger.info(
            "SCAN_FINISHED scan_id=%s status=%s duration=%.2fs "
            "findings=%s verified=%s files=%s tables=%s rows=%s bytes=%s errors=%s",
            scan.id,
            result.status,
            time.monotonic() - started_at,
            len(result.findings),
            len(result.verified_findings),
            result.scan_stats.get("files_scanned", 0),
            result.scan_stats.get("tables_scanned", 0),
            result.scan_stats.get("rows_scanned", 0),
            result.scan_stats.get("bytes_scanned", 0),
            len(result.errors),
        )

        return saved

    def approve(
        self,
        scan_id: int,
        user_id: int,
        approved: bool,
        note: str,
    ) -> AgenticScan:
        """Resume a scan after an analyst decision."""
        scan = self.repo.get_scan(
            scan_id,
            user_id,
        )

        if not scan:
            raise ValueError("Scan not found")

        state = WorkflowState.model_validate(
            scan.workflow_state,
        )

        if (
            state.status != "awaiting_review"
            or not state.approval_required
        ):
            raise ValueError(
                "Scan is not waiting for review"
            )

        result = self.runtime.resume(
            scan.id,
            approved=approved,
            note=note,
        )

        self.repo.decide_review(
            scan_id,
            user_id=user_id,
            approved=approved,
            note=note,
        )

        saved = self.repo.save_workflow(
            scan,
            result.model_dump(mode="json"),
        )

        if result.status in _TERMINAL_STATUSES:
            ScanMemoryStore(self.db).remember(scan.asset_id, result)

        return saved 
