# SQL Style Rules

## Naming Conventions
1. **Tables** - snake_case, plural (users, orders)
2. **Columns** - snake_case (user_id, created_at)
3. **Primary Keys** - id or table_name_id
4. **Foreign Keys** - table_name_id
5. **Indexes** - idx_table_name_column_name

## Query Formatting
1. **Keywords Uppercase** - SELECT, FROM, WHERE
2. **Line Breaks** - Each clause on new line
3. **Indentation** - 2 spaces for subqueries
4. **Aliases** - Descriptive, consistent

## Best Practices
1. **Explicit Columns** - No SELECT *
2. **Table Aliases** - Use for clarity
3. **JOIN Conditions** - ON, not WHERE
4. **Date Handling** - Use date functions
5. **NULL Handling** - IS NULL, IS NOT NULL

## Performance
1. **Indexes** - On frequently filtered columns
2. **EXPLAIN** - Analyze query plans
3. **Avoid SELECT *** - Only select needed columns
4. **Pagination** - Use LIMIT with OFFSET or cursor
5. **Batch Operations** - Process in chunks

## Safety
1. **Parameterized Queries** - Prevent SQL injection
2. **Transaction Management** - Proper commit/rollback
3. **Backup** - Regular backups
4. **Access Control** - Principle of least privilege
