# Testing Rules

## Test Pyramid

```
        /\
       /  \
      /    \      E2E Tests (10%)
     /______\
    /        \
   /          \    Integration Tests (20%)
  /____________\
 /              \
/                \  Unit Tests (70%)
/________________\
```

## Unit Testing Rules

### Coverage Requirements
| Project Type | Minimum Coverage | Target Coverage |
|--------------|-----------------|-----------------|
| Library | 95% | 100% |
| API Service | 85% | 95% |
| Frontend | 80% | 90% |
| Legacy Code | 60% | 80% |

### Test Naming
```python
# ✅ Good: Descriptive, behavior-focused
def test_user_registration_with_valid_email_creates_active_user():
    """Test that valid registration creates user with active status."""
    # Arrange
    email = "newuser@example.com"
    
    # Act
    user = register_user(email=email, password="secure123")
    
    # Assert
    assert user.status == "active"
    assert user.email == email

# ❌ Bad: Unclear, implementation-focused
def test_register():
    u = register("newuser@example.com", "secure123")
    assert u.status == "active"
```

### Test Structure (Arrange-Act-Assert)
```python
def test_calculate_discount_applies_correct_percentage():
    # Arrange
    price = 100.0
    discount_percent = 20
    
    # Act
    final_price = calculate_discount(price, discount_percent)
    
    # Assert
    assert final_price == 80.0
```

## Integration Testing

### API Testing
```python
@pytest.fixture
def api_client():
    return TestAPIClient(base_url="https://api.test.com")

def test_create_user_returns_201(api_client):
    # Act
    response = api_client.post("/users", json={
        "email": "test@example.com",
        "name": "Test User"
    })
    
    # Assert
    assert response.status_code == 201
    assert "id" in response.json()
```

### Database Testing
```python
def test_user_persisted_to_database(db_session):
    # Arrange
    user = User(email="test@example.com")
    
    # Act
    db_session.add(user)
    db_session.commit()
    
    # Assert
    retrieved = db_session.query(User).filter_by(
        email="test@example.com"
    ).first()
    assert retrieved is not None
```

## E2E Testing

### User Journey Testing
```typescript
describe('Checkout Flow', () => {
  it('completes purchase successfully', async () => {
    // Add items to cart
    await addToCart('product-1');
    await addToCart('product-2');
    
    // Proceed to checkout
    await goToCheckout();
    await fillShippingAddress({
      name: 'John Doe',
      address: '123 Main St'
    });
    
    // Complete purchase
    await enterPayment('valid-card');
    await clickCompleteOrder();
    
    // Verify success
    await expect(page).toHaveText(
      'Order confirmed'
    );
  });
});
```

## Test Data Management

### Factories
```python
import factory
from app.models import User

class UserFactory(factory.Factory):
    class Meta:
        model = dict
    
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    name = factory.Faker('name')
    status = 'active'
    created_at = factory.LazyFunction(timezone.now)
```

### Fixtures
```yaml
fixtures:
  users:
    count: 10
    attributes:
      - email
      - name
      
  orders:
    count: 50
    relations:
      user: users
    attributes:
      - total
      - status
```

## Test Environment

### Environment Configuration
```yaml
test_environment:
  database:
    engine: postgresql
    url: postgresql://test:test@localhost/test_db
  
  cache:
    engine: redis
    url: redis://localhost:6379/15
  
  services:
    mock_api: enabled
    message_queue: disabled
```

### Test Isolation
- Each test gets clean database
- No shared state between tests
- Use transactions for rollback
- Mock external services

## Performance Testing

### Load Testing
```yaml
load_test:
  target: "https://api.example.com/users"
  
  phases:
    - duration: 60s
      users: 10
    - duration: 120s
      users: 50
    - duration: 60s
      users: 10
    
  thresholds:
    p95_response_time: < 500ms
    error_rate: < 1%
```

### Test Types
| Type | Purpose | Tools |
|------|---------|-------|
| Load | Normal traffic | k6, Locust |
| Stress | Breakpoint | k6, Gatling |
| Endurance | Memory leaks | JMeter |
| Spike | Sudden load | k6 |

## Continuous Integration

### CI Pipeline
```yaml
test_job:
  runs_on: ubuntu-latest
  
  steps:
    - checkout
    - setup-python
    - pip-install:
        - pytest
        - pytest-cov
    - run-tests:
        command: pytest --cov=app tests/
    - upload-coverage:
        target: 80%
    - gate:
        condition: coverage >= 80
```

### Quality Gates
- All unit tests pass
- Integration tests pass
- Coverage meets threshold
- No security vulnerabilities
- Performance within SLA
