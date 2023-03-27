"""Add ProjectGroup and Student models

Revision ID: 4e15edf52a06
Revises: 
Create Date: 2023-03-27 14:00:01.818149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e15edf52a06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=True),
    sa.Column('linkedin', sa.String(), nullable=True),
    sa.Column('project_groups_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_groups_id'], ['project_groups.id'], name=op.f('fk_students_project_groups_id_project_groups')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    op.drop_table('project_groups')
    # ### end Alembic commands ###
