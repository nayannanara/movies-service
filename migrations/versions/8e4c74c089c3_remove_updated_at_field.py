"""remove_updated_at_field

Revision ID: 8e4c74c089c3
Revises: 2952d0495035
Create Date: 2024-06-10 11:39:35.454194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "8e4c74c089c3"
down_revision: Union[str, None] = "2952d0495035"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("movies", "updated_at")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "movies",
        sa.Column(
            "updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
    )
    # ### end Alembic commands ###