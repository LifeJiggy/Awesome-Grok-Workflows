# REST API Design Rules

## URL Design
1. **Nouns over Verbs** - `/users` not `/getUsers`
2. **Plural Resources** - `/users` not `/user`
3. **Nested Resources** - `/users/{id}/orders`
4. **Consistent Hierarchy** - Predictable structure

## HTTP Methods
1. **GET** - Retrieve resources
2. **POST** - Create resources
3. **PUT** - Replace entire resource
4. **PATCH** - Partial update
5. **DELETE** - Remove resource

## Response Codes
1. **200** - Success
2. **201** - Created
3. **204** - No Content
4. **400** - Bad Request
5. **401** - Unauthorized
6. **403** - Forbidden
7. **404** - Not Found
8. **429** - Rate Limited
9. **500** - Server Error

## Versioning
1. **URL Versioning** - `/v1/users`
2. **Header Versioning** - `Accept: application/vnd.api.v1+json`
3. **Deprecation Policy** - Clear timeline
4. **Backward Compatibility** - Minimize breaking changes

## Best Practices
1. **HATEOAS** - Include navigation links
2. **Pagination** - Cursor or offset-based
3. **Filtering** - Query parameters
4. **Field Selection** - `?fields=name,email`
5. **Rate Limiting** - Standard headers
