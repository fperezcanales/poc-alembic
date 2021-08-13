"""baseline

Revision ID: e190c6f0e8db
Revises: 
Create Date: 2021-08-02 13:35:54.599626

"""

# revision identifiers, used by Alembic.
revision = 'e190c6f0e8db'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'bug',
        sa.Column('nbr', sa.Integer, primary_key=True),
        sa.Column('description', sa.String()),
        schema='poc'
    )

def downgrade():
    op.drop_table('bug', schema='poc')
