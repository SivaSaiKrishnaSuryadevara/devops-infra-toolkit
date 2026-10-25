import sqlalchemy as sa
from alembic import op

revision = "0001"
down_revision = None


def upgrade():
    op.create_table("items", sa.Column("id", sa.Integer, primary_key=True))


def downgrade():
    op.drop_table("items")
