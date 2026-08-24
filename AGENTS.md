# CanonRail project instructions

## Purpose

CanonRail is a documentation framework that is not tied to one agent harness.
It defines and validates contracts for project documents.
The Agent Skill and package manifests expose the same contracts without redefining them.

## Project sources

- `README.md` explains the project and ordinary use.
- `skills/canonrail/references/contracts/` defines each supported document contract.
- `.mdsmith.yml` maps file paths to document types and required sections.
- `skills/canonrail/SKILL.md` defines how compatible agent tools apply the contracts.
- Package manifests expose the Agent Skill without changing the contracts.

## Working rules

- Keep shared contracts free of product, client, profile, and machine-specific facts.
- Put project-specific facts in the project that maintains them.
- Add a document type only with a contract, path mapping, passing example, failing example, and focused test.
- Configure mdsmith instead of writing another Markdown parser or checker.
- Keep public writing plain, direct, and free of private process terms.
- Do not add hooks, daemons, MCP servers, generators, or publishing automation without a demonstrated need.

## Verification

Run both checks before declaring a change complete:

```bash
python -m unittest discover -s tests -v
npx --yes @mdsmith/cli@0.54.0 check .
```
