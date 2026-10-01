# Execution plan contract

An execution plan gives a reader enough current information to deliver one defined result and verify it.

OpenAI's ExecPlan recipe calls for a self-contained, current plan with independently verifiable milestones and observable behavior.
It also calls for exact commands and recovery steps.
CanonRail uses those ideas. The content and review rules below are CanonRail choices.
An execution plan does not grant permission to start work.

## Include

- One goal, the current context, and explicit exclusions.
- The design decisions and input/output contracts needed by the selected slice, with their current sources and decision state.
- Affected paths, work order, and dependencies.
- The inputs each milestone consumes, who supplies them, and which prerequisites are satisfied or unresolved.
- Acceptance criteria based on observable behavior.
- Exact validation commands and expected results.
- Recovery steps for partial or failed work.
- Compatibility and migration constraints when existing interfaces, stored data, or behavior change.
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
- Do not present dependent implementation as ready while a required decision is unresolved.
- Check relevant ownership, shared representations, control flow, states, and failure behavior against project sources. A folder outline alone is insufficient.
- Prefer verifiable end-to-end increments once their required contracts are defined. Separate enabling work only when a consumer actually needs it first.
- Separate requirements from implementation suggestions.
- Leave unresolved choices open instead of guessing.
- Make sure a new reader can resume from the plan and repository alone.
- Keep new-project unknowns explicit and preserve valid existing decisions when adapting a project.
