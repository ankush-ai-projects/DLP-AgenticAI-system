"""Tests for planner tool-calling schemas."""
from app.agents.tool_schemas import DATABASE_TOOLS, SYSTEM_TOOLS, tool_names, tools_for_asset_type


def test_database_asset_gets_database_tools():
    assert tools_for_asset_type("database") is DATABASE_TOOLS


def test_system_asset_gets_system_tools():
    assert tools_for_asset_type("system") is SYSTEM_TOOLS


def test_every_tool_has_openai_function_calling_shape():
    for tool in DATABASE_TOOLS + SYSTEM_TOOLS:
        assert tool["type"] == "function"
        fn = tool["function"]
        assert isinstance(fn["name"], str) and fn["name"]
        assert isinstance(fn["description"], str) and fn["description"]
        assert fn["parameters"]["type"] == "object"
        assert "properties" in fn["parameters"]


def test_tool_names_match_deterministic_plan_order():
    assert tool_names("database") == [
        "test_connection", "discover_schema", "scan_database", "verify", "risk", "report",
    ]
    assert tool_names("system") == [
        "check_path", "discover_files", "scan_system", "verify", "risk", "report",
    ]


def test_scan_tools_never_allow_write_operations():
    """Every tool must be read-only -- no delete/write/execute parameters."""
    forbidden_terms = {"delete", "drop", "write", "execute", "shell", "command"}
    for tool in DATABASE_TOOLS + SYSTEM_TOOLS:
        text = str(tool).lower()
        for term in forbidden_terms:
            assert term not in text, f"{tool['function']['name']} mentions forbidden term '{term}'"
