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

- `AGENTS.md` or equivalent agent instructions;
- a human-facing README;
- a project roadmap;
- a self-contained execution plan;
- a product requirements document;
- another document type registered by the current policy pack.

Do not use it to invent project facts, approve work, change execution authority, or replace the repository's current owners.

## Procedure

### 1. Identify the project root

Work from the repository that owns the target document. Read its current instructions and direct sources before relying on session history or generated summaries.

Complete when the owning repository, target path, and current project authority are known.

### 2. Resolve the document kind

Run:

```bash
mdsmith kinds resolve <path>
```

If the project uses the pinned no-install form, run the equivalent command through `npx --yes @mdsmith/cli@0.54.0`.

If no kind resolves, classify the document from its audience and authority. Do not force it into the nearest template. Add a new shared kind only when the responsibility recurs across projects.

Complete when exactly one primary document responsibility is selected.

### 3. Read the contract

Read `contracts/<kind>.md` from the active CanonRail policy pack. Then identify the project files that own the facts the document needs.

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

Run the project's pinned check, normally:

```bash
mdsmith check <path>
```

Then run the repository's own documentation and project checks. Read the saved file as its intended reader.

Complete when deterministic checks pass and the semantic review finds no ownership, authority, duplication, or unsupported-claim defect.

## Boundaries

- A plugin gives earlier feedback; CI remains the enforcement authority.
- A schema verifies declared structure, not truth or good judgment.
- Project-specific exceptions belong in the project and need an explicit reason and scope.
- Do not add frontmatter to portable root files when path assignment can classify them.
- Do not weaken a shared hard rule to make one stale document pass.

## Verification

- [ ] The target resolved to the correct document kind
- [ ] Current project sources were read
- [ ] Audience, owner, authority, and volatility are explicit
- [ ] No private context or duplicated mutable status leaked into the document
- [ ] Saved Markdown passed the pinned deterministic check
- [ ] Project checks passed
- [ ] Final readback matches the intended reader's needs
