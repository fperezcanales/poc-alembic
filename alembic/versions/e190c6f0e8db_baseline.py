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
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('bug_tracker_url', sa.String(), nullable=False),
        sa.Column('root_cause', sa.String()),
        sa.Column('who', sa.String()),
        sa.Column('when', sa.DateTime(), default=sa.func.now()))


def downgrade():
    op.drop_table('bug')
