from __future__ import annotations

from collections.abc import Callable

from app.agents.state import WorkflowState
from app.tools.filesystem_tools import scan_system_path


class SystemScanAgent:
    name = "system_scan"

    def run(
        self,
        state: WorkflowState,
        progress_callback: Callable[[WorkflowState], None] | None = None,
    ) -> WorkflowState:
        state.status = "scanning"
        existing_errors = list(state.errors)

        def apply_progress(result: dict) -> None:
            state.findings = result["findings"]
            state.scan_stats = result["stats"]
            state.file_hashes = result["file_hashes"]
            state.errors = [*existing_errors, *result["errors"]]

            if progress_callback is not None:
                progress_callback(state)

        result = scan_system_path(
            state.asset["root_path"],
            entities=set(state.requested_entities),
            previous_hashes=state.file_hashes,
            progress_callback=apply_progress,
            file_extensions=state.file_extensions,
        )
        apply_progress(result)
        state.event(
            self.name,
            "scan_system",
            "completed",
            findings=len(state.findings),
            files_scanned=state.scan_stats.get("files_scanned", 0),
        )
        return state 