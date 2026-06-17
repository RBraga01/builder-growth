#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consistency checker for builder-growth.

Truth sources:
  Skill count - number of SKILL.md files in skills/*/
  Agent count - number of Markdown files in .claude/agents/
  Version     - latest ## x.y.z entry in CHANGELOG.md

Run: python scripts/check_consistency.py
Exit 0 = all checks passed. Exit 1 = at least one mismatch.
"""

import io
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).parent.parent


def count_skills() -> int:
    return len(list(REPO_ROOT.glob("skills/*/SKILL.md")))


def count_agents() -> int:
    return len(list(REPO_ROOT.glob(".claude/agents/*.md")))


def changelog_version() -> str:
    text = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    match = re.search(r"^## (\d+\.\d+\.\d+)", text, re.MULTILINE)
    if not match:
        raise SystemExit("ERROR: no version found in CHANGELOG.md")
    return match.group(1)


VERSION_CHECKS = [
    ("README.md", r"# builder-growth[^\n]*v(\d+\.\d+\.\d+)", "README title heading"),
    ("CHANGELOG.md", r"\A# Changelog[^\n]*\n\n## (\d+\.\d+\.\d+)", "CHANGELOG latest heading"),
    ("CLAUDE.md", r"builder-growth[^\n]*v(\d+\.\d+\.\d+)", "CLAUDE pack version"),
    ("AGENTS.md", r"Version:\s*v(\d+\.\d+\.\d+)", "AGENTS version"),
    ("docs/index.html", r'nav-logo-badge">v(\d+\.\d+\.\d+)<', "docs nav badge"),
    (".claude-plugin/plugin.json", r'"version":\s*"(\d+\.\d+\.\d+)"', "Claude plugin version"),
    (".codex-plugin/plugin.json", r'"version":\s*"(\d+\.\d+\.\d+)"', "Codex plugin version"),
]

SKILL_COUNT_CHECKS = [
    ("README.md", r"\|\s*\*\*builder-growth\*\*\s*\|[^\n|]*\|\s*(\d+)\s*\|", "README ecosystem skill count"),
    ("docs/index.html", r"content=\"(\d+) skills and \d+ agents", "docs meta skill count"),
    ("docs/index.html", r"The (\d+) Rules", "docs skills section count"),
    (".claude-plugin/plugin.json", r"(\d+) skills and \d+ agents", "Claude plugin description"),
    (".codex-plugin/plugin.json", r"(\d+) skills and \d+ agents", "Codex plugin description"),
]

AGENT_COUNT_CHECKS = [
    ("README.md", r"\|\s*\*\*builder-growth\*\*\s*\|[^\n|]*\|\s*\d+\s*\|\s*(\d+)\s*\|", "README ecosystem agent count"),
    ("docs/index.html", r"content=\"\d+ skills and (\d+) agents", "docs meta agent count"),
    ("docs/index.html", r"The (\d+) Specialists", "docs agents section count"),
    (".claude-plugin/plugin.json", r"\d+ skills and (\d+) agents", "Claude plugin description"),
    (".codex-plugin/plugin.json", r"\d+ skills and (\d+) agents", "Codex plugin description"),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_regex_checks(checks: list, expected: str) -> list[str]:
    errors = []
    for filepath, pattern, desc in checks:
        path = REPO_ROOT / filepath
        if not path.exists():
            errors.append(f"MISSING  {filepath} ({desc}): file not found")
            continue
        matches = list(re.finditer(pattern, read_text(path), re.MULTILINE))
        if not matches:
            errors.append(f"MISSING  {filepath} ({desc}): pattern not found")
            continue
        for match in matches:
            found = match.group(1)
            if found != str(expected):
                errors.append(
                    f"MISMATCH {filepath} ({desc}): found {found!r}, expected {expected!r}"
                )
    return errors


def validate_json_files(paths: list[str]) -> list[str]:
    errors = []
    for filepath in paths:
        path = REPO_ROOT / filepath
        if not path.exists():
            errors.append(f"MISSING  {filepath}: file not found")
            continue
        try:
            json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            errors.append(f"INVALID  {filepath}: {exc}")
    return errors


def validate_skill_frontmatter() -> list[str]:
    errors = []
    for skill_path in sorted(REPO_ROOT.glob("skills/*/SKILL.md")):
        text = read_text(skill_path)
        if not text.startswith("---\n"):
            errors.append(f"INVALID  {skill_path.relative_to(REPO_ROOT)}: missing YAML frontmatter")
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            errors.append(f"INVALID  {skill_path.relative_to(REPO_ROOT)}: unterminated YAML frontmatter")
            continue
        frontmatter = text[4:end]
        if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
            errors.append(f"INVALID  {skill_path.relative_to(REPO_ROOT)}: missing frontmatter name")
        if not re.search(r"^description:\s*\S+", frontmatter, re.MULTILINE):
            errors.append(f"INVALID  {skill_path.relative_to(REPO_ROOT)}: missing frontmatter description")
    return errors


def main() -> int:
    actual_skills = count_skills()
    actual_agents = count_agents()
    actual_version = changelog_version()

    print(f"Truth: {actual_skills} skills  |  {actual_agents} agents  |  v{actual_version}")
    print()

    errors = []
    errors.extend(run_regex_checks(VERSION_CHECKS, actual_version))
    errors.extend(run_regex_checks(SKILL_COUNT_CHECKS, str(actual_skills)))
    errors.extend(run_regex_checks(AGENT_COUNT_CHECKS, str(actual_agents)))
    errors.extend(validate_json_files([".claude-plugin/plugin.json", ".codex-plugin/plugin.json"]))
    errors.extend(validate_skill_frontmatter())

    if errors:
        print(f"Found {len(errors)} consistency error(s):\n")
        for error in errors:
            print(f"  {error}")
        print()
        print("Fix the mismatches above and re-run.")
        return 1

    total = len(VERSION_CHECKS) + len(SKILL_COUNT_CHECKS) + len(AGENT_COUNT_CHECKS) + 2 + actual_skills
    print(f"All {total} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
