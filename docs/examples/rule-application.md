# Rule Application Example

This document demonstrates how to apply rules in different scenarios.

## Scenario 1: Code Review with Multiple Rules

### Input Code
```python
def CALCULATE_Total(orders):
    total=0
    for o in orders:
        if o.status=="completed":
            total=total+o.amount # Add to total
    return TOTAL
```

### Applied Rules

#### Rule 1: Python Style (python-style.md)
```diff
- def CALCULATE_Total(orders):  # ❌ PascalCase function name
+ def calculate_total(orders):  # ✅ snake_case

- total=0                         # ❌ Missing spaces
+ total = 0                       # ✅ Proper spacing

- for o in orders:                # ❌ Single-letter variable
+ for order in orders:            # ✅ Descriptive name

- return TOTAL                    # ❌ UPPER_SNAKE_CASE variable
+ return total                    # ✅ snake_case
```

#### Rule 2: Documentation Rules (documentation-rules.md)
```diff
- def calculate_total(orders):    # ❌ No docstring
+ def calculate_total(orders):
+     """Calculate the total amount for completed orders."""
+     
+     Args:
+         orders: List of order dictionaries
+         
+     Returns:
+         float: Total amount of completed orders
```

#### Rule 3: Testing Rules (testing-rules.md)
```python
# Required: Unit test for this function
def test_calculate_total():
    """Test calculate_total function."""
    orders = [
        {"status": "completed", "amount": 100},
        {"status": "pending", "amount": 50},
        {"status": "completed", "amount": 75},
    ]
    assert calculate_total(orders) == 175
```

### Refactored Code
```python
def calculate_total(orders: list[dict]) -> float:
    """
    Calculate the total amount for completed orders.
    
    Args:
        orders: List of order dictionaries with 'status' and 'amount' keys
        
    Returns:
        float: Total amount of completed orders
    """
    total = 0
    for order in orders:
        if order["status"] == "completed":
            total += order["amount"]
    return total
```

---

## Scenario 2: API Design with REST Rules

### Input: Poor API Design
```http
POST /getUserInfo.php?user_id=123
GET /deleteUser
POST /updateUserData
```

### Applied Rules: REST API Design (rest-api.md)
```diff
- POST /getUserInfo.php?user_id=123  # ❌ Verb in URL, .php extension
+ GET /users/123                       # ✅ Noun, proper path

- GET /deleteUser                      # ❌ HTTP method mismatch
+ DELETE /users/123                    # ✅ Proper HTTP method

- POST /updateUserData                 # ❌ Verb in URL
+ PATCH /users/123                     # ✅ Partial update
  Body: {"email": "new@example.com"}
```

---

## Scenario 3: Security Rule Application

### Input: Insecure Code
```python
def login(username, password):
    query = f"SELECT * FROM users WHERE name = '{username}' AND pass = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()
```

### Applied Rules: Security Rules (security-rules.md)

```diff
- query = f"SELECT * FROM users WHERE name = '{username}' AND pass = '{password}'"
+ query = "SELECT * FROM users WHERE name = %s AND pass = %s"
+ cursor.execute(query, (username, password))

- return cursor.fetchone()              # ❌ Returns password
+ user = cursor.fetchone()
+ if user and verify_password(password, user['pass']):
+     del user['pass']                   # Remove sensitive data
+     return user
```

### Security Checklist Applied
- ✅ Parameterized queries (prevents SQL injection)
- ✅ Password verification
- ✅ Sensitive data removal
- ✅ No plain text password storage
