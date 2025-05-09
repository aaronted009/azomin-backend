"""update Person (Student, Teacher & StudentTutor) phoneNumber & email to be unique

Revision ID: 77c6aeb1f58a
Revises: 214b389ccf1f
Create Date: 2025-05-09 18:35:01.323094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77c6aeb1f58a'
down_revision: Union[str, None] = '214b389ccf1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint("uq_student_phoneNumber_email", "student", ["phoneNumber", "email"])
    op.create_unique_constraint("uq_teacher_phoneNumber_email", "teacher", ["phoneNumber", "email"])
    op.create_unique_constraint("uq_studenttutor_phoneNumber_email", "studenttutor", ["phoneNumber", "email"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_student_phoneNumber_email", "student", type_="unique")
    op.drop_constraint("uq_teacher_phoneNumber_email", "teacher", type_="unique")
    op.drop_constraint("uq_studenttutor_phoneNumber_email", "studenttutor", type_="unique")
