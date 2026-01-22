#!/usr/bin/env python3
"""
Prompt Optimizer - Analyzes and optimizes prompts for better responses.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class OptimizationSuggestion:
    """Represents a prompt optimization suggestion."""
    line: int
    rule: str
    severity: str  # error, warning, suggestion
    message: str
    original: str
    suggestion: str = ""


class PromptOptimizer:
    """Analyzes and optimizes prompts."""

    def __init__(self, prompt_path: str):
        self.prompt_path = Path(prompt_path)
        self.content = ""
        self.lines: List[str] = []
        self.suggestions: List[OptimizationSuggestion] = []

    def load(self) -> bool:
        """Load the prompt file."""
        try:
            with open(self.prompt_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            self.lines = self.content.split('\n')
            return True
        except FileNotFoundError:
            print(f"Error: File not found: {self.prompt_path}")
            return False

    def analyze_structure(self):
        """Analyze prompt structure."""
        # Check for sections
        section_pattern = re.compile(r'^#+ (.+)$', re.MULTILINE)
        sections = section_pattern.findall(self.content)

        if not sections:
            self.suggestions.append(OptimizationSuggestion(
                line=0,
                rule="STRUCTURE",
                severity="suggestion",
                message="Prompt lacks clear section headers",
                original="",
                suggestion="Add sections like: ## Role, ## Task, ## Constraints, ## Examples"
            ))

        # Check for role definition
        role_patterns = [
            r'you are\s+a?\s*\w+',
            r'as\s+a?\s*\w+',
            r'role[:\s]+\w+'
        ]
        has_role = any(re.search(p, self.content, re.IGNORECASE) for p in role_patterns)

        if not has_role:
            self.suggestions.append(OptimizationSuggestion(
                line=self._find_line("role"),
                rule="ROLE",
                severity="error",
                message="No clear role definition found",
                original="",
                suggestion="Start with: 'You are an expert [domain] with [experience]'"
            ))

    def analyze_clarity(self):
        """Analyze clarity and specificity."""
        # Check for vague words
        vague_words = {
            "stuff": "specific items or concepts",
            "things": "specific items",
            "some": "specific quantity",
            "maybe": "specific answer",
            "possibly": "specific answer",
            "good": "specific quality metric",
            "bad": "specific issue",
            "nice": "specific attribute",
            "awesome": "specific positive trait"
        }

        for line_num, line in enumerate(self.lines, 1):
            for word, suggestion in vague_words.items():
                if re.search(r'\b' + word + r'\b', line, re.IGNORECASE):
                    self.suggestions.append(OptimizationSuggestion(
                        line=line_num,
                        rule="CLARITY",
                        severity="warning",
                        message=f"Vague word '{word}' found",
                        original=line.strip(),
                        suggestion=f"Replace with more specific language: {suggestion}"
                    ))

    def analyze_instructions(self):
        """Analyze instruction clarity."""
        # Check for imperative verbs
        action_verbs = [
            "analyze", "create", "generate", "write", "implement",
            "design", "explain", "describe", "list", "summarize",
            "compare", "evaluate", "assess", "review", "optimize"
        ]

        has_imperative = any(
            re.search(r'^\s*(?:please\s+)?(' + '|'.join(action_verbs) + r')\b', line, re.IGNORECASE)
            for line in self.lines
        )

        if not has_imperative:
            self.suggestions.append(OptimizationSuggestion(
                line=0,
                rule="INSTRUCTIONS",
                severity="suggestion",
                message="No clear action verbs in instructions",
                original="",
                suggestion="Start instructions with action verbs: 'Analyze...', 'Create...', 'Generate...'"
            ))

    def analyze_constraints(self):
        """Check for constraints and rules."""
        constraint_indicators = [
            r'must\s+\w+',
            r'should\s+\w+',
            r'cannot\s+\w+',
            r'don\'t\s+\w+',
            r'avoid\s+\w+',
            r'always\s+\w+',
            r'never\s+\w+',
            r'limit\s+\w+',
            r'restrict\s+\w+'
        ]

        has_constraints = any(
            re.search(pattern, self.content, re.IGNORECASE)
            for pattern in constraint_indicators
        )

        if not has_constraints:
            self.suggestions.append(OptimizationSuggestion(
                line=0,
                rule="CONSTRAINTS",
                severity="suggestion",
                message="No explicit constraints found",
                original="",
                suggestion="Add constraints to guide behavior: 'Must use X...', 'Never do Y...'"
            ))

    def analyze_examples(self):
        """Check for examples."""
        example_patterns = [
            r'example[:\s]',
            r'for instance',
            r'such as',
            r'e\.g\.',
            r'```',  # Code blocks
        ]

        has_examples = any(
            re.search(pattern, self.content, re.IGNORECASE)
            for pattern in example_patterns
        )

        if not has_examples:
            self.suggestions.append(OptimizationSuggestion(
                line=0,
                rule="EXAMPLES",
                severity="suggestion",
                message="No examples provided",
                original="",
                suggestion="Add examples to clarify expected output: 'Example: ...' or code blocks"
            ))

    def analyze_output_format(self):
        """Check for output format specification."""
        format_indicators = [
            r'output[:\s]',
            r'format[:\s]',
            r'response[:\s]',
            r'return[:\s]',
            r'use (?:json|yaml|markdown|text)',
            r'```[a-z]+',  # Code block language
        ]

        has_format = any(
            re.search(pattern, self.content, re.IGNORECASE)
            for pattern in format_indicators
        )

        if not has_format:
            self.suggestions.append(OptimizationSuggestion(
                line=0,
                rule="OUTPUT_FORMAT",
                severity="warning",
                message="No output format specified",
                original="",
                suggestion="Specify output format: 'Return JSON with fields X, Y, Z' or use code blocks"
            ))

    def analyze_length(self):
        """Analyze prompt length."""
        word_count = len(self.content.split())
        line_count = len(self.lines)

        if word_count < 50:
            self.suggestions.append(OptimizationSuggestion(
                line=0,
                rule="LENGTH",
                severity="suggestion",
                message=f"Prompt is very short ({word_count} words)",
                original="",
                suggestion="Add more context, constraints, and examples for better results"
            ))

        if word_count > 2000:
            self.suggestions.append(OptimizationSuggestion(
                line=0,
                rule="LENGTH",
                severity="warning",
                message=f"Prompt is quite long ({word_count} words)",
                original="",
                suggestion="Consider breaking into smaller, focused prompts for better results"
            ))

    def _find_line(self, keyword: str) -> int:
        """Find the line number containing a keyword."""
        for i, line in enumerate(self.lines, 1):
            if keyword.lower() in line.lower():
                return i
        return 0

    def analyze(self) -> List[OptimizationSuggestion]:
        """Run all analyses."""
        self.analyze_structure()
        self.analyze_clarity()
        self.analyze_instructions()
        self.analyze_constraints()
        self.analyze_examples()
        self.analyze_output_format()
        self.analyze_length()
        return self.suggestions

    def print_report(self):
        """Print optimization report."""
        print(f"📝 Prompt Analysis: {self.prompt_path.name}")
        print("=" * 60)

        if not self.suggestions:
            print("✓ No optimization suggestions found")
            return

        errors = [s for s in self.suggestions if s.severity == "error"]
        warnings = [s for s in self.suggestions if s.severity == "warning"]
        suggestions = [s for s in self.suggestions if s.suggestion == "suggestion"]

        print(f"🔴 Errors: {len(errors)}")
        print(f"🟡 Warnings: {len(warnings)}")
        print(f"🔵 Suggestions: {len(self.suggestions) - len(errors) - len(warnings)}")

        print("\n📋 Detailed Report:")
        for suggestion in self.suggestions:
            icon = "🔴" if suggestion.severity == "error" else ("🟡" if suggestion.severity == "warning" else "🔵")
            print(f"\n{icon} [{suggestion.rule}] Line {suggestion.line}")
            print(f"   {suggestion.message}")
            if suggestion.original:
                print(f"   📍 Found: {suggestion.original[:80]}...")
            if suggestion.suggestion:
                print(f"   💡 {suggestion.suggestion}")


def main():
    parser = argparse.ArgumentParser(description="Analyze and optimize prompts")
    parser.add_argument("prompt", help="Prompt file to analyze")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--fix", action="store_true", help="Apply auto-fixes where possible")
    args = parser.parse_args()

    optimizer = PromptOptimizer(args.prompt)
    if not optimizer.load():
        sys.exit(1)

    suggestions = optimizer.analyze()
    optimizer.print_report()

    if args.json:
        import json
        output = [
            {
                "line": s.line,
                "rule": s.rule,
                "severity": s.severity,
                "message": s.message,
                "original": s.original,
                "suggestion": s.suggestion
            }
            for s in suggestions
        ]
        print("\n" + json.dumps(output, indent=2))

    errors = sum(1 for s in suggestions if s.severity == "error")
    if errors > 0:
        print(f"\n⚠️  Found {errors} critical issues to address")
        sys.exit(1)


if __name__ == "__main__":
    main()
