# CanonRail

CanonRail is a documentation framework that is not tied to one agent harness.
It defines and validates contracts for project documents.
Projects keep control of their own facts, decisions, paths, and approval rules.

## What it does

- Defines one contract for each supported document type.
- Makes the same contracts available to compatible agent tools through one Agent Skill.
- Checks required sections and file-to-document mappings when a project configures them.
- Uses repository checks and CI to validate saved files.

## How it works

1. Each contract states what belongs in a document, what belongs elsewhere, and what to review.
2. The CanonRail Agent Skill lets compatible tools apply those contracts without changing them.
3. Each project chooses its own files, path mappings, exceptions, and checks.
4. People, agent tools, and CI can run the same repository checks against saved files.

This repository uses [mdsmith](https://mdsmith.dev/) for its current structure and path checks.
CanonRail does not install mdsmith or add configuration to another project unless that setup work is explicitly selected.

## Current scope

CanonRail includes contracts for:

- [agent instructions](skills/canonrail/references/contracts/agent-instructions.md);
- [human-facing README files](skills/canonrail/references/contracts/readme.md);
- [project roadmaps](skills/canonrail/references/contracts/roadmap.md);
- [execution plans](skills/canonrail/references/contracts/execplan.md);
- [product requirements documents](skills/canonrail/references/contracts/prd.md).

The public install commands below have been tested with Hermes Agent and Codex CLI.
Claude Code is not supported yet. Its manifest is disabled while runtime testing remains deferred.
CanonRail has no stable release. Installations from `main` may change before `v0.1.0` is released.

Project information:

- [Roadmap](PLAN.md)
- [Sources behind the document contracts](docs/research/foundation-sources.md)
- [Changelog](CHANGELOG.md)

## Install

These commands require Agent Skill support in Hermes Agent or Codex CLI.

### Hermes Agent

```bash
hermes skills tap add Kayhusk/canonrail
hermes skills install Kayhusk/canonrail/canonrail
hermes skills check canonrail
```

Start a new Hermes session after installing the skill.

### Codex CLI

```bash
codex plugin marketplace add Kayhusk/canonrail --ref main
codex plugin add canonrail@canonrail
codex plugin list --marketplace canonrail --json
```

Start a new Codex session after installing the plugin.

## Use

People can use the linked contracts directly.
In a compatible agent tool, run the CanonRail skill from the repository that contains the document. For example:

```text
Use CanonRail to review README.md as a human-facing README.
```

You do not need CanonRail configuration for a document review.
If the project provides a document check, CanonRail runs it.
If not, CanonRail states that no automated document check is configured and reviews the file against the matching contract.

For repository checks, see [Contributing](CONTRIBUTING.md).

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
