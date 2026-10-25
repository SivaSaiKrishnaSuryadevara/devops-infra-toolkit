# Hardened production Compose topology

A Docker Compose v2 stack (Nginx, FastAPI, PostgreSQL 16, Redis 7) with deterministic startup, network segmentation, file-based secrets, resource limits and non-root, read-only containers. The `api/` directory holds a minimal FastAPI service with an Alembic migration so the stack runs end to end.

## Topology

| Service | Networks | Host port | Runs as | Starts after |
| --- | --- | --- | --- | --- |
| `nginx` | `dmz` | 80 | 101 | `app` healthy |
| `app` | `dmz`, `backend_net` | none | 10001 | `migrate` exited 0, `redis` healthy |
| `migrate` | `backend_net` | none | 10001 | `postgres` healthy |
| `postgres` | `backend_net` | none | 70 | none |
| `redis` | `backend_net` | none | 999 | none |

`backend_net` is `internal: true`: the data stores have no route to the outside world and publish nothing to the host.

## Run

```bash
cd production-compose

# Secrets are bind-mounted, so host permissions control access.
chmod 700 secrets
openssl rand -base64 32 | tr -d '\n/+=' > secrets/db_password.txt
openssl rand -base64 32 | tr -d '\n/+=' > secrets/redis_password.txt
chmod 444 secrets/*.txt

docker compose up -d --build --wait
curl localhost/items   # {"count":0}
```

## Verify

```bash
docker compose ps -a                                   # app, postgres, redis healthy; migrate exited 0
docker compose exec app sh -c 'id; touch /probe'       # uid=10001, Read-only file system
docker compose exec nginx getent hosts postgres || echo isolated
docker stats --no-stream                               # limits from deploy.resources
```

The secret files are git-ignored; never commit them.
