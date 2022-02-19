"""empty message

Revision ID: fa3cc266007a
Revises: c5952b69df62
Create Date: 2022-02-19 15:14:25.267510

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa3cc266007a'
down_revision = 'c5952b69df62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('PocList',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('flag', sa.Boolean(), nullable=True),
    sa.Column('pocname', sa.String(length=128), nullable=False),
    sa.Column('references', sa.String(length=128), nullable=False),
    sa.Column('created', sa.String(length=128), nullable=False),
    sa.Column('code', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('VulList',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tid', sa.String(length=128), nullable=False),
    sa.Column('pid', sa.String(length=128), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scanTask',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pid', sa.String(length=128), nullable=False),
    sa.Column('tid', sa.String(length=128), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=False),
    sa.Column('starttime', sa.String(length=30), nullable=False),
    sa.Column('endtime', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('poclist')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('poclist',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('flag', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('pocname', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('references', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('created', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('code', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.drop_table('scanTask')
    op.drop_table('VulList')
    op.drop_table('PocList')
    # ### end Alembic commands ###
