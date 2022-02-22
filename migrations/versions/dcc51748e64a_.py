"""empty message

Revision ID: dcc51748e64a
Revises: 27d91a31d427
Create Date: 2022-02-16 14:01:18.821819

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dcc51748e64a'
down_revision = '27d91a31d427'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scanTask',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tid', sa.String(length=128), nullable=False),
    sa.Column('starttime', sa.String(length=30), nullable=False),
    sa.Column('endtime', sa.String(length=30), nullable=False),
    sa.Column('key', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('scantask')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scantask',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('tid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('starttime', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('endtime', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('key', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.drop_table('scanTask')
    # ### end Alembic commands ###