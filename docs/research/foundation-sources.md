# CanonRail source audit

This file records the external sources behind CanonRail's document contracts, Agent Skill package, tool packages, Markdown checks, CI use, and proposed document relationship rules.

Quoted text is preserved exactly. Each note states what the source supports and what remains a CanonRail or project choice.

## Exact source wording

### S01 - ISO/IEC/IEEE 15289:2019

**Source class:** IEEE/ISO/IEC standard catalog entry.

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

**Supports:** Audience needs, presentation, structure, content, and format as concerns for user-facing information.

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

**Source class:** OpenAI product documentation.

**Source:** <https://learn.chatgpt.com/docs/customization/overview>

> `AGENTS.md` gives Codex durable project guidance that travels with your repository and applies before the agent starts work. Keep it small.

> If it finds the right files but reads too many documents, add routing guidance (which directories/files to prioritize).

> Pair `AGENTS.md` with infrastructure that enforces those rules: pre-commit hooks, linters, and type checkers catch issues before you see them, so the system gets smarter about preventing recurring mistakes.

The same page lists build and test commands, review expectations, repository-specific conventions, and directory-specific instructions as suitable repository guidance.

**Supports:** Concise persistent project rules, exact commands, review expectations, routing guidance, directory-specific instructions, and deterministic enforcement outside prose.

**Does not decide:** CanonRail's detailed exclusions, that CI is the only authority, that hooks are mandatory, or that mdsmith is the required validator.

### S08 - OpenAI skills and plugins

**Source class:** OpenAI product documentation.

**Source:** <https://learn.chatgpt.com/docs/build-skills>

> Skills are the authoring format for reusable workflows. Plugins distribute reusable skills and connectors through the universal plugin directory shared by ChatGPT and Codex.

**Supports:** CanonRail can keep its reusable workflow in a skill and distribute that skill in a plugin package.

**Does not decide:** Claude or Hermes plugin structure, one universal marketplace, or identical behavior in every tool.

### S09 - OpenAI plugin packaging

**Source class:** OpenAI plugin documentation.

**Source:** <https://developers.openai.com/plugins/build/plugins>

> Packaging gives the plugin a stable identity and tells ChatGPT and Codex which skills, MCP server connections, and other resources belong together.

**Supports:** A Codex plugin can package CanonRail's skill and related resources under one stable identity.

**Does not decide:** That CanonRail needs MCP, hooks, assets, or a public plugin listing.

### S10 - Claude Code plugins

**Source class:** Anthropic product documentation.

**Source:** <https://code.claude.com/docs/en/plugins>

> Plugins let you extend Claude Code with custom functionality that can be shared across projects and teams.

The same page describes plugins as self-contained directories with skills, agents, hooks, or a `.claude-plugin/plugin.json` manifest for sharing, distribution, versioned releases, and reuse across projects.

**Supports:** A Claude Code plugin can package CanonRail for reuse across projects and teams.

**Does not decide:** Packages for other tools or whether CanonRail needs hooks, agents, or MCP.

### S11 - Claude Code skills

**Source class:** Anthropic product documentation.

**Source:** <https://code.claude.com/docs/en/skills>

> Claude Code skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools.

**Supports:** The same standards-compliant CanonRail skill can be consumed by Claude Code and other compatible tools.

**Does not decide:** Identical discovery, tool permissions, or invocation semantics across those tools.

### S12 - Hermes plugins

**Source class:** Nous Research Hermes Agent documentation.

**Source:** <https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins>

> Hermes has a plugin system for adding custom tools, hooks, and integrations without modifying core code.

> Bundle skills | `ctx.register_skill(name, path)` — namespaced as `plugin:skill`, loaded via `skill_view("plugin:skill")`

**Supports:** A Hermes plugin can register the portable CanonRail skill without changing Hermes core.

**Does not decide:** CanonRail's policy, contract contents, or automatic plugin activation.

### S13 - mdsmith file kinds and schemas

**Source class:** First-party validator documentation.

**Source:** <https://mdsmith.dev/features/file-kinds-schemas/>

> A kind gives each file a role; a schema gives that role a contract.

> Bind files to a kind by a front-matter `kinds:` field or a `kind-assignment` glob.

**Supports:** mdsmith can assign document types by path and check their declared schemas.

**Does not decide:** CanonRail's current path mappings, semantic truth, project authority, whether mdsmith remains the long-term engine, or the contract wording.

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

**Source class:** ISO/IEC/IEEE standard catalog entry.

**Source:** <https://www.iso.org/standard/72089.html>

> — specifies the required information items produced through the implementation of the requirements processes;

> — specifies the required contents of the required information items;

**Supports:** Requirements processes produce required information items with required content. CanonRail separately decides to represent that concern as one document type.

**Does not decide:** The term PRD, CanonRail's PRD headings, product-management workflow, prioritization, or approval state.

### S16 - Anthropic Claude Code best practices

**Source class:** Anthropic product guidance.

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

**Source class:** Nous Research Hermes Agent documentation.

**Source:** <https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills>

> Add your repo as a tap:

> `hermes skills tap add owner/repo`

> Users can then search and install from your repository.

The same documentation defines `skills/<skill-name>/SKILL.md` with optional `references/` as the portable skill package layout.

**Supports:** CanonRail can distribute its self-contained skill and linked contracts through a custom Hermes skill tap.

**Does not decide:** CanonRail's contracts, use by another project, automatic installation, or a need for a Hermes plugin when no tools or hooks are present.

## Project decisions

| CanonRail piece | Evidence | Decision | Limitation |
|---|---|---|---|
| Objective: project-document contracts and validation | S01, S02, S05, S15 | Retain, narrowed | CanonRail defines a harness-agnostic framework; projects still own their facts, selected documents, paths, and approval rules. |
| Human README and agent instructions are separate | S05, S16, S17 | Retain | The current detailed contract bullets remain CanonRail rules, not requirements of the open format. |
| Portable Agent Skill | S06, S08, S11, S18 | Retain | Portability covers the format, not identical discovery or execution in every host. |
| Plugin distribution | S08, S09, S10 | Retain for Codex and deferred Claude packaging | A plugin is a tool-specific package, not the owner of CanonRail's shared contracts. |
| Hermes skill distribution | S06, S18 | Retain as a custom skill tap | CanonRail has no Hermes tools or hooks, so a plugin would add an unnecessary install and scan boundary. |
| Automated checks | S07, S13, S16 | Retain | The validator proves configured structure and paths, not semantic truth. |
| mdsmith as the current engine | S13 | Retain as a pinned pilot dependency | Do not present mdsmith as a formal standard or permanent architectural dependency. |
| Agent-instructions contract | S05, S07, S16 | Retain as a CanonRail contract with source support | The sources support a dedicated entry point, concise persistent instructions, routing, tool-defined scope, and checks outside prose. CanonRail chooses the detailed inclusions, exclusions, and headings. |
| README contract | S02, S05, S17 | Retain as a CanonRail contract with source support | The sources support human orientation, quick starts, audience needs, and clear public writing. CanonRail chooses the detailed inclusions, exclusions, review rules, and headings. |
| Roadmap contract | S01 | Retain as a CanonRail-defined contract | `plan` is a standard information-item type; CanonRail chooses the headings and approval rules. |
| Execution-plan contract | S14 | Retain as an OpenAI-derived CanonRail profile | Self-contained living context, observable behavior, milestones, exact validation, progress, decisions, and recovery are OpenAI-derived. The headings and authority boundary are local. |
| PRD contract | S15 | Retain as a CanonRail-defined contract | The source supports requirements information; CanonRail chooses the term `PRD` and the headings. |
| Document Topology Contracts | S01, S02, S03, S04, S05, S13 | Narrow to a kind and path-binding pilot | The pilot reuses mdsmith mechanisms. No source requires a combined universal topology field set. |
| CI as the saved-file check | S07, S13 | Retain as a CanonRail decision | The sources support checks outside prose. CanonRail requires CI only when a project adopts automated CanonRail checks, so the same check runs against saved files. |
| Plain public writing | S02, S17 | Retain | CanonRail chooses its exact writing rules and automated checks; the sources do not define a complete writing-quality gate. |

## Rule-by-rule contract review

`Supported by source` means the cited wording supports the concern, not the exact CanonRail sentence.
`CanonRail decision` means CanonRail chose the rule without attributing it to an external standard or format.
`Narrow` and `remove` describe changes from the previous contract text.

### Agent instructions contract

| Rule | Decision | Source and limit |
| --- | --- | --- |
| Definition of agent instructions | Narrow - supported by source with a CanonRail change | S05 and S07 support persistent project context and instructions. S16 supports the non-inferable, mistake-prevention test. |
| Required contract headings | Retain - CanonRail decision | No cited source requires `Include`, `Keep elsewhere`, or `Review`. |
| Exact setup, build, test, and validation commands | Retain - supported by source | S05, S07, and S16 name build, test, and non-inferable commands as suitable agent guidance. |
| Project authority, safety boundaries, conventions, and protected paths | Retain - CanonRail decision | S05 and S07 support project conventions and context. CanonRail selects the full category list and the reliability test. |
| Routing pointers to current owners | Retain - supported by source | S07 explicitly recommends routing guidance when agents read too broadly. CanonRail requires pointers only where an owner must be consulted. |
| Completion checks within instruction scope | Narrow - supported by source with a CanonRail change | S05 and S07 support checks and local precedence. The contract leaves scope to the current tool instead of claiming one directory rule for every tool. |
| Exclude identity, preferences, credentials, and private profile context | Retain - CanonRail decision | OpenAI separates global personal guidance from repository guidance, but the full exclusion list is CanonRail safety policy. |
| Exclude volatile status and chronology | Retain - supported by source | S16 excludes frequently changing information. CanonRail lists task status, issue history, receipts, and release chronology as examples. |
| Exclude repository tours and inferable facts | Retain - supported by source | S16 excludes file-by-file descriptions and information available from source. |
| Exclude copied specialist documents | Retain - supported by source with local examples | S16 recommends linking to detailed documentation. CanonRail names architecture, plans, runbooks, and contribution guides. |
| Exclude vague instructions | Narrow - supported by source | S16's removal test supports keeping only instructions that prevent a mistake. The revised line drops the broader observable-behavior claim. |
| Verify commands and paths | Retain - CanonRail decision | Current repository readback is CanonRail's admission rule, not an external format requirement. |
| Review nested instruction files | Narrow - supported by source | S05 supports nearest-file precedence for AGENTS.md. The revised rule requires checking the current tool and does not claim that every tool handles scope the same way. |
| Remove duplicate explanations and changing status | Retain - supported by source | S16 supports concise persistent guidance and excludes changing information. |
| Keep routing pointers specific | Retain - supported by source with a CanonRail change | S07 supports routing and S16 warns against ambiguous guidance. CanonRail requires each link to say when an agent should follow it. |
| Run declared document and project checks | Retain - supported by source with a CanonRail change | S07 supports checks outside prose. The repository selects the actual commands. |

### README contract

| Rule | Decision | Source and limit |
| --- | --- | --- |
| Definition of a README | Narrow - supported by source | S05 names project descriptions, quick starts, and contribution guidelines as human README concerns. The previous generic evaluation claim was removed. |
| Required contract headings | Retain - CanonRail decision | S02 and S05 do not prescribe CanonRail's `Include`, `Keep elsewhere`, or `Review` headings. |
| Project purpose and intended users | Retain - supported by source | S05 supports project descriptions. S02 supports identifying user information needs. |
| Setup for ordinary use | Narrow - supported by source with a CanonRail change | S05 supports quick starts. CanonRail limits setup instructions to the main supported use. |
| Shortest useful example or first check | Narrow - supported by source with a CanonRail change | S05 supports a quick start but does not require one universal form. The contract allows an installation step, example, or first check as appropriate. |
| Public limitations that affect adoption | Retain - CanonRail decision | S02 supports user information needs, but CanonRail selects adoption-relevant limitations as README content. |
| Links to architecture, contribution, security, and support owners | Narrow - CanonRail decision | S05 supports contribution guidance. CanonRail broadens the owner to deeper documentation and requires specialist links only when they exist. |
| Exclude full architecture and implementation history | Retain - CanonRail decision | This keeps the human entry point bounded. No cited source defines the exact exclusion. |
| Exclude task state, private review language, and agent workflow | Retain - supported by sources with CanonRail details | S05 separates human and agent entry points. S16 supports excluding volatile information. The detailed list is local. |
| Exclude internal paths, accounts, credentials, and unpublished evidence | Retain - CanonRail decision | This is a public-information and safety boundary, not an external README standard. |
| Exclude duplicated linked explanations | Retain - CanonRail decision | S17 supports clear, useful writing. CanonRail selects single ownership instead of repetition. |
| Exclude unproved quality and readiness claims | Retain - CanonRail decision | CanonRail requires current proof for strong public claims. The cited sources do not define this list. |
| Read as a new user | Retain - supported by source with a CanonRail method | S02 supports designing around user information needs. CanonRail chooses the no-history review perspective. |
| Verify commands, links, versions, and claims | Retain - CanonRail decision | Current readback is CanonRail's admission rule. |
| Put the common path first | Retain - CanonRail decision | S02 supports audience-aware presentation. CanonRail selects common-path-first ordering. |
| Remove filler, promotion, and generic prose | Retain - supported by source with a CanonRail change | S17 supports clear, direct, useful writing. CanonRail names the specific wording it rejects. |
| First example exercises a supported path | Narrow - CanonRail decision | The new rule verifies every command or runnable example without requiring every README to contain one. |

### Execution plan contract

| Rule | Decision | Source and limit |
| --- | --- | --- |
| Definition of an execution plan | Retain - supported by source | S14 requires a self-contained plan that a novice can follow to working behavior. CanonRail narrows the plan to one bounded result. |
| Required contract headings | Retain - CanonRail decision | S14 provides one customizable profile and does not require CanonRail's three contract headings. |
| Plan presence does not authorize execution | Add - CanonRail decision | S14 describes an implementation method, not project authority. CanonRail makes the authority boundary explicit. |
| One goal, current context, and exclusions | Retain - supported by source with a CanonRail change | S14 supports purpose and complete current context. One defined goal and explicit exclusions are CanonRail choices. |
| Affected paths, ordered work, and dependencies | Retain - supported by source | S14 requires concrete file locations, a work sequence, and milestone dependencies. |
| Observable acceptance | Retain - supported by source | S14 requires demonstrably working behavior and observable inputs and outputs. |
| Exact validation commands and evidence | Retain - supported by source | S14 requires exact commands, working directory, and expected transcripts. |
| Recovery guidance | Retain - supported by source | S14 requires safe repetition, retry, or rollback guidance. |
| Current progress, discoveries, decisions, and outcomes | Add - supported by source | S14 requires a living plan with these records kept current. |
| Exclude roadmap authority and unrelated future work | Retain - CanonRail decision | S14 does not grant roadmap authority. CanonRail keeps one execution result separate from project-wide sequencing. |
| Exclude assumptions presented as architecture | Retain - supported by source with a CanonRail change | S14 requires assumptions to be repeated and decisions recorded. CanonRail forbids presenting unresolved assumptions as settled. |
| Exclude placeholder commands, paths, outputs, and counts | Retain - supported by source | S14 requires concrete paths, exact commands, and expected evidence. |
| Exclude irrelevant private conversation history | Retain - CanonRail decision | S14 requires a self-contained plan with no prior context. CanonRail excludes conversation history that does not change implementation. |
| Exclude a progress diary | Remove and replace | S14 requires current progress, discoveries, decisions, and outcomes. The replacement excludes only chronology that changes none of those records or recovery. |
| Confirm paths and commands | Retain - supported by source | S14 requires current concrete paths and commands. CanonRail adds repository readback. |
| Independently verifiable milestones | Retain - supported by source | S14 states this requirement directly. |
| Distinguish requirements from suggestions | Retain - CanonRail decision | This protects implementation authority. S14 does not define CanonRail's wording test. |
| Preserve unresolved choices | Retain - supported by sources with CanonRail details | S14 requires explicit assumptions and decision records. CanonRail forbids guessing unresolved choices. |
| Fresh reader can resume from plan and repository | Retain - supported by source | S14 requires self-contained novice guidance and a living current state. |

## Selected topology scope

The approved pilot reuses the current mdsmith configuration and proves only:

| Concern | Classification | Pilot decision |
| --- | --- | --- |
| `kind` | S01, S03, and S13 support document or model kinds; S13 supplies the current mechanism. | Resolve the expected primary kind for the selected CanonRail paths. |
| project-selected path or glob | S13 directly supports `kind-assignment` globs. | Keep path mappings in `.mdsmith.yml`. |
| purpose | S01 supports purpose as a document concern. | Keep purpose in each document contract rather than repeat it as machine metadata. |
| audience or information need | S02 supports this concern for software user information. | Keep it in content review; do not promote it into a universal field. |
| relationships | S03 and S04 provide architecture and DITA-specific precedent. | Defer until a CanonRail case defines identity, relation meaning, and one failing example that differs by that rule. |
| logical order | S04 provides DITA-specific ordered relationships. | Defer until a CanonRail case defines cardinality and invalid order. |
| nested instruction scope | S05 supports nearest-file precedence for the AGENTS.md open format. | Defer rules across tools and do not claim that every tool behaves the same way. |

CanonRail's classification is a local decision. The sources do not require these concerns to become one universal topology schema.

The pilot creates no topology file. It keeps document contracts separate from project-selected path mappings and adds no parser, runtime, hook, or dependency.

## Unsupported or deferred

The following items are not selected for implementation:

- general organization of repositories on a user's machine;
- universal directories such as `docs/prd/`, `personal/`, `active/`, or `archive/`;
- automatic file moves or rewrites;
- a claim of ISO, IEEE, OASIS, or Agent Skills conformance for CanonRail as a whole;
- semantic truth or architecture approval inferred from a passing schema;
- identical behavior across Hermes, Claude Code, Codex, or another host;
- automatic tool hooks before tool-specific behavior and consent are tested;
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
5. the smallest CanonRail change;
6. one passing example and one example that differs only in the rule that should fail;
7. a deterministic or observable acceptance check.

If the chain is incomplete, the piece remains deferred or is removed.
