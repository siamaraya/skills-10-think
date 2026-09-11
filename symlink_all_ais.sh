#!/usr/bin/env bash
# ============================================================
# Universal Multi-AI Symlink Setup for Ten Thinking Dimensions
# Automatically connects: Antigravity, Claude Code, Cursor,
# Windsurf, Cline, Roo Code, Continue.dev, GitHub Copilot
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SRC="$SCRIPT_DIR/.agents/skills/ten-thinking-dimensions"
RULE_SRC="$SCRIPT_DIR/GEMINI.md"

echo "============================================================"
echo "  🔗 Multi-AI Symlink Setup: Ten Thinking Dimensions"
echo "============================================================"
echo "Skill Source: $SKILL_SRC"
echo "Rule Source:  $RULE_SRC"
echo ""

link_item() {
  local target="$1"
  local link="$2"

  if [ ! -e "$target" ]; then
    echo "[-] Target does not exist: $target"
    return 1
  fi

  mkdir -p "$(dirname "$link")"

  if [ -L "$link" ] || [ -e "$link" ]; then
    rm -rf "$link"
  fi

  ln -s "$target" "$link"
  echo "[SUCCESS] $link -> $target"
}

# 1. Antigravity / Gemini
link_item "$SKILL_SRC" "$HOME/.gemini/config/skills/ten-thinking-dimensions"
link_item "$SKILL_SRC" "$HOME/.gemini/skills/ten-thinking-dimensions"

# 2. Claude Code & Central ai-brain-core
AI_BRAIN_CORE="$HOME/Code Project/ai-brain-core/skills"
if [ -d "$AI_BRAIN_CORE" ]; then
  link_item "$SKILL_SRC" "$AI_BRAIN_CORE/ten-thinking-dimensions"
fi
link_item "$SKILL_SRC" "$HOME/.claude/skills/ten-thinking-dimensions"

# 3. Cursor Global Rule
link_item "$RULE_SRC" "$HOME/.cursor/rules/ten-thinking-dimensions.mdc"

# 4. Cline & Roo Code
link_item "$SKILL_SRC" "$HOME/.cline/skills/ten-thinking-dimensions"
link_item "$SKILL_SRC" "$HOME/.roo/skills/ten-thinking-dimensions"

# 5. Continue.dev
link_item "$SKILL_SRC" "$HOME/.continue/skills/ten-thinking-dimensions"

# 6. Workspace-level rules for all assistants
link_item "$RULE_SRC" "$SCRIPT_DIR/CLAUDE.md"
link_item "$RULE_SRC" "$SCRIPT_DIR/.cursorrules"
link_item "$RULE_SRC" "$SCRIPT_DIR/.windsurfrules"
link_item "$RULE_SRC" "$SCRIPT_DIR/.clinerules"
link_item "$RULE_SRC" "$SCRIPT_DIR/.github/copilot-instructions.md"

# 7. Claude Code Slash Commands (Workspace & Global ~/.claude/commands/)
mkdir -p "$HOME/.claude/commands"
mkdir -p "$SCRIPT_DIR/.claude/commands"
for cmd_file in "$SCRIPT_DIR/commands"/*.md; do
  if [ -f "$cmd_file" ]; then
    link_item "$cmd_file" "$HOME/.claude/commands/$(basename "$cmd_file")"
    link_item "$cmd_file" "$SCRIPT_DIR/.claude/commands/$(basename "$cmd_file")"
  fi
done


echo ""
echo "============================================================"
echo "🎉 Symlinks configured successfully!"
echo "Any update made in this repository is instantly synced"
echo "across all AI assistants on your system without re-copying."
echo "============================================================"

