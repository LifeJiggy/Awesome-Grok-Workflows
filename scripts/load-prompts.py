#!/usr/bin/env python3
"""
Prompt Loader - Loads and manages prompt collections.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
import yaml


@dataclass
class Prompt:
    """Represents a prompt template."""
    name: str
    path: str
    content: str
    category: str = ""
    description: str = ""
    variables: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "path": self.path,
            "category": self.category,
            "description": self.description,
            "variables": self.variables,
            "tags": self.tags,
            "content_preview": self.content[:200] + "..." if len(self.content) > 200 else self.content
        }


class PromptLoader:
    """Loads and manages prompt collections."""

    def __init__(self, prompts_dir: str = "prompts"):
        self.prompts_dir = Path(prompts_dir)
        self.prompts: List[Prompt] = []
        self.by_category: Dict[str, List[Prompt]] = {}
        self.by_tag: Dict[str, List[Prompt]] = {}

    def discover(self) -> List[Prompt]:
        """Discover all prompts in the prompts directory."""
        self.prompts = []

        # System prompts
        for path in self.prompts_dir.glob("system/*.txt"):
            prompt = self._load_prompt(path, "system")
            self.prompts.append(prompt)

        # Few-shot examples
        for path in self.prompts_dir.glob("few-shot/*.md"):
            prompt = self._load_prompt(path, "few-shot")
            self.prompts.append(prompt)

        # Prompt templates
        for path in self.prompts_dir.glob("templates/*.j2"):
            prompt = self._load_prompt(path, "templates")
            self.prompts.append(prompt)

        # Index prompts
        for prompt in self.prompts:
            self._index_prompt(prompt)

        return self.prompts

    def _load_prompt(self, path: Path, category: str) -> Prompt:
        """Load a single prompt file."""
        content = path.read_text(encoding='utf-8')

        # Extract variables from template syntax
        variables = self._extract_variables(content)

        # Extract description from first lines
        description = self._extract_description(content)

        # Extract tags from frontmatter or content
        tags = self._extract_tags(content)

        return Prompt(
            name=path.stem,
            path=str(path),
            content=content,
            category=category,
            description=description,
            variables=variables,
            tags=tags
        )

    def _extract_variables(self, content: str) -> List[str]:
        """Extract template variables from content."""
        import re
        # Match {{variable}} or {{ var }}
        pattern = r'\{\{\s*(\w+)\s*\}\}'
        matches = re.findall(pattern, content)
        return list(set(matches))

    def _extract_description(self, content: str) -> str:
        """Extract description from content."""
        lines = content.strip().split('\n')
        for line in lines[:5]:
            line = line.strip().lstrip('#').strip()
            if line and not line.startswith('```'):
                return line
        return ""

    def _extract_tags(self, content: str) -> List[str]:
        """Extract tags from content."""
        tags = []

        # Check for tags in comments
        import re
        tag_pattern = re.findall(r'#\s*tag[s]?[:\s]+([^\n]+)', content, re.IGNORECASE)
        for tag_line in tag_pattern:
            tags.extend([t.strip() for t in tag_line.split(',')])

        # Infer tags from content
        content_lower = content.lower()
        if 'python' in content_lower:
            tags.append('python')
        if 'javascript' in content_lower or 'js' in content_lower:
            tags.append('javascript')
        if 'api' in content_lower or 'endpoint' in content_lower:
            tags.append('api')
        if 'test' in content_lower:
            tags.append('testing')

        return list(set(tags))

    def _index_prompt(self, prompt: Prompt):
        """Index prompt by category and tags."""
        if prompt.category not in self.by_category:
            self.by_category[prompt.category] = []
        self.by_category[prompt.category].append(prompt)

        for tag in prompt.tags:
            if tag not in self.by_tag:
                self.by_tag[tag] = []
            self.by_tag[tag].append(prompt)

    def get_by_name(self, name: str) -> Optional[Prompt]:
        """Get a prompt by name."""
        for prompt in self.prompts:
            if prompt.name == name:
                return prompt
        return None

    def get_by_category(self, category: str) -> List[Prompt]:
        """Get prompts by category."""
        return self.by_category.get(category, [])

    def get_by_tag(self, tag: str) -> List[Prompt]:
        """Get prompts by tag."""
        return self.by_tag.get(tag, [])

    def search(self, query: str) -> List[Prompt]:
        """Search prompts by content."""
        query = query.lower()
        results = []
        for prompt in self.prompts:
            if (query in prompt.name.lower() or
                query in prompt.description.lower() or
                query in prompt.content.lower()):
                results.append(prompt)
        return results

    def render(self, name: str, variables: Dict[str, Any]) -> str:
        """Render a prompt with variables."""
        prompt = self.get_by_name(name)
        if not prompt:
            raise ValueError(f"Prompt not found: {name}")

        content = prompt.content
        for key, value in variables.items():
            content = content.replace(f'{{{{{key}}}}}', str(value))
            content = content.replace(f'{{{{ {key} }}}}', str(value))

        return content


def main():
    parser = argparse.ArgumentParser(description="Load and manage prompts")
    parser.add_argument("--dir", default="prompts", help="Prompts directory")
    parser.add_argument("--list", action="store_true", help="List all prompts")
    parser.add_argument("--category", help="Filter by category")
    parser.add_argument("--tag", help="Filter by tag")
    parser.add_argument("--search", help="Search prompts")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--render", metavar="NAME", help="Render a prompt")
    parser.add_argument("--var", action="append", metavar="KEY=VALUE", help="Variables for rendering")

    args = parser.parse_args()

    loader = PromptLoader(args.dir)
    prompts = loader.discover()

    if args.list:
        if args.json:
            print(json.dumps([p.to_dict() for p in prompts], indent=2))
        else:
            print(f"{'Name':<40} {'Category':<15} {'Variables':<20}")
            print("-" * 80)
            for prompt in prompts:
                var_str = ', '.join(prompt.variables[:5])
                if len(prompt.variables) > 5:
                    var_str += f"... +{len(prompt.variables) - 5}"
                print(f"{prompt.name:<40} {prompt.category:<15} {var_str:<20}")

    elif args.category:
        filtered = loader.get_by_category(args.category)
        print(f"Prompts in category '{args.category}':")
        for p in filtered:
            print(f"  - {p.name}")

    elif args.tag:
        filtered = loader.get_by_tag(args.tag)
        print(f"Prompts tagged '{args.tag}':")
        for p in filtered:
            print(f"  - {p.name}")

    elif args.search:
        results = loader.search(args.search)
        print(f"Search results for '{args.search}':")
        for p in results:
            print(f"  - {p.name} ({p.category})")

    elif args.render:
        variables = {}
        if args.var:
            for v in args.var:
                if '=' in v:
                    key, value = v.split('=', 1)
                    variables[key] = value

        try:
            rendered = loader.render(args.render, variables)
            print(rendered)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    else:
        # Default: show summary
        print(f"📚 Prompt Library")
        print("=" * 60)
        print(f"Total Prompts: {len(prompts)}")
        print("\nBy Category:")
        for category, cat_prompts in loader.by_category.items():
            print(f"  {category}: {len(cat_prompts)} prompts")
        print("\nTop Tags:")
        sorted_tags = sorted(loader.by_tag.items(), key=lambda x: len(x[1]), reverse=True)[:5]
        for tag, tag_prompts in sorted_tags:
            print(f"  #{tag}: {len(tag_prompts)} prompts")


if __name__ == "__main__":
    main()
