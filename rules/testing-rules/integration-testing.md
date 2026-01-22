# Integration Testing Rules

## Scope
1. **Multiple Components** - Test interactions
2. **Real Dependencies** - Use real database, cache
3. **External Services** - Mock or use test instances
4. **API Endpoints** - Test HTTP interfaces

## Setup
1. **Test Database** - Separate from production
2. **Seed Data** - Consistent test data
3. **Clean State** - Reset before each test
4. **Resource Management** - Proper cleanup

## Best Practices
1. **Test User Journeys** - End-to-end scenarios
2. **Data Integrity** - Verify database changes
3. **Error Paths** - Test error responses
4. **Concurrency** - Test concurrent requests

## Performance
1. **Parallel Execution** - Run tests in parallel
2. **Database Per Test** - Or use transactions
3. **External Services** - Use fakes or mocks
4. **Timeouts** - Set reasonable timeouts

## Common Patterns
1. **Repository Tests** - Test data access
2. **Service Tests** - Test business logic
3. **API Tests** - Test HTTP endpoints
4. **Event Tests** - Test message handling
