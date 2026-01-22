# Documentation Rules

## Code Documentation
1. **Docstrings** for all public functions, classes, modules
2. **Type hints** for function signatures
3. **Inline comments** for complex logic (explain why)
4. **README.md** for every major component

## Docstring Format
```python
def function_name(param1: Type, param2: Type) -> ReturnType:
    """Short description of what the function does.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ExceptionType: When this exception is raised

    Example:
        >>> function_name(x, y)
        result
    """
```

## API Documentation
1. **OpenAPI/Swagger specs** for all HTTP APIs
2. **Postman collections** for testing
3. **API changelog** - version differences
4. **Deprecation notices** - advance warning

## Architecture Documentation
1. **System diagrams** - architecture overviews
2. **Decision logs** - why decisions were made
3. **Data flow diagrams** - how data moves
4. **Deployment guides** - how to deploy

## Runbooks
1. **Incident response** - step-by-step procedures
2. **Onboarding** - getting started guides
3. **Troubleshooting** - common issues and fixes
4. **Operations** - maintenance procedures

## Style Guide
1. **Active voice** - "Do X" not "X is done"
2. **Consistent terminology** - same words for same concepts
3. **Code examples** - working, up-to-date
4. **Version references** - link to relevant versions

## Review Process
1. **Documentation review** in PRs
2. **Stale detection** - flag outdated docs
3. **Single source of truth** - avoid duplication
4. **Links work** - verify internal links
