# Prompt Engineering Example

This document demonstrates effective prompt engineering techniques.

## Basic Prompt Structure

### Before: Poor Prompt
```
Write code for a user login function.
```

### After: Well-Structured Prompt
```
You are a senior Python developer specializing in secure authentication.

## Task
Write a user login function with the following requirements:

## Requirements
1. Accept email and password
2. Return JWT token on success
3. Rate limit: 5 attempts per minute
4. Return 401 on invalid credentials

## Constraints
- Use Python 3.10+
- Maximum response time: 200ms
- Follow OWASP auth guidelines

## Code Standards
- Include Pydantic models for validation
- Add structured logging
- Use async/await
- Include type hints

## Output Format
Provide a single Python file with:
1. Imports
2. Pydantic models
3. Login function
4. Unit tests
```

---

## Example Prompts by Category

### Code Generation Prompt
```markdown
You are an expert {language} developer.

Task: Generate a {component} for {purpose}

Requirements:
- {requirement_1}
- {requirement_2}

Constraints:
- {constraint_1}
- {constraint_2}

Example input:
```json
{input_example}
```

Example output:
```json
{output_example}
```

Generate the code now.
```

### Analysis Prompt
```markdown
You are a {role} specializing in {domain}.

## Context
{context}

## Data to Analyze
{data}

## Analysis Framework
1. Identify key patterns
2. Evaluate against criteria
3. Provide recommendations

## Output Format
Provide analysis in this structure:
- Summary (2-3 sentences)
- Key Findings (bullet points)
- Recommendations (numbered list)
- Confidence Score (percentage)
```

### Documentation Prompt
```markdown
You are a technical writer.

## Content to Document
{code_or_specification}

## Documentation Type
{type}: {readme|api_docs|runbook|guide}

## Target Audience
{audience}: {developers|end_users|devops|all}

## Required Sections
1. Overview
2. Installation/Setup
3. Usage Examples
4. API Reference
5. Troubleshooting

## Style Guide
- Use active voice
- Include code examples
- Add diagrams where helpful
- Keep sections concise
```

---

## Template Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `{{language}}` | Programming language | Python, JavaScript, Go |
| `{{framework}}` | Framework to use | FastAPI, React, Gin |
| `{{component}}` | Component type | API, Service, Widget |
| `{{domain}}` | Knowledge domain | Security, ML, DevOps |
| `{{role}}` | AI persona | Expert, Reviewer, Architect |
| `{{context}}` | Background info | Project description |
| `{{requirements}}` | Functional needs | What it should do |
| `{{constraints}}` | Limitations | Performance, security |
| `{{output_format}}` | Response format | JSON, Markdown, Code |

---

## Best Practices

### 1. Be Specific
```diff
- "Write a function to process data"
+ "Write an async function to validate email addresses using regex, returning True/False"
```

### 2. Provide Context
```diff
- "Generate API code"
+ "Generate REST API code for a user management service in a fintech application (requires PCI compliance)"
```

### 3. Define Output Format
```diff
- "Explain the solution"
+ "Explain the solution in this format:\n1. Summary\n2. Pros\n3. Cons\n4. Recommendation"
```

### 4. Include Examples
```diff
- "Validate the input"
+ "Validate the input:\nInput: {\"email\": \"test@example.com\"}\nExpected: {\"valid\": true, \"domain\": \"example.com\"}"
```

### 5. Set Constraints
```diff
- "Make it fast"
+ "Optimize for latency < 100ms, memory < 50MB"
```
