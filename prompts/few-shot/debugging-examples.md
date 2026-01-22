---
version: "1.0.0"
created: "2024-01-01"
updated: "2024-01-01"
author: "Grok-Workflow-Builder-v1"
purpose: "Few-shot examples for debugging and problem-solving"
---

# Debugging Examples

## Example 1: Memory Leak Detection

**Problem**: Service memory usage grows continuously until OOM kill

**Debugging Session (Example)**:
```markdown
## Memory Leak Investigation 🐛

### Symptoms
- Memory grows 100MB/hour
- No increase in traffic
- Restart temporarily fixes
- GC doesn't help

### Investigation

**1. Check memory growth pattern**
```
Rate: 100MB/hour = ~1.7MB/minute
Pattern: Linear (not exponential)
```

**2. Profile heap**
```python
# Using tracemalloc
import tracemalloc

tracemalloc.start()

# ... run service for 1 hour ...

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)
```

**3. Findings**
```
Filename: app/cache.py:45
Count: 5000 objects
Size: 150MB
Traceback (most recent call last):
  File "app/cache.py", line 45, in get_or_create
    if key in cache:
  File "app/cache.py", line 67, in __contains__
    return self._cache.get(key) is not None
```

**4. Root Cause Analysis**
```python
# BUG: Cache grows without eviction
class Cache:
    def __init__(self):
        self._cache = {}  # Never cleared!
    
    def get_or_create(self, key, factory):
        if key in self._cache:  # This line creates issue
            return self._cache[key]
        # ...
```

**5. Fix**
```python
class Cache:
    def __init__(self, max_size=1000):
        self._cache = OrderedDict()
        self.max_size = max_size
    
    def get_or_create(self, key, factory):
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        
        if len(self._cache) >= self.max_size:
            self._cache.popitem(last=False)
        
        self._cache[key] = factory()
        return self._cache[key]
```

**6. Verification**
```
After fix: Memory stable at ~150MB for 24 hours
```

### Prevention Checklist
- [ ] Set cache size limits
- [ ] Use LRU eviction
- [ ] Monitor memory in production
- [ ] Set up OOM alerts
- [ ] Regular memory profiling
```

## Example 2: Race Condition

**Problem**: Intermittent test failures, sometimes wrong data

**Debugging Session (Example)**:
```markdown
## Race Condition Investigation 🏃

### Symptoms
- 5% test failure rate
- No consistent failure pattern
- Data sometimes overwritten
- Happens under load

### Investigation

**1. Reproduce under load**
```bash
# Run 100 concurrent requests
for i in {1..100}; do
  curl -X POST http://api/users -d '{"name":"test"}" &
done
wait
```

**2. Find concurrency issue**
```python
# Original code
def update_user(user_id, data):
    user = db.get(user_id)
    user.name = data['name']
    user.save()  # ← Race here!
```

**3. Demonstrate race**
```
Request A: Read user (name="Alice")
Request B: Read user (name="Alice")
Request A: Update name="Bob"
Request B: Update name="Charlie"
Result: name="Charlie" (A's update lost!)
```

**4. Root Cause**
- Read-modify-write pattern
- No optimistic locking
- No transaction isolation

**5. Fix - Option 1: Optimistic Locking**
```python
def update_user(user_id, data, expected_version):
    user = db.get(user_id)
    
    if user.version != expected_version:
        raise ConflictError("Concurrent modification")
    
    user.name = data['name']
    user.version += 1
    user.save()
```

**6. Fix - Option 2: Pessimistic Locking**
```python
def update_user(user_id, data):
    with db.transaction():
        user = db.select_for_update().get(user_id)
        user.name = data['name']
        user.save()
```

**7. Test fix**
```python
def test_concurrent_updates():
    user = create_user()
    
    # Run 100 concurrent updates
    results = []
    for _ in range(100):
        results.append(update_user(user.id, {"name": random_name()}))
    
    # Verify only one update won
    user.refresh()
    assert results.count(user.name) == 1
```

### Prevention Checklist
- [ ] Use transactions for multi-step operations
- [ ] Implement optimistic/pessimistic locking
- [ ] Test under concurrent load
- [ ] Use atomic operations where possible
- [ ] Monitor for conflicts
```

## Example 3: Performance Degradation

**Problem**: API response time increased from 50ms to 2s

**Debugging Session (Example)**:
```markdown
## Performance Regression Investigation ⚡

### Symptoms
- P50: 50ms → 200ms
- P99: 200ms → 2s
- Only affects write operations
- Started after deployment v2.4.0

### Investigation

**1. Compare versions**
```
v2.3.0: P50=50ms, P99=200ms ✓
v2.4.0: P50=200ms, P99=2000ms ✗
```

**2. Code changes in v2.4.0**
```python
# New feature added
def create_user(data):
    user = User(**data)
    user.save()  # Was this changed?
    
    # NEW: Send welcome email
    send_welcome_email(user)  # ← External API call!
    
    # NEW: Log analytics
    analytics.track('user_created', user)  # ← Database insert!
    
    return user
```

**3. Measure each operation**
```
user.save(): 20ms (unchanged)
send_welcome_email(): 150ms (slow!)
analytics.track(): 180ms (very slow!)
Total: 350ms
```

**4. Fix - Async operations**
```python
def create_user(data):
    user = User(**data)
    user.save()
    
    # Run in background
    asyncio.create_task(send_welcome_email(user))
    asyncio.create_task(analytics.track('user_created', user))
    
    return user
```

**5. Verification**
```
After fix: P50=30ms, P99=80ms ✅
```

### Prevention Checklist
- [ ] Profile before/after deployments
- [ ] Set performance budgets
- [ ] Monitor SLOs continuously
- [ ] Async non-critical operations
- [ ] Use feature flags
- [ ] Load test before release
```

---

# Debugging Framework

## Investigation Process

```
1. Reproduce
   ↓
2. Isolate
   ↓
3. Hypothesize
   ↓
4. Test
   ↓
5. Fix
   ↓
6. Verify
   ↓
7. Prevent
```

## Tools by Issue Type

| Issue | Tools |
|-------|-------|
| Memory leaks | tracemalloc, pympler, memory_profiler |
| CPU profiling | cProfile, py-spy, line_profiler |
| Race conditions | ThreadSanitizer, coverage analysis |
| Network issues | tcpdump, wireshark, mitmproxy |
| Database queries | EXPLAIN ANALYZE, slow query log |
| Disk I/O | iostat, strace, lsof |
