# Execution plan contract

An execution plan gives a reader enough current information to deliver one defined result and verify it.

OpenAI's ExecPlan guidance calls for a self-contained, current plan with independently verifiable milestones and observable behavior.
It also calls for exact commands and recovery steps.
CanonRail uses those ideas. The content and review rules below are CanonRail choices.
An execution plan does not grant permission to start work.

## Include

- One goal, the current context, and explicit exclusions.
- Affected paths, work order, and dependencies.
- Acceptance criteria based on observable behavior.
- Exact validation commands and expected results.
- Recovery steps for partial or failed work.
- Current progress, discoveries, decisions, and outcomes needed to resume after a stop.

## Keep elsewhere

- Project-wide roadmap decisions and unrelated future work.
- Assumptions presented as settled architecture.
- Placeholder commands, paths, outputs, and test counts.
- Private conversation history. Record only resulting requirements or decisions that affect the work.
- Timeline details that do not affect the current work or its recovery.

## Review

- Confirm every path and command against the current repository.
- Make each milestone verifiable on its own.
- Separate requirements from implementation suggestions.
- Leave unresolved choices open instead of guessing.
- Make sure a new reader can resume from the plan and repository alone.
