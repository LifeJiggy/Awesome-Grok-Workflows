# New Workflow Quick Start Template

Use this template to create a new workflow for Awesome-Grok-Workflows.

## Quick Template

```yaml
name: your-workflow-name
version: 1.0.0
description: |
  Brief description of what this workflow accomplishes.
  Keep it concise but informative.

author: YourName

tags: [tag1, tag2, tag3]

config:
  max_steps: 8
  timeout: 600
  retry_attempts: 2
  parallel_execution: true

required_skills:
  - research-oracle
  - code-review-team
  # Add other agents as needed

steps:
  - name: analyze-input
    type: thought
    description: Analyze the user input and plan approach
    agent: research-oracle
    inputs:
      user_input: "{{user_input}}"
    outputs:
      analysis: analysis.json

  - name: execute-main-task
    type: action
    description: Perform the main task
    agent: code-review-team
    depends_on: [analyze-input]
    inputs:
      analysis: "{{steps.analyze-input.outputs.analysis}}"
    outputs:
      result: result.json

  - name: validate-output
    type: reflection
    description: Validate the output meets criteria
    agent: code-review-team
    depends_on: [execute-main-task]
    inputs:
      result: "{{steps.execute-main-task.outputs.result}}"
    outputs:
      validation: validation.json

guardrails:
  - must_validate_outputs: true
  - require_human_approval_for: [deployments]
  - never_ship_broken_code: true

success_criteria:
  - output_validated: true
  - all_tests_pass: true
  - user_satisfied: true

error_handling:
  max_retries: 2
  fallback_strategies:
    - simplify_task
    - request_more_input
  escalation_conditions:
    - task_impossible
    - user_intervention_required

example_trace:
  user_input: |
    Your example input here
  steps:
    - step1: What happens
    - step2: What happens
    - step3: What happens
  output: |
    Your example output
```

## Steps to Create

1. **Copy this template** to `workflows/domain-specific/your-workflow.yaml`

2. **Fill in the placeholders**:
   - `name`: Workflow name (kebab-case)
   - `version`: Start with 1.0.0
   - `description`: Clear purpose statement
   - `author`: Your name/handle
   - `tags`: Relevant categories
   - `required_skills`: Agents from Awesome-Grok-Skills
   - `steps`: Workflow logic
   - `guardrails`: Safety constraints
   - `success_criteria`: How to measure success
   - `error_handling`: Recovery strategies
   - `example_trace`: Walkthrough of execution

3. **Validate your workflow**:
   ```bash
   ./scripts/validate-workflow.sh workflows/domain-specific/your-workflow.yaml
   ```

4. **Generate a diagram**:
   ```bash
   python scripts/render-diagram.py --input workflows/domain-specific/your-workflow.yaml
   ```

5. **Add tests**:
   - Create test in `tests/unit/test_your_workflow.py`
   - Run tests: `pytest tests/unit/test_your_workflow.py -v`

6. **Update documentation**:
   - Add to README features list
   - Create example in `docs/examples/`
   - Update CHANGELOG.md

7. **Submit a PR**:
   - Create feature branch
   - Commit changes
   - Open pull request

## Best Practices Checklist

- [ ] Name is descriptive and follows conventions
- [ ] Description clearly explains purpose
- [ ] Steps are focused and not overly complex
- [ ] Dependencies form a DAG (no cycles)
- [ ] Guardrails address safety concerns
- [ ] Success criteria are measurable
- [ ] Error handling includes fallbacks
- [ ] Example trace demonstrates execution
- [ ] YAML passes validation
- [ ] Documentation is updated

## Common Patterns

### Research → Action → Review
```yaml
steps:
  - name: research
    agent: research-oracle
  - name: act
    agent: appropriate-agent
    depends_on: [research]
  - name: review
    agent: code-review-team
    depends_on: [act]
```

### Parallel Execution
```yaml
steps:
  - name: task-a
    agent: agent-a
  - name: task-b
    agent: agent-b
  - name: combine
    agent: combiner-agent
    depends_on: [task-a, task-b]
```

### Iterative Improvement
```yaml
steps:
  - name: generate
    agent: generator-agent
  - name: evaluate
    agent: evaluator-agent
    depends_on: [generate]
  - name: improve
    agent: improver-agent
    depends_on: [evaluate]
```

## Need Help?

- Check existing workflows in `workflows/` for examples
- Read [best-practices.md](docs/best-practices.md)
- Review [architecture.md](docs/architecture.md)
- Ask in discussions or issues
