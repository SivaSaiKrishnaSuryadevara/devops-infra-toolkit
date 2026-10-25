"""Minimal FastAPI service for the hardened Compose topology."""
import os

import redis
from fastapi import FastAPI
from sqlalchemy import create_engine, text

from settings import db_url, read_secret

app = FastAPI()
engine = create_engine(db_url(), pool_pre_ping=True)
cache = redis.Redis(host=os.environ["REDIS_HOST"], password=read_secret("REDIS_PASSWORD_FILE"))


@app.get("/healthz")
def healthz():
    # Healthy only when both data stores answer.
    with engine.connect() as conn:
        conn.execute(text("select 1"))
    cache.ping()
    return {"ok": True}


@app.get("/items")
def items():
    with engine.connect() as conn:
        return {"count": conn.execute(text("select count(*) from items")).scalar()}
