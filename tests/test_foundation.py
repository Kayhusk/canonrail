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
PUBLIC_PROSE_FILES = (
    "AGENTS.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "PLAN.md",
    "README.md",
    ".agents/plugins/marketplace.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".github/workflows/ci.yml",
    ".mdsmith.yml",
    "skills/canonrail/SKILL.md",
    *(f"skills/canonrail/references/contracts/{CONTRACT_FILES[name]}.md" for name in CONTRACTS),
    *(f"fixtures/{name}/valid.md" for name in CONTRACTS),
    *(f"fixtures/{name}/invalid.md.txt" for name in CONTRACTS),
)
QUOTE_PROTECTED_PROSE_FILES = ("docs/research/foundation-sources.md",)
FORBIDDEN_PUBLIC_PHRASES = (
    "a testament to",
    "adjacent-invalid",
    "agent-portable",
    "at its core",
    "delve into",
    "deterministic validation",
    "document guide",
    "foundation source audit",
    "foundation stage",
    "host adapter",
    "host validation",
    "line-level disposition",
    "in order to",
    "it is important to note",
    "not just",
    "policy pack",
    "semantic review",
    "serves as",
    "setting the stage",
    "source-informed",
    "stands as",
)
FORBIDDEN_PROSE_CHARACTERS = {
    "\u00a0": "non-breaking space",
    "\u2013": "en dash",
    "\u2014": "em dash",
    "\u2018": "left single quotation mark",
    "\u2019": "right single quotation mark",
    "\u201c": "left double quotation mark",
    "\u201d": "right double quotation mark",
    "\u2026": "ellipsis",
}
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


def public_prose_violations(relative, text):
    violations = []
    lowered = text.lower()
    for phrase in FORBIDDEN_PUBLIC_PHRASES:
        if phrase in lowered:
            violations.append(f"{relative}: {phrase}")
    for character, name in FORBIDDEN_PROSE_CHARACTERS.items():
        if character in text:
            violations.append(f"{relative}: {name}")
    for character in sorted({character for character in text if not character.isascii()}):
        if character not in FORBIDDEN_PROSE_CHARACTERS:
            violations.append(f"{relative}: non-ASCII U+{ord(character):04X}")
    return violations


class CanonRailTests(unittest.TestCase):
    def test_required_project_files_exist(self):
        missing = [path for path in EXPECTED_FILES if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_versions_match_across_plugin_manifests(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")

        claude_manifest = json.loads(
            (ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        expected_description = (
            "Define and validate project-document contracts across tools and CI."
        )
        self.assertEqual(claude_manifest["name"], "canonrail")
        self.assertEqual(claude_manifest["version"], version)
        self.assertEqual(claude_manifest["description"], expected_description)
        self.assertIs(claude_manifest["defaultEnabled"], False)
        self.assertEqual(claude_manifest["metadata"]["supportStatus"], "deferred")

        codex_manifest = json.loads(
            (ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(codex_manifest["name"], "canonrail")
        self.assertEqual(codex_manifest["version"], version)
        self.assertEqual(codex_manifest["description"], expected_description)
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

    def test_readme_preserves_current_install_blocks(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        install_blocks = re.findall(
            r"(?ms)^### (Hermes Agent|Codex CLI)\n\n```bash\n(.*?)\n```",
            readme,
        )
        self.assertEqual(
            install_blocks,
            [
                (
                    "Hermes Agent",
                    "hermes skills tap add Kayhusk/canonrail\n"
                    "hermes skills install Kayhusk/canonrail/canonrail\n"
                    "hermes skills check canonrail",
                ),
                (
                    "Codex CLI",
                    "codex plugin marketplace add Kayhusk/canonrail --ref main\n"
                    "codex plugin add canonrail@canonrail\n"
                    "codex plugin list --marketplace canonrail --json",
                ),
            ],
        )
        self.assertNotIn("### Claude Code", readme)

    def test_public_positioning_is_not_tied_to_one_harness(self):
        statements = (
            "CanonRail is a documentation framework that is not tied to one agent harness.",
            "It defines and validates contracts for project documents.",
        )
        for relative in ("README.md", "AGENTS.md", "skills/canonrail/SKILL.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            for statement in statements:
                self.assertIn(statement, text, relative)

    def test_public_support_and_release_claims_match_owned_state(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn(f"## {version} - Unreleased", changelog)
        self.assertIn("Hermes Agent and Codex CLI", changelog)
        self.assertIn("Claude Code support is not available in this version", changelog)
        self.assertIn(f"Version {version} has not been released", changelog)

        self.assertIn(
            "The public install commands below have been tested with Hermes Agent and Codex CLI.",
            readme,
        )
        self.assertIn(
            "Claude Code is not supported yet. Its manifest is disabled while runtime testing remains deferred.",
            readme,
        )
        self.assertIn(
            f"CanonRail has no stable release. Installations from `main` may change before `v{version}` is released.",
            readme,
        )

    def test_skill_trigger_names_the_supported_documents(self):
        skill = (ROOT / "skills/canonrail/SKILL.md").read_text(encoding="utf-8")
        match = re.search(r"(?m)^description: (.+)$", skill)
        if match is None:
            self.fail("CanonRail skill description is missing")
        description = match.group(1)
        self.assertEqual(
            description,
            "Write/review AGENTS, READMEs, roadmaps, plans, and PRDs.",
        )
        self.assertLessEqual(len(description), 57)

    def test_skill_handles_projects_without_mdsmith(self):
        skill = (ROOT / "skills/canonrail/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("If the project provides a command that identifies document types", skill)
        self.assertIn("If the project has no such command", skill)
        self.assertIn("State that no automated type check is configured", skill)
        self.assertNotIn("\nRun:\n\n```bash\nmdsmith kinds resolve <path>", skill)

    def test_skill_separates_the_project_and_installation_roots(self):
        skill = (ROOT / "skills/canonrail/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Keep the project root separate from the installed CanonRail skill", skill)
        self.assertIn("Use the current tool's skill loader to open the matching linked contract", skill)
        self.assertIn("Open CanonRail contracts only through the linked skill references above", skill)
        self.assertIn("Do not search the project for CanonRail package files", skill)

    def test_skill_bundles_each_document_contract(self):
        contract_dir = ROOT / "skills/canonrail/references/contracts"
        missing = [
            name
            for name in CONTRACTS
            if not (contract_dir / f"{CONTRACT_FILES[name]}.md").is_file()
        ]
        self.assertEqual(missing, [])

    def test_each_contract_has_required_boundary_headings(self):
        required_headings = ("# ", "## Include", "## Keep elsewhere", "## Review")
        for name in CONTRACTS:
            text = (
                ROOT
                / "skills/canonrail/references/contracts"
                / f"{CONTRACT_FILES[name]}.md"
            ).read_text(encoding="utf-8")
            for heading in required_headings:
                self.assertIn(
                    heading,
                    text,
                    f"{CONTRACT_FILES[name]}.md is missing {heading}",
                )

    def test_each_document_type_has_passing_and_single_rule_failure_examples(self):
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

    def test_config_resolves_each_kind_and_one_unselected_path(self):
        cases = (
            ("AGENTS.md", ["agents"]),
            ("README.md", ["readme"]),
            ("PLAN.md", ["roadmap"]),
            ("fixtures/execplan/valid.md", ["execplan"]),
            ("fixtures/prd/valid.md", ["prd"]),
            ("docs/research/foundation-sources.md", []),
        )
        for path, expected in cases:
            result = run_mdsmith("kinds", "resolve", path)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            kinds_section = result.stdout.split("effective kinds:\n", 1)[1].split("rules:\n", 1)[0]
            resolved = re.findall(r"(?m)^  - ([a-z0-9_-]+)", kinds_section)
            self.assertEqual(resolved, expected, path)

    def test_plan_links_the_source_audit_and_required_sections(self):
        plan = (ROOT / "PLAN.md").read_text(encoding="utf-8")
        evidence = (ROOT / "docs/research/foundation-sources.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("docs/research/foundation-sources.md", plan)
        self.assertIn("There is no automatic release step", plan)
        self.assertIn("Any tag or GitHub release requires separate approval", plan)
        self.assertIn(
            "requires CI only when a project adopts automated CanonRail checks",
            evidence,
        )
        for heading in ("## Status", "## Current phase", "## Next decision", "## Guardrails"):
            self.assertIn(heading, plan)
        for source_id in range(1, 19):
            self.assertIn(f"S{source_id:02d}", evidence)
        for heading in ("## Exact source wording", "## Project decisions", "## Unsupported or deferred"):
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

    def test_public_text_does_not_expose_private_paths(self):
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

    def test_public_prose_avoids_known_filler_jargon_and_non_ascii_text(self):
        violations = []
        for relative in PUBLIC_PROSE_FILES:
            text = (ROOT / relative).read_text(encoding="utf-8")
            violations.extend(public_prose_violations(relative, text))
        for relative in QUOTE_PROTECTED_PROSE_FILES:
            text = (ROOT / relative).read_text(encoding="utf-8")
            authored_notes = "\n".join(
                line for line in text.splitlines() if not line.startswith(">")
            )
            violations.extend(public_prose_violations(relative, authored_notes))
        self.assertEqual(violations, [])

    def test_every_authored_markdown_surface_has_a_prose_check(self):
        listed = subprocess.run(
            ("git", "ls-files", "*.md", "*.txt"),
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        checked = {
            relative
            for relative in (*PUBLIC_PROSE_FILES, *QUOTE_PROTECTED_PROSE_FILES)
            if relative.endswith((".md", ".txt"))
        }
        unclassified = set(listed.stdout.splitlines()) - checked
        self.assertEqual(unclassified, set())

    def test_public_prose_check_rejects_nearby_bad_examples(self):
        cases = (
            ("It is important to note that checks pass.", "it is important to note"),
            ("Checks pass — continue.", "em dash"),
            ("Checks pass ✅", "non-ASCII U+2705"),
        )
        for text, expected in cases:
            violations = public_prose_violations("example.md", text)
            self.assertTrue(any(expected in violation for violation in violations), violations)


if __name__ == "__main__":
    unittest.main()
