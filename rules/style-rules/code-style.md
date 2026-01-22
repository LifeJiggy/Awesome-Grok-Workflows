# Code Style Rules

## Naming Conventions
1. **Variables**: snake_case (e.g., `user_name`, `total_count`)
2. **Constants**: UPPER_SNAKE_CASE (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`)
3. **Classes**: PascalCase (e.g., `UserService`, `PaymentProcessor`)
4. **Functions**: snake_case (e.g., `calculate_total()`, `process_payment()`)
5. **Files**: snake_case (e.g., `user_service.py`, `payment_processor.py`)

## Line Length
- Maximum 100 characters per line
- Use line breaks for long function calls
- Indent continuation lines properly

## Whitespace
- No trailing whitespace
- One blank line between function definitions
- No excessive blank lines
- Use spaces around operators

## Code Organization
1. Imports at the top of files
2. Constants after imports
3. Classes next
4. Functions at the bottom
5. One blank line before top-level functions

## Comment Style
- Use comments sparingly, code should be self-documenting
- Use docstrings for public functions, classes, and modules
- Inline comments for complex logic (explain "why", not "what")
- TODO comments should include ticket/reference

## Code Examples

### Good
```python
def calculate_order_total(items: List[OrderItem]) -> Decimal:
    """Calculate the total price for an order including tax."""
    subtotal = sum(item.price * item.quantity for item in items)
    tax = subtotal * TAX_RATE
    return round(subtotal + tax, 2)
```

### Bad
```python
def CalculateOrderTotal(items): # Don't do this
    total=0
    for i in items:
        total+=i.price*i.quantity
    return total*1.08
```
