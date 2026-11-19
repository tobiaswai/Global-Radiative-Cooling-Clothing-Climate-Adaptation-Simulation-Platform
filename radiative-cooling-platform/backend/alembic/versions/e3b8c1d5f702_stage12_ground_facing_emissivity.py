"""Stage 12: ground-facing longwave emissivity (ADR 0010).

Revision ID: e3b8c1d5f702
Revises: d7e1f3a9b2c4
"""

import sqlalchemy as sa
from alembic import op

revision = "e3b8c1d5f702"
down_revision = "d7e1f3a9b2c4"  # replace with the output of `alembic heads` if different
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "material_versions",
        sa.Column("infrared_emissivity_ground_facing", sa.Float(), nullable=True),
    )
    op.create_check_constraint(
        "ck_material_ir_ground_facing",
        "material_versions",
        "infrared_emissivity_ground_facing IS NULL OR "
        "(infrared_emissivity_ground_facing >= 0 AND infrared_emissivity_ground_facing <= 1)",
    )
    op.create_check_constraint(
        "ck_material_ir_ground_facing_energy_sum",
        "material_versions",
        "infrared_emissivity_ground_facing IS NULL OR "
        "infrared_emissivity_ground_facing + infrared_transmittance <= 1.000001",
    )


def downgrade() -> None:
    op.drop_constraint("ck_material_ir_ground_facing_energy_sum", "material_versions", type_="check")
    op.drop_constraint("ck_material_ir_ground_facing", "material_versions", type_="check")
    op.drop_column("material_versions", "infrared_emissivity_ground_facing")