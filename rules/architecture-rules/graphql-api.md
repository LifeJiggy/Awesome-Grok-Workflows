# GraphQL API Design Rules

## Schema Design
1. **Types over Scalars** - Model domain accurately
2. **Expressive Fields** - Clear, descriptive names
3. **Non-Null by Default** - Explicit nullability
4. **Versionless** - Evolve schema without versions

## Query Design
1. **Flat Queries** - Avoid deep nesting
2. **Connection Pattern** - Pagination with cursors
3. **Aliasing** - Multiple queries with same name
4. **Fragments** - Reusable field sets

## Mutation Design
1. **One Mutation per Operation** - Focused changes
2. **Input Types** - Structured mutation input
3. **Payload Types** - Consistent mutation response
4. **Idempotency** - Safe to retry

## Performance
1. **DataLoader Pattern** - Prevent N+1 queries
2. **Query Complexity Limits** - Prevent expensive queries
3. **Depth Limits** - Prevent deeply nested queries
4. **Caching** - Leverage CDN caching

## Error Handling
1. **Errors Field** - Structured error responses
2. **Extension Data** - Additional error details
3. **Partial Data** - Return partial results on error
4. **Custom Errors** - Domain-specific error types
