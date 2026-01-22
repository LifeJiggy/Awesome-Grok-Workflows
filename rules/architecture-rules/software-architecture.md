# Architecture Rules

## Design Principles
1. **SOLID Principles**:
   - Single Responsibility
   - Open/Closed
   - Liskov Substitution
   - Interface Segregation
   - Dependency Inversion

2. **KISS** - Keep It Simple, Stupid
3. **YAGNI** - You Aren't Gonna Need It
4. **DRY** - Don't Repeat Yourself
5. **Composition over Inheritance**

## Module Organization
1. **High cohesion** - related code together
2. **Low coupling** - minimal dependencies between modules
3. **Clear boundaries** - well-defined interfaces
4. **Dependency injection** - for testability

## API Design
1. **RESTful conventions** for HTTP APIs
2. **Version APIs** - backward compatibility
3. **Error handling** - consistent error responses
4. **Documentation** - OpenAPI specs

## Microservices
1. **Single responsibility** per service
2. **Async communication** when possible
3. **Circuit breakers** for fault tolerance
4. **Service discovery** - dynamic registration

## Data Architecture
1. **Data ownership** - single source of truth
2. **Event sourcing** for audit trails
3. **CQRS** for read-heavy systems
4. **Database per service** - isolation

## Reliability Patterns
1. **Retries with backoff**
2. **Bulkheads** - isolate failures
3. **Dead letter queues** for failed messages
4. **Health checks** for all services
