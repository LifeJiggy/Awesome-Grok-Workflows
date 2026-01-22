# How to Contribute

Thank you for your interest in contributing to Awesome-Grok-Workflows! This guide will walk you through the process.

## Quick Start

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/Awesome-Grok-Workflows.git
cd Awesome-Grok-Workflows

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes
# 5. Run validation
./scripts/validate-workflow.sh workflows/your-new-workflow.yaml

# 6. Commit and push
git add .
git commit -m "feat: Add your feature"
git push origin feature/your-feature-name

# 7. Create a Pull Request
```

## What Can You Contribute?

### New Workflows
Create workflows for new domains or use cases:
1. Use `workflows/templates/base-workflow-template.yaml` as starting point
2. Follow naming convention: `domain-purpose.yaml`
3. Include example traces
4. Validate with `./scripts/validate-workflow.sh`

Example workflow structure:
```yaml
name: my-new-workflow
version: 1.0.0
description: Clear description of what this workflow does
steps:
  - name: first-step
    agent: research-oracle
    outputs: [result]
  - name: second-step
    agent: code-review-team
    depends_on: [first-step]
    outputs: [review_result]
```

### Rules and Guardrails
Add safety rules or domain-specific constraints:
1. Place in appropriate directory (`rules/core-rules/` or `rules/domain-rules/`)
2. Follow existing format
3. Include enforcement mechanisms
4. Add examples of good/bad behavior

### Prompts and Templates
Improve agent prompts or create new templates:
1. Use version metadata
2. Include usage examples
3. Document all variables
4. Test with edge cases

### Documentation
Improve docs, examples, or tutorials:
1. Follow markdown style guide
2. Include code examples
3. Update relevant docs when changing code
4. Add diagrams where helpful

### Tools and Scripts
Improve automation or add new scripts:
1. Add tests for new functionality
2. Update documentation
3. Follow existing code style
4. Make scripts executable

## Development Setup

### Prerequisites
- Python 3.11+
- Git
- YAML validator
- Access to Awesome-Grok-Skills (for integration testing)

### Setup Commands
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt

# Link skills repo
./scripts/setup-symlinks.sh ../Awesome-Grok-Skills

# Verify setup
pytest tests/ -v
```

## Testing Requirements

### Unit Tests
- Test YAML structure validation
- Test dependency resolution
- Test edge cases

### Integration Tests
- Test agent loading from skills repo
- Test workflow execution patterns
- Test cross-component interactions

### Validation Scripts
```bash
# Validate workflow syntax
./scripts/validate-workflow.sh <workflow-file>

# Generate diagrams
python scripts/render-diagram.py --input workflows/

# Run tests
pytest tests/ -v
```

## Code Style

### YAML Files
- 2-space indentation
- Alphabetical sorting within sections
- Descriptive names
- Comments for complex logic

### Python Scripts
- Type hints required
- Docstrings for functions
- Follow PEP 8
- Use logging instead of print

### Markdown Docs
- ATX headers (`##`)
- Max 80 characters per line
- Code blocks with language tags
- Tables for structured data

## Pull Request Process

### Before Submitting
1. Run all validation scripts
2. Add tests for new functionality
3. Update documentation
4. Verify all tests pass
5. Check linting

### PR Description Template
```markdown
## Summary
Brief description of changes

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
- Tests added/updated
- Validation results

## Checklist
- [ ] Validated workflow YAML
- [ ] Added unit tests
- [ ] Updated documentation
- [ ] Followed code style
```

### Review Process
1. Automated checks run
2. Maintainers review code
3. Feedback provided
4. Address feedback
5. Merge when approved

## Recognition

Contributors are recognized in:
- README contributors section
- Release notes
- Annual contributor spotlight

## Questions?

- Check existing issues
- Start a discussion
- Reach out to maintainers

---

**Thank you for contributing!** 🎉
