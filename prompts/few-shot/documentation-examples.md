# Documentation Examples

## Example 1: API Documentation

**Input:**
> Document this REST API for a user management service. Endpoints: create user, get user, update user, delete user, list users.

**Good Response:**
```
# User Management API

## Overview
RESTful API for user lifecycle management. All endpoints require `Authorization: Bearer <token>` header.

## Endpoints

### Create User
`POST /api/v1/users`

**Request Body:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "roles": ["user"],
  "metadata": {
    "source": "signup"
  }
}
```

**Response (201 Created):**
```json
{
  "id": "usr_abc123",
  "email": "user@example.com",
  "name": "John Doe",
  "roles": ["user"],
  "status": "active",
  "created_at": "2024-01-15T10:30:00Z",
  "metadata": {"source": "signup"}
}
```

**Errors:**
- 400: Invalid input
- 409: Email already exists
- 422: Validation error

---

### Get User
`GET /api/v1/users/{user_id}`

**Response (200 OK):**
```json
{
  "id": "usr_abc123",
  "email": "user@example.com",
  "name": "John Doe",
  "roles": ["user"],
  "status": "active",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T12:00:00Z"
}
```

**Errors:**
- 401: Unauthorized
- 403: Forbidden
- 404: User not found

---

### List Users
`GET /api/v1/users?status=active&limit=20&cursor=abc123`

**Query Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| status | string | all | Filter by status |
| limit | int | 20 | Max results (1-100) |
| cursor | string | - | Pagination cursor |

**Response (200 OK):**
```json
{
  "data": [...],
  "pagination": {
    "next_cursor": "xyz789",
    "has_more": true
  }
}
```

---

### Update User
`PATCH /api/v1/users/{user_id}`

**Request Body:**
```json
{
  "name": "John Updated",
  "metadata": {
    "last_login": "2024-01-15T15:00:00Z"
  }
}
```

---

### Delete User
`DELETE /api/v1/users/{user_id}`

**Response (204 No Content)**

*Note: Soft delete — data retained for 30 days.*
```

## Example 2: Technical Concept Explanation

**Input:**
> Explain database indexing to a junior developer.

**Good Response:**
```
# Database Indexing: A Developer's Guide

## What is an Index?
Think of a book index — it's a sorted list that lets you find information without reading every page.

## Types of Indexes

### B-Tree (Most Common)
```
Values: [1, 5, 10, 15, 20, 25, 30]
         ↓     ↓     ↓     ↓     ↓
       Leaf Leaf Leaf Leaf Leaf Leaf
```
- Works great for range queries (`WHERE age > 18`)
- Default in most databases
- O(log n) lookup time

### Hash Index
```
Values: [apple, banana, cherry]
         ↓       ↓        ↓
       Hash    Hash     Hash
```
- Perfect for exact matches (`WHERE email = 'x'`)
- Can't do range queries
- O(1) lookup time

### Full-Text Index
- For searching text content
- Handles stemming, stop words
- `WHERE MATCH(content) AGAINST('search term')`

## When to Index
✅ Columns in WHERE clauses  
✅ Columns used in JOINs  
✅ Columns in ORDER BY  
✅ Foreign keys  

## When NOT to Index
❌ Small tables (overhead > benefit)  
❌ Columns with low cardinality (few unique values)  
❌ Columns frequently updated (index maintenance cost)  

## Performance Example
```sql
-- Without index: Full table scan (100ms)
SELECT * FROM users WHERE email = 'test@example.com';

-- With index: Index seek (1ms)
SELECT * FROM users WHERE email = 'test@example.com';
-- Index used: idx_users_email
```

## The Trade-off
Every index:
- **Writes slower** (must update index)
- **Uses more storage** (duplicate data)
- **Reads faster** (for indexed queries)

Choose wisely! 🚀
```

## Example 3: Runbook/Troubleshooting Guide

**Input:**
> Create a runbook for high CPU usage on production server.

**Good Response:**
```
# Runbook: High CPU Alert

## Severity: P2 - Major

## Diagnosis

### Symptoms
- CPU usage > 90% for > 5 minutes
- Response times increased
- Some requests timing out

### Quick Checks
```bash
# 1. What's consuming CPU?
top -c

# 2. Is it one process or many?
ps aux --sort=-%cpu | head -20

# 3. Database load?
SELECT pid, now() - pg_stat_activity.query_start AS duration, query 
FROM pg_stat_activity 
ORDER BY duration DESC LIMIT 5;
```

## Common Causes

### 1. Runaway Process
**Symptoms:** Single process at 300% CPU
**Fix:**
```bash
# Find the culprit
ps aux | grep -E 'python|node|java' | sort -k3 -r

# Check if legitimate
kill -STOP <pid>  # Pause to investigate
```

### 2. Database Query
**Symptoms:** Many DB connections, slow queries
**Fix:**
```sql
-- Kill long-running query (carefully!)
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE state = 'active' 
AND query_start < NOW() - INTERVAL '5 minutes';
```

### 3. DDoS/Traffic Spike
**Symptoms:** Many similar requests, varied IPs
**Fix:**
```bash
# Check request rates
tail -f /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -20

# If DDoS: Enable rate limiting
nginx -s reload
```

## Remediation Steps

1. **Immediate:** Scale horizontally if possible
2. **Short-term:** Restart problematic services
3. **Medium-term:** Optimize/code review
4. **Long-term:** Architecture changes

## Escalation
- P1: Infrastructure team lead
- P2: On-call engineer
- P3: Next business day

## Post-Incident
- [ ] Document root cause
- [ ] Update monitoring thresholds
- [ ] Add alerting correlation
- [ ] Schedule remediation task
```
