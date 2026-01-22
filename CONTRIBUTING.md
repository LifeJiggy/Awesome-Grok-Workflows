# Contributing to Awesome-Grok-Workflows

Thank you for your interest in contributing! This guide will help you get started.

## Ways to Contribute

- **New Workflows** — Create domain-specific or general-purpose workflows
- **Rules & Guardrails** — Add safety rules, domain compliance, or style guides
- **Prompts** — Versioned prompts, few-shot examples, or prompt templates
- **Examples & Documentation** — Traces, tutorials, or usage guides
- **Tools & Scripts** — Validation, testing, or automation improvements
- **Bug Fixes** — Fix issues in existing workflows or code

## Getting Started

### 1. Prerequisites

- Python 3.11+
- Git
- Access to Awesome-Grok-Skills repo (for integration testing)

### 2. Fork and Clone

```bash
git clone https://github.com/YOUR-USERNAME/Awesome-Grok-Workflows.git
cd Awesome-Grok-Workflows
git remote add upstream https://github.com/LifeJiggy/Awesome-Grok-Workflows.git
```

### 3. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Link skills repo (adjust path)
./scripts/setup-symlinks.sh ../Awesome-Grok-Skills

# Verify setup
./scripts/validate-workflow.sh workflows/planning/research-to-prototype.yaml
```

## Contribution Guidelines

### Workflow Standards

All workflows must:

1. **Follow the template** — Use `workflows/templates/base-workflow-template.yaml`
2. **Include required sections** — name, version, description, steps, guardrails
3. **Define success criteria** — Clear, measurable outcomes
4. **Add error handling** — Retry logic and fallback strategies
5. **Include example traces** — Demonstrate execution flow
6. **Validate against schema** — Run `./scripts/validate-workflow.sh`

### YAML Best Practices

```yaml
# ✅ Good example
name: my-new-workflow
version: 1.0.0
description: Clear description of purpose
author: YourName
tags: [domain, purpose, keywords]

steps:
  - name: first-step
    agent: research-oracle
    outputs: [result_file]

# ❌ Bad example
name: wf1
desc: does stuff
steps:
  - agent: x
```

### Rule Standards

All rules must:

1. **Be specific and actionable** — Clear requirements, not vague suggestions
2. **Include enforcement mechanisms** — How to verify compliance
3. **Provide examples** — Good vs. bad behavior
4. **Cover edge cases** — What happens at boundaries
5. **Link to related rules** — Cross-reference where relevant

### Prompt Standards

All prompts must:

1. **Version explicitly** — Track changes with created/updated dates
2. **Include usage examples** — Demonstrate how to use
3. **Define variables clearly** — Document template variables
4. **Test edge cases** — Verify prompt works in various scenarios
5. **Follow Grok personality** — Match tone and style in `grok-personality.md`

## Development Process

### 1. Create a Branch

```bash
git checkout -b feature/my-new-workflow
```

### 2. Develop Your Contribution

Create or modify files following the standards above.

### 3. Test Your Changes

```bash
# Validate YAML syntax
python scripts/yaml-lint.py .

# Validate against schema
python scripts/schema-validator.py --path workflows/my-new-workflow.yaml

# Run unit tests
pytest tests/unit/ -v

# Test integration (if applicable)
pytest tests/integration/ -v -k workflow
```

### 4. Document Your Changes

Update relevant documentation:
- Add workflow to README features list
- Create example trace in `docs/examples/`
- Update `CHANGELOG.md` with your changes

### 5. Commit and Push

```bash
git add .
git commit -m "feat: Add my-new-workflow

- Created workflow YAML with 5 steps
- Added physics simulation use case
- Included example trace
- Validated against schema"

git push origin feature/my-new-workflow
```

### 6. Create Pull Request

Open a PR with:
- Clear title and description
- Link to related issues
- Screenshots or diagrams (if visual)
- Test results from your local validation

## Review Process

All PRs require:

1. **Automated Checks** — YAML lint, schema validation, tests
2. **Code Review** — At least one maintainer approval
3. **Documentation Check** — Completeness and clarity
4. **Integration Check** — Works with skills repo (if applicable)

## Style Guides

### YAML Style
- 2-space indentation
- Alphabetical sorting within sections
- Comments using `#` (minimal)
- Quotes around strings with special characters

### Markdown Style
- ATX headers (`##` not `##`)
- Max 80 characters per line
- Code blocks with language tags
- Tables for structured data

### Commit Messages
```
type(scope): subject

body

footer
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Recognition

Contributors are recognized in:
- README contributors section
- Release notes
- Annual contributor spotlight

## Questions?

- Check existing [issues](../../issues)
- Start a [discussion](../../discussions)
- Reach out to maintainers

---

**Thank you for contributing to Awesome-Grok-Workflows!** 🎉
