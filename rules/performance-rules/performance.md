# Performance Rules

## Time Complexity
1. **Avoid O(n²) algorithms** when possible
2. **Use appropriate data structures**:
   - Hash maps for O(1) lookups
   - Trees for sorted data
   - Heaps for priority queues

## Memory Management
1. **Release resources promptly** - use context managers
2. **Avoid memory leaks** - clean up references
3. **Use generators** for large datasets
4. **Profile before optimizing** - measure first

## Database Performance
1. **Use indexes** on frequently queried columns
2. **Avoid N+1 queries** - use eager loading
3. **Batch operations** - insert/update in chunks
4. **Connection pooling** - reuse database connections

## Caching Strategy
1. **Cache expensive operations** - computations, DB queries
2. **Use appropriate TTL** - based on data freshness needs
3. **Cache invalidation** - have a clear strategy
4. **Distributed cache** for multi-instance deployments

## Async Performance
1. **Use async/await** for I/O-bound operations
2. **Don't block the event loop** with CPU-intensive tasks
3. **Concurrent execution** - use asyncio.gather() for parallelism
4. **Rate limiting** - respect API limits

## Monitoring
1. **Track performance metrics** - latency, throughput
2. **Set up alerts** for performance degradation
3. **Profile in production** - use sampling profilers
4. **Capacity planning** - plan for growth
