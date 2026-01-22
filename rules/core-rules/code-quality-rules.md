# Code Quality Rules

## General Standards

### Naming Conventions
- **Variables**: `camelCase` for most languages, `snake_case` for Python
- **Constants**: `UPPER_SNAKE_CASE`
- **Classes**: `PascalCase`
- **Files**: `kebab-case` for web, `snake_case` for Python
- **Functions**: `verbNoun` pattern (e.g., `getUserData`, `calculateTotal`)

### Code Organization
- **Single Responsibility**: One function, one purpose
- **Modularity**: Max 50 lines per function
- **Files**: Max 300 lines per file
- **Comments**: Explain why, not what
- **DRY**: Don't Repeat Yourself

### Formatting
- **Indentation**: 2 spaces (JavaScript/Python), 4 spaces (Java/C++)
- **Line Length**: Max 80 characters
- **Blank Lines**: Separate functions and logical sections
- **File Encoding**: UTF-8

## Language-Specific Rules

### Python
```python
# ✅ Good
def calculate_user_metrics(user_id: str) -> Dict[str, float]:
    """Calculate engagement metrics for a user."""
    if not user_id:
        raise ValueError("User ID required")
    
    metrics = {
        "engagement_score": 0.85,
        "activity_level": "high"
    }
    return metrics

# ❌ Bad
def calc(u):
    x={'s':0.85}
    return x
```

### JavaScript/TypeScript
```typescript
// ✅ Good
interface User {
  id: string;
  name: string;
  email: string;
}

function getUserById(id: string): User | null {
  if (!id) {
    throw new Error('User ID required');
  }
  return userDatabase.find(u => u.id === id) || null;
}

// ❌ Bad
function getUser(id){
  return db.find(u=>u.id==id);
}
```

## Documentation Standards

### Functions
```python
def function_name(param1: type, param2: type) -> return_type:
    """Brief description of what function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ExceptionType: When this exception is raised
    """
```

### Classes
```python
class UserService:
    """Service for managing user operations.
    
    Attributes:
        database: Database connection instance
        cache: Cache client instance
    """
    
    def __init__(self, database: Database, cache: Cache):
        """Initialize user service."""
        self.database = database
        self.cache = cache
```

## Testing Standards

### Test Organization
```
tests/
├── unit/
│   ├── test_user_service.py
│   └── test_math_utils.py
├── integration/
│   └── test_api_endpoints.py
└── e2e/
    └── test_user_journey.py
```

### Test Naming
```python
def test_user_registration_with_valid_data_creates_user():
    """Test that valid registration data creates a user."""
    # Arrange
    data = {"email": "test@example.com", "password": "secure123"}
    
    # Act
    result = register_user(data)
    
    # Assert
    assert result.success is True
    assert result.user.email == "test@example.com"
```

## Performance Rules

### Time Complexity
- **APIs**: Max O(n log n) for processing
- **Database Queries**: Indexed lookups preferred (O(log n))
- **Loops**: Avoid nested loops (O(n²))

### Memory Usage
- **Streaming**: Process large files in chunks
- **Caching**: Cache frequently accessed data
- **Lazy Loading**: Load resources on demand

## Security Rules

### Secrets Management
- **Never commit**: API keys, passwords, tokens
- **Use env vars**: Store secrets in environment
- **Rotation**: Rotate secrets regularly

### Input Validation
- **Validate all inputs**: Never trust user input
- **Sanitize**: Escape special characters
- **Type checking**: Verify data types

## Code Review Checklist

- [ ] Code follows style guidelines
- [ ] Functions are small and focused
- [ ] Naming is descriptive
- [ ] Tests cover edge cases
- [ ] Documentation is complete
- [ ] No hardcoded secrets
- [ ] Error handling is robust
- [ ] Performance is acceptable
- [ ] Security best practices followed
- [ ] No commented-out code
