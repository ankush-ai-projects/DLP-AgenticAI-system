"""Connector factory with an intentionally small platform allowlist."""
from __future__ import annotations

from typing import Any

from app.connectors.base import DatabaseConnector


def discover_databases(platform: str, config: dict[str, Any]) -> list[str]:
    """Discover databases through a platform-specific read-only connection."""
    platform = platform.lower().strip()
    if platform == "mysql":
        from app.connectors.mysql import discover_mysql_databases

        return discover_mysql_databases(**config)
    if platform == "mssql":
        from app.connectors.mssql import discover_mssql_databases

        return discover_mssql_databases(**config)
    raise ValueError(f"Database discovery is not supported for platform: {platform}")


def build_database_connector(platform: str, config: dict[str, Any]) -> DatabaseConnector:
    platform = platform.lower().strip()
    if platform == "mysql":
        from app.connectors.mysql import MySQLConnector
        return MySQLConnector(**config)
    if platform == "mssql":
        from app.connectors.mssql import MSSQLConnector
        return MSSQLConnector(**config)
    if platform == "sqlite":
        from app.connectors.sqlite import SQLiteConnector
        return SQLiteConnector(database=config["database"])
    raise ValueError(f"Unsupported database platform: {platform}")
