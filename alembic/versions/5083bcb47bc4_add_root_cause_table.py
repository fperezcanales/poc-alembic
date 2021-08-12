"""add root_cause table

Revision ID: 5083bcb47bc4
Revises: e190c6f0e8db
Create Date: 2021-08-02 14:15:41.304024

"""

# revision identifiers, used by Alembic.
revision = '5083bcb47bc4'
down_revision = 'e190c6f0e8db'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('root_cause',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('tutorials')
    op.drop_table('flyway_schema_history')
    op.add_column('bug', sa.Column('root_cause_id', sa.Integer(), nullable=False))
    op.alter_column('bug', 'bug_tracker_url',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_index(op.f('ix_bug_root_cause_id'), 'bug', ['root_cause_id'], unique=False)
    op.create_unique_constraint(None, 'bug', ['bug_tracker_url'])
    op.create_foreign_key(None, 'bug', 'root_cause', ['root_cause_id'], ['id'])
    op.drop_column('bug', 'root_cause')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bug', sa.Column('root_cause', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'bug', type_='foreignkey')
    op.drop_constraint(None, 'bug', type_='unique')
    op.drop_index(op.f('ix_bug_root_cause_id'), table_name='bug')
    op.alter_column('bug', 'bug_tracker_url',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('bug', 'root_cause_id')
    op.create_table('flyway_schema_history',
    sa.Column('installed_rank', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('version', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('script', sa.VARCHAR(length=1000), autoincrement=False, nullable=False),
    sa.Column('checksum', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('installed_by', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('installed_on', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('execution_time', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('success', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('installed_rank', name='flyway_schema_history_pk')
    )
    op.create_table('tutorials',
    sa.Column('id', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('published', sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    op.drop_table('root_cause')
    ### end Alembic commands ###