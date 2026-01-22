# Git Commit Style Rules

## Message Format
1. **Type** - feat, fix, docs, style, refactor, test, chore
2. **Scope** - Component or area affected
3. **Description** - Brief description
4. **Body** - Detailed explanation (optional)
5. **Footer** - Breaking changes, issues closed

## Example Format
```
type(scope): description

body

footer
```

## Types
1. **feat** - New feature
2. **fix** - Bug fix
3. **docs** - Documentation only
4. **style** - Formatting, no code change
5. **refactor** - Code restructuring
6. **test** - Adding tests
7. **chore** - Maintenance tasks

## Best Practices
1. **Imperative Mood** - "Add feature" not "Added feature"
2. **Short Summary** - 50 characters or less
3. **Explain Why** - Not just what
4. **Reference Issues** - Close related issues
5. **One Commit per Change** - Atomic commits

## Examples
```
feat(auth): add password reset functionality

- Send reset email with secure token
- Token expires in 1 hour
- Rate limited to 3 requests per hour

Closes #123
```

```
fix(database): resolve connection pool leak

- Properly close connections on error
- Add connection validation before use
- Increase pool size to 20

Fixes #456
```
