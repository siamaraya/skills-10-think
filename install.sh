#!/usr/bin/env bash
# ==============================================================================
# Installer for Ten Thinking Dimensions Cognitive OS (macOS & Linux)
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${HOME}/.gemini/config/skills/ten-thinking-dimensions"
SRC_DIR="${SCRIPT_DIR}/.agents/skills/ten-thinking-dimensions"

echo "============================================================"
echo "  Installing: Ten Thinking Dimensions (ผู้ชนะ 10 คิด)"
echo "============================================================"

if [ ! -d "$SRC_DIR" ]; then
    echo "Error: Source directory $SRC_DIR not found!"
    exit 1
fi

mkdir -p "${HOME}/.gemini/config/skills"
rm -rf "$TARGET_DIR"
cp -R "$SRC_DIR" "$TARGET_DIR"

echo ""
echo "[SUCCESS] Installed successfully to:"
echo "  ${TARGET_DIR}"
echo ""
echo "You can now use 'ผู้ชนะ 10 คิด' across all workspaces on this machine!"
echo "============================================================"
