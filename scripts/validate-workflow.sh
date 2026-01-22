#!/usr/bin/env python3
"""
Workflow Validator Script

Validates workflow YAML files against schema and best practices.
"""

import sys
import yaml
import argparse
from pathlib import Path
from jsonschema import validate, ValidationError


def load_yaml(file_path: str) -> dict:
    """Load and parse YAML file."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


def validate_workflow_structure(workflow: dict, file_path: str) -> list:
    """Validate workflow has required structure."""
    errors = []
    required_fields = ['name', 'version', 'description', 'steps']
    
    for field in required_fields:
        if field not in workflow:
            errors.append(f"Missing required field: '{field}' in {file_path}")
    
    if 'steps' in workflow:
        for i, step in enumerate(workflow['steps']):
            if 'name' not in step:
                errors.append(f"Step {i} missing 'name' field")
            if 'agent' not in step:
                errors.append(f"Step '{step.get('name', i)}' missing 'agent' field")
    
    return errors


def validate_dependencies(workflow: dict, file_path: str) -> list:
    """Validate step dependencies are valid."""
    errors = []
    step_names = {step.get('name') for step in workflow.get('steps', [])}
    
    for step in workflow.get('steps', []):
        depends_on = step.get('depends_on', [])
        for dep in depends_on:
            if dep not in step_names:
                errors.append(
                    f"Step '{step['name']}' depends on unknown step '{dep}' in {file_path}"
                )
    
    return errors


def detect_cycles(workflow: dict) -> list:
    """Detect circular dependencies."""
    errors = []
    steps = workflow.get('steps', [])
    
    # Build adjacency list
    graph = {step.get('name'): set(step.get('depends_on', [])) for step in steps}
    
    # DFS cycle detection
    visited = set()
    rec_stack = set()
    
    def detect_cycle(node, path):
        if node not in visited:
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if detect_cycle(neighbor, path + [node]):
                        return True
                elif neighbor in rec_stack:
                    errors.append(
                        f"Circular dependency detected: {' -> '.join(path + [node, neighbor])}"
                    )
                    return True
            
            rec_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            detect_cycle(node, [node])
    
    return errors


def validate_against_schema(workflow: dict, schema: dict) -> list:
    """Validate workflow against JSON schema."""
    errors = []
    try:
        validate(instance=workflow, schema=schema)
    except ValidationError as e:
        errors.append(f"Schema validation failed: {e.message}")
    
    return errors


def main():
    parser = argparse.ArgumentParser(description='Validate workflow YAML files')
    parser.add_argument('paths', nargs='+', help='Paths to validate')
    parser.add_argument('--schema', default='schemas/workflow-schema.json',
                        help='Path to JSON schema')
    parser.add_argument('--skip-schema', action='store_true',
                        help='Skip JSON schema validation')
    args = parser.parse_args()
    
    all_errors = []
    
    # Load schema if not skipped
    schema = None
    if not args.skip_schema:
        try:
            schema = load_yaml(args.schema)
        except FileNotFoundError:
            print(f"Warning: Schema file not found: {args.schema}")
    
    # Process each path
    for path_str in args.paths:
        path = Path(path_str)
        
        if path.is_file() and path.suffix in ['.yaml', '.yml']:
            files = [path]
        else:
            files = list(path.rglob('*.yaml')) + list(path.rglob('*.yml'))
        
        for file_path in files:
            print(f"Validating: {file_path}")
            
            try:
                workflow = load_yaml(str(file_path))
            except yaml.YAMLError as e:
                all_errors.append(f"YAML syntax error in {file_path}: {e}")
                continue
            
            # Structure validation
            all_errors.extend(validate_workflow_structure(workflow, str(file_path)))
            
            # Dependency validation
            all_errors.extend(validate_dependencies(workflow, str(file_path)))
            
            # Cycle detection
            all_errors.extend(detect_cycles(workflow))
            
            # Schema validation
            if schema and workflow:
                all_errors.extend(validate_against_schema(workflow, schema))
    
    # Report results
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} errors:")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("\n✅ All validations passed!")
        sys.exit(0)


if __name__ == '__main__':
    main()
