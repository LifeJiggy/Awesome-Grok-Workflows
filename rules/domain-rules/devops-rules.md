# DevOps Rules

## Infrastructure as Code

### Terraform Standards
```hcl
# ✅ Good: Modular, versioned, documented
module "aws_vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
  
  name = "production-vpc"
  cidr = "10.0.0.0/16"
  
  azs             = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]
  
  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}

# ❌ Bad: Hard-coded, no version, no tags
resource "aws_vpc" "vpc" {
  cidr_block = "10.0.0.0/16"
}
```

### State Management
- **Use remote state** (S3, GCS, Azure Blob)
- **Enable state locking** (DynamoDB, Azure Table)
- **Never edit state** manually
- **Use workspaces** for environments
- **Backup state files**

## CI/CD Pipeline

### Pipeline Stages
```yaml
stages:
  - lint          # Code quality checks
  - test          # Unit & integration tests
  - build         # Build artifacts
  - security      # SAST, dependency scan
  - deploy_staging   # Deploy to staging
  - integration_test # E2E tests
  - deploy_production # Deploy to production
  - verify        # Smoke tests
```

### Quality Gates
| Stage | Gate | Action on Fail |
|-------|------|----------------|
| Lint | 0 errors | Block |
| Test | 80% coverage | Warn |
| Security | 0 critical | Block |
| Deploy | Smoke tests pass | Rollback |

## Container Standards

### Dockerfile
```dockerfile
# ✅ Good: Multi-stage, minimal, secure
# Build stage
FROM python:3.11-slim-bookworm AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-user --prefix=/install .

# Production stage
FROM python:3.11-slim-bookworm AS production
COPY --from=builder /install /usr/local
COPY . .
RUN useradd --create-home --shell /bin/bash appuser
USER appuser
EXPOSE 8080
CMD ["python", "app.py"]

# ❌ Bad: No user, large base, COPY early
FROM python:3.11
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### Security Scanning
- Scan images for CVEs
- Don't run as root
- Use minimal base images
- Pin dependency versions
- Regular base image updates

## Monitoring Rules

### Key Metrics
```yaml
metrics:
  - name: request_latency
    type: histogram
    labels: [method, endpoint, status]
    threshold: p99 < 500ms
    
  - name: error_rate
    type: counter
    labels: [endpoint, error_type]
    threshold: < 1%
    
  - name: availability
    type: gauge
    threshold: > 99.9%
```

### Alerting
- **Critical**: Page within 5 minutes
- **Warning**: Notify within 1 hour
- **Info**: Daily digest
- **Escalation**: After 15 minutes no ack

## GitOps Principles

### Branch Strategy
```
main          → Production
develop       → Development
feature/*     → Feature branches
hotfix/*      → Emergency fixes
release/*     → Release candidates
```

### Commit Messages
```
<type>(<scope>): <subject>

<body>

<footer>
```

Types: feat, fix, docs, style, refactor, test, chore

### Code Review
- All PRs require review
- Minimum 1 approval
- Tests must pass
- CI must green
- No unresolved comments

## Disaster Recovery

### Backup Requirements
- **Database**: Hourly incremental, daily full
- **Configs**: Version controlled, auto-sync
- **Secrets**: Encrypted, regularly rotated
- **State**: State files backed up

### Recovery Time Objective (RTO)
| Tier | RTO | RPO |
|------|-----|-----|
| Critical | 1 hour | 15 min |
| Important | 4 hours | 1 hour |
| Standard | 24 hours | 24 hours |

### Testing
- **Monthly**: DR drills
- **Quarterly**: Full failover test
- **Annually**: Complete restore test
