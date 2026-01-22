#!/usr/bin/env python3
"""
Generate Workflow - Creates new workflows from templates.
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
import yaml


class WorkflowGenerator:
    """Generates new workflow files from templates."""

    TEMPLATES = {
        "basic": {
            "name": "Basic Workflow",
            "description": "Simple linear workflow with a few steps",
            "triggers": ["on_push"],
            "steps": 3
        },
        "parallel": {
            "name": "Parallel Workflow",
            "description": "Workflow with parallel execution paths",
            "triggers": ["on_push", "on_pr"],
            "steps": 6
        },
        "ci-cd": {
            "name": "CI/CD Pipeline",
            "description": "Build, test, and deploy workflow",
            "triggers": ["on_push", "on_pr", "on_release"],
            "steps": 8
        },
        "multi-agent": {
            "name": "Multi-Agent Orchestration",
            "description": "Coordinates multiple agents",
            "triggers": ["on_push", "manual"],
            "steps": 5
        },
        "data-pipeline": {
            "name": "Data Pipeline",
            "description": "ETL/ELT data processing workflow",
            "triggers": ["on_schedule"],
            "steps": 7
        }
    }

    def __init__(self, output_dir: str = "workflows"):
        self.output_dir = Path(output_dir)

    def generate(self, name: str, template: str = "basic", **kwargs) -> Path:
        """Generate a new workflow file."""
        if template not in self.TEMPLATES:
            print(f"Unknown template: {template}")
            print(f"Available templates: {', '.join(self.TEMPLATES.keys())}")
            sys.exit(1)

        template_config = self.TEMPLATES[template]
        workflow = self._create_workflow(
            name=name,
            template=template,
            config=template_config,
            **kwargs
        )

        # Generate filename
        filename = self._to_kebab_case(name)
        output_path = self.output_dir / f"{filename}.yaml"

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write workflow
        with open(output_path, 'w') as f:
            yaml.dump(workflow, f, default_flow_style=False, sort_keys=False)

        return output_path

    def _create_workflow(self, name: str, template: str, config: Dict, **kwargs) -> Dict:
        """Create workflow structure based on template."""
        workflow = {
            "name": name,
            "version": "1.0.0",
            "description": kwargs.get("description", config["description"]),
            "created_at": datetime.utcnow().isoformat() + "Z",
            "author": kwargs.get("author", "Grok Workflow Generator"),
            "triggers": kwargs.get("triggers", config["triggers"]),
            "guards": kwargs.get("guards", []),
            "steps": self._generate_steps(template, config["steps"], **kwargs),
            "outputs": kwargs.get("outputs", {}),
            "environment": kwargs.get("environment", {})
        }

        return workflow

    def _generate_steps(self, template: str, num_steps: int, **kwargs) -> List[Dict]:
        """Generate steps based on template."""
        base_steps = []

        if template == "basic":
            base_steps = [
                {"name": "checkout", "action": "git.checkout", "outputs": ["commit"]},
                {"name": "setup", "action": "environment.setup", "needs": ["checkout"], "outputs": ["env_vars"]},
                {"name": "execute", "action": "runner.execute", "needs": ["setup"]},
            ]

        elif template == "parallel":
            base_steps = [
                {"name": "checkout", "action": "git.checkout"},
                {"name": "lint", "action": "linter.run", "needs": ["checkout"]},
                {"name": "test", "action": "test.runner", "needs": ["checkout"]},
                {"name": "build", "action": "builder.run", "needs": ["test"]},
                {"name": "deploy-staging", "action": "deployer.deploy", "needs": ["build"], "params": {"target": "staging"}},
                {"name": "verify", "action": "verifier.run", "needs": ["deploy-staging"]},
            ]

        elif template == "ci-cd":
            base_steps = [
                {"name": "checkout", "action": "git.checkout"},
                {"name": "install", "action": "package.install", "needs": ["checkout"]},
                {"name": "lint", "action": "linter.run", "needs": ["install"]},
                {"name": "test", "action": "test.runner", "needs": ["install"]},
                {"name": "build", "action": "builder.run", "needs": ["test"]},
                {"name": "security-scan", "action": "security.scan", "needs": ["build"]},
                {"name": "deploy-staging", "action": "deployer.deploy", "needs": ["security-scan"], "params": {"env": "staging"}},
                {"name": "deploy-production", "action": "deployer.deploy", "needs": ["deploy-staging"], "params": {"env": "production"}, "condition": "inputs.environment == 'production'"},
            ]

        elif template == "multi-agent":
            base_steps = [
                {"name": "planner", "agent": "orchestrator", "outputs": ["plan"]},
                {"name": "researcher", "agent": "researcher", "needs": ["planner"], "params": {"query": "{{outputs.planner.research_query}}"}},
                {"name": "developer", "agent": "developer", "needs": ["planner"], "params": {"task": "{{outputs.planner.development_task}}"}},
                {"name": "reviewer", "agent": "reviewer", "needs": ["developer", "researcher"]},
                {"name": "finalizer", "agent": "orchestrator", "needs": ["reviewer"]},
            ]

        elif template == "data-pipeline":
            base_steps = [
                {"name": "extract", "action": "data.extract", "outputs": ["raw_data"]},
                {"name": "validate", "action": "data.validate", "needs": ["extract"], "outputs": ["validation_results"]},
                {"name": "transform", "action": "data.transform", "needs": ["validate"], "outputs": ["clean_data"]},
                {"name": "enrich", "action": "data.enrich", "needs": ["transform"], "outputs": ["enriched_data"]},
                {"name": "aggregate", "action": "data.aggregate", "needs": ["enrich"], "outputs": ["metrics"]},
                {"name": "load", "action": "data.load", "needs": ["aggregate"], "outputs": ["loaded_records"]},
                {"name": "notify", "action": "notification.send", "needs": ["load"]},
            ]

        # Apply any overrides from kwargs
        if "steps" in kwargs:
            base_steps = kwargs["steps"]

        return base_steps

    def _to_kebab_case(self, name: str) -> str:
        """Convert name to kebab-case."""
        import re
        name = name.lower().replace(' ', '-')
        name = re.sub(r'[^a-z0-9\-]', '', name)
        return name


def main():
    parser = argparse.ArgumentParser(description="Generate new workflows")
    parser.add_argument("name", help="Workflow name")
    parser.add_argument("--template", default="basic", choices=["basic", "parallel", "ci-cd", "multi-agent", "data-pipeline"],
                        help="Workflow template to use")
    parser.add_argument("--output", default="workflows", help="Output directory")
    parser.add_argument("--description", help="Workflow description")
    parser.add_argument("--author", help="Author name")
    parser.add_argument("--triggers", nargs="+", help="Trigger events")

    args = parser.parse_args()

    generator = WorkflowGenerator(args.output)

    try:
        output_path = generator.generate(
            name=args.name,
            template=args.template,
            description=args.description,
            author=args.author,
            triggers=args.triggers
        )
        print(f"✅ Workflow created: {output_path}")
        print(f"\nNext steps:")
        print(f"  1. Edit the workflow: {output_path}")
        print(f"  2. Validate it: ./scripts/validate-workflow.sh {output_path}")
        print(f"  3. Commit and push to your repository")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
