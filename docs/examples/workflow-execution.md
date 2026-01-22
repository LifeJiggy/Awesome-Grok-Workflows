# Workflow Execution Example

This document demonstrates a complete workflow execution trace.

## Example Workflow: CI/CD Pipeline

### Input Configuration
```yaml
workflow: ci-cd-pipeline
version: 1.0.0
environment: production
trigger: push
branch: main
```

### Execution Trace

```
[2024-01-22 10:00:00] 🚀 Workflow started: ci-cd-pipeline
[2024-01-22 10:00:01] ✓ checkout: Completed (commit: abc123)
[2024-01-22 10:00:05] ✓ install-dependencies: Completed (2.3s)
[2024-01-22 10:00:06] � Parallel execution started:
  ├─ [10:00:06] run-linter: Started
  ├─ [10:00:06] run-tests: Started
  └─ [10:00:06] build-image: Started
[2024-01-22 10:00:15] ✓ run-linter: Completed (9.2s)
  └─ Output: lint_report.json
[2024-01-22 10:00:45] ✓ run-tests: Completed (39.8s)
  └─ Output: test_results.json (45 passed, 0 failed)
[2024-01-22 10:01:00] ✓ build-image: Completed (54.2s)
  └─ Output: image: myapp:v1.0.0
[2024-01-22 10:01:02] ✓ security-scan: Started
[2024-01-22 10:01:30] ✓ security-scan: Completed (28.5s)
  └─ Output: 0 critical, 2 medium vulnerabilities
[2024-01-22 10:01:35] ✓ deploy-staging: Started
[2024-01-22 10:02:00] ✓ deploy-staging: Completed (25.1s)
  └─ URL: https://staging.myapp.com
[2024-01-22 10:02:05] ✓ integration-tests: Started
[2024-01-22 10:03:00] ✓ integration-tests: Completed (55.3s)
  └─ Output: 28 passed, 0 failed
[2024-01-22 10:03:05] ✓ deploy-production: Started
[2024-01-22 10:03:45] ✓ deploy-production: Completed (40.2s)
  └─ URL: https://myapp.com
[2024-01-22 10:03:50] ✓ notify-complete: Started
[2024-01-22 10:03:52] ✓ notify-complete: Completed (2.1s)
[2024-01-22 10:03:52] 🎉 Workflow completed successfully!
```

### Summary
- **Total Duration**: 3 minutes 52 seconds
- **Steps Executed**: 10
- **Parallel Steps**: 3
- **Success Rate**: 100%
- **Deployments**: 2 (staging + production)

### Generated Artifacts
1. `lint_report.json` - Linting results
2. `test_results.json` - Test coverage and results
3. `security_report.html` - Security scan report
4. `deployment_log.txt` - Deployment history

### Metrics
```json
{
  "duration_seconds": 232,
  "steps_total": 10,
  "steps_passed": 10,
  "steps_failed": 0,
  "parallel_execution": 3,
  "test_coverage": 85.4,
  "vulnerabilities": {
    "critical": 0,
    "high": 0,
    "medium": 2
  }
}
```
