"""MCP server tests.

The one property that must never regress: no tool here returns a raw
finding value -- only aggregate counts and risk labels. See the safety
boundary comment at the top of mcp_server.py.
"""
import json

import pytest

pytest.importorskip("mcp")


@pytest.fixture
def mcp_tools(tmp_path, monkeypatch):
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{tmp_path}/mcp_test.db")
    monkeypatch.setenv("SYSTEM_SCAN_ALLOWED_ROOTS", str(tmp_path))

    import importlib

    import app.core.config as config_module
    importlib.reload(config_module)

    import app.db.session as session_module
    importlib.reload(session_module)

    import mcp_server
    importlib.reload(mcp_server)

    return mcp_server


def test_registered_tools_are_all_read_only(mcp_tools):
    """Every tool must be explicitly marked read-only/non-destructive."""
    for tool in mcp_tools.server._tool_manager.list_tools():
        assert tool.annotations is not None
        assert tool.annotations.read_only_hint is True
        assert tool.annotations.destructive_hint is False


def test_no_remediation_tools_are_registered(mcp_tools):
    """Remediation must never be reachable from this server."""
    tool_names = {tool.name for tool in mcp_tools.server._tool_manager.list_tools()}
    forbidden = {"mask", "redact", "encrypt", "delete", "remediate", "approve"}
    assert not (tool_names & forbidden)


def test_scan_system_never_returns_raw_pii(mcp_tools, tmp_path):
    sample = tmp_path / "sample.txt"
    sample.write_text(
        "Email: rahul.sharma@gmail.com Phone: 9876543210 PAN: ABCDE1234F",
        encoding="utf-8",
    )

    from app.core.dependencies import _get_or_create_dev_user
    from app.db.session import SessionLocal
    from app.repositories.enterprise_repo import EnterpriseRepository
    from app.schemas.enterprise import AssetCreate

    db = SessionLocal()
    user = _get_or_create_dev_user(db)
    repo = EnterpriseRepository(db)
    asset = repo.create_asset(
        user.id,
        AssetCreate(
            name="pii-leak-check",
            asset_type="system",
            platform="linux",
            root_path=str(tmp_path),
        ),
    )
    db.close()

    result = mcp_tools.scan_system(
        asset_id=asset.id, goal="Check for PII leakage in MCP tool output"
    )
    serialized = json.dumps(result)

    for raw_value in ("rahul.sharma@gmail.com", "9876543210", "ABCDE1234F"):
        assert raw_value not in serialized

    assert "findings_by_entity_type" in result
    assert isinstance(result["findings_by_entity_type"], dict)


def test_list_assets_excludes_credentials(mcp_tools):
    for asset in mcp_tools.list_assets():
        assert "secret_ref" not in asset
        assert "config" not in asset
        assert "password" not in json.dumps(asset).lower()


def test_scan_database_rejects_a_system_asset(mcp_tools, tmp_path):
    from app.core.dependencies import _get_or_create_dev_user
    from app.db.session import SessionLocal
    from app.repositories.enterprise_repo import EnterpriseRepository
    from app.schemas.enterprise import AssetCreate

    db = SessionLocal()
    user = _get_or_create_dev_user(db)
    repo = EnterpriseRepository(db)
    asset = repo.create_asset(
        user.id,
        AssetCreate(
            name="wrong-tool-check",
            asset_type="system",
            platform="linux",
            root_path=str(tmp_path),
        ),
    )
    db.close()

    result = mcp_tools.scan_database(asset_id=asset.id, goal="Should be rejected")

    assert "error" in result
    assert "scan_system" in result["error"]
