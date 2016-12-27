# coding=utf-8
"""Add related values table and related enum value, also added shipped out PO status

Revision ID: 668c5802ed96
Revises: db9ee0625c86
Create Date: 2016-09-09 13:14:32.786613

"""

# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = '668c5802ed96'
down_revision = 'db9ee0625c86'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('related_values',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_object_id', sa.Integer(), nullable=False),
    sa.Column('from_object_type', sa.Text(), nullable=False),
    sa.Column('to_object_id', sa.Integer(), nullable=False),
    sa.Column('to_object_type', sa.Text(), nullable=False),
    sa.Column('relation_type_id', sa.Integer(), nullable=True),
    sa.Column('remark', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['relation_type_id'], ['enum_values.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.get_bind().execute(text("INSERT INTO enum_values (type_id, code, display) VALUES (1, 'RELATED_TYPE', '对象关联类型');"))
    op.get_bind().execute(text("INSERT INTO enum_values (type_id, code, display) VALUES ((SELECT id FROM enum_values WHERE code='RELATED_TYPE'), 'FRANCHISE_PO_TO_SO', '加盟商采购单关联销售单');"))
    op.get_bind().execute(text("INSERT INTO enum_values (type_id, code, display) VALUES ((SELECT id FROM enum_values WHERE code='PURCHASE_ORDER_STATUS'), 'PURCHASE_ORDER_SHIPPED_OUT', '采购单已发货');"))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.get_bind().execute(text("DELETE FROM enum_values where code in ('RELATED_TYPE', 'FRANCHISE_PO_TO_SO', 'PURCHASE_ORDER_SHIPPED_OUT')"))
    op.drop_table('related_values')
    ### end Alembic commands ###
