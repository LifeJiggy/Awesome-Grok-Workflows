# Unit Testing Rules

## Test Structure
1. **AAA Pattern** - Arrange, Act, Assert
2. **One Assertion** - Per test when possible
3. **Test Name** - Descriptive: should_do_something
4. **Isolation** - Tests don't depend on each other

## What to Test
1. **Public APIs** - Test public interfaces
2. **Edge Cases** - Empty, null, boundary values
3. **Error Cases** - Invalid inputs, exceptions
4. **Happy Path** - Main functionality

## What NOT to Test
1. **Implementation Details** - Private methods
2. **Third-Party Code** - Don't test libraries
3. **Trivial Code** - Getters, setters
4. **Duplicated Tests** - Don't repeat

## Test Quality
1. **Descriptive Names** - Clear test purpose
2. **Fast Tests** - Under 100ms per test
3. **Deterministic** - Same result every time
4. **Independent** - Can run in any order

## Best Practices
1. **Test Behavior** - Not implementation
2. **Mock Dependencies** - External services
3. **Use Fixtures** - Shared test data
4. **Coverage** - Aim for 80%+ coverage
