"""Identifier validation and database row helpers."""
from __future__ import annotations

import re
from typing import Any


SAFE_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_$#@]*$")


def require_safe_identifier(value: str) -> str:
    if not SAFE_IDENTIFIER.fullmatch(value):
        raise ValueError(f"Unsafe database identifier: {value!r}")
    return value


def quote_mysql_identifier(value: str) -> str:
    """Safely quote a MySQL identifier returned by server metadata."""
    if not value or "\x00" in value:
        raise ValueError("Invalid MySQL identifier")
    return f"`{value.replace('`', '``')}`"


def quote_mssql_identifier(value: str) -> str:
    """Safely quote an MSSQL identifier returned by server metadata."""
    if not value or "\x00" in value:
        raise ValueError("Invalid MSSQL identifier")
    return f"[{value.replace(']', ']]')}]"


def rows_to_dicts(description: Any, rows: list[Any]) -> list[dict[str, Any]]:
    names = [item[0] for item in description]
    return [dict(zip(names, row)) for row in rows]
