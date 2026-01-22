# Security Testing Rules

## Types of Tests
1. **SAST** - Static Application Security Testing
2. **DAST** - Dynamic Application Security Testing
3. **SCA** - Software Composition Analysis
4. **Penetration Testing** - Manual security testing

## OWASP Top 10
1. **Injection** - SQL, command, LDAP injection
2. **Broken Auth** - Weak authentication
3. **Sensitive Data** - Unprotected data exposure
4. **XML External Entities** - XXE attacks
5. **Broken Access Control** - Insecure permissions
6. **Security Misconfigurations** - Default configs
7. **XSS** - Cross-site scripting
8. **Insecure Deserialization** - Object injection
9. **Vulnerable Components** - Outdated libraries
10. **Insufficient Logging** - No audit trail

## Best Practices
1. **Shift Left** - Test early in SDLC
2. **Automate** - Include in CI/CD
3. **Regular Scans** - Weekly or daily
4. **Fix Critical** - Address immediately

## Tools
1. **SonarQube** - SAST and code quality
2. **OWASP ZAP** - DAST
3. **Snyk** - SCA
4. **Bandit** - Python SAST
