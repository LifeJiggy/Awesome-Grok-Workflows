# Database Rules

## Schema Design
1. **Use meaningful table/column names** - snake_case, descriptive
2. **Primary keys** - Use UUIDs for distributed systems, auto-increment for single-node
3. **Foreign keys** - Explicit relationships with ON DELETE CASCADE where appropriate
4. **Indexes** - Index frequently queried columns, avoid over-indexing
5. **Soft deletes** - Use `deleted_at` timestamp instead of hard deletes

## Query Optimization
1. **Avoid SELECT *** - Specify columns explicitly
2. **Use EXPLAIN ANALYZE** to analyze query plans
3. **Pagination** - Use cursor-based for large datasets
4. **Batch operations** - Process in chunks (1000-5000 rows)
5. **N+1 problem** - Use eager loading or joins

## Transactions
1. **Keep transactions short** - Minimize lock time
2. **Deadlock prevention** - Consistent order of table access
3. **Idempotent operations** - Safe to retry
4. **Isolation levels** - Use appropriate level (READ COMMITTED default)

## Migration Best Practices
1. **Backward compatible migrations** - Deploy schema before code
2. **Non-blocking ALTERs** - Use online DDL where available
3. **Backup before migration** - Test rollbacks
4. **Version migrations** - Track schema version

## NoSQL Guidelines
1. **Choose right model** - Document vs key-value vs wide-column
2. **Denormalization** - Accept for read performance
3. **Consistency model** - Understand eventual consistency
4. **Index strategy** - Secondary indexes impact write performance

## Data Integrity
1. **Constraints** - NOT NULL, CHECK, UNIQUE where applicable
2. **Enum types** - For fixed sets of values
3. **Data validation** - At application layer too
4. **Auditing** - Track create/update timestamps

## Grok Note
- "A query without an EXPLAIN is like a physics experiment without measurements"
- Always measure before optimizing
- Index wisely - every index has a cost
