# Testing Rules

## Test Pyramid
1. **Unit tests**: 70% - Fast, isolated, focused
2. **Integration tests**: 20% - Test interactions
3. **E2E tests**: 10% - Critical user journeys

## Unit Testing
1. **One assertion per test** - when possible
2. **Test behavior, not implementation**
3. **Use descriptive names** - given_when_then
4. **Test edge cases** - nulls, empty, boundary values
5. **Mock external dependencies**

## Integration Testing
1. **Test real integrations** - databases, APIs
2. **Use test databases** - not production
3. **Clean up after tests** - no state leakage
4. **Test failure scenarios** - timeouts, errors

## E2E Testing
1. **Test critical paths** - user workflows
2. **Use stable selectors** - avoid implementation details
3. **Parallel execution** - faster feedback
4. **Visual regression testing** - UI consistency

## Test Coverage
1. **Aim for 80%+ coverage** on critical code
2. **Cover edge cases** - not just happy paths
3. **Mutation testing** - verify test quality
4. **Don't chase 100%** - focus on value

## Test Data
1. **Factories over fixtures** - more flexible
2. **Randomized data** - catch hidden dependencies
3. **Deterministic when needed** - reproducible failures
4. **Realistic data** - represents production

## Test Performance
1. **Fast feedback** - under 10 minutes for full suite
2. **Parallel execution** - by test file or suite
3. **Selective running** - run affected tests first
4. **Mock slow operations** - network, file I/O
