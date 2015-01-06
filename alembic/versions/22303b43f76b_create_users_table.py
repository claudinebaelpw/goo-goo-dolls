"""Create users table

Revision ID: 22303b43f76b
Revises: None
Create Date: 2014-10-22 17:49:34.647527

"""

# revision identifiers, used by Alembic.
revision = '22303b43f76b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('middle_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(255), nullable=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
    )


def downgrade():
    pass
