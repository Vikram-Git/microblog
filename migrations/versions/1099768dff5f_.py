"""empty message

Revision ID: 1099768dff5f
Revises: 85a2dc63dde3
Create Date: 2018-11-30 16:42:48.385388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1099768dff5f'
down_revision = '85a2dc63dde3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('intrest')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('intrest',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('intrest_name', sa.TEXT(), nullable=True),
    sa.Column('intrest_type', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
