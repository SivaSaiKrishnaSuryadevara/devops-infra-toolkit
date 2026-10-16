# devops-infra-toolkit

Infrastructure-as-code examples for deploying containerized services, using
[predictive-cicd-remediation](https://github.com/SivaSaiKrishnaSuryadevara/predictive-cicd-remediation)
as the reference workload.

## Contents

- `docker-compose.yml` - local development stack: API service, Redis, Postgres, and an nginx reverse proxy.
- `k8s/` - Kubernetes manifests: Deployment, Service, and a HorizontalPodAutoscaler.
- `terraform/` - a minimal AWS module provisioning a VPC and an ECS Fargate service behind an ALB.

## Local development

```bash
docker compose up --build
```

## Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
```

## Terraform

```bash
cd terraform
terraform init
terraform plan
```

## Status

Reference infrastructure examples intended as a companion to
predictive-cicd-remediation. Adjust resource sizing and secrets management
before using in a real production environment.
