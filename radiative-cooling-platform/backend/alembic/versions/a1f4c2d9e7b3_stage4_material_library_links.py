"""stage4 material library links and constraints

Revision ID: a1f4c2d9e7b3
Revises: c7d2e9f4a1b8
Create Date: 2026-10-20 10:00:00.000000

Adds
* CHECK constraints that make every stored material version a valid
  MaterialInput (IR energy sum, Re,cl range).
* Nullable FK columns on simulation_jobs and global_batch_jobs recording
  which material versions a request was resolved against.

The upgrade refuses to run while rows violate the new constraints, instead
of silently failing half-way through.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a1f4c2d9e7b3'
down_revision: Union[str, Sequence[str], None] = 'c7d2e9f4a1b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


JOB_TABLES = ("simulation_jobs", "global_batch_jobs")
LINK_COLUMNS = ("control_material_version_id", "rc_material_version_id")


def _assert_no_violations() -> None:
    bind = op.get_bind()

    checks = {
        "evaporative_resistance_m2pa_w outside [0, 1000]": (
            "SELECT count(*) FROM material_versions "
            "WHERE evaporative_resistance_m2pa_w IS NOT NULL "
            "AND (evaporative_resistance_m2pa_w < 0 "
            "OR evaporative_resistance_m2pa_w > 1000)"
        ),
        "infrared_emissivity + infrared_transmittance > 1": (
            "SELECT count(*) FROM material_versions "
            "WHERE infrared_emissivity + infrared_transmittance > 1.000001"
        ),
    }

    problems = [
        f"{label}: {count} row(s)"
        for label, sql in checks.items()
        if (count := bind.execute(sa.text(sql)).scalar_one())
    ]

    if problems:
        raise RuntimeError(
            "Cannot apply Stage 4 constraints; fix these material versions "
            "first: " + "; ".join(problems)
        )


def upgrade() -> None:
    _assert_no_violations()

    op.create_check_constraint(
        'ck_material_evaporative_resistance',
        'material_versions',
        'evaporative_resistance_m2pa_w IS NULL OR '
        '(evaporative_resistance_m2pa_w >= 0 '
        'AND evaporative_resistance_m2pa_w <= 1000)',
    )
    op.create_check_constraint(
        'ck_material_ir_energy_sum',
        'material_versions',
        'infrared_emissivity + infrared_transmittance <= 1.000001',
    )

    for table in JOB_TABLES:
        for column in LINK_COLUMNS:
            op.add_column(table, sa.Column(column, sa.String(length=36), nullable=True))
            op.create_foreign_key(
                f'fk_{table}_{column}',
                table,
                'material_versions',
                [column],
                ['id'],
                ondelete='SET NULL',
            )
            op.create_index(f'ix_{table}_{column}', table, [column])


def downgrade() -> None:
    for table in JOB_TABLES:
        for column in LINK_COLUMNS:
            op.drop_index(f'ix_{table}_{column}', table_name=table)
            op.drop_constraint(f'fk_{table}_{column}', table, type_='foreignkey')
            op.drop_column(table, column)

    op.drop_constraint('ck_material_ir_energy_sum', 'material_versions', type_='check')
    op.drop_constraint('ck_material_evaporative_resistance', 'material_versions', type_='check')