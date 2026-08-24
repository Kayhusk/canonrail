# CanonRail

<p align="center">
  <img src="assets/logo-mark.svg" width="112" alt="CanonRail logo">
</p>

CanonRail is a framework for project document contracts.
People and compatible agent tools can use the contracts.
Configured checks verify required sections.
They also verify file-to-document mappings.
Projects keep control of their own facts, decisions, paths, and approval rules.

## What it does

CanonRail keeps document contracts separate from project-owned facts, paths, and approval rules.

## How it works

Each contract states what belongs in a document and what belongs elsewhere.
Projects choose their files, path mappings, exceptions, and checks.
Configured checks verify required sections and file-to-document mappings against saved files locally or in CI.

This repository uses [mdsmith](https://mdsmith.dev/) for its current structure and path checks.
CanonRail installs or configures mdsmith in another project only when the user requests that setup.

## Current scope

CanonRail includes contracts for:

- [agent instructions](skills/canonrail/references/contracts/agent-instructions.md);
- [human-facing README files](skills/canonrail/references/contracts/readme.md);
- [project roadmaps](skills/canonrail/references/contracts/roadmap.md);
- [execution plans](skills/canonrail/references/contracts/execplan.md);
- [product requirements documents](skills/canonrail/references/contracts/prd.md).

CanonRail supports installation through a Hermes Agent skill tap and a Codex CLI plugin marketplace.
Claude Code is not supported in this version.
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
