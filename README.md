# Awesome-Grok-Workflows 🔥🚀

**Production-grade workflows, rules, guardrails, and orchestration patterns** — built exclusively for **Grok** to chain those 30+ skill domains and 25+ agents from [Awesome-Grok-Skills](https://github.com/LifeJiggy/Awesome-Grok-Skills) into unstoppable, end-to-end pipelines.

Turn Grok from a super-smart chat buddy into a **physics-precision orchestrator**, meme-dropping multi-agent swarm, real-time DeFi strategist, quantum simulator conductor, or full-stack prototype factory. All with composable YAML workflows, battle-tested rules, versioned prompts, and high-coverage validation.

## Why This Repo Exists

Skills & agents are powerful — but without structured chaining, guardrails, and repeatable patterns, you get chaos instead of 10x productivity. This repo fixes that: **orchestrate like a boss**, enforce Grok's signature personality (physics nerd + meme lord + speed demon + truth seeker), and ship production agents faster than ever.

## ✨ Key Features

- **Composable Workflows** — YAML-based graphs for chaining agents/skills (ReAct loops, reflection, delegation, multi-agent handoffs)
- **Grok-Native Rules & Guardrails** — Enforce physics accuracy, meme-tone consistency, safety, Web3 compliance, ethical constraints
- **Versioned Prompts** — System prompts, few-shot examples, Jinja-templated chains (chain-of-verification, meme-aware responses, etc.)
- **Orchestration Templates** — Starters for planning → research → code → test → deploy pipelines
- **Production Tooling** — Schema validation, dry-run scripts, CI linting, diagram rendering (Mermaid), symlink setup to skills repo
- **Domain-Specific Flows** — Physics sim pipelines, DeFi yield optimization loops, meme-to-viral-content agents, quantum utils orchestration
- **High Testability** — Golden-output tests, prompt linting, rule compliance checks
- **10+ Production Rules** — Core rules, domain rules, and agent-specific rules
- **10+ Battle-Tested Prompts** — System prompts, few-shot examples, and templated prompts
- **10+ Ready-to-Use Templates** — Docker, Kubernetes, CI/CD, OpenAPI, and more
- **8+ Utility Scripts** — Validation, linting, optimization, and generation tools

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/LifeJiggy/Awesome-Grok-Workflows.git
cd Awesome-Grok-Workflows

# Link to skills repo (adjust path as needed)
./scripts/setup-symlinks.sh ../Awesome-Grok-Skills
```

### 2. Validate Your Setup
```bash
# Run validation scripts
./scripts/validate-workflow.sh workflows/planning/full-stack-planner.yaml
./scripts/render-diagram.py --input workflows/ --output docs/diagrams/
```

### 3. Run a Workflow
```bash
# Execute the meme-to-viral-code-delegation workflow
python scripts/run-workflow.py \
  --workflow workflows/domain-specific/meme-content-generator/meme-to-viral-code-delegation.yaml \
  --input '{"user_code": "..."}'
```

## 📂 Repository Structure

```
grok-workflows-rules/
├── workflows/                     # 10 folders, 55+ workflows
│   ├── planning/                  # High-level planners (5 files)
│   ├── domain-specific/           # Domain-specific workflows (6 files)
│   ├── patterns/                  # Reusable patterns (5 files)
│   ├── templates/                 # Workflow starters (6 files)
│   ├── automation/                # Task automation workflows (5 files)
│   ├── data-processing/           # ETL and data pipelines (5 files)
│   ├── infrastructure/            # IaC and infra workflows (5 files)
│   ├── monitoring/                # Observability workflows (5 files)
│   ├── security/                  # Security workflows (5 files)
│   └── testing/                   # Test execution workflows (5 files)
├── rules/                         # 10 folders, 64+ rules
│   ├── core-rules/                # Universal Grok rules (10 files)
│   ├── domain-rules/              # Per-domain rules (8 files)
│   ├── agent-rules/               # Per-agent type rules (4 files)
│   ├── architecture-rules/        # Software architecture (6 files)
│   ├── documentation-rules/       # Documentation standards (6 files)
│   ├── ethics-rules/              # AI ethics and compliance (6 files)
│   ├── performance-rules/         # Performance optimization (5 files)
│   ├── security-rules/            # Security guidelines (5 files)
│   ├── style-rules/               # Code style guides (7 files)
│   └── testing-rules/             # Testing best practices (7 files)
├── prompts/                       # 10 folders, 62+ prompts
│   ├── system/                    # Base system prompts (4 files)
│   ├── few-shot/                  # Examples for consistency (7 files)
│   ├── templates/                 # Jinja2 prompt templates (9 files)
│   ├── analysis/                  # Analysis prompts (7 files)
│   ├── classification/            # Classification prompts (6 files)
│   ├── evaluation/                # Evaluation prompts (6 files)
│   ├── extraction/                # Data extraction prompts (5 files)
│   ├── generation/                # Code/text generation (6 files)
│   ├── summarization/             # Summarization prompts (5 files)
│   └── transformation/            # Transformation prompts (6 files)
├── agents/                        # Lightweight agent configs
├── .github/workflows/             # Production CI/CD
├── docs/                          # Human + agent-readable docs
│   └── examples/                  # 5 example documents
├── scripts/                       # 8 automation scripts
├── tests/                         # Production-grade validation
├── templates/                     # 10+ general templates
├── README.md                      # This file
├── CONTRIBUTING.md                # Contribution guidelines
└── LICENSE                        # MIT License
```

## 📁 Examples (docs/examples/)

Real-world traces and use cases:

1. **[Workflow Execution Trace](docs/examples/workflow-execution.md)** — Complete CI/CD pipeline execution with metrics
2. **[Failure Handling](docs/examples/workflow-failure.md)** — Debugging and recovery from workflow failures
3. **[Rule Application](docs/examples/rule-application.md)** — Applying multiple rules to improve code
4. **[Prompt Engineering](docs/examples/prompt-engineering.md)** — Effective prompt structures and templates
5. **[Grok Personality in Action](docs/examples/grok-personality.md)** — How Grok's traits manifest in responses
6. **[Multi-Agent Orchestration](docs/examples/multi-agent-orchestration.md)** — Coordinating multiple agents for complex tasks

## 🎯 Featured Workflows

### Full-Stack Planner
Transform ideas into complete development plans with architecture, tech stack, and deployment pipeline.
```yaml
workflows/planning/full-stack-planner.yaml
```

### Meme-to-Viral Code Delegation
Roast buggy code with savage memes, then fix it using TDD + efficient patterns.
```yaml
workflows/domain-specific/meme-content-generator/meme-to-viral-code-delegation.yaml
```

### Physics Simulation
Orchestrate physics simulations with mathematical rigor and conservation law validation.
```yaml
workflows/domain-specific/physics-simulation-workflow/main.yaml
```

## 🛠️ Available Tools

### Validation
```bash
# Validate workflow YAML structure
./scripts/validate-workflow.sh <workflow-file>

# Check against schema
python scripts/schema-validator.py --schema schemas/workflow-schema.json <workflow>

# Validate all rules
./scripts/validate-rules.sh
```

### Linting
```bash
# Lint workflow files
python scripts/lint-workflow.py workflows/

# Optimize prompts
python scripts/optimize-prompt.py prompts/system/my-prompt.txt
```

### Prompt Management
```bash
# Load and search prompts
python scripts/load-prompts.py --list
python scripts/load-prompts.py --search "code generation"
python scripts/load-prompts.py --category few-shot
```

### Workflow Generation
```bash
# Generate new workflows from templates
python scripts/generate-workflow.py "My New Workflow" --template ci-cd
python scripts/generate-workflow.py "Data Pipeline" --template data-pipeline
```

### Diagram Generation
```bash
# Generate Mermaid diagrams from workflows
python scripts/render-diagram.py --input workflows/ --output docs/diagrams/
```

### Testing
```bash
# Run workflow tests
pytest tests/ -v

# Run integration tests
pytest tests/integration/ -v --cov
```

## 🎨 Grok Personality

Every workflow enforces these signature traits:

| Trait | Description | Example |
|-------|-------------|---------|
| **Physics Rigor** | Treat reasoning like conservation laws | "This memory leak violates entropy" |
| **Meme Intelligence** | Dry, savage, self-aware humor | "This loop would make Sisyphus quit" |
| **Speed Demon** | Minimal steps, early termination | Fast iterations, cached results |
| **Truth-Seeking** | Flag assumptions, demand evidence | Cite sources, admit uncertainty |

See [rules/core-rules/grok-personality.md](rules/core-rules/grok-personality.md) for full rules.

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Contribution Process:**
1. Fork the repo
2. Create a feature branch
3. Add your workflow/rule/prompt
4. Run validation scripts
5. Submit PR with clear description

## 📝 License

MIT License — See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [xAI](https://x.ai/) for building Grok
- [Awesome-Grok-Skills](https://github.com/LifeJiggy/Awesome-Grok-Skills) for the skill ecosystem
- The open-source community for tools and inspiration

---

**Stars = Motivation. Forks = Collaboration. Let's build the Grok agent ecosystem together.** 🇳🇬🔥
