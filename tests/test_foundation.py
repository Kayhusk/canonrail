import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MDSMITH = ("npx", "--yes", "@mdsmith/cli@0.54.0")
CONTRACTS = ("agents", "readme", "roadmap", "execplan", "prd")
CONTRACT_FILES = {**{name: name for name in CONTRACTS}, "agents": "agent-instructions"}
KIND_HEADINGS = {
    "agents": ("## Purpose", "## Project sources", "## Working rules", "## Verification"),
    "readme": ("## What it does", "## How it works", "## Current scope", "## Use", "## License"),
    "roadmap": ("## Status", "## Current phase", "## Next decision", "## Guardrails"),
    "execplan": ("## Goal", "## Context", "## Plan", "## Validation", "## Recovery"),
    "prd": ("## Problem", "## Users", "## Outcomes", "## Scope", "## Acceptance"),
}
EXPECTED_FILES = (
    "README.md",
    "CHANGELOG.md",
    "PLAN.md",
    "docs/research/foundation-sources.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "VERSION",
    ".gitignore",
    ".mdsmith.yml",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    "skills/canonrail/SKILL.md",
    ".github/workflows/ci.yml",
    *(
        f"skills/canonrail/references/contracts/{CONTRACT_FILES[name]}.md"
        for name in CONTRACTS
    ),
)
FORBIDDEN_PUBLIC_FRAGMENTS = (
    "/home/",
    ".hermes/profiles/",
    ".codex/plugins/cache/",
)
PUBLIC_TEXT_SUFFIXES = {".json", ".md", ".py", ".txt", ".yaml", ".yml"}


def run_mdsmith(*args, stdin=None):
    return subprocess.run(
        (*MDSMITH, *args),
        cwd=ROOT,
        input=stdin,
        text=True,
        capture_output=True,
        timeout=60,
        check=False,
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
        self.assertIs(claude_manifest["defaultEnabled"], False)
        self.assertEqual(claude_manifest["metadata"]["supportStatus"], "deferred")

        codex_manifest = json.loads(
            (ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(codex_manifest["name"], "canonrail")
        self.assertEqual(codex_manifest["version"], version)
        self.assertEqual(codex_manifest["skills"], "./skills/")


    def test_codex_marketplace_exposes_the_root_plugin(self):
        marketplace = json.loads(
            (ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8")
        )
        self.assertEqual(marketplace["name"], "canonrail")
        self.assertEqual(marketplace["interface"]["displayName"], "CanonRail")
        self.assertEqual(len(marketplace["plugins"]), 1)

        plugin = marketplace["plugins"][0]
        self.assertEqual(plugin["name"], "canonrail")
        self.assertEqual(plugin["source"], {"source": "local", "path": "./"})
        self.assertEqual(
            plugin["policy"],
            {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        )
        self.assertEqual(plugin["category"], "Productivity")
        self.assertTrue((ROOT / plugin["source"]["path"] / ".codex-plugin/plugin.json").is_file())

    def test_readme_documents_verified_public_install_paths(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("hermes skills tap add Kayhusk/canonrail", readme)
        self.assertIn("hermes skills install Kayhusk/canonrail/canonrail", readme)
        self.assertIn("hermes skills check canonrail", readme)
        self.assertIn("codex plugin marketplace add Kayhusk/canonrail --ref main", readme)
        self.assertIn("codex plugin add canonrail@canonrail", readme)
        self.assertNotIn("### Claude Code", readme)

    def test_release_notes_match_the_two_host_scope(self):
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("## 0.1.0 - Unreleased", changelog)
        self.assertIn("Hermes Agent and Codex CLI", changelog)
        self.assertIn("Claude Code runtime support remains deferred", changelog)

    def test_portable_skill_trigger_is_specific_to_supported_documents(self):
        skill = (ROOT / "skills/canonrail/SKILL.md").read_text(encoding="utf-8")
        match = re.search(r"(?m)^description: (.+)$", skill)
        if match is None:
            self.fail("CanonRail skill description is missing")
        description = match.group(1)
        self.assertEqual(
            description,
            "Author/review AGENTS, READMEs, roadmaps, plans, and PRDs.",
        )
        self.assertLessEqual(len(description), 57)

    def test_portable_skill_handles_projects_without_mdsmith(self):
        skill = (ROOT / "skills/canonrail/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("If the project declares a document-kind command", skill)
        self.assertIn("If no document-kind command is configured", skill)
        self.assertNotIn("\nRun:\n\n```bash\nmdsmith kinds resolve <path>", skill)

    def test_portable_skill_separates_project_and_policy_roots(self):
        skill = (ROOT / "skills/canonrail/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Keep the project root separate from the loaded CanonRail skill", skill)
        self.assertIn("read the matching linked contract listed above", skill)
        self.assertIn("Load CanonRail contracts only through linked skill references", skill)
        self.assertIn("Do not search the project for CanonRail package files", skill)

    def test_portable_skill_bundles_each_contract_as_a_reference(self):
        contract_dir = ROOT / "skills/canonrail/references/contracts"
        missing = [
            name
            for name in CONTRACTS
            if not (contract_dir / f"{CONTRACT_FILES[name]}.md").is_file()
        ]
        self.assertEqual(missing, [])

    def test_each_contract_has_a_bounded_responsibility(self):
        required_headings = ("# ", "## Owns", "## Must not absorb", "## Review")
        for name in CONTRACTS:
            text = (
                ROOT
                / "skills/canonrail/references/contracts"
                / f"{CONTRACT_FILES[name]}.md"
            ).read_text(encoding="utf-8")
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

            result = run_mdsmith("check", "--no-color", "-", stdin=invalid)
            output = result.stdout + result.stderr
            self.assertEqual(result.returncode, 1, output)
            diagnostics = re.findall(r"(?m)^<stdin>:[0-9]+:[0-9]+ (MDS[0-9]+)", output)
            self.assertEqual(diagnostics, ["MDS020"], output)
            self.assertIn(missing[0], output)

    def test_mdsmith_config_maps_every_contract_kind(self):
        config = (ROOT / ".mdsmith.yml").read_text(encoding="utf-8")
        for name in CONTRACTS:
            self.assertRegex(config, rf"(?m)^  {re.escape(name)}:$")
        for path in ("AGENTS.md", "README.md", "PLAN.md", ".canonrail/plans/*.md", "docs/prd/**/*.md"):
            self.assertIn(path, config)

    def test_canonrail_pilot_resolves_only_selected_path_bindings(self):
        cases = (
            ("AGENTS.md", ["agents"]),
            ("README.md", ["readme"]),
            ("PLAN.md", ["roadmap"]),
            ("docs/research/foundation-sources.md", []),
        )
        for path, expected in cases:
            result = run_mdsmith("kinds", "resolve", path)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            kinds_section = result.stdout.split("effective kinds:\n", 1)[1].split("rules:\n", 1)[0]
            resolved = re.findall(r"(?m)^  - ([a-z0-9_-]+)", kinds_section)
            self.assertEqual(resolved, expected, path)

    def test_plan_has_a_complete_source_audit(self):
        plan = (ROOT / "PLAN.md").read_text(encoding="utf-8")
        evidence = (ROOT / "docs/research/foundation-sources.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("docs/research/foundation-sources.md", plan)
        for heading in ("## Status", "## Current phase", "## Next decision", "## Guardrails"):
            self.assertIn(heading, plan)
        for source_id in range(1, 19):
            self.assertIn(f"S{source_id:02d}", evidence)
        for heading in ("## Exact source wording", "## Foundation audit", "## Unsupported or deferred"):
            self.assertIn(heading, evidence)

    def test_hermes_skill_tap_package_is_self_contained(self):
        skill_root = ROOT / "skills/canonrail"
        skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        for name in CONTRACTS:
            self.assertIn(f"](references/contracts/{CONTRACT_FILES[name]}.md)", skill)
        referenced = re.findall(
            r"(?:\]\(|`)((?:references|templates|scripts|assets|examples)/[^\s)`]+)",
            skill,
        )
        self.assertTrue(referenced)
        self.assertEqual(
            [path for path in referenced if not (skill_root / path).is_file()],
            [],
        )
        self.assertFalse((ROOT / "plugin.yaml").exists())
        self.assertFalse((ROOT / "__init__.py").exists())

    def test_public_text_does_not_expose_private_project_jargon(self):
        listed = subprocess.run(
            ("git", "ls-files", "--cached", "--others", "--exclude-standard"),
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        public_files = [
            ROOT / relative
            for relative in listed.stdout.splitlines()
            if (ROOT / relative).suffix in PUBLIC_TEXT_SUFFIXES
            and "tests" not in (ROOT / relative).parts
        ]
        self.assertTrue(public_files)
        violations = []
        for path in public_files:
            text = path.read_text(encoding="utf-8")
            for fragment in FORBIDDEN_PUBLIC_FRAGMENTS:
                if fragment in text:
                    violations.append(f"{path.relative_to(ROOT)}: {fragment}")
        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main()
