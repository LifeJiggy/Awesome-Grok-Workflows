# Property-Based Testing Rules

## Concept
1. **Generate Inputs** - Random or combinatorial
2. **Test Invariants** - Properties that always hold
3. **Shrinking** - Find minimal failing case
4. **Coverage** - Explore edge cases automatically

## What to Test
1. **Invariants** - Properties that always true
2. **Symmetry** - Round-trip transformations
3. **Idempotence** - Same result for same input
4. **Laws** - Mathematical properties

## Best Practices
1. **Define Properties** - Clear, testable properties
2. **Seed Randomness** - Reproducible failures
3. **Reasonable Ranges** - Realistic input ranges
4. **Counterexamples** - Document failures

## Tools
1. **Hypothesis** - Python
2. **QuickCheck** - Haskell, ported to many languages
3. **JsVerify** - JavaScript
4. **ScalaCheck** - Scala

## Examples
```python
# Test that sorting twice gives same result
def test_sort_idempotent():
    def property(xs):
        return sorted(sorted(xs)) == sorted(xs)
    
    hypothesis.test(property)
```

```python
# Test that reverse twice returns original
def test_reverse_twice():
    def property(xs):
        return list(reversed(list(reversed(xs)))) == list(xs)
    
    hypothesis.test(property)
```
