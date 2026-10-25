FROM python:3.12-slim
RUN pip install --no-cache-dir fastapi==0.115.* uvicorn==0.32.* alembic==1.14.* "sqlalchemy==2.0.*" "psycopg[binary]==3.2.*" redis==5.2.*
WORKDIR /srv
COPY . .
# The root filesystem is read-only at runtime, so skip .pyc writes.
ENV PYTHONDONTWRITEBYTECODE=1
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
