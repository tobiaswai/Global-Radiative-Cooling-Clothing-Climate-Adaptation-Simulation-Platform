"""Stage 13: surrogate datasets, chunks and models (ADR 0011).

Revision ID: a7c4e2f9b1d3
Revises: e3b8c1d5f702
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision = "a7c4e2f9b1d3"
down_revision = "e3b8c1d5f702"
branch_labels = None
depends_on = None

JSONB = postgresql.JSONB(astext_type=sa.Text())


def _timestamps() -> list[sa.Column]:
    return [
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    ]


def upgrade() -> None:
    op.create_table(
        "surrogate_datasets",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("status", sa.String(30), nullable=False),
        sa.Column("spec_json", JSONB, nullable=False),
        sa.Column("context_sha256", sa.String(64), nullable=False),
        sa.Column("model_version", sa.String(20), nullable=False),
        sa.Column("parameter_fingerprint", sa.String(64), nullable=False),
        sa.Column("total_chunks", sa.Integer(), nullable=False),
        sa.Column("completed_chunks", sa.Integer(), server_default="0", nullable=False),
        sa.Column("failed_chunks", sa.Integer(), server_default="0", nullable=False),
        sa.Column("valid_material_count", sa.Integer(), nullable=False),
        sa.Column("row_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("manifest_path", sa.Text(), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        *_timestamps(),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("cancel_requested_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_surrogate_datasets_status", "surrogate_datasets", ["status"])
    op.create_index("ix_surrogate_datasets_context_sha256", "surrogate_datasets", ["context_sha256"])

    op.create_table(
        "surrogate_dataset_chunks",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("dataset_id", sa.String(36), nullable=False),
        sa.Column("city_id", sa.String(100), nullable=False),
        sa.Column("month", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(30), nullable=False),
        sa.Column("attempt", sa.Integer(), server_default="0", nullable=False),
        sa.Column("row_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("simulation_count", sa.Integer(), server_default="0", nullable=False),
        sa.Column("file_path", sa.Text(), nullable=True),
        sa.Column("file_sha256", sa.String(64), nullable=True),
        sa.Column("weather_payload_sha256", sa.String(64), nullable=True),
        sa.Column("skipped_json", JSONB, nullable=True),
        sa.Column("elapsed_seconds", sa.Float(), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        *_timestamps(),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["dataset_id"], ["surrogate_datasets.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("dataset_id", "city_id", "month", name="uq_surrogate_chunk"),
    )
    op.create_index(
        "ix_surrogate_dataset_chunks_dataset_status", "surrogate_dataset_chunks", ["dataset_id", "status"]
    )

    op.create_table(
        "surrogate_models",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("dataset_id", sa.String(36), nullable=True),
        sa.Column("status", sa.String(30), nullable=False),
        sa.Column("accepted", sa.Boolean(), server_default="false", nullable=False),
        sa.Column("training_spec_json", JSONB, nullable=False),
        sa.Column("spec_json", JSONB, nullable=False),
        sa.Column("targets_json", JSONB, nullable=False),
        sa.Column("report_json", JSONB, nullable=True),
        sa.Column("artifact_path", sa.Text(), nullable=True),
        sa.Column("artifact_sha256", sa.String(64), nullable=True),
        sa.Column("context_sha256", sa.String(64), nullable=False),
        sa.Column("model_version", sa.String(20), nullable=False),
        sa.Column("parameter_fingerprint", sa.String(64), nullable=False),
        sa.Column("error_message", sa.Text(), nullable=True),
        *_timestamps(),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["dataset_id"], ["surrogate_datasets.id"], ondelete="SET NULL"),
    )
    op.create_index("ix_surrogate_models_status", "surrogate_models", ["status"])
    op.create_index("ix_surrogate_models_dataset_id", "surrogate_models", ["dataset_id"])


def downgrade() -> None:
    op.drop_table("surrogate_models")
    op.drop_table("surrogate_dataset_chunks")
    op.drop_table("surrogate_datasets")