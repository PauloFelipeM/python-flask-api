"""empty message

Revision ID: 6baccf7a9075
Revises: 5319790e8c02
Create Date: 2023-11-06 16:00:51.729154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6baccf7a9075'
down_revision = '5319790e8c02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher_formation',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('formation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['formation_id'], ['formations.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('teacher_id', 'formation_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher_formation')
    # ### end Alembic commands ###
