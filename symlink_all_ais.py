#!/usr/bin/env python3
"""
Universal Multi-AI Symlinker for Ten Thinking Dimensions Cognitive OS
Creates symlinks for: Antigravity, Claude Code, Cursor, Windsurf, Cline, Roo Code, Continue.dev, Copilot
"""

import os
import sys
from pathlib import Path

SKILL_NAME = "ten-thinking-dimensions"

def create_symlink(target_path, link_path):
    target = Path(target_path).resolve()
    link = Path(link_path).resolve()

    if not target.exists():
        print(f"[-] Target does not exist: {target}")
        return False

    link.parent.mkdir(parents=True, exist_ok=True)

    if link.is_symlink() or link.exists():
        if link.is_dir() and not link.is_symlink():
            import shutil
            shutil.rmtree(link)
        else:
            link.unlink()

    try:
        link.symlink_to(target)
        print(f"[SUCCESS] {link} -> {target}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed linking {link}: {e}")
        return False

def main():
    script_dir = Path(__file__).resolve().parent
    skill_src = script_dir / ".agents" / "skills" / SKILL_NAME
    rule_src = script_dir / "GEMINI.md"
    home = Path.home()

    print("============================================================")
    print("  🔗 Multi-AI Symlink Manager: Ten Thinking Dimensions")
    print("============================================================")
    print(f"Skill Source: {skill_src}")
    print(f"Rule Source:  {rule_src}\n")

    links = []

    # 1. Antigravity / Gemini
    links.append((skill_src, home / ".gemini" / "config" / "skills" / SKILL_NAME))
    links.append((skill_src, home / ".gemini" / "skills" / SKILL_NAME))

    # 2. Claude Code & Central ai-brain-core
    ai_brain_core = home / "Code Project" / "ai-brain-core" / "skills"
    if ai_brain_core.exists():
        links.append((skill_src, ai_brain_core / SKILL_NAME))
    links.append((skill_src, home / ".claude" / "skills" / SKILL_NAME))

    # 3. Cursor
    links.append((rule_src, home / ".cursor" / "rules" / "ten-thinking-dimensions.mdc"))

    # 4. Cline & Roo Code
    links.append((skill_src, home / ".cline" / "skills" / SKILL_NAME))
    links.append((skill_src, home / ".roo" / "skills" / SKILL_NAME))

    # 5. Continue.dev
    links.append((skill_src, home / ".continue" / "skills" / SKILL_NAME))

    # 6. Workspace Root Rules (Universal Assistant Support)
    links.append((rule_src, script_dir / "CLAUDE.md"))
    links.append((rule_src, script_dir / ".cursorrules"))
    links.append((rule_src, script_dir / ".windsurfrules"))
    links.append((rule_src, script_dir / ".clinerules"))
    links.append((rule_src, script_dir / ".github" / "copilot-instructions.md"))

    success_count = 0
    for target, link in links:
        if create_symlink(target, link):
            success_count += 1

    print("\n============================================================")
    print(f"🎉 Symlink creation complete! ({success_count}/{len(links)} linked)")
    print("Every AI on this machine now shares the exact same 10-Think brain.")
    print("Any edit made to this repository will reflect in ALL AIs instantly!")
    print("============================================================\n")

if __name__ == "__main__":
    main()
