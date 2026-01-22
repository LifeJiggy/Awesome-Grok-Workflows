# Container Security Rules

## Image Security
1. **Minimal Base Images** - Small attack surface
2. **No Root User** - Run as non-root
3. **Signed Images** - Verify image signatures
4. **Scan for Vulnerabilities** - Regular scanning

## Runtime Security
1. **Read-Only Filesystem** - When possible
2. **No New Privileges** - Prevent privilege escalation
3. **Resource Limits** - CPU, memory caps
4. **Network Policies** - Restrict network access

## Secret Management
1. **Don't Embed Secrets** - Use secret managers
2. **Rotate Secrets** - Regular rotation
3. **Vault Integration** - HashiCorp Vault
4. **Environment Variables** - Injected at runtime

## Orchestration Security
1. **RBAC** - Role-based access control
2. **Pod Security Policies** - Restrict pod capabilities
3. **Network Policies** - Isolate namespaces
4. **Audit Logging** - Track all actions

## Monitoring
1. **Anomaly Detection** - Unusual behavior
2. **Log Aggregation** - Centralized logging
3. **Runtime Protection** - Falco, Sysdig
4. **Incident Response** - Prepared procedures
