"""SQLite connector for local demos and automated integration tests."""
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any, Iterator

from app.connectors.base import ColumnInfo, DatabaseConnector, TableInfo
from app.connectors.sql_utils import require_safe_identifier


class SQLiteConnector(DatabaseConnector):
    platform = "sqlite"

    def __init__(self, *, database: str):
        path = Path(database).expanduser().resolve()
        if not path.is_file():
            raise ValueError(f"SQLite database does not exist: {path}")
        self.path = path
        self.connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)

    def test_connection(self) -> dict[str, Any]:
        version = self.connection.execute("SELECT sqlite_version()").fetchone()[0]
        return {"ok": True, "platform": self.platform, "database": self.path.name, "version": version}

    def discover_schema(self) -> list[TableInfo]:
        names = self.connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        ).fetchall()
        tables: list[TableInfo] = []
        for (name,) in names:
            safe_name = require_safe_identifier(name)
            columns = [
                ColumnInfo("main", name, row[1], row[2] or "TEXT", not bool(row[3]))
                for row in self.connection.execute(f'PRAGMA table_info("{safe_name}")').fetchall()
            ]
            count = self.connection.execute(f'SELECT COUNT(*) FROM "{safe_name}"').fetchone()[0]
            tables.append(TableInfo("main", name, columns, int(count)))
        return tables

    def iter_table_batches(
        self, table: TableInfo, columns: list[str], batch_size: int, row_limit: int
    ) -> Iterator[list[dict[str, Any]]]:
        table_name = require_safe_identifier(table.name)
        selected = [require_safe_identifier(column) for column in columns]
        quoted = ", ".join(f'"{name}"' for name in selected)
        offset = 0
        while offset < row_limit:
            limit = min(batch_size, row_limit - offset)
            cursor = self.connection.execute(
                f'SELECT {quoted} FROM "{table_name}" LIMIT ? OFFSET ?', (limit, offset)
            )
            rows = cursor.fetchall()
            if not rows:
                break
            yield [dict(zip(selected, row)) for row in rows]
            offset += len(rows)

    def close(self) -> None:
        self.connection.close()
