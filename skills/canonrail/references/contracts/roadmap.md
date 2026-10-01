# Roadmap contract

A roadmap shows the current phase, distinguishes proposed from approved work, records deferred work and decisions, and names the approval or decision needed next.
Its presence does not grant permission to start implementation.

CanonRail chose the sections and review rules below.
They are not requirements of an external roadmap standard.

## Include

- The current phase.
- The immediate next action, separate from the first useful delivery milestone.
- Proposed and approved work, clearly distinguished and ordered by dependency.
- For each prerequisite, name the decision or artifact needed, its owner, and the evidence required to advance.
- Deferred work and decisions with their prerequisites.
- The approval or decision needed to advance, including any move from proposal to implementation.

## Keep elsewhere

- Step-by-step implementation instructions that belong in an execution plan.
- Architecture details already maintained in another document.
- Completion claims without current evidence.
- Old evidence that no longer affects the next decision.
- General permission to install, deploy, publish, or change production systems.

## Review

- Keep proposed, approved, implemented, and verified states distinct.
- Confirm that the next item follows the real dependencies rather than its position in a list.
- Put unresolved design decisions before the implementation that consumes them. Reuse satisfied prerequisites and do not block independent work.
- Require only foundations consumed by the selected delivery, not completion of every layer or future component.
- Check repeated next-step claims against this sequence. Report conflicts outside the authorized document scope.
- Remove stale status and repeated technical detail.
- State what the roadmap does not permit when a reader could mistake it for approval.
- Verify the current decision against project sources.
