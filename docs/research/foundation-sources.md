# CanonRail foundation source audit

This file owns the external evidence for CanonRail's objective, document contracts, portable skill, host adapters, validator, CI boundary, and proposed document topology feature.

It preserves exact source wording. The notes after each quotation state only what that wording supports and what it leaves to CanonRail or an adopting project.

## Exact source wording

### S01 - ISO/IEC/IEEE 15289:2019

**Source class:** Active IEEE/ISO/IEC standard catalog entry.

**Source:** <https://standards.ieee.org/ieee/15289/7196/>

> The information item contents are defined according to generic document types (description, plan, policy, procedure, report, request, and specification) and the specific purpose of the document.

> Information items may be combined or subdivided as needed for project or organizational purposes.

**Supports:** Document kinds based on type and purpose. Project or organization tailoring can combine or split information items.

**Does not decide:** CanonRail filenames, directories, headings, ownership fields, lifecycle values, or approval rules.

### S02 - ISO/IEC/IEEE 26514:2022

**Source class:** Published international standard catalog entry.

**Source:** <https://www.iso.org/standard/77451.html>

> This document covers the development process for designers and developers of information for users of software. It describes how to establish what information users need, how to determine the way in which that information should be presented, and how to prepare the information and make it available.

> This document provides requirements for the structure, information content, and format of information for users of software.

**Supports:** Audience needs, presentation, structure, content, format, and maintenance as concerns for user-facing information.

**Does not decide:** A universal README template, directory tree, or CanonRail wording rule.

### S03 - ISO/IEC/IEEE 42010:2022

**Source class:** Published international standard catalog entry.

**Source:** <https://www.iso.org/standard/74393.html>

> This document specifies requirements for an architecture description framework (ADF), an architecture description language (ADL), architecture viewpoints and model kinds in order to usefully support the development and use of an AD.

> This document does not specify any format or media for recording an AD.

**Supports:** Architecture descriptions can use explicit viewpoints and model kinds. The description is distinct from the format or medium used to record it.

**Does not decide:** How CanonRail should organize non-architecture documents or which Markdown files are authoritative in a project.

### S04 - OASIS DITA 1.3 map

**Source class:** OASIS Standards Track work product.

**Source:** <https://docs.oasis-open.org/dita/dita/v1.3/os/part1-base/langRef/base/map.html>

> Maps consist of references to topics, maps, and other resources organized into hierarchies, groups, and tables. Maps express these relationships in a single common format that can be used for different outputs.

> Ordered. Child topics can be labeled as having an ordered relationship, which means they are referenced in a definite sequence.

**Supports:** Logical relationships and order can be declared separately from the content resources themselves.

**Does not decide:** That CanonRail should use DITA XML, DITA elements, or DITA file placement.

### S05 - AGENTS.md open format

**Source class:** Open format stewarded by the Agentic AI Foundation.

**Source:** <https://agents.md/>

> Think of AGENTS.md as a README for agents: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project.

> README.md files are for humans: quick starts, project descriptions, and contribution guidelines.

> The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything.

**Supports:** Separate human and agent entry points, nested instruction scope, and more-specific local guidance.

**Does not decide:** CanonRail's full AGENTS contract, exact sections, or behavior in hosts whose discovery rules differ.

### S06 - Agent Skills specification

**Source class:** Open Agent Skills format specification.

**Source:** <https://agentskills.io/specification>

> The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

The same specification lists `SKILL.md` as required and `scripts/`, `references/`, and `assets/` as optional directories.

**Supports:** A portable CanonRail skill with Markdown instructions and optional support files.

**Does not decide:** Installation paths, host invocation behavior, tools, or plugin packaging.

### S07 - OpenAI Codex customization

**Source class:** Current OpenAI product documentation.

**Source:** <https://learn.chatgpt.com/docs/customization/overview>

> `AGENTS.md` gives Codex durable project guidance that travels with your repository and applies before the agent starts work. Keep it small.

> If it finds the right files but reads too many documents, add routing guidance (which directories/files to prioritize).

> Pair `AGENTS.md` with infrastructure that enforces those rules: pre-commit hooks, linters, and type checkers catch issues before you see them, so the system gets smarter about preventing recurring mistakes.

The same page lists build and test commands, review expectations, repository-specific conventions, and directory-specific instructions as suitable repository guidance.

**Supports:** Concise persistent project rules, exact commands, review expectations, routing guidance, directory-specific instructions, and deterministic enforcement outside prose.

**Does not decide:** CanonRail's detailed exclusions, that CI is the only authority, that hooks are mandatory, or that mdsmith is the required validator.

### S08 - OpenAI skills and plugins

**Source class:** Current OpenAI product documentation.

**Source:** <https://learn.chatgpt.com/docs/build-skills>

> Skills are the authoring format for reusable workflows. Plugins distribute reusable skills and connectors through the universal plugin directory shared by ChatGPT and Codex.

**Supports:** CanonRail can keep its reusable workflow in a skill and distribute it through a plugin adapter.

**Does not decide:** Claude or Hermes plugin structure, one universal marketplace, or cross-host behavioral parity.

### S09 - OpenAI plugin packaging

**Source class:** Current OpenAI plugin documentation.

**Source:** <https://developers.openai.com/plugins/build/plugins>

> Packaging gives the plugin a stable identity and tells ChatGPT and Codex which skills, MCP server connections, and other resources belong together.

**Supports:** A Codex adapter can package CanonRail's skill and related resources under one stable plugin identity.

**Does not decide:** That CanonRail needs MCP, hooks, assets, or a public plugin listing.

### S10 - Claude Code plugins

**Source class:** Current Anthropic product documentation.

**Source:** <https://code.claude.com/docs/en/plugins>

> Plugins let you extend Claude Code with custom functionality that can be shared across projects and teams.

The same page describes plugins as self-contained directories with skills, agents, hooks, or a `.claude-plugin/plugin.json` manifest for sharing, distribution, versioned releases, and reuse across projects.

**Supports:** A Claude adapter can package CanonRail for reuse across projects and teams.

**Does not decide:** Other host adapters or whether CanonRail needs hooks, agents, or MCP.

### S11 - Claude Code skills

**Source class:** Current Anthropic product documentation.

**Source:** <https://code.claude.com/docs/en/skills>

> Claude Code skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools.

**Supports:** The same standards-compliant CanonRail skill can be consumed by Claude Code and other compatible tools.

**Does not decide:** Identical discovery, tool permissions, or invocation semantics across those tools.

### S12 - Hermes plugins

**Source class:** Current Nous Research Hermes Agent documentation.

**Source:** <https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins>

> Hermes has a plugin system for adding custom tools, hooks, and integrations without modifying core code.

> Bundle skills | `ctx.register_skill(name, path)` — namespaced as `plugin:skill`, loaded via `skill_view("plugin:skill")`

**Supports:** A standalone Hermes adapter can register the portable CanonRail skill without changing Hermes core.

**Does not decide:** CanonRail's policy, contract contents, or automatic plugin activation.

### S13 - mdsmith file kinds and schemas

**Source class:** First-party validator documentation.

**Source:** <https://mdsmith.dev/features/file-kinds-schemas/>

> A kind gives each file a role; a schema gives that role a contract.

> Bind files to a kind by a front-matter `kinds:` field or a `kind-assignment` glob.

**Supports:** CanonRail's current deterministic mapping from file paths to document kinds and schemas.

**Does not decide:** Semantic truth, project authority, whether mdsmith remains the long-term engine, or the contract wording.

### S14 - OpenAI ExecPlans

**Source class:** First-party OpenAI Cookbook article. It presents one approach, not an open standard.

**Source:** <https://raw.githubusercontent.com/openai/openai-cookbook/main/articles/codex_exec_plans.md>

> Every ExecPlan must be fully self-contained. Self-contained means that in its current form it contains all knowledge and instructions needed for a novice to succeed.

> Every ExecPlan is a living document. Contributors are required to revise it as progress is made, as discoveries occur, and as design decisions are finalized. Each revision must remain fully self-contained.

> Every ExecPlan must produce a demonstrably working behavior, not merely code changes to "meet a definition".

> Each milestone must be independently verifiable and incrementally implement the overall goal of the execution plan.

> State the exact commands to run and where to run them (working directory). When a command generates output, show a short expected transcript so the reader can compare.

> If steps can be repeated safely, say so. If a step is risky, provide a safe retry or rollback path. Keep the environment clean after completion.

**Supports:** CanonRail's execution-plan contract can require self-contained context, current progress and decisions, ordered and independently verifiable milestones, exact validation, observable behavior, and recovery guidance.

**Does not decide:** A universal execution-plan format, CanonRail's required headings, roadmap semantics, or authority to execute a plan.

### S15 - ISO/IEC/IEEE 29148:2018

**Source class:** Current published international standard catalog entry. A replacement is under development.

**Source:** <https://www.iso.org/standard/72089.html>

> — specifies the required information items produced through the implementation of the requirements processes;

> — specifies the required contents of the required information items;

**Supports:** CanonRail can treat requirements information as a distinct information-item class.

**Does not decide:** The term PRD, CanonRail's PRD headings, product-management workflow, prioritization, or approval state.

### S16 - Anthropic Claude Code best practices

**Source class:** Current Anthropic product guidance.

**Source:** <https://code.claude.com/docs/en/best-practices>

> CLAUDE.md is a special file that Claude reads at the start of every conversation. Include Bash commands, code style, and workflow rules. This gives Claude persistent context it can't infer from code alone.

> Keep it concise. For each line, ask: *"Would removing this cause Claude to make mistakes?"* If not, cut it.

The same page says to exclude information that source can reveal, frequently changing information, and file-by-file codebase descriptions. It recommends links instead of copied detailed documentation.

**Supports:** Keep persistent instructions small, broad, non-inferable, and specific enough to prevent mistakes. Exclude volatile status, repository tours, and copied specialist documentation.

**Does not decide:** CanonRail's exact prose rules, AGENTS.md behavior, a mandatory hook architecture, or behavior in non-Claude hosts.

### S17 - Google developer documentation style guide

**Source class:** First-party public developer documentation guidance.

**Sources:** <https://developers.google.com/style/tone> and <https://developers.google.com/style>

> But remember that the primary purpose of the document is to provide information to someone who's looking for it and may be in a hurry.

> Even if you're having trouble hitting the right tone, make sure you're communicating useful information in a clear and direct way; that's the most important part.

> This guide contains guidelines, not rules. Depart from it when doing so improves your content.

**Supports:** Clear, direct, useful public technical writing with audience needs and project judgment taking precedence over generic style advice.

**Does not decide:** CanonRail's full wording policy, README sections, required quick-start shape, or an automated semantic gate.

### S18 - Hermes custom skill taps

**Source class:** Current Nous Research Hermes Agent documentation.

**Source:** <https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills>

> Add your repo as a tap:

> `hermes skills tap add owner/repo`

> Users can then search and install from your repository.

The same documentation defines `skills/<skill-name>/SKILL.md` with optional `references/` as the portable skill package layout.

**Supports:** CanonRail can distribute its self-contained skill and linked contracts through a custom Hermes skill tap.

**Does not decide:** CanonRail's contracts, project adoption, automatic installation, or a need for a Hermes plugin when no tools or hooks are present.

## Foundation audit

| CanonRail piece | Evidence | Decision | Limitation |
|---|---|---|---|
| Objective: typed project-document guidance | S01, S02, S05, S15 | Retain, narrowed | CanonRail defines a reusable governance method; projects still own their facts and selected document set. |
| Human README and agent instructions are separate | S05, S16, S17 | Retain | The current detailed contract bullets remain CanonRail rules, not requirements of the open format. |
| Portable Agent Skill | S06, S08, S11, S18 | Retain | Portability covers the format, not identical discovery or execution in every host. |
| Plugin distribution | S08, S09, S10 | Retain for Codex and deferred Claude packaging | A plugin is a host distribution form, not CanonRail's neutral policy owner. |
| Hermes skill distribution | S06, S18 | Retain as a custom skill tap | CanonRail has no Hermes tools or hooks, so a plugin would add an unnecessary install and scan boundary. |
| Deterministic validation | S07, S13, S16 | Retain | The validator proves configured structure and paths, not semantic truth. |
| mdsmith as the current engine | S13 | Retain as a pinned pilot dependency | Do not present mdsmith as a formal standard or permanent architectural dependency. |
| Agent-instructions contract | S05, S07, S16 | Retain as a source-informed CanonRail profile | The dedicated entry point, concise persistent guidance, routing, host-defined scope, and deterministic checks are source-backed. Detailed ownership and exclusions are local. |
| README contract | S02, S05, S17 | Retain as a source-informed CanonRail profile | Human orientation, quick starts, audience needs, and clear public writing are source-backed. Detailed ownership, exclusions, review rules, and headings are local. |
| Roadmap contract | S01 | Retain as a CanonRail-local profile | `plan` is a standard information-item type; the headings and authority language are explicit local CanonRail rules. |
| Execution-plan contract | S14 | Retain as an OpenAI-derived CanonRail profile | Self-contained living context, observable behavior, milestones, exact validation, progress, decisions, and recovery are OpenAI-derived. The headings and authority boundary are local. |
| PRD contract | S15 | Retain as a CanonRail-local profile | Requirements information is supported; `PRD` and the current headings are explicit local CanonRail choices. |
| Document Topology Contracts | S01, S02, S03, S04, S05, S13 | Narrow to a kind and path-binding pilot | The pilot reuses mdsmith mechanisms. No source requires a combined universal topology field set. |
| CI as the persisted deterministic gate | S07, S13 | Retain as a CanonRail decision | The sources support enforcement infrastructure; CanonRail selects required CI for reproducible project adoption. |
| Plain public writing | S02, S17 | Retain | Unslop is an authoring method used during review, not a public CanonRail dependency or formal standard. |

## Line-level contract reconciliation

`Source-backed` means the cited wording supports the concern, not the exact CanonRail sentence.
`CanonRail-local` means CanonRail deliberately retains the rule without attributing it to an external standard or format.
`Narrow` and `remove` identify changes from the previous contract text.

### Agent instructions contract

| Rule | Disposition | Basis and boundary |
| --- | --- | --- |
| Definition of agent instructions | Narrow - source-backed with a CanonRail adaptation | S05 and S07 support persistent project context and instructions. S16 supports the non-inferable, mistake-prevention test. |
| Required contract headings | Retain - CanonRail-local | No cited source requires `Owns`, `Must not absorb`, or `Review`. |
| Exact setup, build, test, and validation commands | Retain - source-backed | S05, S07, and S16 name build, test, and non-inferable commands as suitable agent guidance. |
| Project authority, safety boundaries, conventions, and protected paths | Retain - CanonRail-local | S05 and S07 support project conventions and context. CanonRail selects the full category list and the reliability test. |
| Routing pointers to current owners | Retain - source-backed | S07 explicitly recommends routing guidance when agents read too broadly. CanonRail requires pointers only where an owner must be consulted. |
| Completion checks within instruction scope | Narrow - source-backed with a CanonRail adaptation | S05 and S07 support checks and local precedence. The contract now defers scope to the active host instead of claiming one directory rule for every host. |
| Exclude identity, preferences, credentials, and private profile context | Retain - CanonRail-local | OpenAI separates global personal guidance from repository guidance, but the full exclusion list is CanonRail safety policy. |
| Exclude volatile status and chronology | Retain - source-backed | S16 excludes frequently changing information. CanonRail lists task status, issue history, receipts, and release chronology as examples. |
| Exclude repository tours and inferable facts | Retain - source-backed | S16 excludes file-by-file descriptions and information available from source. |
| Exclude copied specialist documents | Retain - source-backed with local examples | S16 recommends linking to detailed documentation. CanonRail names architecture, plans, runbooks, and contribution guides. |
| Exclude vague instructions | Narrow - source-backed | S16's removal test supports keeping only instructions that prevent a mistake. The revised line drops the broader observable-behavior claim. |
| Verify commands and paths | Retain - CanonRail-local | Current repository readback is CanonRail's admission rule, not an external format requirement. |
| Review nested instruction files | Narrow - source-backed | S05 supports nearest-file precedence for AGENTS.md. The revised rule requires checking the active host and does not claim cross-host parity or forbid host-defined overrides. |
| Remove duplicate explanations and changing status | Retain - source-backed | S16 supports concise persistent guidance and excludes changing information. |
| Keep routing pointers specific | Retain - source-backed with a CanonRail adaptation | S07 supports routing and S16 warns against ambiguous guidance. CanonRail defines the followability test. |
| Run declared document and project checks | Retain - source-backed with a CanonRail adaptation | S07 supports deterministic enforcement outside prose. The repository selects the actual checks. |

### README contract

| Rule | Disposition | Basis and boundary |
| --- | --- | --- |
| Definition of a README | Narrow - source-backed | S05 names project descriptions, quick starts, and contribution guidelines as human README concerns. The previous generic evaluation claim was removed. |
| Required contract headings | Retain - CanonRail-local | S02 and S05 do not prescribe CanonRail's `Owns`, `Must not absorb`, or `Review` headings. |
| Project purpose and intended users | Retain - source-backed | S05 supports project descriptions. S02 supports identifying user information needs. |
| Setup for ordinary use | Narrow - source-backed with a CanonRail adaptation | S05 supports quick starts. CanonRail now limits setup guidance to the primary supported use. |
| Shortest useful example or first check | Narrow - source-backed with a CanonRail adaptation | S05 supports a quick start but does not require one universal form. The contract now allows an installation step, example, or first check as appropriate. |
| Public limitations that affect adoption | Retain - CanonRail-local | S02 supports user information needs, but CanonRail selects adoption-relevant limitations as README content. |
| Links to architecture, contribution, security, and support owners | Narrow - CanonRail-local | S05 supports contribution guidance. CanonRail broadens the owner to deeper documentation and requires specialist links only when they exist. |
| Exclude full architecture and implementation history | Retain - CanonRail-local | This keeps the human entry point bounded. No cited source defines the exact exclusion. |
| Exclude task state, private review language, and agent workflow | Retain - source-informed CanonRail policy | S05 separates human and agent entry points. S16 supports excluding volatile information. The detailed list is local. |
| Exclude internal paths, accounts, credentials, and unpublished evidence | Retain - CanonRail-local | This is a public-information and safety boundary, not an external README standard. |
| Exclude duplicated linked explanations | Retain - CanonRail-local | S17 supports clear, useful writing. CanonRail selects single ownership instead of repetition. |
| Exclude unproved quality and readiness claims | Retain - CanonRail-local | CanonRail requires current proof for strong public claims. The cited sources do not define this list. |
| Read as a new user | Retain - source-backed with a CanonRail method | S02 supports designing around user information needs. CanonRail chooses the no-history review perspective. |
| Verify commands, links, versions, and claims | Retain - CanonRail-local | Current readback is CanonRail's admission rule. |
| Put the common path first | Retain - CanonRail-local | S02 supports audience-aware presentation. CanonRail selects common-path-first ordering. |
| Remove filler, promotion, and generic prose | Retain - source-backed with a CanonRail adaptation | S17 supports clear, direct, useful writing. CanonRail names the concrete rejection cases. |
| First example exercises a supported path | Narrow - CanonRail-local | The new rule verifies every command or runnable example without requiring every README to contain one. |

### Execution plan contract

| Rule | Disposition | Basis and boundary |
| --- | --- | --- |
| Definition of an execution plan | Retain - source-backed | S14 requires a self-contained plan that a novice can follow to working behavior. CanonRail narrows the plan to one bounded result. |
| Required contract headings | Retain - CanonRail-local | S14 provides one customizable profile and does not require CanonRail's five headings. |
| Plan presence does not authorize execution | Add - CanonRail-local | S14 describes an implementation method, not project authority. CanonRail makes the authority boundary explicit. |
| One goal, current context, and exclusions | Retain - source-backed with a CanonRail adaptation | S14 supports purpose and complete current context. One bounded goal and explicit exclusions are CanonRail choices. |
| Affected paths, ordered work, and dependencies | Retain - source-backed | S14 requires concrete file locations, a work sequence, and milestone dependencies. |
| Observable acceptance | Retain - source-backed | S14 requires demonstrably working behavior and observable inputs and outputs. |
| Exact validation commands and evidence | Retain - source-backed | S14 requires exact commands, working directory, and expected transcripts. |
| Recovery guidance | Retain - source-backed | S14 requires safe repetition, retry, or rollback guidance. |
| Current progress, discoveries, decisions, and outcomes | Add - source-backed | S14 requires a living plan with these records kept current. |
| Exclude roadmap authority and unrelated future work | Retain - CanonRail-local | S14 does not grant roadmap authority. CanonRail keeps one execution result separate from project-wide sequencing. |
| Exclude assumptions presented as architecture | Retain - source-backed with a CanonRail adaptation | S14 requires assumptions to be repeated and decisions recorded. CanonRail forbids presenting unresolved assumptions as settled. |
| Exclude placeholder commands, paths, outputs, and counts | Retain - source-backed | S14 requires concrete paths, exact commands, and expected evidence. |
| Exclude irrelevant private conversation history | Retain - CanonRail-local | S14 requires a self-contained plan with no prior context. CanonRail excludes conversation history that does not change implementation. |
| Exclude a progress diary | Remove and replace | S14 requires current progress, discoveries, decisions, and outcomes. The replacement excludes only chronology that changes none of those records or recovery. |
| Confirm paths and commands | Retain - source-backed | S14 requires current concrete paths and commands. CanonRail adds repository readback. |
| Independently verifiable milestones | Retain - source-backed | S14 states this requirement directly. |
| Distinguish requirements from suggestions | Retain - CanonRail-local | This protects implementation authority. S14 does not define CanonRail's wording test. |
| Preserve unresolved choices | Retain - source-informed CanonRail policy | S14 requires explicit assumptions and decision records. CanonRail forbids guessing unresolved choices. |
| Fresh reader can resume from plan and repository | Retain - source-backed | S14 requires self-contained novice guidance and a living current state. |

## Selected topology scope

The approved pilot reuses the current mdsmith configuration and proves only:

| Concern | Classification | Pilot decision |
| --- | --- | --- |
| `kind` | S01, S03, and S13 support document or model kinds; S13 supplies the current mechanism. | Resolve the expected primary kind for the selected CanonRail paths. |
| project-selected path or glob | S13 directly supports `kind-assignment` globs. | Keep `.mdsmith.yml` as the physical binding owner. |
| purpose | S01 supports purpose as a document concern. | Keep it in each semantic contract rather than duplicate it as machine metadata. |
| audience or information need | S02 supports this concern for software user information. | Keep it in semantic review; do not promote it into a universal field. |
| relationships | S03 and S04 provide architecture and DITA-specific precedent. | Defer until a CanonRail case defines identity, relation meaning, and an adjacent-invalid example. |
| logical order | S04 provides DITA-specific ordered relationships. | Defer until a CanonRail case defines cardinality and invalid order. |
| nested instruction scope | S05 supports nearest-file precedence for the AGENTS.md open format. | Defer cross-host enforcement and do not claim universal host parity. |

CanonRail's classification is a local decision. The sources do not require these concerns to become one universal topology schema.

The pilot creates no topology artifact. It keeps semantic contracts separate from project-selected path binding and adds no parser, runtime, hook, or dependency.

## Unsupported or deferred

The following items are not selected for implementation:

- general organization of repositories on a user's machine;
- universal directories such as `docs/prd/`, `personal/`, `active/`, or `archive/`;
- automatic file moves or rewrites;
- a claim of ISO, IEEE, OASIS, or Agent Skills conformance for CanonRail as a whole;
- semantic truth or architecture approval inferred from a passing schema;
- identical behavior across Hermes, Claude Code, Codex, or another host;
- automatic host hooks before host-specific contracts and consent are tested;
- an MCP server, daemon, custom Markdown parser, or custom validation engine;
- public marketplace publication;
- `owner`, `authority`, `lifecycle`, or `exceptions` as universal topology fields until an exact source or explicit CanonRail decision owns each field;
- roadmap headings as an external standard;
- PRD headings as an external standard;
- mdsmith as an irreversible dependency.

## Admission rule

A CanonRail piece can move from proposal to implementation only when its plan entry names:

1. a current source;
2. exact source wording;
3. the claim that wording supports;
4. what the source does not decide;
5. the smallest CanonRail adaptation;
6. a valid fixture and adjacent-invalid fixture;
7. a deterministic or observable acceptance check.

If the chain is incomplete, the piece remains deferred or is removed.
