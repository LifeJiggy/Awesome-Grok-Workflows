# Performance Optimization Rules

## General Principles

### Measure First, Optimize After
1. Profile before optimizing
2. Identify actual bottlenecks
3. Measure improvement impact
4. Don't optimize what doesn't matter

### The 90/10 Rule
- 90% of time is spent in 10% of code
- Focus optimization efforts on hot paths
- Use profiling tools to identify bottlenecks

## Time Complexity Rules

### Acceptable Complexities
| Operation | Acceptable | Warning | Unacceptable |
|-----------|-----------|---------|--------------|
| Single lookup | O(1) | O(log n) | O(n) |
| Search in collection | O(log n) | O(n) | O(n²) |
| Nested iteration | O(n²) | O(n³) | O(2ⁿ) |
| Sorting | O(n log n) | O(n²) | O(2ⁿ) |

### Optimization Strategies
- **Hash maps** for O(1) lookups
- **Binary search** for sorted data
- **Caching** for repeated operations
- **Lazy evaluation** for expensive computations

## Memory Optimization

### Memory Efficiency Rules
1. **Use streams** for large files
2. **Release references** promptly
3. **Avoid memory leaks** - clean up resources
4. **Use generators** for large sequences
5. **Reuse objects** instead of creating new ones

### Memory Profiling
```python
import memory_profiler

@profile
def memory_intensive_function():
    data = [i for i in range(1000000)]
    return sum(data)
```

## Algorithm Optimization

### Common Optimizations
```python
# ❌ Slow: O(n²)
for i in range(n):
    for j in range(n):
        result[i] += matrix[i][j] * vector[j]

# ✅ Fast: O(n)
for i in range(n):
    result[i] = sum(row * vector for row, vector in zip(matrix[i], vector))
```

### Caching Strategies
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(x, y):
    """Cache results of expensive operations."""
    return complex_calculation(x, y)
```

## Database Optimization

### Query Optimization
1. **Index columns** used in WHERE clauses
2. **Select only needed columns** - avoid SELECT *
3. **Use pagination** for large result sets
4. **Avoid N+1 queries** - use eager loading
5. **Optimize JOINs** - minimize joined tables

### Example
```sql
-- ❌ Bad
SELECT * FROM users WHERE active = true;

-- ✅ Good
SELECT id, name, email FROM users WHERE active = true LIMIT 100;
```

## API Performance

### Response Optimization
1. **Compression** - gzip responses
2. **Pagination** - limit response size
3. **Caching** - cache frequent responses
4. **Async operations** - don't block on I/O
5. **Rate limiting** - prevent abuse

### Example Headers
```
Cache-Control: max-age=3600, must-revalidate
ETag: "abc123"
Vary: Accept-Encoding
```

## Frontend Performance

### Core Web Vitals
| Metric | Good | Needs Improvement |
|--------|------|-------------------|
| LCP | ≤2.5s | >2.5s |
| FID | ≤100ms | >100ms |
| CLS | ≤0.1 | >0.1 |

### Optimization Techniques
1. **Minimize bundle size** - tree shaking
2. **Code splitting** - lazy load routes
3. **Image optimization** - modern formats (WebP)
4. **CDN usage** - serve assets globally
5. **Preloading** - preload critical resources

## Monitoring and Alerting

### Key Metrics
- **Response time**: P95, P99 percentiles
- **Error rate**: 5xx errors per second
- **Throughput**: Requests per second
- **Resource usage**: CPU, memory, disk I/O

### Alert Thresholds
- **Warning**: Response time > 1s
- **Critical**: Response time > 5s
- **Warning**: Error rate > 1%
- **Critical**: Error rate > 5%
