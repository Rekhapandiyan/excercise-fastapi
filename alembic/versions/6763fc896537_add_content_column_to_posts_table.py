"""add content column to posts table

Revision ID: 6763fc896537
Revises: 581288518aaf
Create Date: 2024-06-04 12:30:22.729644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6763fc896537'
down_revision: Union[str, None] = '581288518aaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
