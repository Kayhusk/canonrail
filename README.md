# CanonRail

CanonRail applies versioned contracts to project documents across AI coding tools and CI.
It keeps each document focused on its audience and authority without tying the rules to one agent.

## What it does

- Classifies documents such as `AGENTS.md`, README, roadmaps, execution plans, and PRDs.
- Gives agents concise guidance for each document type.
- Uses deterministic checks for structure, links, paths, and declared fields.
- Leaves project-specific facts and exceptions in the project that owns them.

## How it works

CanonRail combines three parts:

1. Document contracts describe what each file owns and what belongs elsewhere.
2. A portable Agent Skill guides authoring and review.
3. [mdsmith](https://mdsmith.dev/) validates saved Markdown when a project adopts the supplied configuration pattern.

Hermes, Claude Code, and Codex adapters package the same skill. Project sources and configured repository checks remain authoritative.

## Current scope

This foundation defines contracts for:

- agent instructions;
- human-facing README files;
- project roadmaps;
- executable implementation plans;
- product requirements documents.

The contracts are deliberately small. New document types can be added without changing the validator or host adapters.

Hermes and Codex have completed local host validation.
The Claude Code adapter is disabled by default, and its runtime validation remains deferred.

- [Project plan](PLAN.md)
- [Foundation source audit](docs/research/foundation-sources.md)
- [Changelog](CHANGELOG.md)

## Install

Use a current Hermes Agent or Codex CLI release with plugin support.

### Hermes Agent

```bash
hermes plugins install Kayhusk/canonrail --enable
hermes plugins doctor canonrail --ci
```

Start a new Hermes session after enabling the plugin.

### Codex CLI

```bash
codex plugin marketplace add Kayhusk/canonrail --ref main
codex plugin add canonrail@canonrail
codex plugin list --marketplace canonrail --json
```

Start a new Codex session after installing the plugin.

## Use

Run CanonRail from the repository that owns the document. For example:

```text
Use CanonRail to review README.md as a human-facing README.
```

No project configuration is required for semantic review.
If the project declares a document-kind command or document check, CanonRail uses it.
Otherwise, CanonRail states that deterministic validation is not configured and continues with the semantic contract.

To verify this repository:

```bash
python -m unittest discover -s tests -v
npx --yes @mdsmith/cli@0.54.0 check .
```

CanonRail is at an early foundation stage. It has no stable release yet.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
