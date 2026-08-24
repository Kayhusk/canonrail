# Execution plan contract

An execution plan gives a fresh implementer enough current context to deliver one bounded result and prove it works.

## Owns

- One goal, its current context, and explicit exclusions.
- The affected paths, ordered work, and dependency sequence.
- Acceptance criteria based on observable behavior.
- Exact validation commands and expected evidence.
- Recovery guidance for partial or failed execution.

## Must not absorb

- Project-wide roadmap authority or unrelated future work.
- Assumptions presented as settled architecture.
- Placeholder commands, paths, outputs, or test counts.
- Private conversation history that does not change implementation.
- A progress diary when only current state and recovery matter.

## Review

- Confirm every path and command against the current repository.
- Make each milestone independently verifiable.
- Distinguish requirements from implementation suggestions.
- Preserve unresolved choices instead of guessing.
- Ensure a fresh reader can resume from the plan and repository alone.
