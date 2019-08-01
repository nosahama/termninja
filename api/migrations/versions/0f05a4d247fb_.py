"""empty message

Revision ID: 0f05a4d247fb
Revises: 
Create Date: 2019-07-26 22:30:59.795557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f05a4d247fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('server_name', sa.String(length=64), nullable=False),
    sa.Column('slug', sa.String(length=64), nullable=False),
    sa.Column('description', sa.Text(), server_default='', nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('last_active', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_games_slug'), 'games', ['slug'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('play_token', sa.String(length=36), nullable=False),
    sa.Column('play_token_expires_at', sa.DateTime(), nullable=False),
    sa.Column('score', sa.Integer(), server_default='0', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('rounds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('played_at', sa.DateTime(), nullable=False),
    sa.Column('game_slug', sa.String(length=64), nullable=False),
    sa.Column('user_username', sa.String(length=64), nullable=True),
    sa.Column('score', sa.Integer(), server_default='0', nullable=True),
    sa.Column('result_message', sa.String(length=128), server_default='', nullable=True),
    sa.Column('result_snapshot', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['game_slug'], ['games.slug'], ),
    sa.ForeignKeyConstraint(['user_username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rounds')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_games_slug'), table_name='games')
    op.drop_table('games')
    # ### end Alembic commands ###