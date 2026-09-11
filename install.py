#!/usr/bin/env python3
"""
Universal Installer & Packager for Ten Thinking Dimensions Cognitive OS
Works on macOS, Linux, and Windows (Python 3.6+)
"""

import os
import sys
import shutil
import zipfile
import argparse
from pathlib import Path

SKILL_NAME = "ten-thinking-dimensions"

def get_source_dir():
    current_dir = Path(__file__).resolve().parent
    # Check if we are running from project root
    candidate1 = current_dir / ".agents" / "skills" / SKILL_NAME
    if candidate1.exists():
        return candidate1
    # Check if we are running from inside the skill dir
    if (current_dir / "SKILL.md").exists():
        return current_dir
    raise FileNotFoundError(f"Cannot find source files for {SKILL_NAME}")

def install_global():
    src = get_source_dir()
    global_dest = Path.home() / ".gemini" / "config" / "skills" / SKILL_NAME
    print(f"Installing {SKILL_NAME} to Global Antigravity Config...")
    print(f"  Source: {src}")
    print(f"  Target: {global_dest}")

    if global_dest.exists():
        shutil.rmtree(global_dest)
    
    shutil.copytree(src, global_dest)
    print(f"\n[SUCCESS] Installed successfully to Global Config!")
    print(f"You can now use 'Ten Thinking Dimensions' in ANY project on this machine.\n")

def install_to_project(project_path):
    src = get_source_dir()
    target_project = Path(project_path).resolve()
    dest = target_project / ".agents" / "skills" / SKILL_NAME
    print(f"Installing {SKILL_NAME} to Project...")
    print(f"  Project: {target_project}")
    print(f"  Target:  {dest}")

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)

    shutil.copytree(src, dest)
    print(f"\n[SUCCESS] Installed successfully to project: {target_project.name}!")

def create_zip_bundle(output_file=None):
    src = get_source_dir()
    if not output_file:
        output_file = Path(__file__).resolve().parent / f"{SKILL_NAME}.zip"
    else:
        output_file = Path(output_file).resolve()

    print(f"Creating portable ZIP bundle...")
    print(f"  Source: {src}")
    print(f"  Output: {output_file}")

    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(src):
            for file in files:
                abs_path = Path(root) / file
                rel_path = abs_path.relative_to(src.parent)
                zf.write(abs_path, rel_path)

    print(f"\n[SUCCESS] ZIP bundle created at:")
    print(f"  {output_file}")
    print(f"You can share this zip file to any other machine or user!")

def main():
    parser = argparse.ArgumentParser(description="Universal Installer for Ten Thinking Dimensions")
    parser.add_argument("--global", "-g", dest="is_global", action="store_true", help="Install globally to ~/.gemini/config/skills/")
    parser.add_argument("--project", "-p", dest="project_path", help="Install into a specific project workspace path")
    parser.add_argument("--zip", "-z", dest="create_zip", action="store_true", help="Create a portable .zip bundle for sharing")
    parser.add_argument("--out", "-o", dest="out_zip", help="Output path for .zip bundle")

    args = parser.parse_args()

    # Default action if no arguments provided: install globally
    if not args.is_global and not args.project_path and not args.create_zip:
        install_global()
    else:
        if args.is_global:
            install_global()
        if args.project_path:
            install_to_project(args.project_path)
        if args.create_zip:
            create_zip_bundle(args.out_zip)

if __name__ == "__main__":
    main()
