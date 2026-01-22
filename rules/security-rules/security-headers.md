# Security Headers Rules

## Essential Headers
1. **Strict-Transport-Security** - Enforce HTTPS
2. **Content-Security-Policy** - Control resources
3. **X-Content-Type-Options** - Prevent MIME sniffing
4. **X-Frame-Options** - Prevent clickjacking
5. **Referrer-Policy** - Control referrer info

## CSP Configuration
1. **Default-src** - Fallback for other sources
2. **Script-src** - JavaScript sources
3. **Style-src** - CSS sources
4. **Img-src** - Image sources
5. **Connect-src** - Fetch/XHR sources

## CORS Configuration
1. **Origin Whitelist** - Allowed origins
2. **Methods** - Allowed HTTP methods
3. **Headers** - Allowed headers
4. **Credentials** - Allow cookies
5. **Max Age** - Preflight cache time

## Reporting
1. **CSP Report-URI** - Violation reports
2. **NEL** - Network error logging
3. **Expect-CT** - Certificate transparency
4. **Permissions-Policy** - Feature controls

## Testing
1. **Security Scanners** - Automated testing
2. **Manual Testing** - Pen testing
3. **Headers Check** - Verify all headers
4. **Updates** - Keep policies current
