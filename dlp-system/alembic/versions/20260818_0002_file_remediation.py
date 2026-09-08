"""file remediation jobs

Revision ID: 20260818_0002
Revises: 20260815_0001
Create Date: 2026-08-18
"""

from alembic import op
import sqlalchemy as sa


revision = "20260818_0002"
down_revision = "20260815_0001"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "remediation_jobs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("scan_id", sa.Integer(), sa.ForeignKey("agentic_scans.id"), nullable=False),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("file_path", sa.String(1000), nullable=False),
        sa.Column("original_sha256", sa.String(64), nullable=False),
        sa.Column(
            "action",
            sa.Enum("MASK", "REDACT", "ENCRYPT", "DELETE", name="remediationaction"),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.Enum(
                "AWAITING_APPROVAL",
                "APPROVED",
                "REJECTED",
                "EXECUTING",
                "COMPLETED",
                "FAILED",
                name="remediationstatus",
            ),
            nullable=False,
        ),
        sa.Column("entity_types", sa.JSON(), nullable=False),
        sa.Column("finding_indexes", sa.JSON(), nullable=False),
        sa.Column("planner_output", sa.JSON(), nullable=False),
        sa.Column("preview", sa.JSON(), nullable=False),
        sa.Column("approval_required", sa.Boolean(), nullable=False),
        sa.Column("admin_required", sa.Boolean(), nullable=False),
        sa.Column("approved_by", sa.Integer(), sa.ForeignKey("users.id")),
        sa.Column("approval_note", sa.Text()),
        sa.Column("approved_at", sa.DateTime()),
        sa.Column("executed_at", sa.DateTime()),
        sa.Column("encrypted_backup_path", sa.String(1000)),
        sa.Column("output_path", sa.String(1000)),
        sa.Column("result", sa.JSON(), nullable=False),
        sa.Column("error_message", sa.Text()),
    )
    op.create_index("ix_remediation_jobs_scan_id", "remediation_jobs", ["scan_id"])
    op.create_index("ix_remediation_jobs_user_id", "remediation_jobs", ["user_id"])
    op.create_index("ix_remediation_jobs_file_path", "remediation_jobs", ["file_path"])
    op.create_index("ix_remediation_jobs_action", "remediation_jobs", ["action"])
    op.create_index("ix_remediation_jobs_status", "remediation_jobs", ["status"])


def downgrade():
    op.drop_index("ix_remediation_jobs_status", table_name="remediation_jobs")
    op.drop_index("ix_remediation_jobs_action", table_name="remediation_jobs")
    op.drop_index("ix_remediation_jobs_file_path", table_name="remediation_jobs")
    op.drop_index("ix_remediation_jobs_user_id", table_name="remediation_jobs")
    op.drop_index("ix_remediation_jobs_scan_id", table_name="remediation_jobs")
    op.drop_table("remediation_jobs")
