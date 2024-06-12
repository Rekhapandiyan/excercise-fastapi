"""add more columns to posts table

Revision ID: 63a3a710c272
Revises: 6763fc896537
Create Date: 2024-06-04 15:58:45.890371

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63a3a710c272'
down_revision: Union[str, None] = '6763fc896537'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('posts', sa.Column('published', sa.Boolean, nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('owner_id',sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk',source_table='posts',referent_table='users',local_cols=['owner_id'], remote_cols=['id'],
                          ondelete='CASCADE')

    pass


def downgrade():
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts','owner_id')
    pass
