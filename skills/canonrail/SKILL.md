---
name: canonrail
description: Govern project documents through versioned contracts.
version: 0.1.0
author: Edward Bowie, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Documentation, Governance, Agents, Validation]
    related_skills: []
---

# CanonRail

CanonRail guides the creation and review of project documents.
It uses project-owned facts, a contract for each document type, and deterministic validation of the saved files.

## When to use

Use CanonRail when creating or changing:

- agent instruction files;
- a human-facing README;
- a project roadmap;
- a self-contained execution plan;
- a product requirements document;
- another document type registered by the current policy pack.

Do not use it to invent project facts, approve work, change execution authority, or replace the repository's current owners.

## Contracts

- [Agent guidance](references/contracts/agent-instructions.md)
- [README](references/contracts/readme.md)
- [Roadmap](references/contracts/roadmap.md)
- [Execution plan](references/contracts/execplan.md)
- [Product requirements](references/contracts/prd.md)

## Procedure

### 1. Identify the project root

Work from the repository that owns the target document. Read its current instructions and direct sources before relying on session history or generated summaries.

Keep the project root separate from the loaded CanonRail skill.
Resolve target documents from the project root.
Load CanonRail contracts only through linked skill references.
Do not search the project for CanonRail package files.

Complete when the project root, target path, and current project authority are known.

### 2. Resolve the document kind

If the project declares a document-kind command, run that exact command.
The CanonRail repository uses `npx --yes @mdsmith/cli@0.54.0 kinds resolve <path>`.

If no document-kind command is configured, classify the document from its audience and authority.
State that deterministic kind resolution is not configured.
Do not invoke an absent validator or add project configuration.

If the configured command resolves no kind, use the same semantic classification.
Do not force the document into the nearest template.
Add a new shared kind only when the responsibility recurs across projects.

Complete when exactly one primary document responsibility is selected.

### 3. Read the contract

Use the host's skill loader to read the matching linked contract listed above. Then identify the project files that own the facts the document needs.

The contract governs document responsibility. The project governs names, commands, architecture, status, and approval.

Complete when every material statement has a current project source or is labeled as an assumption.

### 4. Write for the audience

Keep the document direct and easy to scan:

- answer the reader's first question early;
- use the project's exact terms, paths, and commands;
- state each fact once in its owner;
- link to deeper detail instead of copying it;
- separate current facts, plans, assumptions, and evidence;
- remove filler, promotional language, vague advice, and private process terms.

Preserve exact legal, safety, protocol, accessibility, and authority language when wording is part of the contract.

Complete when every section serves the selected audience and responsibility.

### 5. Validate the saved document

Run the project's declared document check when one exists. Then run the repository's own project checks and read the saved file as its intended reader.

If no document check is configured, perform the semantic review.
State that deterministic document validation is not configured.

Do not install a validator or copy CanonRail configuration unless the project has selected that adoption work.

Complete when all configured checks pass and the semantic review finds no ownership, authority, duplication, or unsupported-claim defect.

## Boundaries

- Host integrations give earlier feedback; configured repository checks remain the enforcement authority.
- A schema verifies declared structure, not truth or good judgment.
- Project-specific exceptions belong in the project and need an explicit reason and scope.
- Do not add frontmatter to portable root files when path assignment can classify them.
- Do not weaken a shared hard rule to make one stale document pass.

## Verification

- [ ] The target resolved to the correct document kind
- [ ] Current project sources were read
- [ ] Audience, owner, authority, and volatility are explicit
- [ ] No private context or duplicated mutable status leaked into the document
- [ ] The configured deterministic check passed, or its absence was stated
- [ ] Project checks passed
- [ ] Final readback matches the intended reader's needs
