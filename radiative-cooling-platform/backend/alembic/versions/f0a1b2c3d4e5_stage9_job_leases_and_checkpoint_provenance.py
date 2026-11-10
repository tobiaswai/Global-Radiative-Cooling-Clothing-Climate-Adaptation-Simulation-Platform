"""stage9 job leases and checkpoint provenance

Revision ID: f0a1b2c3d4e5
Revises: 165a424d6ba1
Create Date: 2026-11-06 10:00:00.000000

* simulation_jobs gains the same lease columns as global_city_results so the
  single-job worker path has the same redelivery / crash guarantees.
* global_city_checkpoints records which model version, parameter fingerprint
  and request hash produced each row. A resumed worker only trusts rows whose
  provenance matches the current batch; legacy rows (NULL) are recomputed.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "f0a1b2c3d4e5"
down_revision: Union[str, Sequence[str], None] = "165a424d6ba1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("simulation_jobs", sa.Column("attempt", sa.Integer(), server_default="0", nullable=False))
    op.add_column("simulation_jobs", sa.Column("lease_owner", sa.String(length=100), nullable=True))
    op.add_column("simulation_jobs", sa.Column("lease_expires_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("simulation_jobs", sa.Column("last_heartbeat_at", sa.DateTime(timezone=True), nullable=True))
    op.create_index("ix_simulation_jobs_lease_reap", "simulation_jobs", ["status", "lease_expires_at"])

    op.add_column("global_city_checkpoints", sa.Column("model_version", sa.String(length=20), nullable=True))
    op.add_column("global_city_checkpoints", sa.Column("parameter_fingerprint", sa.String(length=64), nullable=True))
    op.add_column("global_city_checkpoints", sa.Column("request_sha256", sa.String(length=64), nullable=True))


def downgrade() -> None:
    op.drop_column("global_city_checkpoints", "request_sha256")
    op.drop_column("global_city_checkpoints", "parameter_fingerprint")
    op.drop_column("global_city_checkpoints", "model_version")

    op.drop_index("ix_simulation_jobs_lease_reap", table_name="simulation_jobs")
    op.drop_column("simulation_jobs", "last_heartbeat_at")
    op.drop_column("simulation_jobs", "lease_expires_at")
    op.drop_column("simulation_jobs", "lease_owner")
    op.drop_column("simulation_jobs", "attempt")