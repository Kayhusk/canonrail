# Execution plan contract

An execution plan gives a fresh implementer enough current context to deliver one bounded result and prove it works.

OpenAI's ExecPlan guidance says a plan must stay current and stand on its own.
It requires milestones that can be checked on their own.

The same guidance requires visible behavior, exact commands, current progress and decisions, and safe recovery.

CanonRail uses that guidance for this local profile. The contract and its required headings are not a universal plan standard.
The plan itself does not authorize execution.
The CanonRail foundation source audit records the line-level disposition.

## Owns

- One goal, its current context, and explicit exclusions.
- The affected paths, ordered work, and dependency sequence.
- Acceptance criteria based on observable behavior.
- Exact validation commands and expected evidence.
- Recovery guidance for partial or failed execution.
- Current progress, discoveries, decisions, and outcomes needed to resume after a stopping point.

## Must not absorb

- Project-wide roadmap authority or unrelated future work.
- Assumptions presented as settled architecture.
- Placeholder commands, paths, outputs, or test counts.
- Private conversation history that does not change implementation.
- Chronology that does not change current progress, decisions, discoveries, outcomes, or recovery.

## Review

- Confirm every path and command against the current repository.
- Make each milestone independently verifiable.
- Distinguish requirements from implementation suggestions.
- Preserve unresolved choices instead of guessing.
- Ensure a fresh reader can resume from the plan and repository alone.
