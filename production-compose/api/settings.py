"""Configuration: non-secret values from the environment, passwords from /run/secrets."""
import os
from pathlib import Path


def read_secret(env_var: str) -> str:
    return Path(os.environ[env_var]).read_text().strip()


def db_url() -> str:
    return (
        f"postgresql+psycopg://{os.environ['DB_USER']}:{read_secret('DB_PASSWORD_FILE')}"
        f"@{os.environ['DB_HOST']}:5432/{os.environ['DB_NAME']}"
    )
