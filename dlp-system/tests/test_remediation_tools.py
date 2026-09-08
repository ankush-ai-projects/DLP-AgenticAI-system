"""Safety regression tests for bounded file remediation."""

from pathlib import Path

from app.agents.remediation_planner import RemediationPlannerAgent
from app.core.config import settings
from app.tools.filesystem_tools import file_sha256
from app.tools.remediation_tools import execute_file_remediation


class OfflineModel:
    def generate_json(self, **_kwargs):
        raise RuntimeError("offline")


def configure_remediation(tmp_path: Path) -> None:
    settings.SYSTEM_SCAN_ALLOWED_ROOTS = str(tmp_path)
    settings.REMEDIATION_BACKUP_ROOT = str(tmp_path / "backups")
    settings.REMEDIATION_MASTER_KEY = "test-remediation-master-key-with-32-characters"


def test_planner_uses_masked_metadata_and_deterministic_fallback(tmp_path):
    plan = RemediationPlannerAgent(model_client=OfflineModel()).plan(
        file_path=str(tmp_path / "customers.txt"),
        findings=[
            {
                "entity_type": "CREDIT_CARD",
                "masked_value": "4111-XXXX-XXXX-1111",
                "risk_level": "critical",
                "confidence": 1,
            }
        ],
        requested_action="mask",
        reason="Preserve the source format",
    )

    assert plan["recommended_action"] == "mask"
    assert plan["planner_source"] == "deterministic_fallback"
    assert plan["approval_required"] is True


def test_mask_creates_encrypted_backup_and_verifies(tmp_path):
    configure_remediation(tmp_path)
    source = tmp_path / "customers.txt"
    source.write_text(
        "Card 4111111111111111 and email test@example.com",
        encoding="utf-8",
    )

    result = execute_file_remediation(
        job_id=1,
        file_path=str(source),
        expected_sha256=file_sha256(source),
        action="mask",
        entity_types={"CREDIT_CARD", "EMAIL"},
    )

    assert result["verified"] is True
    assert result["replacements"] == 2
    assert Path(str(result["encrypted_backup_path"])).exists()
    assert "test@example.com" not in source.read_text(encoding="utf-8")


def test_hash_mismatch_blocks_write(tmp_path):
    configure_remediation(tmp_path)
    source = tmp_path / "customers.txt"
    source.write_text("Card 4111111111111111", encoding="utf-8")

    try:
        execute_file_remediation(
            job_id=2,
            file_path=str(source),
            expected_sha256="0" * 64,
            action="mask",
            entity_types={"CREDIT_CARD"},
        )
    except RuntimeError as error:
        assert "changed after scanning" in str(error)
    else:
        raise AssertionError("Hash mismatch must block remediation")
