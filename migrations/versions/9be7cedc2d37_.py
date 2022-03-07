"""empty message

Revision ID: 9be7cedc2d37
Revises: 1d65de4af196
Create Date: 2022-03-06 17:00:30.466410

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9be7cedc2d37'
down_revision = '1d65de4af196'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('PocList',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('position', sa.Boolean(), nullable=True),
    sa.Column('filename', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('VulList',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tid', sa.String(length=128), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.Column('pocname', sa.String(length=128), nullable=True),
    sa.Column('references', sa.String(length=128), nullable=False),
    sa.Column('created', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pluginList',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('filename', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scanTask',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pid', sa.String(length=128), nullable=False),
    sa.Column('tid', sa.String(length=128), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=False),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.Column('starttime', sa.String(length=30), nullable=False),
    sa.Column('endtime', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('poclist')
    op.drop_table('vullist')
    op.drop_table('scantask')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scantask',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('pid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('tid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('status', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('starttime', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('endtime', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('vullist',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('tid', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('pocname', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('references', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('created', mysql.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('poclist',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('position', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('filename', mysql.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.drop_table('scanTask')
    op.drop_table('pluginList')
    op.drop_table('VulList')
    op.drop_table('PocList')
    # ### end Alembic commands ###