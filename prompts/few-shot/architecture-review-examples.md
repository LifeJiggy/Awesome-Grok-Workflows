# Architecture Review Examples

## Example 1: Microservices Migration

**Input:**
> Review this monolith-to-microservices migration plan. Current: Django monolith, 200k LOC, 50 tables. Target: 12 microservices.

**Good Response:**
```
## Architecture Review: Monolith → Microservices

### Overall Assessment: APPROVED WITH CONDITIONS ✓

### Strengths ✓
1. **Domain-driven decomposition** - Clear service boundaries
2. **API-first design** - Contract-first approach
3. **Event-driven communication** - Decoupled services
4. **Database-per-service** - Proper isolation

### Concerns ⚠️
1. **Distributed tracing missing** - How will we debug cross-service?
2. **Service mesh not considered** - Traffic management needs
3. **Migration order questionable** - Start with less coupled services

### Specific Findings

#### CRITICAL: Data Consistency
❌ "Saga pattern implementation incomplete"
- Pattern identified but compensation logic missing
- "This is a distributed transaction waiting to cause entropy"
- Add: Rollback procedures, eventual consistency guarantees

#### MAJOR: Observability
❌ "No tracing strategy defined"
- Cross-service debugging will be impossible
- Recommendation: Jaeger or Zipkin from day one

#### MINOR: API Versioning
⚠️ "Consider API gateway for versioning"
- Easier than per-service versioning

### Recommendation Score: 7/10
Proceed after addressing critical items.

### Next Steps
1. [ ] Implement distributed tracing
2. [ ] Design saga choreography
3. [ ] Select service mesh
4. [ ] Document API versioning strategy
```

## Example 2: Event-Driven Architecture

**Input:**
> Review this event-driven system design. Using Kafka, 1M events/day, 5 producers, 20 consumers.

**Good Response:**
```
## Architecture Review: Event-Driven System

### Overall Assessment: APPROVED ✓✓

### Excellent Decisions ⭐
1. **Kafka for durability** - Correct choice for this scale
2. **Schema registry** - Proactive data contracts
3. **Dead letter queues** - Error handling considered
4. **Consumer groups** - Scalable consumption

### Potential Improvements

#### PERFORMANCE
⚠️ "Partition strategy needs review"
- Current: user_id partitioning
- Consider: Time-based for analytics consumers
- "This partition key is about to become a bottleneck"

#### RELIABILITY
⚠️ "Consumer lag monitoring missing"
- No alerting on processing delays
- Add: Kafka monitoring, lag thresholds

#### SECURITY
⚠️ "Encryption at rest not configured"
- Kafka data at rest is unprotected
- Add: Disk encryption, ACLs

### Score: 8.5/10
Solid foundation, polish observability.

### Quick Wins
- Add consumer lag dashboard
- Implement schema evolution rules
- Document retry policies
```

## Example 3: Database Schema Review

**Input:**
> Review this schema for a high-traffic e-commerce system. Expecting 10k RPS.

**Good Response:**
```
## Database Schema Review

### Overall Assessment: NEEDS WORK ⚠️

### Critical Issues 🚨

#### ID GENERATION
❌ "Auto-increment PKs at scale = pain"
- MySQL auto-increment has single-node limitation
- Recommendation: UUID v7 or Snowflake
- "This is a distributed systems problem waiting to happen"

#### MISSING INDEXES
❌ "No indexes on frequently queried columns"
- `SELECT * FROM orders WHERE user_id AND status` — full table scan
- Add: (user_id, status), (created_at), (status, created_at)

#### LOCK CONTENTION
❌ "Inventory table will be hotspot"
- Single row for inventory per product
- Recommendation: Shard by product category or use optimistic locking

### Design Issues

#### N+1 RISK
⚠️ "Address table design encourages N+1 queries"
- Users have multiple addresses with type
- Consider: JSONB column for simple cases

#### SOFT DELETES
⚠️ "No soft delete strategy"
- Deleted orders still counted in queries
- Add: `deleted_at` with composite index

### Recommendations Summary
1. Switch to UUID v7 for IDs
2. Add 3+ critical indexes
3. Implement inventory sharding
4. Add soft deletes

### Score: 5/10
Fix before production.
```
