"""empty message

Revision ID: e9c5cc215f95
Revises: 9040c25a4248
Create Date: 2018-06-16 00:30:53.170503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9c5cc215f95'
down_revision = '9040c25a4248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_vacancy_vacancy_id', table_name='vacancy')
    op.create_index(op.f('ix_vacancy_vacancy_id'), 'vacancy', ['vacancy_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vacancy_vacancy_id'), table_name='vacancy')
    op.create_index('ix_vacancy_vacancy_id', 'vacancy', ['vacancy_id'], unique=False)
    # ### end Alembic commands ###
