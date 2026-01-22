# API Design Rules

## RESTful API Standards
1. **Resource Naming**: Use nouns for resources, HTTP methods for actions
   - `GET /users` not `GET /getUsers`
   - `POST /users` for creation
   - `PUT /users/{id}` for full update
   - `PATCH /users/{id}` for partial update

2. **Versioning**: Include API version in URL
   - `/api/v1/users`
   - Maintain backward compatibility for at least 2 versions

3. **Response Codes**:
   - `200` - Success
   - `201` - Created
   - `204` - No Content (DELETE)
   - `400` - Bad Request
   - `401` - Unauthorized
   - `403` - Forbidden
   - `404` - Not Found
   - `429` - Rate Limited
   - `500` - Server Error

4. **Error Response Format**:
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": {}
  }
}
```

5. **Pagination**: Use cursor-based pagination for large datasets
   - `?limit=20&cursor=abc123`

6. **HATEOAS**: Include navigation links in responses when applicable

7. **Idempotency**: Support idempotency keys for POST/PUT requests

8. **Rate Limiting**: Include rate limit headers:
   - `X-RateLimit-Limit`
   - `X-RateLimit-Remaining`
   - `X-RateLimit-Reset`

9. **Security**:
   - All APIs require authentication unless explicitly public
   - Use HTTPS only
   - Implement CORS properly
   - Validate all inputs

10. **Documentation**: OpenAPI/Swagger spec for all endpoints
