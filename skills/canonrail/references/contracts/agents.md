# Agent instructions contract

Agent instruction files tell coding agents how to work in a project.
CanonRail keeps broad rules when source cannot reveal them and removing them could cause a specific mistake.

The sources support a dedicated agent entry point, short persistent rules, routing, host-defined precedence, and checks outside prose.

CanonRail defines the details below as local policy. This includes the owners, exclusions, review rules, and required headings.
Each host still owns its scope and precedence.
The [foundation source audit](../../../../docs/research/foundation-sources.md#agent-instructions-contract) records the line-level disposition.

## Owns

- Exact setup, build, test, and validation commands that differ from common defaults.
- Project-specific authority, safety boundaries, conventions, and protected paths that an agent cannot reliably infer.
- Short routing pointers to the current owners an agent must consult.
- Completion checks that apply broadly within the instruction file's host-defined scope.

## Must not absorb

- Agent identity, user preferences, credentials, or private profile context.
- Volatile task status, issue history, test receipts, or release chronology.
- File-by-file repository tours or facts visible in manifests and source.
- Full copies of architecture, plans, runbooks, or contribution guides.
- Vague or self-evident instructions that would not prevent a specific mistake.

## Review

- Verify every command and path against the current repository.
- If the active host supports nested instruction files, verify effective scope and precedence against that host's current rules.
- Remove duplicate explanations and changing status.
- Keep each pointer specific enough that an agent can tell when to follow it.
- Run the repository's declared document and project checks.
