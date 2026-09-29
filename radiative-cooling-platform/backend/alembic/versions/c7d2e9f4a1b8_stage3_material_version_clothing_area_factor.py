"""stage3 material version clothing area factor

Revision ID: c7d2e9f4a1b8
Revises: 18a914bf4989
Create Date: 2026-10-06 10:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7d2e9f4a1b8'
down_revision: Union[str, Sequence[str], None] = '18a914bf4989'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'material_versions',
        sa.Column('clothing_area_factor', sa.Float(), nullable=True),
    )
    op.create_check_constraint(
        'ck_material_clothing_area_factor',
        'material_versions',
        'clothing_area_factor IS NULL OR '
        '(clothing_area_factor >= 1.0 AND clothing_area_factor <= 2.0)',
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        'ck_material_clothing_area_factor',
        'material_versions',
        type_='check',
    )
    op.drop_column('material_versions', 'clothing_area_factor')