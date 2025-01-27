"""Add theme preference to User model

Revision ID: 550b397ee5a1
Revises: 25f05db9f7c4
Create Date: 2025-01-27 01:49:07.805894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '550b397ee5a1'
down_revision = '25f05db9f7c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('theme_preference', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('theme_preference')

    # ### end Alembic commands ###
