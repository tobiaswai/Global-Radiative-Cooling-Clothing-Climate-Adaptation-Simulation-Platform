"""inverse optimization jobs

Revision ID: b4d8e2a6c1f3
Revises: f0a1b2c3d4e5
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "b4d8e2a6c1f3"
down_revision: Union[str, Sequence[str], None] = "f0a1b2c3d4e5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "optimization_jobs",
        sa.Column("id", sa.String(36), nullable=False),
        sa.Column("celery_task_id", sa.String(255), nullable=True),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("city_id", sa.String(100), nullable=False),
        sa.Column("status", sa.String(30), nullable=False),
        sa.Column("stage", sa.String(100), nullable=False),
        sa.Column("progress", sa.Integer(), server_default="0", nullable=False),
        sa.Column("evaluation_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("request_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("history_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("result_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("attempt", sa.Integer(), server_default="0", nullable=False),
        sa.Column("lease_owner", sa.String(100), nullable=True),
        sa.Column("lease_expires_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_heartbeat_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("cancel_requested_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("control_material_version_id", sa.String(36), nullable=True),
        sa.Column("base_material_version_id", sa.String(36), nullable=True),
        sa.ForeignKeyConstraint(["control_material_version_id"], ["material_versions.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["base_material_version_id"], ["material_versions.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_optimization_jobs_status", "optimization_jobs", ["status"])
    op.create_index("ix_optimization_jobs_city_id", "optimization_jobs", ["city_id"])
    op.create_index("ix_optimization_jobs_celery_task_id", "optimization_jobs", ["celery_task_id"])
    op.create_index("ix_optimization_jobs_lease_reap", "optimization_jobs", ["status", "lease_expires_at"])
    op.create_index("ix_optimization_jobs_control_material_version_id", "optimization_jobs", ["control_material_version_id"])
    op.create_index("ix_optimization_jobs_base_material_version_id", "optimization_jobs", ["base_material_version_id"])


def downgrade() -> None:
    op.drop_table("optimization_jobs")