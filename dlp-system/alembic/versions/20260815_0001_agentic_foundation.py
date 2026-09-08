"""agentic enterprise foundation

Revision ID: 20260815_0001
Revises:
Create Date: 2026-08-15
"""
from alembic import op
import sqlalchemy as sa


revision = "20260815_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "assets",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("owner_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("tenant_key", sa.String(80), nullable=False),
        sa.Column("name", sa.String(120), nullable=False),
        sa.Column("asset_type", sa.String(20), nullable=False),
        sa.Column("platform", sa.String(40), nullable=False),
        sa.Column("host", sa.String(255)),
        sa.Column("port", sa.Integer()),
        sa.Column("database_name", sa.String(255)),
        sa.Column("root_path", sa.String(1000)),
        sa.Column("secret_ref", sa.String(255)),
        sa.Column("config", sa.JSON(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
    )
    op.create_table(
        "agentic_scans",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("asset_id", sa.Integer(), sa.ForeignKey("assets.id"), nullable=False),
        sa.Column("goal", sa.Text(), nullable=False),
        sa.Column("status", sa.String(40), nullable=False),
        sa.Column("plan", sa.JSON(), nullable=False),
        sa.Column("workflow_state", sa.JSON(), nullable=False),
        sa.Column("summary", sa.JSON(), nullable=False),
        sa.Column("iteration_count", sa.Integer(), nullable=False),
        sa.Column("approval_required", sa.Boolean(), nullable=False),
        sa.Column("error_message", sa.Text()),
    )
    for table_name, columns in (
        ("agent_runs", [
            sa.Column("agent_name", sa.String(80), nullable=False),
            sa.Column("action", sa.String(120), nullable=False),
            sa.Column("status", sa.String(30), nullable=False),
            sa.Column("input_summary", sa.JSON(), nullable=False),
            sa.Column("output_summary", sa.JSON(), nullable=False),
            sa.Column("duration_ms", sa.Integer()),
            sa.Column("error_message", sa.Text()),
        ]),
        ("human_reviews", [
            sa.Column("status", sa.String(30), nullable=False),
            sa.Column("reason", sa.Text(), nullable=False),
            sa.Column("decision_by", sa.Integer(), sa.ForeignKey("users.id")),
            sa.Column("decision_note", sa.Text()),
        ]),
        ("sensitive_findings", [
            sa.Column("entity_type", sa.String(60), nullable=False),
            sa.Column("masked_value", sa.String(255), nullable=False),
            sa.Column("confidence", sa.String(20), nullable=False),
            sa.Column("source", sa.String(40), nullable=False),
            sa.Column("risk_level", sa.String(20), nullable=False),
            sa.Column("location", sa.JSON(), nullable=False),
        ]),
    ):
        op.create_table(
            table_name,
            sa.Column("id", sa.Integer(), primary_key=True),
            sa.Column("created_at", sa.DateTime(), nullable=False),
            sa.Column("updated_at", sa.DateTime(), nullable=False),
            sa.Column("scan_id", sa.Integer(), sa.ForeignKey("agentic_scans.id"), nullable=False),
            *columns,
        )
    op.create_table(
        "audit_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("scan_id", sa.Integer(), sa.ForeignKey("agentic_scans.id")),
        sa.Column("actor", sa.String(120), nullable=False),
        sa.Column("event_type", sa.String(120), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
    )


def downgrade():
    for table_name in (
        "audit_events", "sensitive_findings", "human_reviews", "agent_runs", "agentic_scans", "assets"
    ):
        op.drop_table(table_name)
