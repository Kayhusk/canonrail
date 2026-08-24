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

> Pair `AGENTS.md` with infrastructure that enforces those rules: pre-commit hooks, linters, and type checkers catch issues before you see them, so the system gets smarter about preventing recurring mistakes.

**Supports:** Agent instructions are not sufficient as enforcement. Deterministic infrastructure should protect enforceable rules.

**Does not decide:** That CI is the only authority, that hooks are mandatory, or that mdsmith is the required validator.

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

> Every ExecPlan must produce a demonstrably working behavior, not merely code changes to "meet a definition".

**Supports:** CanonRail's execution-plan contract can require self-contained context and observable behavior.

**Does not decide:** A universal execution-plan format, CanonRail roadmap semantics, or authority to execute a plan.

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

> CLAUDE.md is loaded every session, so only include things that apply broadly.

> For each line, ask: *"Would removing this cause Claude to make mistakes?"* If not, cut it.

> Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens.

**Supports:** Keep always-loaded instructions small and reserve deterministic host hooks for rules that must execute at host lifecycle points.

**Does not decide:** CanonRail's exact prose rules, a mandatory hook architecture, or behavior in non-Claude hosts.

### S17 - Google developer documentation style guide

**Source class:** First-party public developer documentation guidance.

**Source:** <https://developers.google.com/style>

> This style guide provides editorial guidelines for writing clear and consistent technical documentation for an audience of software developers and other technical practitioners.

The same page places project-specific style before the general guide and states that the guide contains guidelines rather than rules.

**Supports:** Clear, consistent, audience-aware public technical writing with project-specific terms taking precedence.

**Does not decide:** CanonRail's full wording policy or an automated semantic gate.

## Foundation audit

| CanonRail piece | Evidence | Decision | Limitation |
|---|---|---|---|
| Objective: typed project-document guidance | S01, S02, S05, S15 | Retain, narrowed | CanonRail defines a reusable governance method; projects still own their facts and selected document set. |
| Human README and agent instructions are separate | S05, S16, S17 | Retain | The current detailed contract bullets remain CanonRail rules, not requirements of the open format. |
| Portable Agent Skill | S06, S08, S11 | Retain | Portability covers the format, not identical discovery or execution in every host. |
| Plugin distribution | S08, S09, S10, S12 | Retain as adapters | A plugin is a host distribution form, not CanonRail's neutral policy owner. |
| Deterministic validation | S07, S13, S16 | Retain | The validator proves configured structure and paths, not semantic truth. |
| mdsmith as the current engine | S13 | Retain as a pinned pilot dependency | Do not present mdsmith as a formal standard or permanent architectural dependency. |
| Agent-instructions contract | S05, S07, S16 | Retain, subject to line-level review | Exact headings and exclusions are CanonRail decisions. |
| README contract | S02, S05, S17 | Retain, subject to line-level review | Exact sections and the first-example rule are CanonRail decisions. |
| Roadmap contract | S01 | Provisional | `plan` is a standard information-item type; the current roadmap headings and authority language are local CanonRail rules. |
| Execution-plan contract | S14 | Retain as an OpenAI-derived profile | ExecPlan is an OpenAI approach, not a universal standard. |
| PRD contract | S15 | Provisional and narrowed | Requirements information is supported; `PRD` and the current headings are local choices. |
| Document Topology Contracts | S01, S02, S03, S04, S05, S13 | Add to the plan only | See the selected scope below. Do not implement broader fields without evidence. |
| CI as the persisted deterministic gate | S07, S13 | Retain as a CanonRail decision | The sources support enforcement infrastructure; CanonRail selects required CI for reproducible project adoption. |
| Plain public writing | S02, S17 | Retain | Unslop is an authoring method used during review, not a public CanonRail dependency or formal standard. |

## Selected topology scope

The current evidence supports these required fields only:

| Field | Evidence |
|---|---|
| `kind` | S01, S03, S13 |
| `purpose` | S01 |
| `audience` or information need | S02 |
| `relationships` | S03, S04 |
| `logical_order` when order matters | S04 |
| `scope` for agent instructions | S05 |
| `path_binding` chosen by the project | S01, S03, S13 |

The feature shall keep two sets separate:

```text
logical topology
- kind
- purpose
- audience or information need
- relationships
- logical order, when order matters

project binding
- project-selected path or glob
- nested instruction scope, when the host supports it
```

The quoted sources do not establish universal path names. CanonRail therefore shall not require one repository tree.

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
