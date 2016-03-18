# coding=utf-8
""" Add import store data role to system

Revision ID: a1ed2f75cb13
Revises: a3c89010eabb
Create Date: 2016-03-18 20:29:04.081699

"""

# revision identifiers, used by Alembic.
revision = 'a1ed2f75cb13'
down_revision = 'a3c89010eabb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    res = op.get_bind().execute('SELECT max(id)+1 FROM role')
    enum_values_table = sa.table('role',
                                 sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                                 sa.Column('name', sa.Integer(), nullable=True),
                                 sa.Column('description', sa.String(length=32), nullable=True),
                                 )
    cm = 46
    for r in res.fetchall():
        cm = r[0]
    from sqlalchemy.sql import text
    op.bulk_insert(enum_values_table, [
        {'id': cm, 'name': 'import_store_data', 'description': u'导入店铺运营数据'},
    ], multiinsert=False)
    op.get_bind().execute(text("ALTER SEQUENCE role_id_seq RESTART WITH " + str(cm + 1) + ";"))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
