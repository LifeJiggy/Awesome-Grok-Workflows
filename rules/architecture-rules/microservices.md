# Microservices Architecture Rules

## Service Design
1. **Single Responsibility** - Each service does one thing well
2. **Loose Coupling** - Services communicate via APIs, not shared databases
3. **High Cohesion** - Related functionality in one service
4. **Stateless Services** - External state in databases or caches

## Communication Patterns
1. **Synchronous** - HTTP/REST for request-response
2. **Asynchronous** - Message queues for event-driven
3. **Service Mesh** - Istio, Linkerd for cross-cutting concerns
4. **API Gateway** - Single entry point for routing

## Data Management
1. **Database per Service** - Own data store per microservice
2. **Saga Pattern** - Distributed transactions
3. **Event Sourcing** - State changes as events
4. **CQRS** - Separate read and write models

## Reliability
1. **Circuit Breakers** - Prevent cascade failures
2. **Retries with Backoff** - Handle transient failures
3. **Bulkheads** - Isolate failures
4. **Dead Letter Queues** - Handle failed messages

## Deployment
1. **Containerization** - Docker for consistency
2. **Orchestration** - Kubernetes for management
3. **CI/CD** - Automated testing and deployment
4. **Blue-Green Deployment** - Zero-downtime releases
