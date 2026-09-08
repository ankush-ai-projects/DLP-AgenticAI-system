"""Default durable LangGraph runtime for the bounded DLP agent workflow."""
from __future__ import annotations

import threading
from collections.abc import Callable
from pathlib import Path
from typing import Any, TypedDict

from app.agents.state import WorkflowState
from app.agents.supervisor import SupervisorAgent
from app.core.config import settings


class GraphState(TypedDict, total=False):
    scan_id: int | None
    goal: str
    asset: dict[str, Any]
    requested_entities: list[str]
    file_extensions: list[str] | None
    batch_size: int
    row_limit: int
    require_human_review_for_critical: bool
    dry_run: bool
    status: str
    plan: dict[str, Any]
    findings: list[dict[str, Any]]
    verified_findings: list[dict[str, Any]]
    scan_stats: dict[str, Any]
    risk_summary: dict[str, Any]
    policy_decision: dict[str, Any]
    report: dict[str, Any]
    file_hashes: dict[str, str]
    errors: list[dict[str, Any]]
    events: list[dict[str, Any]]
    retry_count: int
    iteration_count: int
    approval_required: bool
    human_decision: str | None
    last_error: dict[str, Any] | None
    runtime: str
    thread_id: str | None
    memory_context: str


def _dump(state: WorkflowState) -> GraphState:
    return state.model_dump(mode="json")


ProgressCallback = Callable[[WorkflowState], None]


def build_langgraph(
    supervisor: SupervisorAgent | None = None,
    checkpointer=None,
    progress_callback: ProgressCallback | None = None,
):
    """Build the real orchestration graph; tools remain bounded inside agents."""
    try:
        from langgraph.graph import END, START, StateGraph
        from langgraph.types import interrupt 
    except ImportError as exc:
        raise RuntimeError(
            "LangGraph is required. Install dependencies with: pip install -r requirements.txt"
        ) from exc

    supervisor = supervisor or SupervisorAgent()

    def finish_node(state: WorkflowState) -> GraphState:
        if progress_callback is not None:
            progress_callback(state)
        return _dump(state)

    def plan_node(raw: GraphState) -> GraphState:
        state = WorkflowState.model_validate(raw)
        state.iteration_count += 1
        if state.iteration_count > settings.MAX_AGENT_ITERATIONS:
            state.last_error = {
                "stage": "planning",
                "error": "IterationLimitExceeded",
                "message": "Maximum agent iterations exceeded",
            }
            state.errors.append(state.last_error)
            state.event("langgraph", "iteration_guard", "failed")
            return finish_node(state)
        try:
            supervisor.planner.run(state)
            state.last_error = None
        except Exception as exc:
            state.last_error = {
                "stage": "planning",
                "error": type(exc).__name__,
                "message": str(exc),
            }
            state.errors.append(state.last_error)
            state.event("planner", "create_plan", "failed", error_type=type(exc).__name__)
        return finish_node(state)

    def scan_node(raw: GraphState) -> GraphState:
        state = WorkflowState.model_validate(raw)
        try:
            specialist = (
                supervisor.database
                if state.asset["asset_type"] == "database"
                else supervisor.system
            )
            specialist.run(
                state,
                progress_callback=progress_callback,
            )
            state.last_error = None
        except Exception as exc:
            state.retry_count += 1
            state.last_error = {
                "stage": state.status,
                "error": type(exc).__name__,
                "message": str(exc),
                "attempt": state.retry_count,
            }
            state.errors.append(state.last_error)
            state.event(
                "langgraph",
                "specialist_retry",
                "failed",
                attempt=state.retry_count,
                error_type=type(exc).__name__,
            )
        return finish_node(state)

    def verify_node(raw: GraphState) -> GraphState:
        state = WorkflowState.model_validate(raw)
        try:
            supervisor.critic.run(state)
            state.last_error = None
        except Exception as exc:
            state.last_error = {
                "stage": "verifying",
                "error": type(exc).__name__,
                "message": str(exc),
            }
            state.errors.append(state.last_error)
            state.event("critic", "verify_findings", "failed", error_type=type(exc).__name__)
        return finish_node(state)

    def risk_node(raw: GraphState) -> GraphState:
        state = WorkflowState.model_validate(raw)
        try:
            supervisor.risk.run(state)
            state.last_error = None
        except Exception as exc:
            state.last_error = {
                "stage": "risk_analysis",
                "error": type(exc).__name__,
                "message": str(exc),
            }
            state.errors.append(state.last_error)
            state.event("risk_policy", "calculate_risk", "failed", error_type=type(exc).__name__)
        return finish_node(state)

    def review_node(raw: GraphState) -> GraphState:
        state = WorkflowState.model_validate(raw)
        decision = interrupt(
            {
                "scan_id": state.scan_id,
                "reason": "Critical DLP risk",
                "risk": state.risk_summary,
            }
        )
        approved = bool(decision.get("approved"))
        state.human_decision = "approved" if approved else "rejected"
        state.approval_required = False
        state.policy_decision["human_decision"] = state.human_decision
        state.policy_decision["review_note"] = str(decision.get("note", ""))[:1000]
        if not approved:
            state.policy_decision["action"] = "rejected_by_human"
        state.event(
            "human_review",
            "resume_checkpoint",
            "completed",
            decision=state.human_decision,
        )
        return finish_node(state)

    def report_node(raw: GraphState) -> GraphState:
        state = WorkflowState.model_validate(raw)
        try:
            supervisor.reporting.run(state)
            state.last_error = None
        except Exception as exc:
            state.last_error = {
                "stage": "reporting",
                "error": type(exc).__name__,
                "message": str(exc),
            }
            state.errors.append(state.last_error)
            state.event("reporting", "generate_report", "failed", error_type=type(exc).__name__)
        return finish_node(state)

    def failure_node(raw: GraphState) -> GraphState:
        state = WorkflowState.model_validate(raw)
        state.status = "failed"
        state.approval_required = False
        state.event(
            "langgraph",
            "workflow_failed",
            "failed",
            retry_count=state.retry_count,
        )
        return finish_node(state)

    def after_plan(raw: GraphState) -> str:
        return "failure" if raw.get("last_error") else "scan"

    def after_scan(raw: GraphState) -> str:
        if not raw.get("last_error"):
            return "verify"
        return (
            "planner"
            if int(raw.get("retry_count", 0)) < settings.MAX_AGENT_RETRIES
            else "failure"
        )

    def after_risk(raw: GraphState) -> str:
        if raw.get("last_error"):
            return "failure"
        return "review" if raw.get("approval_required") else "reporter"

    graph = StateGraph(GraphState)
    graph.add_node("planner", plan_node)
    graph.add_node("scan", scan_node)
    graph.add_node("verify", verify_node)
    graph.add_node("risk", risk_node)
    graph.add_node("review", review_node)
    graph.add_node("reporter", report_node)
    graph.add_node("failure", failure_node)
    graph.add_edge(START, "planner")
    graph.add_conditional_edges(
        "planner", after_plan, {"scan": "scan", "failure": "failure"}
    )
    graph.add_conditional_edges(
        "scan",
        after_scan,
        {"planner": "planner", "verify": "verify", "failure": "failure"},
    )
    graph.add_conditional_edges(
        "verify",
        lambda raw: "failure" if raw.get("last_error") else "risk",
        {"risk": "risk", "failure": "failure"},
    )
    graph.add_conditional_edges(
        "risk",
        after_risk,
        {"review": "review", "reporter": "reporter", "failure": "failure"},
    )
    graph.add_edge("review", "reporter")
    graph.add_conditional_edges(
        "reporter",
        lambda raw: "failure" if raw.get("last_error") else "done",
        {"done": END, "failure": "failure"},
    )
    graph.add_edge("failure", END)
    return graph.compile(checkpointer=checkpointer)


class LangGraphRuntime:
    """Owns a durable checkpointer and exposes invoke/resume operations."""

    def __init__(self, checkpointer=None):
        self._checkpointer_context = None
        self._progress_callbacks: dict[int, ProgressCallback] = {}
        self._progress_lock = threading.RLock()
        self.checkpointer = checkpointer or self._open_checkpointer()
        self.graph = build_langgraph(
            checkpointer=self.checkpointer,
            progress_callback=self._publish_progress,
        )

    def _publish_progress(self, state: WorkflowState) -> None:
        if state.scan_id is None:
            return

        with self._progress_lock:
            callback = self._progress_callbacks.get(state.scan_id)

        if callback is not None:
            callback(state)

    def _open_checkpointer(self):
        mode = settings.LANGGRAPH_CHECKPOINTER.lower().strip()
        postgres_url = settings.LANGGRAPH_POSTGRES_URL
        if mode == "auto" and not postgres_url and settings.DATABASE_URL.startswith(
            ("postgresql://", "postgres://")
        ):
            postgres_url = settings.DATABASE_URL

        if mode == "postgres" or (mode == "auto" and postgres_url):
            if not postgres_url:
                raise RuntimeError("LANGGRAPH_POSTGRES_URL is required for postgres checkpoints")
            try:
                from langgraph.checkpoint.postgres import PostgresSaver
            except ImportError as exc:
                raise RuntimeError("Install langgraph-checkpoint-postgres and psycopg") from exc
            self._checkpointer_context = PostgresSaver.from_conn_string(postgres_url)
            saver = self._checkpointer_context.__enter__()
            saver.setup()
            return saver

        if mode not in {"auto", "sqlite"}:
            raise RuntimeError("LANGGRAPH_CHECKPOINTER must be auto, sqlite, or postgres")
        try:
            from langgraph.checkpoint.sqlite import SqliteSaver
        except ImportError as exc:
            raise RuntimeError("Install langgraph-checkpoint-sqlite") from exc
        checkpoint_path = Path(settings.LANGGRAPH_SQLITE_PATH).expanduser().resolve()
        checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        self._checkpointer_context = SqliteSaver.from_conn_string(str(checkpoint_path))
        return self._checkpointer_context.__enter__()

    @staticmethod
    def thread_id(scan_id: int) -> str:
        return f"dlp-scan-{scan_id}"

    @staticmethod
    def _config(scan_id: int) -> dict[str, Any]:
        return {"configurable": {"thread_id": LangGraphRuntime.thread_id(scan_id)}}

    def invoke(self, state: WorkflowState) -> WorkflowState:
        if state.scan_id is None:
            raise ValueError("scan_id is required before invoking LangGraph")
        state.runtime = "langgraph"
        state.thread_id = self.thread_id(state.scan_id)
        result = self.graph.invoke(_dump(state), config=self._config(state.scan_id))
        clean = {key: value for key, value in result.items() if key != "__interrupt__"}
        current = WorkflowState.model_validate(clean)
        if result.get("__interrupt__"):
            current.status = "awaiting_review"
            current.approval_required = True
        return current

    def invoke_with_progress(
        self,
        state: WorkflowState,
        progress_callback: ProgressCallback,
    ) -> WorkflowState:
        """Invoke a scan while publishing each completed workflow stage."""
        if state.scan_id is None:
            raise ValueError("scan_id is required before invoking LangGraph")

        with self._progress_lock:
            self._progress_callbacks[state.scan_id] = progress_callback

        try:
            return self.invoke(state)
        finally:
            with self._progress_lock:
                self._progress_callbacks.pop(state.scan_id, None)

    def resume(self, scan_id: int, *, approved: bool, note: str = "") -> WorkflowState:
        try:
            from langgraph.types import Command
        except ImportError as exc:
            raise RuntimeError("LangGraph is required to resume a scan") from exc
        result = self.graph.invoke(
            Command(resume={"approved": approved, "note": note}),
            config=self._config(scan_id),
        )
        clean = {key: value for key, value in result.items() if key != "__interrupt__"}
        if result.get("__interrupt__"):
            raise RuntimeError("Workflow paused again while processing the review decision")
        return WorkflowState.model_validate(clean)

    def close(self) -> None:
        if self._checkpointer_context is not None:
            self._checkpointer_context.__exit__(None, None, None)
            self._checkpointer_context = None


_runtime: LangGraphRuntime | None = None
_runtime_lock = threading.Lock()


def get_langgraph_runtime() -> LangGraphRuntime:
    global _runtime
    if _runtime is None:
        with _runtime_lock:
            if _runtime is None:
                _runtime = LangGraphRuntime()
    return _runtime


def close_langgraph_runtime() -> None:
    global _runtime
    with _runtime_lock:
        if _runtime is not None:
            _runtime.close()
            _runtime = None  