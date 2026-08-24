# CanonRail plan

## Status

Foundation reconciliation is active. The bounded pilot, five current document contracts, public install paths, and consumer behavior in Hermes and Codex are locally verified.
Claude Code runtime validation remains deferred, and its adapter is disabled by default. CanonRail still has no stable release or approved project rollout.

The exact external wording and current audit live in
[Foundation source audit](docs/research/foundation-sources.md).
That file is the evidence owner.
This plan links source IDs instead of copying quotations.

`PLAN.md` records current decisions and test status.

Publication of this foundation candidate to the project repository is approved.
It does not approve a stable release, downstream project adoption, or deployment.

## Current phase

The current phase is to reduce the existing foundation to pieces with a complete evidence chain.

CanonRail's selected objective is:

> Package document guidance as a portable Agent Skill.
> Use thin host adapters and project-selected checks.

The objective has this evidence chain:

- S01 and S02 support information-item types and audience needs.
- S06 supports the open skill format.
- S08 supports the skill and plugin split.
- S09 through S12 support the host adapters.
- S13 supports the current validator mechanism.

The project source remains authoritative for project facts, selected document types,
paths, terminology, and approval.
CanonRail supplies reusable contracts and checks.
It does not become the source of project truth.

### Foundation disposition

| Piece                       | Status                   | Evidence      | Current decision                                                                                                           |
| --------------------------- | ------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Agent instructions contract | Source-informed contract | S05, S07, S16 | Retain the source-backed core and label the detailed ownership, exclusions, review rules, and headings as CanonRail-local. |
| README contract             | Source-informed contract | S02, S05, S17 | Retain human orientation, quick starts, audience needs, and clear writing; label the detailed profile as CanonRail-local.  |
| Roadmap contract            | CanonRail-local contract | S01           | Retain the current semantics and headings as explicit local choices, not an external standard.                             |
| Execution plan contract     | OpenAI-derived contract  | S14           | Retain the living-plan requirements and label the headings and execution-authority boundary as CanonRail-local.            |
| PRD contract                | CanonRail-local contract | S15           | Retain the current profile as a local choice for requirements information. Do not call `PRD` or its headings standardized. |
| Portable Agent Skill        | Consumer verified        | S06, S08, S11 | Hermes and Codex loaded linked contracts from the installed skill while reviewing a separate consumer repository.          |
| Claude adapter              | Disabled and deferred    | S10, S11      | Keep the valid package disabled by default and do not call it host-verified without an authenticated Claude Code run.      |
| Codex adapter               | Host verified            | S08, S09      | Codex installed the root package through its repository marketplace and completed a read-only consumer review.             |
| Hermes adapter              | Host verified            | S12           | Hermes passed Plugin Doctor and loaded linked contract references in an isolated consumer-review profile.                  |
| mdsmith configuration       | Pinned pilot             | S13           | Use the current engine only for capabilities proven by a pinned execution.                                                 |
| Required CI check           | CanonRail decision       | S07, S13      | Keep one persisted deterministic gate for adopted projects.                                                                |
| Public wording policy       | Locally verified         | S02, S17      | Keep public text neutral and enforce the private-term check across publishable text files.                                 |

### Bounded kind and path-binding pilot

Document Topology Contracts remain a research proposal.
The approved pilot adds no topology file, schema, parser, or runtime.
It reuses `.mdsmith.yml` and the pinned mdsmith CLI to prove current kind resolution and path binding.

| Concern                         | Source basis  | Pilot treatment                                                                            |
| ------------------------------- | ------------- | ------------------------------------------------------------------------------------------ |
| `kind`                          | S01, S03, S13 | Resolve one expected primary kind for each selected path.                                  |
| project-selected `path_binding` | S13           | Use the existing `kind-assignment` globs.                                                  |
| purpose                         | S01           | Keep in the semantic document contracts. Do not duplicate it as a machine field.           |
| audience or information need    | S02           | Keep in the semantic document contracts. Do not duplicate it as a machine field.           |
| relationships                   | S03, S04      | Treat as domain-specific precedent and defer a CanonRail field.                            |
| `logical_order`                 | S04           | Defer until a real case defines identity, cardinality, and invalid order.                  |
| instruction `scope`             | S05           | Defer cross-host enforcement; the open format does not define one universal host behavior. |

This classification is a CanonRail decision informed by the cited sources. No source requires the combined field set as a universal document-topology schema.

The pilot does not read or change other repositories.
It does not move files, prescribe directories, infer authority from directory order, or add broader topology fields.

## Evidence gate

No new objective, contract, field, adapter, hook, dependency, or enforcement claim advances without:

1. the current owning source;
2. exact source wording in `docs/research/foundation-sources.md`;
3. a supported claim and an explicit limitation;
4. the smallest CanonRail adaptation;
5. a valid fixture and adjacent-invalid fixture;
6. a deterministic or observable acceptance check.

A user-selected CanonRail rule can remain a local product decision.
It must be labeled as local and must not be attributed to an external standard.

## Work order

1. Prove that every adjacent-invalid fixture fails through the pinned public mdsmith command.
2. Record the enforced roadmap and PRD profiles as CanonRail-local decisions.
3. Freeze the CanonRail pilot corpus and adjacent non-trigger.
4. Prove current kind resolution and project-selected path binding without adding a topology artifact.
5. Reconcile the remaining current contract bullets before proposing broader semantic enforcement.
6. Consider relationships, logical order, or instruction scope only after a real case defines deterministic semantics and adjacent-invalid behavior.
7. Validate the portable skill independently in Hermes and Codex for the `0.1.0` release scope.
8. Prepare a private `0.1.0` release candidate after host checks and public wording review pass.

Items 1 through 5 and item 7 are locally verified.
Item 6 remains deferred. Item 8 is active.

## Next decision

The portable skill passed representative matching and adjacent non-trigger cases in:

- an isolated Hermes profile using linked contract references;
- Codex using the repository marketplace from a separate consumer repository.

Public Hermes and Codex install instructions and the repository Codex marketplace are locally verified. This does not create a stable release.

Claude Code runtime validation remains deferred. For the `0.1.0` release candidate:

- the Claude adapter remains disabled by default and is not host-verified;
- no relationship, order, scope, hook, installation rollout, or project adoption work is approved.

The next decision is acceptance of a private, immutable `0.1.0` candidate for Hermes and Codex.
Repository visibility changes only after that candidate is functional, proven, documented, and ready to ship.

## Guardrails

- Current project sources outrank generic CanonRail guidance.
- Exact quotations remain in the evidence owner; the plan does not paraphrase them into stronger claims.
- Formal standards, open formats, host documentation, first-party tool documentation, and CanonRail decisions remain visibly distinct.
- A passing schema proves configured structure, not truth, approval, completeness, or semantic quality.
- Host adapters package the portable core; they do not own shared policy.
- No unsupported piece is implemented to make the framework look complete.
- Public files do not expose private projects, profiles, paths, conversations, or internal review language.
- The roadmap is not execution authority.
