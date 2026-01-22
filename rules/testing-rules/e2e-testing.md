# E2E Testing Rules

## Scope
1. **Critical Paths** - Most important user journeys
2. **Full Stack** - Test entire application
3. **Real Browser** - Test in real browser
4. **Real User Scenarios** - How users actually use it

## Best Practices
1. **Stable Selectors** - Use data-testid attributes
2. **Independent Tests** - No shared state
3. **Explicit Waits** - Wait for elements, not sleep
4. **Page Objects** - Abstract page structure

## Test Coverage
1. **Happy Path** - Main user flow
2. **Error States** - Error messages, validation
3. **Edge Cases** - Empty states, limits
4. **Responsive Design** - Different screen sizes

## Performance
1. **Timeout Settings** - Reasonable timeouts
2. **Screenshots** - On failure for debugging
3. **Video Recording** - For CI failures
4. **Parallel Execution** - Faster feedback

## Anti-Patterns
1. **Testing Everything** - Focus on value
2. **Brittle Tests** - Fragile selectors
3. **Long Tests** - Break into smaller tests
4. **Flaky Tests** - Must be deterministic
