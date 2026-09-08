from pathlib import Path

from app.tools.filesystem_tools import scan_system_path


def test_system_scan_masks_sensitive_values(tmp_path):
    sample = tmp_path / "sample.txt"
    sample.write_text("Email analyst@example.com card 4111111111111111", encoding="utf-8")
    result = scan_system_path(
        str(tmp_path),
        entities={"EMAIL", "CREDIT_CARD"},
        allowed_roots=[Path(tmp_path).resolve()],
    )
    assert result["stats"]["files_scanned"] == 1
    assert result["entity_counts"] == {"EMAIL": 1, "CREDIT_CARD": 1}
    assert "4111111111111111" not in str(result["findings"])


def test_system_scan_rejects_path_outside_allowlist(tmp_path):
    allowed = tmp_path / "allowed"
    denied = tmp_path / "denied"
    allowed.mkdir()
    denied.mkdir()
    try:
        scan_system_path(str(denied), entities={"EMAIL"}, allowed_roots=[allowed.resolve()])
    except PermissionError:
        return
    raise AssertionError("Path outside allowlist was not rejected")
