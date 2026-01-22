# Integration Tests for Workflow Execution
# Tests for workflow chaining and agent interactions

import pytest
import yaml
from pathlib import Path


class TestWorkflowIntegration:
    """Integration tests for workflow execution patterns."""
    
    @pytest.fixture
    def workflows_dir(self):
        """Get workflows directory."""
        return Path(__file__).parent.parent.parent / 'workflows'
    
    def test_workflow_files_loadable(self, workflows_dir):
        """All workflow YAML files should load without errors."""
        for wf_file in workflows_dir.rglob('*.yaml'):
            with open(wf_file, 'r') as f:
                workflow = yaml.safe_load(f)
            
            assert workflow is not None, f"Failed to load: {wf_file}"
    
    def test_base_template_is_valid(self, workflows_dir):
        """Base workflow template should be valid and usable."""
        template_file = workflows_dir / 'templates' / 'base-workflow-template.yaml'
        
        with open(template_file, 'r') as f:
            template = yaml.safe_load(f)
        
        assert template is not None
        assert 'name' in template
        assert 'steps' in template
        assert template['name'] == 'base-workflow-template'
    
    def test_pattern_files_are_valid(self, workflows_dir):
        """Reusable pattern files should be valid."""
        patterns_dir = workflows_dir / 'patterns'
        
        if not patterns_dir.exists():
            pytest.skip("Patterns directory not found")
        
        for pattern_file in patterns_dir.glob('*.yaml'):
            with open(pattern_file, 'r') as f:
                pattern = yaml.safe_load(f)
            
            assert pattern is not None
            assert 'name' in pattern
            assert 'pattern_type' in pattern


class TestSkillsIntegration:
    """Test integration with Awesome-Grok-Skills repo."""
    
    @pytest.fixture
    def skills_path(self):
        """Get skills repo path."""
        skills_path = Path(__file__).parent.parent.parent / 'symlinks' / 'agents'
        return skills_path
    
    def test_skills_symlink_exists(self, skills_path):
        """Skills symlink should exist."""
        assert skills_path.exists(), f"Skills symlink not found at {skills_path}"
    
    def test_agent_configs_accessible(self, skills_path):
        """Agent configs from skills repo should be accessible."""
        if not skills_path.exists():
            pytest.skip("Skills repo not linked")
        
        agent_dirs = [d for d in skills_path.iterdir() if d.is_dir()]
        assert len(agent_dirs) > 0, "No agent directories found"
        
        # Check a sample agent has required files
        if agent_dirs:
            sample_agent = agent_dirs[0]
            expected_files = ['config.yaml', 'system-prompt.txt']
            
            for expected in expected_files:
                assert (sample_agent / expected).exists(), \
                    f"Agent {sample_agent.name} missing {expected}"


class TestDocumentationIntegration:
    """Test documentation files are properly integrated."""
    
    @pytest.fixture
    def docs_dir(self):
        """Get docs directory."""
        return Path(__file__).parent.parent.parent / 'docs'
    
    def test_docs_structure_exists(self, docs_dir):
        """Documentation directory structure should exist."""
        if not docs_dir.exists():
            pytest.skip("Docs directory not found")
        
        expected_dirs = ['examples', 'generated']
        for expected in expected_dirs:
            assert (docs_dir / expected).exists(), \
                f"Documentation missing {expected} directory"
    
    def test_readme_exists(self):
        """README.md should exist at repo root."""
        root = Path(__file__).parent.parent.parent
        readme = root / 'README.md'
        assert readme.exists(), "README.md not found"
    
    def test_contributing_exists(self):
        """CONTRIBUTING.md should exist at repo root."""
        root = Path(__file__).parent.parent.parent
        contributing = root / 'CONTRIBUTING.md'
        assert contributing.exists(), "CONTRIBUTING.md not found"
    
    def test_file_structure_matches_docs(self):
        """file-structure.md should match actual directory structure."""
        root = Path(__file__).parent.parent.parent
        
        # Read file-structure.md
        structure_file = root / 'file-structure.md'
        with open(structure_file, 'r') as f:
            structure_content = f.read()
        
        # Check key directories mentioned in structure
        required_dirs = [
            'workflows',
            'rules',
            'prompts',
            'agents',
            '.github',
            'docs',
            'scripts',
            'tests',
        ]
        
        for dir_name in required_dirs:
            assert dir_name in structure_content, \
                f"Directory {dir_name} not documented in file-structure.md"
            
            dir_path = root / dir_name
            assert dir_path.exists(), \
                f"Directory {dir_name} does not exist"


class TestScriptIntegration:
    """Test automation scripts are properly integrated."""
    
    @pytest.fixture
    def scripts_dir(self):
        """Get scripts directory."""
        return Path(__file__).parent.parent.parent / 'scripts'
    
    def test_validate_script_exists(self, scripts_dir):
        """validate-workflow.sh should exist."""
        script = scripts_dir / 'validate-workflow.sh'
        assert script.exists(), "validate-workflow.sh not found"
        assert script.stat().st_mode & 0o111, "Script not executable"
    
    def test_render_script_exists(self, scripts_dir):
        """render-diagram.py should exist."""
        script = scripts_dir / 'render-diagram.py'
        assert script.exists(), "render-diagram.py not found"
    
    def test_symlink_script_exists(self, scripts_dir):
        """setup-symlinks.sh should exist."""
        script = scripts_dir / 'setup-symlinks.sh'
        assert script.exists(), "setup-symlinks.sh not found"
        assert script.stat().st_mode & 0o111, "Script not executable"


class TestCIIntegration:
    """Test CI/CD workflows are properly configured."""
    
    @pytest.fixture
    def github_dir(self):
        """Get .github/workflows directory."""
        return Path(__file__).parent.parent.parent / '.github' / 'workflows'
    
    def test_ci_workflows_exist(self, github_dir):
        """CI/CD workflow files should exist."""
        if not github_dir.exists():
            pytest.skip(".github/workflows directory not found")
        
        expected_workflows = [
            'test-workflows.yaml',
            'render-examples.yaml',
            'release-notes.yaml',
        ]
        
        for workflow in expected_workflows:
            assert (github_dir / workflow).exists(), \
                f"CI workflow {workflow} not found"
    
    def test_workflows_have_on_push_triggers(self, github_dir):
        """CI workflows should trigger on push."""
        if not github_dir.exists():
            pytest.skip(".github/workflows directory not found")
        
        for workflow_file in github_dir.glob('*.yaml'):
            with open(workflow_file, 'r') as f:
                workflow = yaml.safe_load(f)
            
            assert workflow is not None
            assert 'on' in workflow, \
                f"Workflow {workflow_file.name} missing 'on' trigger"
            
            assert 'push' in workflow['on'] or 'pull_request' in workflow['on'], \
                f"Workflow {workflow_file.name} should trigger on push/pr"
