"""Bounded database discovery and scan tools used by the Database Agent."""
from __future__ import annotations

from collections import Counter
from collections.abc import Callable
from typing import Any

from app.connectors import build_database_connector
from app.connectors.base import TableInfo
from app.core.secrets import (
    CREDENTIAL_CONFIG_KEY,
    EnvironmentSecretProvider,
    SecretProvider,
    decrypt_credentials,
)
from app.tools.detection_tools import detect_masked


SENSITIVE_COLUMN_HINTS = {
    "card", "credit", "debit", "pan", "aadhaar", "aadhar", "email", "mail",
    "phone", "mobile", "name", "address", "ssn", "passport", "account",
}
TEXT_TYPES = {
    "char", "varchar", "nvarchar", "text", "ntext", "string", "clob",
}


def prioritize_columns(table: TableInfo) -> list[str]:
    def score(column) -> tuple[int, str]:
        name = column.name.lower()
        hint_score = sum(10 for hint in SENSITIVE_COLUMN_HINTS if hint in name)
        type_score = 2 if any(item in column.data_type.lower() for item in TEXT_TYPES) else 0
        return (hint_score + type_score, column.name)

    eligible = [column for column in table.columns if score(column)[0] > 0]
    return [column.name for column in sorted(eligible, key=score, reverse=True)]


def build_connector_config(asset: dict[str, Any], secret_provider: SecretProvider) -> dict[str, Any]:
    platform = asset["platform"]
    if platform == "sqlite":
        return {"database": asset.get("database_name") or asset.get("config", {}).get("path")}
    asset_config = asset.get("config", {})
    encrypted_credentials = asset_config.get(CREDENTIAL_CONFIG_KEY)
    secret = (
        decrypt_credentials(encrypted_credentials)
        if encrypted_credentials
        else secret_provider.resolve(asset.get("secret_ref") or "")
    )
    config: dict[str, Any] = {
        "host": asset["host"],
        "port": asset["port"],
        "database": asset["database_name"],
        "username": secret["username"],
        "password": secret["password"],
    }
    for key in ("driver", "encrypt", "trust_server_certificate"):
        if key in asset_config:
            config[key] = asset_config[key]
    return config


def scan_database(
    asset: dict[str, Any],
    *,
    entities: set[str],
    batch_size: int,
    row_limit: int,
    secret_provider: SecretProvider | None = None,
    progress_callback: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    secret_provider = secret_provider or EnvironmentSecretProvider()
    connector_config = build_connector_config(asset, secret_provider)
    findings: list[dict[str, Any]] = []
    stats: dict[str, Any] = {
        "tables_discovered": 0,
        "tables_scanned": 0,
        "rows_scanned": 0,
        "columns_scanned": 0,
        "bytes_scanned": 0,
        "progress_percent": 0,
        "skipped_tables": [],
    }

    def publish_progress() -> None:
        processed_tables = stats["tables_scanned"] + len(stats["skipped_tables"])
        total_tables = stats["tables_discovered"]
        stats["tables_processed"] = processed_tables
        stats["total_tables"] = total_tables
        stats["progress_percent"] = (
            round(processed_tables * 100 / total_tables)
            if total_tables
            else 100
        )
        stats["findings_detected"] = len(findings)

        if progress_callback is not None:
            progress_callback(
                {
                    "stats": dict(stats),
                    "findings": list(findings),
                }
            )

    with build_database_connector(asset["platform"], connector_config) as connector:
        connection = connector.test_connection()
        tables = connector.discover_schema()
        stats["tables_discovered"] = len(tables)
        publish_progress()
        for table in tables:
            columns = prioritize_columns(table)
            if not columns:
                stats["skipped_tables"].append(f"{table.schema}.{table.name}")
                publish_progress()
                continue
            stats["columns_scanned"] += len(columns)
            row_number = 0
            for batch in connector.iter_table_batches(table, columns, batch_size, row_limit):
                for row in batch:
                    row_number += 1
                    stats["rows_scanned"] += 1
                    for column, value in row.items():
                        if value is None:
                            continue
                        stats["bytes_scanned"] += len(
                            str(value).encode("utf-8", errors="replace")
                        )
                        location = {
                            "source": "database",
                            "schema": table.schema,
                            "table": table.name,
                            "column": column,
                            "row_number": row_number,
                        }
                        matches = detect_masked(str(value), location)
                        findings.extend(match for match in matches if match["entity_type"] in entities)
                publish_progress()
            stats["tables_scanned"] += 1
            publish_progress()
        stats["progress_percent"] = 100
        publish_progress()
    counts = Counter(item["entity_type"] for item in findings)
    return {
        "connection": connection,
        "stats": stats,
        "findings": findings,
        "entity_counts": dict(counts),
    }
