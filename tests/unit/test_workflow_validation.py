# Workflow Validation Tests
# Tests for YAML validation and schema compliance

import pytest
import yaml
from pathlib import Path


class TestWorkflowYAMLStructure:
    """Test workflow YAML files have correct structure."""
    
    @pytest.fixture
    def workflow_files(self):
        """Get all workflow YAML files."""
        workflows_dir = Path(__file__).parent.parent / 'workflows'
        return list(workflows_dir.rglob('*.yaml'))
    
    def test_workflow_has_name(self, workflow_files):
        """Each workflow must have a name field."""
        for wf_file in workflow_files:
            with open(wf_file, 'r') as f:
                workflow = yaml.safe_load(f)
            
            if workflow is None:
                pytest.skip(f"Empty file: {wf_file}")
            
            assert 'name' in workflow, f"Workflow {wf_file} missing 'name' field"
    
    def test_workflow_has_version(self, workflow_files):
        """Each workflow must have a version field."""
        for wf_file in workflow_files:
            with open(wf_file, 'r') as f:
                workflow = yaml.safe_load(f)
            
            if workflow is None:
                pytest.skip(f"Empty file: {wf_file}")
            
            assert 'version' in workflow, f"Workflow {wf_file} missing 'version' field"
    
    def test_workflow_has_description(self, workflow_files):
        """Each workflow must have a description field."""
        for wf_file in workflow_files:
            with open(wf_file, 'r') as f:
                workflow = yaml.safe_load(f)
            
            if workflow is None:
                pytest.skip(f"Empty file: {wf_file}")
            
            assert 'description' in workflow, f"Workflow {wf_file} missing 'description' field"
    
    def test_workflow_has_steps(self, workflow_files):
        """Each workflow must have at least one step."""
        for wf_file in workflow_files:
            with open(wf_file, 'r') as f:
                workflow = yaml.safe_load(f)
            
            if workflow is None:
                pytest.skip(f"Empty file: {wf_file}")
            
            assert 'steps' in workflow, f"Workflow {wf_file} missing 'steps' field"
            assert len(workflow['steps']) > 0, f"Workflow {wf_file} has no steps"
    
    def test_steps_have_required_fields(self, workflow_files):
        """Each step must have required fields."""
        for wf_file in workflow_files:
            with open(wf_file, 'r') as f:
                workflow = yaml.safe_load(f)
            
            if workflow is None:
                continue
            
            for i, step in enumerate(workflow.get('steps', [])):
                assert 'name' in step, f"Step {i} in {wf_file} missing 'name'"
                assert 'agent' in step, f"Step '{step.get('name', i)}' in {wf_file} missing 'agent'"


class TestWorkflowDependencies:
    """Test workflow step dependencies."""
    
    @pytest.fixture
    def workflows(self):
        """Load all workflows."""
        workflows_dir = Path(__file__).parent.parent / 'workflows'
        workflows = {}
        
        for wf_file in workflows_dir.rglob('*.yaml'):
            with open(wf_file, 'r') as f:
                workflows[wf_file.name] = yaml.safe_load(f)
        
        return workflows
    
    def test_dependencies_reference_valid_steps(self, workflows):
        """Step dependencies must reference existing steps."""
        for wf_name, workflow in workflows.items():
            if workflow is None:
                continue
            
            step_names = {step.get('name') for step in workflow.get('steps', [])}
            
            for step in workflow.get('steps', []):
                for dep in step.get('depends_on', []):
                    assert dep in step_names, \
                        f"Workflow {wf_name}: Step '{step['name']}' depends on unknown step '{dep}'"
    
    def test_no_circular_dependencies(self, workflows):
        """Workflows must not have circular dependencies."""
        for wf_name, workflow in workflows.items():
            if workflow is None:
                continue
            
            # Build graph
            graph = {}
            step_names = []
            
            for step in workflow.get('steps', []):
                step_name = step.get('name')
                step_names.append(step_name)
                graph[step_name] = set(step.get('depends_on', []))
            
            # Check for cycles
            visited = set()
            rec_stack = set()
            
            def has_cycle(node, path):
                if node not in visited:
                    visited.add(node)
                    rec_stack.add(node)
                    
                    for neighbor in graph.get(node, []):
                        if neighbor not in visited:
                            if has_cycle(neighbor, path + [node]):
                                return True
                        elif neighbor in rec_stack:
                            return True
                    
                    rec_stack.remove(node)
                return False
            
            for step_name in step_names:
                if step_name not in visited:
                    assert not has_cycle(step_name, [step_name]), \
                        f"Circular dependency in {wf_name}"


class TestWorkflowGuardrails:
    """Test workflow guardrails and safety rules."""
    
    @pytest.fixture
    def workflows(self):
        """Load all workflows."""
        workflows_dir = Path(__file__).parent.parent / 'workflows'
        workflows = {}
        
        for wf_file in workflows_dir.rglob('*.yaml'):
            with open(wf_file, 'r') as f:
                workflows[wf_file.name] = yaml.safe_load(f)
        
        return workflows
    
    def test_workflow_has_guardrails(self, workflows):
        """Each workflow should have guardrails defined."""
        for wf_name, workflow in workflows.items():
            if workflow is None:
                continue
            
            # Guardrails are recommended but not strictly required
            # This is a soft check
            if 'guardrails' not in workflow:
                print(f"Warning: Workflow {wf_name} has no guardrails defined")


class TestWorkflowSuccessCriteria:
    """Test workflow success criteria."""
    
    @pytest.fixture
    def workflows(self):
        """Load all workflows."""
        workflows_dir = Path(__file__).parent.parent / 'workflows'
        workflows = {}
        
        for wf_file in workflows_dir.rglob('*.yaml'):
            with open(wf_file, 'r') as f:
                workflows[wf_file.name] = yaml.safe_load(f)
        
        return workflows
    
    def test_workflow_has_success_criteria(self, workflows):
        """Each workflow should define success criteria."""
        for wf_name, workflow in workflows.items():
            if workflow is None:
                continue
            
            # Success criteria are recommended but not strictly required
            if 'success_criteria' not in workflow:
                print(f"Warning: Workflow {wf_name} has no success criteria defined")


class TestYAMLSyntax:
    """Test YAML syntax validity."""
    
    @pytest.fixture
    def yaml_files(self):
        """Get all YAML files."""
        root = Path(__file__).parent.parent
        
        yaml_patterns = [
            'workflows/**/*.yaml',
            'rules/**/*.yaml',
            'rules/**/*.md',
            'prompts/**/*.yaml',
            'prompts/**/*.md',
        ]
        
        files = []
        for pattern in yaml_patterns:
            files.extend(root.glob(pattern))
        
        return files
    
    def test_valid_yaml_syntax(self, yaml_files):
        """All YAML files must have valid syntax."""
        for yaml_file in yaml_files:
            try:
                with open(yaml_file, 'r') as f:
                    content = f.read()
                    yaml.safe_load(content)
            except yaml.YAMLError as e:
                pytest.fail(f"Invalid YAML in {yaml_file}: {e}")
