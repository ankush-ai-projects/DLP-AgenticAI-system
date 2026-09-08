from __future__ import annotations

from collections.abc import Callable

from app.agents.state import WorkflowState
from app.core.secrets import EnvironmentSecretProvider, SecretProvider
from app.tools.database_tools import scan_database


class DatabaseScanAgent:
    name = "database_scan"

    def __init__(self, secret_provider: SecretProvider | None = None):
        self.secret_provider = secret_provider or EnvironmentSecretProvider()

    def run(
        self,
        state: WorkflowState,
        progress_callback: Callable[[WorkflowState], None] | None = None,
    ) -> WorkflowState:
        state.status = "scanning"

        def apply_progress(progress: dict) -> None:
            state.findings = progress["findings"]
            state.scan_stats = progress["stats"]

            if progress_callback is not None:
                progress_callback(state)

        result = scan_database(
            state.asset,
            entities=set(state.requested_entities),
            batch_size=state.batch_size,
            row_limit=state.row_limit,
            secret_provider=self.secret_provider,
            progress_callback=apply_progress,
        )
        state.findings = result["findings"]
        state.scan_stats = result["stats"]
        state.scan_stats["connection"] = result["connection"]
        state.event(
            self.name,
            "scan_database",
            "completed",
            findings=len(state.findings),
            rows_scanned=state.scan_stats.get("rows_scanned", 0),
        )
        return state
