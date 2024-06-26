"""create users table

Revision ID: 581288518aaf
Revises: 0f81ba63639d
Create Date: 2024-06-04 12:21:02.792953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '581288518aaf'
down_revision: Union[str, None] = '0f81ba63639d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("users", sa.Column("id", sa.Integer, nullable=False),
                    sa.Column("email", sa.String, nullable=False),
                    sa.Column("password", sa.String, nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table("users")
    pass
