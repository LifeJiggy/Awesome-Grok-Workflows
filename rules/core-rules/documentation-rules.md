# Documentation Rules

## Documentation Types

### 1. Code Documentation
- **Docstrings**: Every public function/class
- **Inline comments**: Complex logic only
- **Type hints**: All function signatures
- **README**: Project overview

### 2. API Documentation
- **Endpoint descriptions**: Purpose and usage
- **Parameters**: Types, required/optional
- **Response formats**: Examples for all cases
- **Error codes**: All possible errors

### 3. Architecture Documentation
- **System diagrams**: Visual architecture
- **Data flow**: How data moves through system
- **Component descriptions**: What each part does
- **Decision records**: Why decisions were made

### 4. User Documentation
- **Getting started**: Quick setup guide
- **Tutorials**: Step-by-step walkthroughs
- **How-to guides**: accomplish specific tasks
- **FAQ**: Common questions answered

## Documentation Standards

### Language
- **Tense**: Present tense
- **Voice**: Active voice
- **Clarity**: Simple, clear language
- **Consistency**: Same terms throughout

### Structure
```
# Title (H1)

## Overview
Brief description

## Usage
How to use

## Examples
Code examples

## API Reference
Detailed API docs

## Troubleshooting
Common issues

## See Also
Related documentation
```

### Example Docstring (Python)
```python
def calculate_compound_interest(
    principal: float,
    rate: float,
    time_years: int,
    compounding_frequency: int = 12
) -> float:
    """Calculate compound interest with regular compounding.
    
    Calculates the future value of an investment using the compound
    interest formula: A = P(1 + r/n)^(nt)
    
    Args:
        principal: Initial investment amount (positive float)
        rate: Annual interest rate as decimal (e.g., 0.05 for 5%)
        time_years: Investment duration in years
        compounding_frequency: Times per year interest is compounded
            - 12 = monthly
            - 4 = quarterly
            - 1 = annually
    
    Returns:
        Future value of the investment
    
    Raises:
        ValueError: If principal is negative
        ValueError: If rate is outside [0, 1]
    
    Example:
        >>> calculate_compound_interest(1000, 0.05, 10, 12)
        1647.009497690583
    
    See Also:
        - Simple interest: calculate_simple_interest()
        - APY calculation: calculate_apy()
    """
    if principal < 0:
        raise ValueError("Principal must be positive")
    if not 0 <= rate <= 1:
        raise ValueError("Rate must be between 0 and 1")
    
    return principal * (1 + rate / compounding_frequency) ** (
        compounding_frequency * time_years
    )
```

### Example API Doc (OpenAPI)
```yaml
/users/{user_id}:
  get:
    summary: Get user by ID
    description: Retrieves user information for the specified user ID
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: string
          format: uuid
        description: Unique user identifier
      - name: include_profile
        in: query
        schema:
          type: boolean
          default: false
        description: Include user profile data
    responses:
      '200':
        description: User found
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
      '404':
        description: User not found
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Error'
```

## Version Control

### Changelog Format
```markdown
# Changelog

## [version] - YYYY-MM-DD

### Added
- Feature X
- Feature Y

### Changed
- Behavior Z updated
- Performance improvement

### Deprecated
- Feature W (use Feature V instead)

### Removed
- Old API endpoint /old

### Fixed
- Bug in feature Y

### Security
- Vulnerability CVE-XXXX-XXXX patched
```

### Version Documentation
- Document all breaking changes
- Provide migration guides
- Maintain backwards compatibility when possible
- Deprecate features before removal

## Review Process

### Documentation Review Checklist
- [ ] Grammar and spelling correct
- [ ] Code examples work
- [ ] Links are valid
- [ ] Diagrams are clear
- [ ] Consistent terminology
- [ ] Up to date with code changes
- [ ] Appropriate detail level
- [ ] Good file organization
