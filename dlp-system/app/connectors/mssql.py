"""Read-only Microsoft SQL Server connector using pyodbc."""
from __future__ import annotations

from typing import Any, Iterator

from app.connectors.base import ColumnInfo, DatabaseConnector, TableInfo
from app.connectors.sql_utils import quote_mssql_identifier, rows_to_dicts


MSSQL_SYSTEM_DATABASES = {"master", "model", "msdb", "tempdb"}


def _odbc_value(value: object) -> str:
    """Brace and escape an ODBC connection-string value."""
    return "{" + str(value).replace("}", "}}") + "}"


def discover_mssql_databases(
    *,
    host: str,
    port: int,
    username: str,
    password: str,
    driver: str = "ODBC Driver 18 for SQL Server",
    encrypt: bool = True,
    trust_server_certificate: bool = False,
    include_system: bool = False,
) -> list[str]:
    """Return online MSSQL databases accessible to the supplied login."""
    try:
        import pyodbc
    except ImportError as exc:
        raise RuntimeError(
            "Install pyodbc and the Microsoft ODBC driver to connect to MSSQL"
        ) from exc

    connection_string = (
        f"DRIVER={_odbc_value(driver)};SERVER={_odbc_value(f'{host},{port}')};"
        f"DATABASE=master;UID={_odbc_value(username)};PWD={_odbc_value(password)};"
        f"Encrypt={'yes' if encrypt else 'no'};"
        f"TrustServerCertificate={'yes' if trust_server_certificate else 'no'};"
        "ApplicationIntent=ReadOnly;Connection Timeout=10;"
    )
    connection = pyodbc.connect(connection_string, autocommit=False, timeout=30)
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT name
            FROM sys.databases
            WHERE state_desc = 'ONLINE' AND HAS_DBACCESS(name) = 1
            ORDER BY name
            """
        )
        names = [str(row[0]) for row in cursor.fetchall()]
        cursor.close()
    finally:
        connection.close()

    if not include_system:
        names = [name for name in names if name.lower() not in MSSQL_SYSTEM_DATABASES]
    return sorted(set(names), key=str.casefold)


class MSSQLConnector(DatabaseConnector):
    platform = "mssql"

    def __init__(
        self,
        *,
        host: str,
        port: int,
        database: str,
        username: str,
        password: str,
        driver: str = "ODBC Driver 18 for SQL Server",
        encrypt: bool = True,
        trust_server_certificate: bool = False,
    ):
        try:
            import pyodbc
        except ImportError as exc:
            raise RuntimeError("Install pyodbc and the Microsoft ODBC driver to scan MSSQL") from exc
        if not database or "\x00" in database:
            raise ValueError("Invalid MSSQL database name")
        self.database = database
        connection_string = (
            f"DRIVER={_odbc_value(driver)};SERVER={_odbc_value(f'{host},{port}')};"
            f"DATABASE={_odbc_value(database)};UID={_odbc_value(username)};"
            f"PWD={_odbc_value(password)};Encrypt={'yes' if encrypt else 'no'};"
            f"TrustServerCertificate={'yes' if trust_server_certificate else 'no'};"
            "ApplicationIntent=ReadOnly;Connection Timeout=10;"
        )
        self.connection = pyodbc.connect(connection_string, autocommit=False, timeout=30)

    def test_connection(self) -> dict[str, Any]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT @@VERSION, DB_NAME()")
        version, database = cursor.fetchone()
        cursor.close()
        return {"ok": True, "platform": self.platform, "database": database, "version": str(version)}

    def discover_schema(self) -> list[TableInfo]:
        query = """
            SELECT s.name, t.name, c.name, ty.name, c.is_nullable,
                   SUM(CASE WHEN p.index_id IN (0,1) THEN p.rows ELSE 0 END)
            FROM sys.tables t
            JOIN sys.schemas s ON s.schema_id = t.schema_id
            JOIN sys.columns c ON c.object_id = t.object_id
            JOIN sys.types ty ON ty.user_type_id = c.user_type_id
            LEFT JOIN sys.partitions p ON p.object_id = t.object_id
            GROUP BY s.name, t.name, c.name, ty.name, c.is_nullable, c.column_id
            ORDER BY s.name, t.name, c.column_id
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        grouped: dict[tuple[str, str], TableInfo] = {}
        for schema, table, column, data_type, nullable, estimated_rows in rows:
            key = (schema, table)
            grouped.setdefault(key, TableInfo(schema, table, estimated_rows=int(estimated_rows or 0)))
            grouped[key].columns.append(ColumnInfo(schema, table, column, data_type, bool(nullable)))
        return list(grouped.values())

    def iter_table_batches(
        self, table: TableInfo, columns: list[str], batch_size: int, row_limit: int
    ) -> Iterator[list[dict[str, Any]]]:
        schema = quote_mssql_identifier(table.schema)
        table_name = quote_mssql_identifier(table.name)
        selected = [quote_mssql_identifier(column) for column in columns]
        if not selected:
            return
        quoted = ", ".join(selected)
        offset = 0
        while offset < row_limit:
            limit = min(batch_size, row_limit - offset)
            query = (
                f"SELECT {quoted} FROM {schema}.{table_name} "
                "ORDER BY (SELECT NULL) OFFSET ? ROWS FETCH NEXT ? ROWS ONLY"
            )
            cursor = self.connection.cursor()
            cursor.execute(query, (offset, limit))
            rows = cursor.fetchall()
            if not rows:
                cursor.close()
                break
            batch = rows_to_dicts(cursor.description, rows)
            cursor.close()
            yield batch
            offset += len(rows)

    def close(self) -> None:
        self.connection.close()
