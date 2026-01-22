# Database Performance Rules

## Query Optimization
1. **Use Indexes** - On frequently queried columns
2. **Avoid SELECT *** - Select only needed columns
3. **Limit Results** - Use LIMIT and pagination
4. **Optimize Joins** - Use appropriate join types

## Schema Design
1. **Normalize** - Proper normalization
2. **Index Strategy** - Balance read/write performance
3. **Partitioning** - For large tables
4. **Denormalization** - For read-heavy workloads

## Connection Management
1. **Connection Pooling** - Reuse connections
2. **Timeout Settings** - Appropriate timeouts
3. **Failover** - Automatic failover
4. **Load Balancing** - Distribute read load

## Caching
1. **Query Cache** - Cache frequent queries
2. **Application Cache** - Redis, Memcached
3. **CDN** - Cache static content
4. **Cache Invalidation** - Clear strategy

## Monitoring
1. **Slow Query Log** - Identify slow queries
2. **Index Usage** - Monitor index effectiveness
3. **Connection Pool** - Track pool usage
4. **Performance Metrics** - Track over time
