from alembic import context
from sqlalchemy import create_engine

from settings import db_url

with create_engine(db_url()).connect() as conn:
    context.configure(connection=conn)
    with context.begin_transaction():
        context.run_migrations()
