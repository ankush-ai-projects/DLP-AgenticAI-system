"""Explicit function-calling schemas for every tool the planner may select.

Previously the planner only emitted a flat list of tool-name strings picked
from a hardcoded deterministic list. That works, but it is not real
tool-calling: there was no per-tool contract (arguments, constraints) for an
LLM to reason over, and no validation that a chosen tool's arguments made
sense. These schemas follow the OpenAI function-calling shape so they can be
passed directly as `tools=[...]` to any OpenAI-compatible chat completion
call, and are also used locally to validate the deterministic fallback plan.
"""
from __future__ import annotations

from typing import Any

DATABASE_TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "test_connection",
            "description": "Verify read-only connectivity to the target database asset before scanning.",
            "parameters": {
                "type": "object",
                "properties": {"asset_id": {"type": "integer"}},
                "required": ["asset_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "discover_schema",
            "description": "List tables/columns available for scanning, without reading row data.",
            "parameters": {
                "type": "object",
                "properties": {"asset_id": {"type": "integer"}},
                "required": ["asset_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "scan_database",
            "description": "Run the hybrid PII/PCI detector over a bounded, read-only sample of rows.",
            "parameters": {
                "type": "object",
                "properties": {
                    "asset_id": {"type": "integer"},
                    "batch_size": {"type": "integer", "minimum": 1, "maximum": 5000},
                    "row_limit": {"type": "integer", "minimum": 1, "maximum": 50000},
                    "entities": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Entity types to look for, e.g. CREDIT_CARD, SSN, EMAIL.",
                    },
                },
                "required": ["asset_id", "entities"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "verify",
            "description": "Deduplicate and validate raw detector hits into verified findings.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "risk",
            "description": "Score verified findings and decide whether human review is required.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "report",
            "description": "Produce the final, citation-grounded scan report.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]

SYSTEM_TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "check_path",
            "description": "Confirm the requested filesystem path is inside the configured allow-list.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "discover_files",
            "description": "Enumerate files under the allowed path without reading their contents.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "scan_system",
            "description": "Run the hybrid PII/PCI detector over allowlisted files.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "entities": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["path", "entities"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "verify",
            "description": "Deduplicate and validate raw detector hits into verified findings.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "risk",
            "description": "Score verified findings and decide whether human review is required.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "report",
            "description": "Produce the final, citation-grounded scan report.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]


def tools_for_asset_type(asset_type: str) -> list[dict[str, Any]]:
    return DATABASE_TOOLS if asset_type == "database" else SYSTEM_TOOLS


def tool_names(asset_type: str) -> list[str]:
    return [tool["function"]["name"] for tool in tools_for_asset_type(asset_type)]
