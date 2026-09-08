"""Read-only MySQL connector. The pymysql package is imported lazily."""
from __future__ import annotations

from typing import Any, Iterator

from app.connectors.base import ColumnInfo, DatabaseConnector, TableInfo
from app.connectors.sql_utils import quote_mysql_identifier, rows_to_dicts


MYSQL_SYSTEM_DATABASES = {
    "information_schema",
    "mysql",
    "performance_schema",
    "sys",
}


def discover_mysql_databases(
    *,
    host: str,
    port: int,
    username: str,
    password: str,
    include_system: bool = False,
) -> list[str]:
    """Return databases visible to the supplied read-only MySQL account."""
    try:
        import pymysql
    except ImportError as exc:
        raise RuntimeError("Install pymysql to connect to MySQL") from exc

    connection = pymysql.connect(
        host=host,
        port=port,
        user=username,
        password=password,
        connect_timeout=10,
        read_timeout=30,
        write_timeout=10,
        autocommit=False,
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            names = [str(row[0]) for row in cursor.fetchall()]
    finally:
        connection.close()

    if not include_system:
        names = [name for name in names if name.lower() not in MYSQL_SYSTEM_DATABASES]
    return sorted(set(names), key=str.casefold)


class MySQLConnector(DatabaseConnector):
    platform = "mysql"

    def __init__(self, *, host: str, port: int, database: str, username: str, password: str):
        try:
            import pymysql
        except ImportError as exc:
            raise RuntimeError("Install pymysql to scan MySQL databases") from exc
        if not database or "\x00" in database:
            raise ValueError("Invalid MySQL database name")
        self.database = database
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database,
            connect_timeout=10,
            read_timeout=30,
            write_timeout=10,
            autocommit=False,
        )

    def test_connection(self) -> dict[str, Any]:
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT @@version, DATABASE()")
            version, database = cursor.fetchone()
        return {"ok": True, "platform": self.platform, "database": database, "version": str(version)}

    def discover_schema(self) -> list[TableInfo]:
        query = """
            SELECT c.TABLE_SCHEMA, c.TABLE_NAME, c.COLUMN_NAME, c.DATA_TYPE,
                   c.IS_NULLABLE, t.TABLE_ROWS
            FROM information_schema.COLUMNS c
            JOIN information_schema.TABLES t
              ON t.TABLE_SCHEMA = c.TABLE_SCHEMA AND t.TABLE_NAME = c.TABLE_NAME
            WHERE c.TABLE_SCHEMA = %s AND t.TABLE_TYPE = 'BASE TABLE'
            ORDER BY c.TABLE_NAME, c.ORDINAL_POSITION
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (self.database,))
            rows = cursor.fetchall()
        grouped: dict[tuple[str, str], TableInfo] = {}
        for schema, table, column, data_type, nullable, estimated_rows in rows:
            key = (schema, table)
            grouped.setdefault(key, TableInfo(schema, table, estimated_rows=estimated_rows))
            grouped[key].columns.append(ColumnInfo(schema, table, column, data_type, nullable == "YES"))
        return list(grouped.values())

    def iter_table_batches(
        self, table: TableInfo, columns: list[str], batch_size: int, row_limit: int
    ) -> Iterator[list[dict[str, Any]]]:
        schema = quote_mysql_identifier(table.schema)
        table_name = quote_mysql_identifier(table.name)
        selected = [quote_mysql_identifier(column) for column in columns]
        if not selected:
            return
        quoted = ", ".join(selected)
        offset = 0
        while offset < row_limit:
            limit = min(batch_size, row_limit - offset)
            query = f"SELECT {quoted} FROM {schema}.{table_name} LIMIT %s OFFSET %s"
            with self.connection.cursor() as cursor:
                cursor.execute(query, (limit, offset))
                rows = cursor.fetchall()
                if not rows:
                    break
                yield rows_to_dicts(cursor.description, rows)
            offset += len(rows)

    def close(self) -> None:
        self.connection.close()
