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
3. [mdsmith](https://mdsmith.dev/) validates saved Markdown in local checks and CI.

Hermes, Claude Code, and Codex adapters package the same skill. The repository check remains the final authority.

## Current scope

This foundation defines contracts for:

- agent instructions;
- human-facing README files;
- project roadmaps;
- executable implementation plans;
- product requirements documents.

The contracts are deliberately small. New document types can be added without changing the validator or host adapters.

## Use

Run the local foundation tests:

```bash
python -m unittest discover -s tests -v
```

Run the pinned Markdown checks:

```bash
npx --yes @mdsmith/cli@0.54.0 check .
```

CanonRail is at an early foundation stage. It has no stable release yet.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
