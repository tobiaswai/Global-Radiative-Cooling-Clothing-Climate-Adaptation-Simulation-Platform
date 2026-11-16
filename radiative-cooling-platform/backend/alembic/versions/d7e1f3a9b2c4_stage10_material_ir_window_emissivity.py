"""stage10 material infrared window emissivity

Revision ID: d7e1f3a9b2c4
Revises: b4d8e2a6c1f3
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d7e1f3a9b2c4"
down_revision: Union[str, Sequence[str], None] = "b4d8e2a6c1f3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "material_versions",
        sa.Column("infrared_emissivity_window", sa.Float(), nullable=True),
    )
    op.create_check_constraint(
        "ck_material_ir_emissivity_window",
        "material_versions",
        "infrared_emissivity_window IS NULL OR "
        "(infrared_emissivity_window >= 0 AND infrared_emissivity_window <= 1)",
    )
    op.create_check_constraint(
        "ck_material_ir_window_energy_sum",
        "material_versions",
        "infrared_emissivity_window IS NULL OR "
        "infrared_emissivity_window + infrared_transmittance <= 1.000001",
    )


def downgrade() -> None:
    op.drop_constraint("ck_material_ir_window_energy_sum", "material_versions", type_="check")
    op.drop_constraint("ck_material_ir_emissivity_window", "material_versions", type_="check")
    op.drop_column("material_versions", "infrared_emissivity_window")