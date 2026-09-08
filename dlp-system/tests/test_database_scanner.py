import sqlite3

from app.tools.database_tools import scan_database


def test_sqlite_demo_database_is_scanned_read_only(tmp_path):
    database = tmp_path / "target.db"
    connection = sqlite3.connect(database)
    connection.execute("CREATE TABLE payments (id INTEGER, card_number TEXT, customer_email TEXT)")
    connection.execute(
        "INSERT INTO payments VALUES (?, ?, ?)",
        (1, "4111111111111111", "analyst@example.com"),
    )
    connection.commit()
    connection.close()

    result = scan_database(
        {
            "platform": "sqlite",
            "database_name": str(database),
            "config": {},
        },
        entities={"CREDIT_CARD", "EMAIL"},
        batch_size=100,
        row_limit=100,
    )

    assert result["stats"]["tables_scanned"] == 1
    assert result["stats"]["rows_scanned"] == 1
    assert result["entity_counts"] == {"CREDIT_CARD": 1, "EMAIL": 1}
    assert all("4111111111111111" not in str(item) for item in result["findings"])
