"""empty message

Revision ID: c68f62d0293f
Revises: 34c19e023e91
Create Date: 2018-12-01 01:59:50.383293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c68f62d0293f'
down_revision = '34c19e023e91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogxxxx',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogxxxx')
    # ### end Alembic commands ###
