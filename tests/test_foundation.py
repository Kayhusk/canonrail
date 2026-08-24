import importlib.util
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ("agents", "readme", "roadmap", "execplan", "prd")
KIND_HEADINGS = {
    "agents": ("## Purpose", "## Project sources", "## Working rules", "## Verification"),
    "readme": ("## What it does", "## How it works", "## Current scope", "## Use", "## License"),
    "roadmap": ("## Status", "## Current phase", "## Next decision", "## Guardrails"),
    "execplan": ("## Goal", "## Context", "## Plan", "## Validation", "## Recovery"),
    "prd": ("## Problem", "## Users", "## Outcomes", "## Scope", "## Acceptance"),
}
EXPECTED_FILES = (
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "VERSION",
    ".gitignore",
    ".mdsmith.yml",
    "plugin.yaml",
    "__init__.py",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    "skills/canonrail/SKILL.md",
    ".github/workflows/ci.yml",
    *(f"contracts/{name}.md" for name in CONTRACTS),
)
FORBIDDEN_PUBLIC_TERMS = (
    "Artemis",
    "SourceBand",
    "Foldly",
    "Apollo",
    "MiglioHoldings",
    "/home/",
)


class FoundationTests(unittest.TestCase):
    def test_required_foundation_files_exist(self):
        missing = [path for path in EXPECTED_FILES if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_versions_match_across_plugin_manifests(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertRegex(version, r"^0\.1\.0$")

        claude_manifest = json.loads(
            (ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(claude_manifest["name"], "canonrail")
        self.assertEqual(claude_manifest["version"], version)

        codex_manifest = json.loads(
            (ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(codex_manifest["name"], "canonrail")
        self.assertEqual(codex_manifest["version"], version)
        self.assertEqual(codex_manifest["skills"], "./skills/")

        hermes_manifest = (ROOT / "plugin.yaml").read_text(encoding="utf-8")
        self.assertRegex(hermes_manifest, r"(?m)^name: canonrail$")
        self.assertRegex(hermes_manifest, rf"(?m)^version: {re.escape(version)}$")
        self.assertRegex(hermes_manifest, r"(?m)^  - canonrail$")

    def test_each_contract_has_a_bounded_responsibility(self):
        required_headings = ("# ", "## Owns", "## Must not absorb", "## Review")
        for name in CONTRACTS:
            text = (ROOT / "contracts" / f"{name}.md").read_text(encoding="utf-8")
            for heading in required_headings:
                self.assertIn(heading, text, f"{name}.md is missing {heading}")

    def test_each_kind_has_valid_and_adjacent_invalid_fixtures(self):
        for name, headings in KIND_HEADINGS.items():
            fixture_dir = ROOT / "fixtures" / name
            valid_path = fixture_dir / "valid.md"
            invalid_path = fixture_dir / "invalid.md.txt"
            self.assertTrue(valid_path.is_file(), f"missing {valid_path.relative_to(ROOT)}")
            self.assertTrue(invalid_path.is_file(), f"missing {invalid_path.relative_to(ROOT)}")

            valid = valid_path.read_text(encoding="utf-8")
            invalid = invalid_path.read_text(encoding="utf-8")
            self.assertTrue(all(heading in valid for heading in headings))
            missing = [heading for heading in headings if heading not in invalid]
            self.assertEqual(len(missing), 1, f"{name} invalid fixture must miss one heading")

    def test_mdsmith_config_maps_every_contract_kind(self):
        config = (ROOT / ".mdsmith.yml").read_text(encoding="utf-8")
        for name in CONTRACTS:
            self.assertRegex(config, rf"(?m)^  {re.escape(name)}:$")
        for path in ("AGENTS.md", "README.md", "PLAN.md", ".canonrail/plans/*.md", "docs/prd/**/*.md"):
            self.assertIn(path, config)

    def test_hermes_plugin_registers_the_portable_skill(self):
        plugin_path = ROOT / "__init__.py"
        spec = importlib.util.spec_from_file_location("canonrail_plugin", plugin_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        class Context:
            def __init__(self):
                self.skills = []

            def register_skill(self, name, path):
                self.skills.append((name, Path(path)))

        context = Context()
        module.register(context)
        self.assertEqual([name for name, _ in context.skills], ["canonrail"])
        self.assertTrue(context.skills[0][1].is_file())

    def test_public_markdown_does_not_expose_private_project_jargon(self):
        markdown_files = [
            path
            for path in ROOT.rglob("*.md")
            if ".git" not in path.parts and "tests" not in path.parts
        ]
        self.assertTrue(markdown_files)
        violations = []
        for path in markdown_files:
            text = path.read_text(encoding="utf-8")
            for term in FORBIDDEN_PUBLIC_TERMS:
                if term in text:
                    violations.append(f"{path.relative_to(ROOT)}: {term}")
        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
