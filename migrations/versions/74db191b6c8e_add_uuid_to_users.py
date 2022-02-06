"""Add uuid to users


Revision ID: 74db191b6c8e
Revises: 53843843bbc0
Create Date: 2022-02-05 03:14:36.368846

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from src.users.user_model import User
from setup import db

# revision identifiers, used by Alembic.
revision = '74db191b6c8e'
down_revision = '53843843bbc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column(
        'uuid', postgresql.UUID(as_uuid=True), nullable=True))

    for x in range(1, 1000001):
        op.bulk_insert(User.__table__, [
            {
                "email": f'user{x}@example.com',
                "first_name": f'first{x}',
                "last_name": f'last{x}'
            }
        ])
    # op.bulk_insert(User.__table__, [
    #     {
    #         "email": f'user{x}@example.com',
    #         "first_name": f'first{x}',
    #         "last_name": f'last{x}'
    #     } for x in range(1, 1001)
    # ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'uuid')
    # ### end Alembic commands ###
