---
version: "1.0.0"
created: "2024-01-01"
updated: "2024-01-01"
author: "Grok-Workflow-Builder-v1"
purpose: "Few-shot examples for code review and refactoring"
---

# Code Review Examples

## Example 1: Security Vulnerability Detection

**Input Code (Bad)**:
```python
def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
```

**Good Review (Example)**:
```markdown
## Security Review: SQL Injection Vulnerability ⚠️

**Severity**: Critical  
**CWE**: CWE-89: SQL Injection  
**Line**: 2

### Issue
This code is vulnerable to SQL injection attacks. The `user_id` is directly interpolated into the query string.

**Attack Vector**:
```python
# Malicious input
get_user_data("1; DROP TABLE users;--")
```

### Fix (Good Code)
```python
def get_user_data(user_id):
    # Parameterized query
    return db.execute(
        "SELECT * FROM users WHERE id = %s",
        [user_id]
    )
```

### Why This Works
- Separates query structure from data
- Database handles escaping
- Prevents injection attacks
```

## Example 2: Performance Optimization

**Input Code (Bad)**:
```python
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                duplicates.append(items[i])
    return list(set(duplicates))
```

**Good Review (Example)**:
```markdown
## Performance Review: O(n²) to O(n) ⚡

**Complexity**: O(n²) → O(n)  
**Speedup**: ~100x for n=10,000

### Issues
1. Nested loops = quadratic complexity
2. Redundant duplicate entries
3. Inefficient list appending

### Optimized Code
```python
from collections import Counter

def find_duplicates(items):
    counter = Counter(items)
    return [item for item, count in counter.items() if count > 1]
```

### Benchmark Results
| n | Original | Optimized | Speedup |
|---|----------|-----------|---------|
| 100 | 0.01s | 0.001s | 10x |
| 1000 | 0.5s | 0.005s | 100x |
| 10000 | 50s | 0.05s | 1000x |
```

## Example 3: Error Handling

**Input Code (Bad)**:
```python
def parse_json(data):
    try:
        return json.loads(data)
    except:
        return {}
```

**Good Review (Example)**:
```markdown
## Code Quality: Silent Error Suppression 🛡️

**Issue**: Empty except clause masks all errors

### Problems
1. Catches KeyboardInterrupt, SystemExit
2. Returns empty dict for any error
3. No logging or error reporting
4. Makes debugging impossible

### Improved Code
```python
import logging
from json import JSONDecodeError

logger = logging.getLogger(__name__)

def parse_json(data):
    try:
        return json.loads(data)
    except JSONDecodeError as e:
        logger.error(f"Failed to parse JSON: {e}")
        raise ValueError(f"Invalid JSON: {e}") from e
```

### Best Practices
- Catch specific exceptions only
- Log errors for debugging
- Provide context in errors
- Consider recovery options
```

## Example 4: API Design

**Input Code (Bad)**:
```python
class User:
    def __init__(self, id, name, email, password, created):
        self.id = id
        self.name = name
        self.email = email
        self.password = password  # Exposed!
        self.created = created
```

**Good Review (Example)**:
```markdown
## Design Review: Data Encapsulation 🚀

**Issues**:
1. Password stored in plaintext
2. All attributes public
3. No validation on init
4. No representation methods

### Improved Code
```python
class User:
    def __init__(self, id: int, name: str, email: str, password_hash: str):
        self._id = id
        self._name = name
        self._email = email
        self._password_hash = password_hash
        self._created = datetime.now()
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def email(self) -> str:
        return self._email
    
    def verify_password(self, password: str) -> bool:
        return check_password_hash(self._password_hash, password)
    
    def __repr__(self) -> str:
        return f"<User(id={self._id}, email={self._email})>"
```

### Improvements
- Password never exposed
- Validation in init
- Read-only properties
- Proper representations
- Password verification
```

## Example 5: Async/Await Pattern

**Input Code (Bad)**:
```python
async def fetch_data(url):
    response = await requests.get(url)
    return response.json()
```

**Good Review (Example)**:
```markdown
## Async Review: Blocking I/O in Async Code ⚠️

**Severity**: Medium  
**Impact**: Blocks event loop

### Issue
`requests` library is synchronous and will block the async event loop.

### Fix (Good Code)
```python
import aiohttp

async def fetch_data(url: str, timeout: int = 10) -> dict:
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
```

### Benefits
- True async I/O
- Proper timeout handling
- Connection pooling
- Automatic cleanup
```

---

# Template for Code Review

## Review Structure
```
1. Overview (2-3 sentences)
2. Severity & Category
3. Issue Description
4. Code Example (before/after)
5. Why This Matters
6. Best Practice Reference
7. Fix Recommendation
```

## Severity Levels
| Level | Description | Example |
|-------|-------------|---------|
| Critical | Security/Availability | SQL injection, DoS |
| High | Data corruption | Unhandled exceptions |
| Medium | Performance/Maintainability | O(n²) algorithms |
| Low | Style/Convention | Naming, formatting |
