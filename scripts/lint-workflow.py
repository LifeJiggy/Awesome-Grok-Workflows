#!/usr/bin/env python3
"""
Workflow Linter - Validates workflow YAML files against best practices.
"""

import argparse
import yaml
import sys
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class LintResult:
    """Represents a linting result."""
    file: str
    rule: str
    severity: str  # error, warning, info
    message: str
    line: int = 0
    suggestion: str = ""


class WorkflowLinter:
    """Lints workflow YAML files."""

    def __init__(self, workflow_path: str):
        self.workflow_path = Path(workflow_path)
        self.results: List[LintResult] = []
        self.workflow = None

    def load(self) -> bool:
        """Load and parse the workflow file."""
        try:
            with open(self.workflow_path, 'r') as f:
                self.workflow = yaml.safe_load(f)
            return True
        except yaml.YAMLError as e:
            self.results.append(LintResult(
                file=str(self.workflow_path),
                rule="YAML_VALID",
                severity="error",
                message=f"Invalid YAML syntax: {e}"
            ))
            return False
        except FileNotFoundError:
            self.results.append(LintResult(
                file=str(self.workflow_path),
                rule="FILE_EXISTS",
                severity="error",
                message="Workflow file not found"
            ))
            return False

    def lint_required_fields(self):
        """Check for required fields."""
        required_fields = ['name', 'version', 'description', 'triggers', 'steps']
        for field in required_fields:
            if field not in self.workflow:
                self.results.append(LintResult(
                    file=str(self.workflow_path),
                    rule="REQUIRED_FIELD",
                    severity="error",
                    message=f"Missing required field: {field}",
                    suggestion=f"Add {field} to the workflow definition"
                ))

    def lint_version(self):
        """Check version format."""
        version = self.workflow.get('version', '')
        if not version:
            return

        # Accept semantic versioning
        parts = str(version).split('.')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            self.results.append(LintResult(
                file=str(self.workflow_path),
                rule="VERSION_FORMAT",
                severity="warning",
                message=f"Version '{version}' doesn't follow semantic versioning",
                suggestion="Use format: major.minor.patch (e.g., 1.0.0)"
            ))

    def lint_triggers(self):
        """Check trigger configuration."""
        triggers = self.workflow.get('triggers', [])
        if not triggers:
            self.results.append(LintResult(
                file=str(self.workflow_path),
                rule="TRIGGERS_EMPTY",
                severity="error",
                message="No triggers defined",
                suggestion="Add at least one trigger (on_push, on_schedule, manual)"
            ))

    def lint_steps(self):
        """Check step configuration."""
        steps = self.workflow.get('steps', [])
        if not steps:
            self.results.append(LintResult(
                file=str(self.workflow_path),
                rule="STEPS_EMPTY",
                severity="error",
                message="No steps defined"
            ))
            return

        step_names = []
        for i, step in enumerate(steps):
            if 'name' not in step:
                self.results.append(LintResult(
                    file=str(self.workflow_path),
                    rule="STEP_NAME",
                    severity="error",
                    message=f"Step {i+1} missing name",
                    suggestion="Add a descriptive name to the step"
                ))

            name = step.get('name', f"step_{i}")
            if name in step_names:
                self.results.append(LintResult(
                    file=str(self.workflow_path),
                    rule="STEP_NAME_DUPLICATE",
                    severity="error",
                    message=f"Duplicate step name: {name}"
                ))
            step_names.append(name)

            # Check for action
            if 'action' not in step and 'agent' not in step:
                self.results.append(LintResult(
                    file=str(self.workflow_path),
                    rule="STEP_ACTION",
                    severity="error",
                    message=f"Step '{name}' missing action or agent"
                ))

            # Check for dependencies
            if 'depends_on' in step:
                deps = step['depends_on']
                for dep in deps:
                    if dep not in step_names and dep not in [s.get('name') for s in steps]:
                        self.results.append(LintResult(
                            file=str(self.workflow_path),
                            rule="STEP_DEPENDENCY",
                            severity="warning",
                            message=f"Step '{name}' depends on unknown step: {dep}",
                            suggestion=f"Ensure '{dep}' is defined as a step name"
                        ))

    def lint_guards(self):
        """Check guardrails and conditions."""
        steps = self.workflow.get('steps', [])
        for i, step in enumerate(steps):
            name = step.get('name', f"step_{i}")

            # Check for output usage without validation
            if 'condition' in step:
                condition = step['condition']
                if 'outputs.' in str(condition):
                    # Ensure the referenced output exists
                    for other_step in steps:
                        if other_step.get('name') in str(condition):
                            outputs = other_step.get('outputs', [])
                            for output in outputs:
                                if f"outputs.{other_step['name']}.{output}" not in str(condition):
                                    pass  # Would need deeper analysis

    def lint_naming_conventions(self):
        """Check naming conventions."""
        name = self.workflow.get('name', '')

        # Workflow name should be kebab-case
        if ' ' in name or '_' in name:
            self.results.append(LintResult(
                file=str(self.workflow_path),
                rule="NAMING_CONVENTION",
                severity="info",
                message=f"Workflow name '{name}' should use kebab-case",
                suggestion="Example: my-workflow-name (not my_workflow_name or my workflow name)"
            ))

    def lint_complexity(self):
        """Check workflow complexity."""
        steps = self.workflow.get('steps', [])

        if len(steps) > 20:
            self.results.append(LintResult(
                file=str(self.workflow_path),
                rule="COMPLEXITY_HIGH",
                severity="warning",
                message=f"Workflow has {len(steps)} steps - consider breaking into sub-workflows",
                suggestion="Split into smaller, focused workflows for better maintainability"
            ))

        # Check for linear vs complex DAG
        dependencies = set()
        for step in steps:
            for dep in step.get('depends_on', []):
                dependencies.add(dep)

        if len(dependencies) > len(steps) * 2:
            self.results.append(LintResult(
                file=str(self.workflow_path),
                rule="COMPLEXITY_DAG",
                severity="info",
                message="Complex dependency graph detected",
                suggestion="Ensure proper error handling for parallel execution"
            ))

    def lint(self) -> List[LintResult]:
        """Run all linting checks."""
        if not self.workflow:
            return self.results

        self.lint_required_fields()
        self.lint_version()
        self.lint_triggers()
        self.lint_steps()
        self.lint_guards()
        self.lint_naming_conventions()
        self.lint_complexity()

        return self.results

    def print_results(self):
        """Print lint results."""
        if not self.results:
            print(f"✓ {self.workflow_path}: No issues found")
            return

        print(f"✗ {self.workflow_path}:")
        for result in self.results:
            icon = "🔴" if result.severity == "error" else ("🟡" if result.severity == "warning" else "🔵")
            print(f"  {icon} [{result.rule}] {result.message}")
            if result.suggestion:
                print(f"     └─ 💡 {result.suggestion}")


def main():
    parser = argparse.ArgumentParser(description="Lint workflow YAML files")
    parser.add_argument("workflows", nargs="+", help="Workflow files or directories to lint")
    parser.add_argument("--fix", action="store_true", help="Attempt to fix issues")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--exit-zero", action="store_true", help="Exit with 0 even if errors found")
    args = parser.parse_args()

    all_results = []

    for path_str in args.workflows:
        path = Path(path_str)

        if path.is_file() and path.suffix in ['.yaml', '.yml']:
            linter = WorkflowLinter(str(path))
            if linter.load():
                all_results.extend(linter.lint())
            linter.print_results()
        elif path.is_dir():
            for yaml_file in path.rglob("*.yaml"):
                linter = WorkflowLinter(str(yaml_file))
                if linter.load():
                    all_results.extend(linter.lint())
                linter.print_results()
            for yaml_file in path.rglob("*.yml"):
                linter = WorkflowLinter(str(yaml_file))
                if linter.load():
                    all_results.extend(linter.lint())
                linter.print_results()

    errors = sum(1 for r in all_results if r.severity == "error")
    warnings = sum(1 for r in all_results if r.severity == "warning")

    print(f"\n{'='*60}")
    print(f"Lint Results: {errors} errors, {warnings} warnings")

    if args.json:
        import json
        output = [
            {
                "file": r.file,
                "line": r.line,
                "rule": r.rule,
                "severity": r.severity,
                "message": r.message,
                "suggestion": r.suggestion
            }
            for r in all_results
        ]
        print(json.dumps(output, indent=2))

    if errors > 0 and not args.exit_zero:
        sys.exit(1)


if __name__ == "__main__":
    main()
