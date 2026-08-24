# CanonRail plan

## Status

Foundation reconciliation is active. CanonRail has a tested foundation, but it has no stable release and no approved project rollout.

The exact external wording and current audit live in
[Foundation source audit](docs/research/foundation-sources.md).
That file is the evidence owner.
This plan links source IDs instead of copying quotations.

`PLAN.md` orders decisions. It does not authorize implementation, plugin installation, project adoption, publication, or deployment.

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

| Piece                       | Status                   | Evidence      | Current decision                                                                                                                       |
| --------------------------- | ------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Agent instructions contract | Candidate retained       | S05, S07, S16 | Review every current bullet against the exact source and keep CanonRail-local rules labeled as local.                                  |
| README contract             | Candidate retained       | S02, S05, S17 | Review every current bullet; do not present the current headings as a standard.                                                        |
| Roadmap contract            | Provisional              | S01           | Keep `plan` as a supported information-item type. Treat the current roadmap semantics and headings as local until explicitly accepted. |
| Execution plan contract     | Candidate retained       | S14           | Keep it as an OpenAI-derived profile, not a universal plan standard.                                                                   |
| PRD contract                | Provisional and narrowed | S15           | Map it to requirements information. Do not claim that `PRD` or its current headings are standardized.                                  |
| Portable Agent Skill        | Candidate retained       | S06, S08, S11 | Keep the standards-compliant core free of host-only requirements.                                                                      |
| Claude adapter              | Candidate retained       | S10, S11      | Validate against the current Claude plugin schema before release.                                                                      |
| Codex adapter               | Candidate retained       | S08, S09      | Validate against the current Codex plugin schema before release.                                                                       |
| Hermes adapter              | Candidate retained       | S12           | Keep it standalone and out of Hermes core.                                                                                             |
| mdsmith configuration       | Pinned pilot             | S13           | Use the current engine only for capabilities proven by a pinned execution.                                                             |
| Required CI check           | CanonRail decision       | S07, S13      | Keep one persisted deterministic gate for adopted projects.                                                                            |
| Public wording policy       | Candidate retained       | S02, S17      | Keep public text clear, audience-aware, neutral, and free of private process language.                                                 |

### Document Topology Contracts

Document Topology Contracts are added to the roadmap as a research-backed feature proposal. They are not implemented by this plan entry.

The selected required fields are limited to the current evidence:

| Field                                  | Evidence      |
| -------------------------------------- | ------------- |
| `kind`                                 | S01, S03, S13 |
| `purpose`                              | S01           |
| `audience` or information need         | S02           |
| `relationships`                        | S03, S04      |
| `logical_order` when order matters     | S04           |
| `scope` for agent instructions         | S05           |
| `path_binding` selected by the project | S01, S03, S13 |

The feature separates logical topology from physical binding. A project can bind a kind to its own path or glob. CanonRail does not prescribe universal directories.

The following are explicitly excluded from this feature:

- organizing repositories on a user's machine;
- automatic file moves;
- universal `docs/`, `active/`, `archive/`, or project-category folders;
- a claim that directory order is document authority;
- universal topology fields not admitted by the current evidence audit.

The earlier observe-before-enforce rollout remains a proposed CanonRail safety choice. It is not presented as an ISO or OASIS requirement.

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

1. Reconcile the five current contracts line by line against the foundation audit.
2. Remove, narrow, or label every rule that lacks the required evidence chain.
3. Define valid and adjacent-invalid topology fixtures using only the selected topology fields.
4. Run a read-only topology pilot against one real repository layout.
5. Compare the pinned mdsmith result with the contract and record unexpressed requirements.
6. Validate the portable skill independently in Hermes, Claude Code, and Codex.
7. Decide whether host hooks add necessary early feedback without duplicating CI.
8. Consider a release only after the pilot, adapter checks, and public wording review pass.

## Next decision

Approve or revise the evidence-bounded topology pilot scope.

The proposed pilot proves only:

- document kind resolution;
- project-selected path binding;
- declared relationships and logical order;
- valid and adjacent-invalid fixture behavior;
- persisted deterministic validation.

The pilot does not install CanonRail into another profile or project.
It does not move files, enable hooks, publish a plugin, or claim standards conformance.

## Guardrails

- Current project sources outrank generic CanonRail guidance.
- Exact quotations remain in the evidence owner; the plan does not paraphrase them into stronger claims.
- Formal standards, open formats, host documentation, first-party tool documentation, and CanonRail decisions remain visibly distinct.
- A passing schema proves configured structure, not truth, approval, completeness, or semantic quality.
- Host adapters package the portable core; they do not own shared policy.
- No unsupported piece is implemented to make the framework look complete.
- Public files do not expose private projects, profiles, paths, conversations, or internal review language.
- The roadmap is not execution authority.
