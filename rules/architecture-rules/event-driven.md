# Event-Driven Architecture Rules

## Event Design
1. **Immutable Events** - Events never change after publishing
2. **Event Carried State Transfer** - Include necessary data
3. **Schema Evolution** - Backward and forward compatibility
4. **Idempotent Events** - Safe to process multiple times

## Event Sourcing
1. **Append-Only Log** - Store all state changes as events
2. **Point-in-Time Queries** - Replay events to any point
3. **Event Replay** - Rebuild state by replaying
4. **Snapshots** - Optimize large event streams

## Message Queues
1. **Topic Design** - Clear, hierarchical topics
2. **Partition Strategy** - Distribute load
3. **Consumer Groups** - Scale consumers
4. **Message Retention** - Appropriate TTL

## Reliability Patterns
1. **Exactly-Once Delivery** - Deduplication at consumer
2. **Ordered Delivery** - Per partition ordering
3. **Poison Pill Handling** - Dead letter queues
4. **Consumer Lag Monitoring** - Track processing

## Anti-Patterns to Avoid
1. **Shared State Events** - Don't couple services
2. **Chatty Events** - Batched events better
3. **Synchronous Events** - Avoid blocking calls
4. **Version Mixing** - Support multiple versions
