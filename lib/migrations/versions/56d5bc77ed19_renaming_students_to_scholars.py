"""Renaming students to scholars

Revision ID: 56d5bc77ed19
Revises: 791279dd0760
Create Date: 2023-06-08 12:12:13.337053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d5bc77ed19'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')

def downgrade() -> None:
    op.rename_table('scholars', 'students')
