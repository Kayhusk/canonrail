# Execution plan contract

An execution plan gives someone enough current information to complete one defined result and verify it.

OpenAI's ExecPlan guidance calls for a self-contained, current plan with independently verifiable milestones, visible behavior, exact commands, and recovery steps.
CanonRail uses those ideas, but this set of sections is its own choice.
An execution plan does not grant permission to start work.

## Include

- One goal, the current context, and explicit exclusions.
- Affected paths, work order, and dependencies.
- Acceptance criteria based on behavior a reviewer can observe.
- Exact validation commands and the results a reviewer should expect.
- Recovery steps for partial or failed work.
- Current progress, discoveries, decisions, and outcomes needed to resume after a stop.

## Keep elsewhere

- Project-wide roadmap decisions and unrelated future work.
- Assumptions presented as settled architecture.
- Placeholder commands, paths, outputs, and test counts.
- Private conversation history that does not change the work.
- Timeline details that do not change current progress, decisions, discoveries, outcomes, or recovery.

## Review

- Confirm every path and command against the current repository.
- Make each milestone verifiable on its own.
- Separate requirements from implementation suggestions.
- Leave unresolved choices open instead of guessing.
- Make sure a new reader can resume from the plan and repository alone.
