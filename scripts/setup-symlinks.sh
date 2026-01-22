#!/bin/bash
# Setup Symlinks to Awesome-Grok-Skills Repository
# This script creates symlinks from this repo to the skills repo

set -e  # Exit on error

SKILLS_PATH="${1:-../Awesome-Grok-Skills}"
SKILLS_DIR=$(readlink -f "$SKILLS_PATH" 2>/dev/null || echo "$SKILLS_PATH")

echo "🔗 Setting up symlinks to Awesome-Grok-Skills..."
echo "Skills path: $SKILLS_DIR"

# Check if skills repo exists
if [ ! -d "$SKILLS_DIR" ]; then
    echo "❌ Error: Skills directory not found at $SKILLS_DIR"
    echo "Please ensure Awesome-Grok-Skills is cloned and accessible."
    exit 1
fi

# Create symlinks directory
mkdir -p symlinks

# Symlink skills agents
if [ -d "$SKILLS_DIR/agents" ]; then
    echo "📦 Linking agents..."
    rm -rf symlinks/agents
    ln -sf "$SKILLS_DIR/agents" symlinks/agents
    echo "  ✅ agents/ -> $SKILLS_DIR/agents"
else
    echo "  ⚠️  No agents directory found in skills repo"
fi

# Symlink skills domains
if [ -d "$SKILLS_DIR/domains" ]; then
    echo "🎯 Linking domains..."
    rm -rf symlinks/domains
    ln -sf "$SKILLS_DIR/domains" symlinks/domains
    echo "  ✅ domains/ -> $SKILLS_DIR/domains"
else
    echo "  ⚠️  No domains directory found in skills repo"
fi

# Symlink skills templates
if [ -d "$SKILLS_DIR/templates" ]; then
    echo "📝 Linking templates..."
    rm -rf symlinks/templates
    ln -sf "$SKILLS_DIR/templates" symlinks/templates
    echo "  ✅ templates/ -> $SKILLS_DIR/templates"
else
    echo "  ⚠️  No templates directory found in skills repo"
fi

# Symlink skills scripts
if [ -d "$SKILLS_DIR/scripts" ]; then
    echo "🔧 Linking scripts..."
    rm -rf symlinks/scripts
    ln -sf "$SKILLS_DIR/scripts" symlinks/scripts
    echo "  ✅ scripts/ -> $SKILLS_DIR/scripts"
else
    echo "  ⚠️  No scripts directory found in skills repo"
fi

# Symlink AGENTS.md for reference
if [ -f "$SKILLS_DIR/AGENTS.md" ]; then
    echo "📚 Linking AGENTS.md..."
    rm -f symlinks/AGENTS.md
    ln -sf "$SKILLS_DIR/AGENTS.md" symlinks/AGENTS.md
    echo "  ✅ AGENTS.md -> $SKILLS_DIR/AGENTS.md"
fi

# Symlink README.md for reference
if [ -f "$SKILLS_DIR/README.md" ]; then
    echo "📖 Linking README.md..."
    rm -f symlinks/README.md
    ln -sf "$SKILLS_DIR/README.md" symlinks/README.md
    echo "  ✅ README.md -> $SKILLS_DIR/README.md"
fi

echo ""
echo "✅ Symlink setup complete!"
echo ""
echo "Available symlinks:"
ls -la symlinks/

echo ""
echo "📝 Usage examples:"
echo "  - Access skills via: symlinks/agents/"
echo "  - Reference domains: symlinks/domains/"
echo "  - Use templates: symlinks/templates/"
echo ""
echo "⚠️  Note: These are read-only symlinks. To modify skills, edit the original repo."
