# Best Practices

## Workflow Design

### Keep Workflows Focused
Each workflow should do one thing well:
- **Do**: `meme-to-viral-code-delegation` - Roast and fix code
- **Don't**: `do-everything` - Too many responsibilities

### Limit Step Count
- Optimal: 4-8 steps
- Maximum: 12 steps (use sub-workflows if more needed)
- Each step should be meaningful

### Design for Failure
- Always include error handling
- Define fallback strategies
- Set retry limits
- Plan for human escalation

### Make Steps Independent
- Minimize dependencies where possible
- Enable parallel execution
- Reduce coupling between steps

## YAML Structure

### Naming Conventions
```yaml
# ✅ Good
name: defi-yield-optimizer
name: physics-simulation-workflow

# ❌ Bad
name: myworkflow
name: wf1
```

### Versioning
- Start with `1.0.0`
- Use semantic versioning
- Update version on changes
- Document breaking changes

### Descriptive Fields
```yaml
# ✅ Good
description: |
  Orchestrate DeFi yield optimization by analyzing
  protocols, calculating APY, and executing strategies.

# ❌ Bad
description: "Does yield stuff"
```

## Agent Selection

### Match Agent to Task
| Task Type | Best Agent |
|-----------|------------|
| Research | ResearchOracle |
| Code Review | CodeReviewTeam |
| Physics | PhysicsSimulator |
| Humor | MemeRoaster |

### Provide Context
- Include relevant history
- Specify constraints clearly
- Define success criteria
- Set confidence thresholds

## State Management

### Track State Explicitly
```yaml
steps:
  - name: collect-data
    outputs: [raw_data]
  - name: process-data
    inputs: {data: "{{steps.collect-data.outputs.raw_data}}"}
    outputs: [processed_data]
```

### Avoid State Bloat
- Only pass necessary data
- Use references where possible
- Clean up temporary files
- Document state dependencies

## Error Handling

### Retry Strategy
```yaml
error_handling:
  max_retries: 3
  fallback_strategies:
    - simplify_task
    - use_backup_agent
    - request_human_help
```

### Clear Error Messages
- Explain what went wrong
- Suggest remediation
- Include relevant context
- Provide recovery options

## Testing Workflows

### Validate Early
```bash
./scripts/validate-workflow.sh your-workflow.yaml
```

### Test with Real Inputs
- Use realistic test data
- Cover edge cases
- Test error conditions
- Verify success criteria

### Document Test Results
- Record validation output
- Note any warnings
- Document workarounds
- Share with reviewers

## Performance Optimization

### Parallel Execution
Identify independent steps:
```yaml
steps:
  - name: collect-requirements
    outputs: [reqs]
  - name: research-solutions
    outputs: [research]
  # These can run in parallel if designed properly
```

### Minimize Token Usage
- Be concise in prompts
- Use variable references
- Avoid redundant outputs
- Cache where safe

### Set Appropriate Timeouts
- Simple tasks: 5-10 minutes
- Complex workflows: 30-60 minutes
- Research tasks: longer allowed
- User approval for very long tasks

## Security Considerations

### Sensitive Data
- Never include credentials in YAML
- Use environment variables
- Reference secure vaults
- Log with redaction

### Human Checkpoints
- Before deployments
- Before data modifications
- When confidence is low
- At security boundaries

### Audit Trail
- Log all state changes
- Record agent decisions
- Track handoffs
- Preserve for review

## Documentation

### Self-Documenting Workflows
```yaml
name: well-documented-workflow
description: |
  Detailed explanation of purpose and approach.
  This workflow accomplishes X by doing Y then Z.

# Comments for complex logic
steps:
  # This step does A because of reason
  - name: step-a
```

### Example Traces
Include execution traces:
```yaml
example_trace:
  input: "sample input"
  steps:
    - step-1: result
    - step-2: result
  output: final-result
```

### Update Documentation
- Update docs when changing workflows
- Version documentation
- Review docs periodically
- Remove outdated content

## Grok Personality Integration

### Use Physics Analogies
```yaml
# Instead of "This has a memory leak"
# Use "This violates conservation of memory"
```

### Meme Integration
- Use memes to enhance understanding
- Match meme level to context
- Never sacrifice accuracy for humor
- Roast bugs, not people

### Speed Optimization
- Minimize unnecessary steps
- Use caching
- Parallelize where possible
- Terminate early on success

## Anti-Patterns to Avoid

### ❌ God Workflow
```yaml
# One workflow trying to do everything
name: do-everything
steps: [step1, step2, step3, ..., step20]
```

### ❌ Undocumented Workflow
```yaml
name: wf1  # What does this do?
description: "stuff"
steps: []  # No context
```

### ❌ Missing Error Handling
```yaml
steps:
  - name: risky-operation
    # No error handling defined!
```

### ❌ Circular Dependencies
```yaml
steps:
  - name: a
    depends_on: [b]
  - name: b
    depends_on: [a]
```

### ❌ Hard-coded Values
```yaml
steps:
  - name: step
    # Using literal values instead of variables
    timeout: 3600  # What is this magic number?
```

## Checklist Before Submitting

- [ ] Workflow YAML is valid
- [ ] All steps have required fields
- [ ] Dependencies are valid (no cycles)
- [ ] Error handling is defined
- [ ] Success criteria are measurable
- [ ] Example trace is included
- [ ] Documentation is updated
- [ ] Tests pass
- [ ] Follows naming conventions
- [ ] Grok personality integrated
