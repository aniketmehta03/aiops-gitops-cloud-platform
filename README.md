# AIOps GitOps Cloud Platform

An end-to-end DevOps + AIOps platform showcasing how to **build, deploy, monitor, and analyze** a Kubernetes-based application using **GitOps**, **CI/CD**, **observability**, and **AI agents**.

## What makes it unique

- **GitOps CD** with ArgoCD
- **CI with immutable image tags** (GitHub SHA)
- **Kubernetes + Helm** production-style deployments
- **Observability stack** (Prometheus + Grafana)
- **AIOps layer**: AI agents analyze Prometheus metrics and propose remediation

## Architecture overview

```text
Developer push code
  ↓
GitHub Actions (CI)
  ↓
Docker image build + push
  ↓
Update Helm values.yaml (image tag)
  ↓
ArgoCD (GitOps CD)
  ↓
Kubernetes deployment (EKS)
  ↓
Prometheus (metrics collection)
  ↓
Grafana (dashboards)
  ↓
AI agent (AIOps analysis)
```

## Repository structure

```text
.
├── app/                 # FastAPI CRUD application
├── ai-service/          # AI Agents (AIOps engine)
├── helm/                # Helm charts
├── kubernetes/          # Raw manifests (reference)
├── terraform/           # AWS infrastructure (IaC)
├── .github/workflows/   # CI pipelines
├── docker-compose.yaml  # Local dev setup
├── Dockerfile           # Production container build
└── docs/                # Architecture & diagrams
```

## Features

### Application layer

- FastAPI CRUD application
- PostgreSQL database
- Health checks (liveness/readiness)
- Prometheus metrics endpoint at **`/metrics`**

### Containerization

- Multi-stage Docker build
- Lightweight Alpine-based images
- Runs as **non-root** for security

### Kubernetes deployment

- Deployment + Service + HPA
- Resource requests/limits and autoscaling
- ConfigMap + Secret integration
- Readiness and liveness probes

### Helm (production deployment)

- Parameterized configuration via `values.yaml`
- Environment-ready deployments
- Reusable templates

### CI/CD

**CI (GitHub Actions)**
- Build Docker image
- Tag with GitHub SHA
- Push to DockerHub / ECR
- Auto-update Helm `values.yaml`

**CD (GitOps with ArgoCD)**
- ArgoCD monitors Git repo and syncs automatically
- Self-healing and pruning
- No manual `kubectl apply`

### Infrastructure (Terraform)

- VPC, subnets, networking
- EKS cluster
- ECR repository
- IAM roles
- Remote state (S3 + DynamoDB)

### Observability

**Prometheus**
- Scrapes `/metrics`
- Collects application + cluster metrics

**Grafana**
- Kubernetes dashboards
- Custom app dashboards
- Real-time monitoring

## AIOps layer (AI agents)

This is the core differentiator of the project.

### What it does

- Fetches real-time metrics from Prometheus
- Sends metrics to an AI model (Ollama / LLM)
- Produces an explanation and remediation suggestion, for example:

```json
{
  "issue": "High CPU usage",
  "reason": "Increased traffic load",
  "solution": "Scale pods or optimize application"
}
```

### Use cases

- Anomaly detection
- Alert explanation
- Root cause analysis
- Intelligent troubleshooting

## GitOps workflow (ArgoCD)

```text
Git push → CI → image build → Helm update → ArgoCD sync → deploy
```

## Quick start

### Local development (Docker)

```bash
docker build -t aiops-app .
docker compose up -d
```

### Helm deployment (Kubernetes)

```bash
helm lint helm/
helm template aiops helm/
helm upgrade --install aiops helm/ -n aiops
```

## CI/CD usage

Push to `main`:

```bash
git push origin main
```

This triggers:
- Build
- Push
- Helm update
- ArgoCD deployment

## Monitoring access (Grafana)

```bash
kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
```

Open `http://localhost:3000`.
