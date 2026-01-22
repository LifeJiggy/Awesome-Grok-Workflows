# API Security Rules

## Authentication
1. **OAuth 2.0/OIDC** - standard for user authentication
2. **JWT validation** - verify signature, check expiry
3. **Refresh tokens** - secure rotation, one-time use
4. **Multi-factor auth** - for sensitive operations

## Authorization
1. **Role-based access control (RBAC)**
2. **Principle of least privilege**
3. **Attribute-based access control (ABAC)** for complex rules
4. **Resource-level permissions**

## Input Validation
1. **Validate all inputs** - never trust user input
2. **Parameterized queries** - prevent SQL injection
3. **Output encoding** - prevent XSS
4. **Content security policy** - mitigate attacks

## Data Protection
1. **TLS 1.3** - encrypt all traffic
2. **Encryption at rest** - sensitive data
3. **Key rotation** - regular key changes
4. **Secrets management** - never hardcode credentials

## Rate Limiting
1. **Per-user limits** - prevent abuse
2. **Per-IP limits** - prevent DDoS
3. **Exponential backoff** - for retries
4. **Rate limit headers** - inform clients

## Security Headers
1. `Strict-Transport-Security`
2. `Content-Security-Policy`
3. `X-Content-Type-Options`
4. `X-Frame-Options`
5. `Referrer-Policy`

## Logging & Monitoring
1. **Audit logs** - track all security events
2. **Anomaly detection** - unusual patterns
3. **Alerting** - security incidents
4. **Incident response** - prepared procedures

## API-Specific
1. **Versioning** - support multiple API versions
2. **Deprecation** - clear communication
3. **CORS** - proper origin restrictions
4. **API keys** - rotate periodically
