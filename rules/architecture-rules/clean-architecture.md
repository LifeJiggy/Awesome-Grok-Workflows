# Clean Architecture Rules

## Layer Separation
1. **Entities** - Core business objects
2. **Use Cases** - Application-specific business rules
3. **Interface Adapters** - Convert data between layers
4. **Frameworks/Drivers** - External concerns

## Dependency Rule
1. **Dependencies point inward** - Inner layers don't know outer
2. **Abstractions** - Depend on interfaces, not implementations
3. **Dependency Injection** - Loose coupling
4. **Testable** - Each layer independently testable

## Organization
1. **Package by Feature** - Vertical slices over horizontal
2. **Feature Folders** - Self-contained modules
3. **Shared Kernel** - Minimal shared code
4. **Clear Boundaries** - Well-defined interfaces

## Benefits
1. **Testability** - Each layer can be tested in isolation
2. **Maintainability** - Changes localized
3. **Flexibility** - Swap implementations
4. **Independence** - Database, UI, framework independent

## Common Mistakes
1. **Anemic Domain** - Objects without behavior
2. **God Objects** - Classes doing too much
3. **Circular Dependencies** - Architecture violations
4. **Skipping Layers** - Direct database access from UI
