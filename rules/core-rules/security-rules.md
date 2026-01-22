# Security Rules

## Authentication & Authorization
1. **Never hardcode credentials** - Use environment variables or secrets management
2. **Implement principle of least privilege** - Users/agents get minimum permissions needed
3. **Use OAuth 2.0/OIDC** for user authentication
4. **JWT tokens** should have short expiry (15-60 minutes)
5. **Refresh tokens** should be stored securely (HttpOnly cookies)

## Data Protection
1. **Encrypt data at rest** - Use AES-256 for sensitive data
2. **Encrypt data in transit** - TLS 1.3 minimum
3. **Never log sensitive data** - Mask PII, credentials, tokens
4. **Input validation** - Sanitize all user inputs
5. **Output encoding** - Prevent XSS attacks

## API Security
1. **Rate limiting** - Prevent brute force attacks
2. **CSRF protection** - Use anti-CSRF tokens
3. **CORS** - Whitelist only required origins
4. **Security headers**:
   - Content-Security-Policy
   - X-Content-Type-Options
   - X-Frame-Options
   - Strict-Transport-Security

## Secrets Management
1. **Never commit secrets** to version control
2. **Use secret scanning** tools in CI/CD
3. **Rotate secrets** regularly (90 days minimum)
4. **Use HashiCorp Vault** or cloud provider secrets manager

## Incident Response
1. **Log all auth failures** with context
2. **Alert on suspicious activity**
3. **Have incident response plan** documented
4. **Regular security audits** and penetration testing

## Grok-Specific
- When discussing security, be paranoid but practical
- Flag potential vulnerabilities immediately
- Suggest fixes, not just problems
- Never provide code that could be used maliciously
