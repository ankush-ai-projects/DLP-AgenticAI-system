"""Safe connector contracts used by database-scanning tools."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterator


@dataclass(slots=True)
class ColumnInfo:
    schema: str
    table: str
    name: str
    data_type: str
    nullable: bool = True


@dataclass(slots=True)
class TableInfo:
    schema: str
    name: str
    columns: list[ColumnInfo] = field(default_factory=list)
    estimated_rows: int | None = None


class DatabaseConnector(ABC):
    """A connector exposes discovery and read-only batch operations only."""

    platform: str

    @abstractmethod
    def test_connection(self) -> dict[str, Any]: ...

    @abstractmethod
    def discover_schema(self) -> list[TableInfo]: ...

    @abstractmethod
    def iter_table_batches(
        self,
        table: TableInfo,
        columns: list[str],
        batch_size: int,
        row_limit: int,
    ) -> Iterator[list[dict[str, Any]]]: ...

    @abstractmethod
    def close(self) -> None: ...

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
