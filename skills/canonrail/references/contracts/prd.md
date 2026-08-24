# Product requirements contract

A product requirements document states the user problem and desired outcomes.
It also defines scope and acceptance criteria.
It does not present implementation choices as settled decisions.

ISO/IEC/IEEE 29148 defines requirements information, but it does not require the name `PRD` or the sections below.
CanonRail chose this format for its product requirements contract.

## Include

- The problem and the people affected by it.
- User outcomes and evidence that would show improvement.
- Included and excluded scope.
- Product, legal, privacy, accessibility, and operational constraints.
- Acceptance criteria stated as behavior a reviewer can observe.

## Keep elsewhere

- Architecture or technology choices unless the requirement depends on them.
- Agent workflows, prompts, tool history, and review conversations.
- Invented metrics, deadlines, users, limits, and market claims.
- Task breakdowns that belong in tickets or an execution plan.
- Approval or launch status without a current project source.

## Review

- Trace every requirement to user evidence, a binding constraint, or an explicit project decision.
- Mark assumptions and unresolved questions.
- Measure user or product outcomes rather than file changes.
- Remove implementation details that do not constrain the product.
- Use one term for each concept throughout the document.
