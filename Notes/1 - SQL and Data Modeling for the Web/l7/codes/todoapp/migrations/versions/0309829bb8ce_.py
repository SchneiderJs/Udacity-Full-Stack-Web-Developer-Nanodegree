"""empty message

Revision ID: 0309829bb8ce
Revises: 
Create Date: 2021-03-24 14:54:38.143325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0309829bb8ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    # ### end Alembic commands ###