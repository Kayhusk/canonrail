# CanonRail plan

## Status

Foundation reconciliation is active. The bounded CanonRail-only kind and path-binding pilot is locally verified. CanonRail still has no stable release or approved project rollout.

The exact external wording and current audit live in
[Foundation source audit](docs/research/foundation-sources.md).
That file is the evidence owner.
This plan links source IDs instead of copying quotations.

`PLAN.md` records approval of only the bounded pilot under `Next decision`. It does not approve plugin installation, project adoption, publication, or deployment.

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
| Agent instructions contract | Candidate retained       | S05, S07, S16 | Review every current bullet against the exact source and keep CanonRail-local rules labeled as local.                      |
| README contract             | Candidate retained       | S02, S05, S17 | Review every current bullet; do not present the current headings as a standard.                                            |
| Roadmap contract            | CanonRail-local contract | S01           | Retain the current semantics and headings as explicit local choices, not an external standard.                             |
| Execution plan contract     | Candidate retained       | S14           | Keep it as an OpenAI-derived profile, not a universal plan standard.                                                       |
| PRD contract                | CanonRail-local contract | S15           | Retain the current profile as a local choice for requirements information. Do not call `PRD` or its headings standardized. |
| Portable Agent Skill        | Candidate retained       | S06, S08, S11 | Keep the standards-compliant core free of host-only requirements.                                                          |
| Claude adapter              | Candidate retained       | S10, S11      | Validate against the current Claude plugin schema before release.                                                          |
| Codex adapter               | Candidate retained       | S08, S09      | Validate against the current Codex plugin schema before release.                                                           |
| Hermes adapter              | Candidate retained       | S12           | Keep it standalone and out of Hermes core.                                                                                 |
| mdsmith configuration       | Pinned pilot             | S13           | Use the current engine only for capabilities proven by a pinned execution.                                                 |
| Required CI check           | CanonRail decision       | S07, S13      | Keep one persisted deterministic gate for adopted projects.                                                                |
| Public wording policy       | Candidate retained       | S02, S17      | Keep public text clear, audience-aware, neutral, and free of private process language.                                     |

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
7. Validate the portable skill independently in Hermes, Claude Code, and Codex before release.
8. Consider a release only after adapter checks and public wording review pass.

Items 1 through 4 are locally verified. Items 5 through 8 remain pending.

## Next decision

The approved pilot is limited to this CanonRail corpus:

| Path                                  | Expected result            |
| ------------------------------------- | -------------------------- |
| `AGENTS.md`                           | exactly one `agents` kind  |
| `README.md`                           | exactly one `readme` kind  |
| `PLAN.md`                             | exactly one `roadmap` kind |
| `docs/research/foundation-sources.md` | no document-contract kind  |

Acceptance requires:

- every selected path to resolve to the expected result through mdsmith 0.54.0;
- every adjacent-invalid fixture to fail through `mdsmith check -` with MDS020 and the missing heading;
- the repository foundation test and Markdown check to pass;
- no topology artifact, parser, dependency, hook, installation, file move, publication, or project rollout.

The bounded pilot passed local acceptance. The next decision is whether a real document failure justifies one deferred relationship, order, or instruction-scope rule. No such rule is approved now.

## Guardrails

- Current project sources outrank generic CanonRail guidance.
- Exact quotations remain in the evidence owner; the plan does not paraphrase them into stronger claims.
- Formal standards, open formats, host documentation, first-party tool documentation, and CanonRail decisions remain visibly distinct.
- A passing schema proves configured structure, not truth, approval, completeness, or semantic quality.
- Host adapters package the portable core; they do not own shared policy.
- No unsupported piece is implemented to make the framework look complete.
- Public files do not expose private projects, profiles, paths, conversations, or internal review language.
- The roadmap is not execution authority.
