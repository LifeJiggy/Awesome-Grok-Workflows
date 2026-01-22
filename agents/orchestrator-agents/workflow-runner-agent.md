---
version: "1.0.0"
created: "2024-01-01"
updated: "2024-01-01"
author: "Grok-Workflow-Builder-v1"
description: |
  Meta-agent that executes workflows by orchestrating sub-agents
  and managing state across complex multi-step workflows.
agent_type: orchestrator
capabilities:
  - workflow_execution
  - state_management
  - agent_coordination
  - error_handling
  - progress_tracking
  - human_checkpoint_management
tags: [orchestrator, workflow, meta-agent, coordination]
---

# Workflow Runner Agent

## Agent Profile

| Attribute | Value |
|-----------|-------|
| Type | Meta-Orchestrator |
| Version | 1.0.0 |
| Complexity | High |
| Parallelization | Supports full workflow parallelization |

## Capabilities

### Core Functions
- Parse and validate workflow YAML specifications
- Execute workflow steps with proper dependency management
- Manage state across workflow execution
- Handle errors with intelligent recovery strategies
- Coordinate handoffs between specialized agents
- Track progress and report metrics

### Advanced Functions
- Dynamic workflow adaptation based on conditions
- Parallel execution of independent branches
- Human-in-the-loop checkpoint management
- Workflow performance optimization
- Learning from workflow execution history

## Configuration

### Required Settings
```yaml
config:
  workflow_path: workflows/  # Path to workflow YAML files
  skills_path: ../Awesome-Grok-Skills/  # Path to skills repo
  state_store: ./workflow_state/  # Persistent state storage
  checkpoint_enabled: true
  max_parallel_steps: 4
  retry_policy:
    max_attempts: 3
    backoff_multiplier: 2
    initial_delay_ms: 1000
```

### Optional Settings
```yaml
config:
  cache_enabled: true
  cache_ttl: 3600  # seconds
  metrics_enabled: true
  debug_mode: false
  log_level: info
```

## Input Specification

### Direct Input
```yaml
workflow_name: full-stack-planner
user_input: "Build a React e-commerce app with payment integration"
context:
  user_preferences:
    tech_stack: "React, Node.js, PostgreSQL"
    deployment: "AWS"
  constraints:
    budget: "low"
    timeline: "2 weeks"
```

### API Input
```json
{
  "workflow": "full-stack-planner",
  "parameters": {
    "user_input": "Build a React e-commerce app"
  },
  "options": {
    "checkpoint_frequency": "every_3_steps",
    "parallel_execution": true
  }
}
```

## Output Specification

### Standard Output
```yaml
execution_status: completed
results:
  artifacts: [list of output files]
  final_state: {completed state}
  metrics:
    total_steps: 12
    successful_steps: 12
    failed_steps: 0
    total_time_seconds: 847
    total_tokens: 45000
execution_trace:
  - step: "analyze-requirements"
    status: "success"
    duration_ms: 4500
  - step: "design-architecture"
    status: "success"
    duration_ms: 12000
```

### Error Output
```yaml
execution_status: failed
failed_step: "build-mvp"
error:
  type: "AgentFailure"
  message: "Code generation agent failed to produce working prototype"
  details: {...}
recovery_options:
  - "Retry with increased timeout"
  - "Simplify prototype scope"
  - "Escalate to human developer"
```

## Execution Flow

### 1. Initialization
- Load workflow YAML from specified path
- Validate workflow structure and dependencies
- Check required skills availability
- Initialize state management system
- Set up monitoring and logging

### 2. Planning Phase
- Build dependency graph (DAG)
- Identify parallel execution opportunities
- Calculate resource requirements
- Set checkpoint triggers
- Estimate execution timeline

### 3. Execution Phase
- Execute steps according to dependency order
- Monitor step progress and resource usage
- Handle step failures with recovery strategies
- Update state after each step
- Trigger checkpoints when scheduled

### 4. Completion Phase
- Validate all success criteria met
- Collect and organize output artifacts
- Generate execution report
- Clean up temporary resources
- Archive state for learning

## Integration with Skills Repo

### Available Agents (dynamically loaded)
```
ResearchOracle → research-oracle
CodeReviewTeam → code-review-team
PhysicsSimulator → physics-simulator
MemeRoaster → meme-roaster
TDDAgent → tdd-agent
EfficientCodePatterns → efficient-code-patterns
ArchitecturePlanner → architecture-planner
DeploymentAutomation → deployment-automation
ValidationEngineer → validation-engineer
```

### Agent Loading
```python
def load_agent(agent_name: str) -> Agent:
    agent_path = f"{skills_path}/agents/{agent_name}/"
    agent_config = load_yaml(f"{agent_path}/config.yaml")
    agent_prompt = load_file(f"{agent_path}/system-prompt.txt")
    return Agent(config=agent_config, prompt=agent_prompt)
```

## State Management

### State Structure
```yaml
workflow_state:
  workflow_id: "uuid"
  workflow_name: "full-stack-planner"
  current_step: "design-architecture"
  step_outputs: {}
  accumulated_context: {}
  execution_history: []
  checkpoints: []
  error_log: []
```

### State Persistence
- Save state after each step completion
- Enable recovery from last checkpoint
- Support state rollback for error recovery
- Archive completed workflow states

## Error Handling

### Error Types
| Type | Description | Handling Strategy |
|------|-------------|-------------------|
| ValidationError | Invalid workflow spec | Fail fast with details |
| AgentNotFound | Missing agent | Try alternative, escalate |
| AgentFailure | Agent execution failed | Retry, fallback, escalate |
| TimeoutError | Step timeout | Retry with longer timeout |
| StateError | State corruption | Rollback to checkpoint |
| HumanRequired | Checkpoint reached | Pause, request input |

### Recovery Strategies
1. **Retry** - Re-execute failed step (max 3 attempts)
2. **Fallback** - Use alternative agent or approach
3. **Simplify** - Reduce scope, retry
4. **Escalate** - Request human intervention

## Performance Optimization

### Parallelization Rules
- Independent steps: Execute simultaneously
- Dependent steps: Chain with proper handoffs
- Resource limits: Respect agent capacity limits
- Caching: Reuse deterministic results

### Caching Strategy
- Cache agent outputs when safe
- Use content-addressable cache keys
- Implement TTL-based cache expiration
- Cache invalidation on state changes

## Metrics & Monitoring

### Key Metrics
- Step execution time
- Token consumption per step
- Success/failure rates per agent
- Workflow completion rate
- Average time to completion

### Monitoring Integration
- Real-time progress dashboard
- Alerting on failures
- Performance trending
- Resource utilization tracking

## Usage Examples

### Basic Execution
```yaml
# input.yaml
workflow_name: meme-to-viral-code-delegation
user_code: |
  function sum(arr) {
    let s = 0;
    for (let i = 0; i <= arr.length; i++) {
      s += arr[i];
    }
    return s;
  }
```

### Command Line
```bash
python run_workflow.py --workflow meme-to-viral-code-delegation \
  --input input.yaml \
  --output results.yaml \
  --checkpoint human@step_3
```

### API Call
```python
from workflow_runner import execute_workflow

result = execute_workflow(
    workflow="meme-to-viral-code-delegation",
    input_data=user_code,
    options={
        "checkpoint_frequency": "every_step",
        "parallel_execution": False,
        "meme_level": "savage"
    }
)
```

## Best Practices

1. **Always validate** workflow YAML before execution
2. **Set checkpoints** for irreversible operations
3. **Monitor resources** during long workflows
4. **Archive states** for future learning
5. **Test recovery** scenarios periodically
6. **Document deviations** from original plan

## Limitations

- Cannot execute workflows requiring external system access
- Limited to agents available in skills repo
- State size limited by memory constraints
- Cannot modify workflow YAML during execution

## Future Enhancements

- Dynamic workflow modification during execution
- Multi-workflow orchestration
- Learning from execution history
- A/B testing of workflow variants
- Workflow template generation from examples
