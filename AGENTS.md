# CanonRail project instructions

## Purpose

CanonRail is an agent-portable document governance framework. The policy pack owns document contracts. Host adapters only expose the same portable skill to their agent runtime.

## Project sources

- `README.md` is the human-facing introduction and usage guide.
- `skills/canonrail/references/contracts/` defines the semantic boundary for each document type.
- `.mdsmith.yml` maps paths to document kinds and deterministic schemas.
- `skills/canonrail/SKILL.md` defines the portable authoring and review workflow.
- Codex and Claude manifests plus the Hermes skill tap expose the portable skill without owning its policy.

## Working rules

- Keep the neutral policy free of product, client, profile, and machine-specific facts.
- Put project-specific truth in the project that owns it.
- Add a document kind only with a contract, path mapping, valid fixture, invalid fixture, and focused test.
- Prefer configuring mdsmith over writing another parser or validator.
- Keep user-facing writing plain, direct, and free of private process language.
- Do not add hooks, daemons, MCP servers, generators, or publishing automation without a demonstrated requirement.

## Verification

Run both checks before declaring a change complete:

```bash
python -m unittest discover -s tests -v
npx --yes @mdsmith/cli@0.54.0 check .
```
