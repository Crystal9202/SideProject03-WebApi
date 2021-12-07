"""empty message

Revision ID: 4259a9dfeeb2
Revises: 8bc5df9c6e92
Create Date: 2021-12-07 19:39:04.695732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4259a9dfeeb2'
down_revision = '8bc5df9c6e92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('style_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('style', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('style')
    )
    op.create_table('room_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('roomtype', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('style_id', sa.Integer(), nullable=True),
    sa.Column('user_id_now', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['style_id'], ['style_model.id'], ),
    sa.ForeignKeyConstraint(['user_id_now'], ['user_model.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('room_model')
    op.drop_table('style_model')
    # ### end Alembic commands ###
