"""empty message

Revision ID: 6a626f9c0277
Revises: 649be17a7c99
Create Date: 2018-11-30 16:58:03.138180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a626f9c0277'
down_revision = '649be17a7c99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_achievements_timestamp', table_name='achievements')
    op.drop_table('achievements')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievements',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('medal_count', sa.INTEGER(), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_achievements_timestamp', 'achievements', ['timestamp'], unique=False)
    # ### end Alembic commands ###