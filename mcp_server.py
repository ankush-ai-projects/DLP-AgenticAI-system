"""SentinelDLP MCP server.

Exposes this project's scanning capability to any MCP client (Claude
Desktop, Claude Code, or any other MCP-compatible agent) as a set of
tools, using the exact same service layer the FastAPI app uses --
AgenticScanService, EnterpriseRepository, and the connector layer -- so
there is no second implementation of scanning logic to drift out of sync.

SAFETY BOUNDARY -- read this before adding a tool here:

Only read-only, non-destructive operations are exposed:
    - list_assets            (list registered scan targets)
    - discover_schema        (list tables/columns, no row data)
    - scan_database          (bounded, read-only scan of a DB asset)
    - scan_system            (bounded, read-only scan of a filesystem asset)
    - get_scan_status         (poll status/progress)
    - get_scan_findings_summary (aggregate counts only, never raw values)

Deliberately NOT exposed here: anything from app/api/v1/endpoints/remediation.py
(plan/approve/execute mask, redact, encrypt, delete). Remediation stays
gated behind the authenticated web UI with an explicit human-approval
step (RemediationWorkspace.jsx) -- an MCP tool sitting in a chat
conversation is one ambiguous instruction away from "delete this file"
being sent by accident. If remediation is ever exposed here, it must
still require the same human-approval-required flow, not a direct
execute call.

Every finding-returning tool strips raw PII values before returning --
only entity types, counts, and risk levels cross this boundary. Same
principle as ScanMemoryStore's summaries (app/agents/memory.py).

Run standalone:
    python mcp_server.py

Or point an MCP client (e.g. Claude Desktop's config) at this file with
`python` (or the project's venv python) as the command.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

BACKEND_ROOT = Path(__file__).resolve().parent
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

from mcp.server import MCPServer  # noqa: E402
from mcp.types import ToolAnnotations  # noqa: E402

from app.connectors import build_database_connector  # noqa: E402
from app.core.dependencies import _get_or_create_dev_user  # noqa: E402
from app.db.session import SessionLocal  # noqa: E402
from app.repositories.enterprise_repo import EnterpriseRepository  # noqa: E402
from app.schemas.enterprise import ScanGoalRequest  # noqa: E402
from app.services.agentic_scan_service import (  # noqa: E402
    AgenticScanService,
    asset_to_state,
)
from app.tools.database_tools import build_connector_config  # noqa: E402
from app.core.secrets import EnvironmentSecretProvider  # noqa: E402
from app.db.session import engine  # noqa: E402
from app.models.base import Base  # noqa: E402
import app.models  # noqa: E402,F401 -- registers every model on Base.metadata

# This server can run standalone (not through the FastAPI app, which
# normally creates tables in its startup lifespan) -- so it needs to do
# the same table-creation step itself the first time it runs.
Base.metadata.create_all(bind=engine)

READ_ONLY = ToolAnnotations(read_only_hint=True, destructive_hint=False)

server = MCPServer(
    name="sentineldlp",
    title="SentinelDLP AI",
    description=(
        "Read-only DLP scanning over registered database and filesystem "
        "assets. Remediation (mask/redact/encrypt/delete) is intentionally "
        "not available here -- use the SentinelDLP web app for that, "
        "where every remediation action requires explicit human approval."
    ),
)


def _summarize_findings(verified_findings: list[dict[str, Any]]) -> dict[str, int]:
    """Aggregate-only view -- never returns a raw finding value."""
    counts: dict[str, int] = {}
    for finding in verified_findings:
        entity_type = finding.get("entity_type", "UNKNOWN")
        counts[entity_type] = counts.get(entity_type, 0) + 1
    return counts


@server.tool(
    name="list_assets",
    description="List registered scan targets (databases and filesystem roots). No credentials or scan data included.",
    annotations=READ_ONLY,
)
def list_assets() -> list[dict[str, Any]]:
    db = SessionLocal()
    try:
        user = _get_or_create_dev_user(db)
        repo = EnterpriseRepository(db)
        assets = repo.list_assets(user.id)
        return [
            {
                "asset_id": asset.id,
                "name": asset.name,
                "asset_type": asset.asset_type.value if hasattr(asset.asset_type, "value") else str(asset.asset_type),
                "platform": asset.platform,
            }
            for asset in assets
        ]
    finally:
        db.close()


@server.tool(
    name="discover_schema",
    description="List tables and column names for a registered database asset. Returns structure only -- no row data.",
    annotations=READ_ONLY,
)
def discover_schema(asset_id: int) -> dict[str, Any]:
    db = SessionLocal()
    try:
        user = _get_or_create_dev_user(db)
        repo = EnterpriseRepository(db)
        asset = repo.get_asset(asset_id, user.id)
        if not asset:
            return {"error": f"No asset found with id {asset_id}"}
        if asset.asset_type.value != "database":
            return {"error": "discover_schema only applies to database assets"}

        state_asset = asset_to_state(asset)
        config = build_connector_config(state_asset, EnvironmentSecretProvider())
        connector = build_database_connector(asset.platform, config)
        tables = connector.discover_schema()
        return {
            "asset_id": asset_id,
            "tables": [
                {"table": table.name, "columns": [c.name for c in table.columns]}
                for table in tables
            ],
        }
    finally:
        db.close()


def _run_scan(
    *,
    asset_id: int,
    goal: str,
    entities: list[str] | None,
    expected_asset_type: str,
) -> dict[str, Any]:
    """Shared execution path for scan_database and scan_system.

    Kept as one internal helper (not two copies of the same logic) while
    still exposing two distinct, specifically-named/described public MCP
    tools -- separate tools give the calling LLM a much stronger signal
    for tool selection than one generic "start_scan" would, at the cost
    of this one small duplication-avoiding wrapper.
    """
    db = SessionLocal()
    try:
        user = _get_or_create_dev_user(db)
        repo = EnterpriseRepository(db)
        asset = repo.get_asset(asset_id, user.id)
        if not asset:
            return {"error": f"No asset found with id {asset_id}"}
        actual_type = asset.asset_type.value if hasattr(asset.asset_type, "value") else str(asset.asset_type)
        if actual_type != expected_asset_type:
            return {
                "error": (
                    f"Asset {asset_id} is a '{actual_type}' asset. "
                    f"Use {'scan_system' if expected_asset_type == 'database' else 'scan_database'} for it instead."
                )
            }

        service = AgenticScanService(db)
        payload = ScanGoalRequest(
            asset_id=asset_id,
            goal=goal,
            entities=entities or ["CREDIT_CARD", "AADHAAR", "PAN", "EMAIL", "PHONE"],
        )
        scan = service.create(user.id, payload)
        scan = service.execute(scan.id, user.id)
        state = scan.workflow_state or {}
        return {
            "scan_id": scan.id,
            "status": state.get("status"),
            "approval_required": state.get("approval_required", False),
            "risk_summary": state.get("risk_summary", {}),
            "findings_by_entity_type": _summarize_findings(state.get("verified_findings", [])),
        }
    except ValueError as error:
        return {"error": str(error)}
    finally:
        db.close()


@server.tool(
    name="scan_database",
    description=(
        "Scan a registered DATABASE asset (MySQL, MSSQL, or SQLite) for "
        "PII/PCI. Runs the full Planner/Specialist/Critic/Risk/Reporting "
        "workflow, read-only, and returns a masked risk summary -- never "
        "raw sensitive values. Critical findings still require human "
        "review in the web app before any remediation."
    ),
    annotations=READ_ONLY,
)
def scan_database(
    asset_id: int,
    goal: str,
    entities: list[str] | None = None,
) -> dict[str, Any]:
    return _run_scan(
        asset_id=asset_id, goal=goal, entities=entities, expected_asset_type="database"
    )


@server.tool(
    name="scan_system",
    description=(
        "Scan a registered filesystem (Windows/Linux) asset for PII/PCI, "
        "restricted to its allowlisted root path. Runs the full "
        "Planner/Specialist/Critic/Risk/Reporting workflow, read-only, and "
        "returns a masked risk summary -- never raw sensitive values. "
        "Critical findings still require human review in the web app "
        "before any remediation."
    ),
    annotations=READ_ONLY,
)
def scan_system(
    asset_id: int,
    goal: str,
    entities: list[str] | None = None,
) -> dict[str, Any]:
    return _run_scan(
        asset_id=asset_id, goal=goal, entities=entities, expected_asset_type="system"
    )


@server.tool(
    name="get_scan_status",
    description="Check the status and masked risk summary of a previously started scan.",
    annotations=READ_ONLY,
)
def get_scan_status(scan_id: int) -> dict[str, Any]:
    db = SessionLocal()
    try:
        user = _get_or_create_dev_user(db)
        repo = EnterpriseRepository(db)
        scan = repo.get_scan(scan_id, user.id)
        if not scan:
            return {"error": f"No scan found with id {scan_id}"}
        state = scan.workflow_state or {}
        return {
            "scan_id": scan.id,
            "status": state.get("status"),
            "approval_required": state.get("approval_required", False),
            "risk_summary": state.get("risk_summary", {}),
            "findings_by_entity_type": _summarize_findings(state.get("verified_findings", [])),
        }
    finally:
        db.close()


if __name__ == "__main__":
    server.run(transport="stdio")
