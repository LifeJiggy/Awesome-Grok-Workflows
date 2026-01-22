#!/usr/bin/env python3
"""
Mermaid Diagram Renderer

Generates Mermaid diagrams from workflow YAML files.
"""

import sys
import yaml
import argparse
from pathlib import Path


def yaml_to_mermaid(yaml_content: dict) -> str:
    """Convert workflow YAML to Mermaid diagram."""
    lines = []
    lines.append("```mermaid")
    lines.append("graph TD")
    
    # Subgraph for workflow
    workflow_name = yaml_content.get('name', 'workflow')
    lines.append(f"    subgraph {workflow_name}")
    
    # Add steps as nodes
    step_names = []
    for step in yaml_content.get('steps', []):
        step_name = step.get('name', 'unnamed')
        step_names.append(step_name)
        
        description = step.get('description', '').replace('"', "'")[:50]
        step_type = step.get('type', 'action')
        
        # Node styling based on type
        if step_type == 'thought':
            style = "[?"
        elif step_type == 'reflection':
            style = "{?}"
        else:
            style = "[?]"
        
        lines.append(f"    {step_name}{style}\"{step_type}: {description}\"")
    
    lines.append("    end")
    
    # Add dependencies as edges
    for step in yaml_content.get('steps', []):
        step_name = step.get('name', 'unnamed')
        depends_on = step.get('depends_on', [])
        
        for dep in depends_on:
            lines.append(f"    {dep} --> {step_name}")
    
    # Add final node
    if step_names:
        lines.append(f"    Start((🟢)) --> {step_names[0]}")
        lines.append(f"    {step_names[-1]} --> End((✅))")
    
    lines.append("```")
    
    return '\n'.join(lines)


def yaml_to_sequence_mermaid(yaml_content: dict) -> str:
    """Convert workflow YAML to sequence diagram."""
    lines = []
    lines.append("```mermaid")
    lines.append("sequenceDiagram")
    
    workflow_name = yaml_content.get('name', 'workflow')
    lines.append(f"    title {workflow_name}")
    
    # Add participants
    lines.append("    participant User")
    for step in yaml_content.get('steps', []):
        agent = step.get('agent', 'Agent')
        lines.append(f"    participant {agent.replace(' ', '')}")
    
    # Add flow
    lines.append("    User->>Orchestrator: Execute workflow")
    
    prev_step = None
    for step in yaml_content.get('steps', []):
        step_name = step.get('name', 'unnamed')
        agent = step.get('agent', 'Agent').replace(' ', '')
        
        if prev_step:
            lines.append(f"    {prev_step.replace(' ', '')}->>{agent}: {step_name}")
        else:
            lines.append(f"    Orchestrator->>{agent}: {step_name}")
        
        lines.append(f"    {agent}-->>{prev_step.replace(' ', '') if prev_step else 'Orchestrator'}: Result")
        prev_step = agent
    
    lines.append("    Orchestrator-->>User: Workflow complete")
    lines.append("```")
    
    return '\n'.join(lines)


def render_workflow(yaml_path: str, output_dir: str, format: str = 'mmd') -> list:
    """Render a single workflow to diagram."""
    generated = []
    
    with open(yaml_path, 'r') as f:
        workflow = yaml.safe_load(f)
    
    if not workflow:
        return generated
    
    workflow_name = workflow.get('name', 'workflow')
    
    # Generate Mermaid flowchart
    mermaid_content = yaml_to_mermaid(workflow)
    
    output_file = Path(output_dir) / f"{workflow_name}.mmd"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w') as f:
        f.write(mermaid_content)
    
    generated.append(str(output_file))
    
    # Generate sequence diagram
    sequence_content = yaml_to_sequence_mermaid(workflow)
    seq_output_file = Path(output_dir) / f"{workflow_name}_sequence.mmd"
    
    with open(seq_output_file, 'w') as f:
        f.write(sequence_content)
    
    generated.append(str(seq_output_file))
    
    return generated


def main():
    parser = argparse.ArgumentParser(description='Render Mermaid diagrams from workflows')
    parser.add_argument('--input', required=True, help='Input workflow file or directory')
    parser.add_argument('--output', default='docs/diagrams', help='Output directory')
    parser.add_argument('--format', default='mmd', choices=['mmd', 'png', 'svg'],
                        help='Output format')
    parser.add_argument('--recursive', action='store_true', help='Recursively process directories')
    args = parser.parse_args()
    
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    generated_files = []
    
    input_path = Path(args.input)
    
    if input_path.is_file() and input_path.suffix in ['.yaml', '.yml']:
        generated = render_workflow(str(input_path), str(output_dir), args.format)
        generated_files.extend(generated)
    elif input_path.is_dir():
        pattern = '**/*.yaml' if args.recursive else '*.yaml'
        for yaml_file in input_path.glob(pattern):
            generated = render_workflow(str(yaml_file), str(output_dir), args.format)
            generated_files.extend(generated)
    else:
        print(f"Error: Invalid input path: {args.input}")
        sys.exit(1)
    
    print(f"Generated {len(generated_files)} diagram files:")
    for f in generated_files:
        print(f"  - {f}")
    
    print(f"\nOutput directory: {output_dir}")


if __name__ == '__main__':
    main()
