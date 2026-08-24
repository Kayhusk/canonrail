---
name: canonrail
description: Write and review agent docs, READMEs, plans, and PRDs.
version: 0.1.0
author: Edward Anthony Escudero Bowie
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Documentation, Governance, Agents, Validation]
    related_skills: []
---

# CanonRail

CanonRail is a framework for project document contracts.
People and compatible agent tools can use the contracts.
Configured checks verify required sections.
They also verify file-to-document mappings.

## When to use

Use this skill when creating, reviewing, or changing:

- agent instruction files;
- a human-facing README;
- a project roadmap;
- a self-contained execution plan;
- a product requirements document;

Do not invent project facts, grant approval, or start unapproved work.
Treat the project's current files and systems as the source of project information.

## Document contracts

- [Agent instructions](references/contracts/agent-instructions.md)
- [README](references/contracts/readme.md)
- [Roadmap](references/contracts/roadmap.md)
- [Execution plan](references/contracts/execplan.md)
- [Product requirements](references/contracts/prd.md)

## Procedure

### 1. Find the project root

Work from the repository that contains the target document.
Read its current instructions and source files before using session history or generated summaries.

Keep the project root separate from the installed CanonRail skill.
Resolve target documents from the project root.
Open CanonRail contracts only through the linked skill references above.
Do not search the project for CanonRail package files.

Complete this step when the project root, target path, and controlling project instructions are known.

### 2. Identify the document type

If the project provides a command that identifies document types, run that command exactly.

If the project has no such command, use the target document's purpose, intended reader, and authority to choose its type.
State that no automated type check is configured.
Do not add configuration or invoke a checker that the project does not use.

If the configured command returns no type, review the target document's purpose, intended reader, and authority.
Do not force the document into the closest template.
Do not add a shared document type unless the user asked to extend CanonRail and the same responsibility appears across projects.

Complete this step when one primary document type is selected.

### 3. Read the matching contract

Use the current tool's skill loader to open the matching linked contract.
Then read the project files that contain the facts needed by the document.

The contract says what belongs in the document.
The project supplies its names, commands, architecture, status, and approval rules.

Complete this step when each material statement has a current project source or is clearly marked as an assumption.

### 4. Write for the reader

Keep the document direct and easy to scan:

- answer the reader's first question early;
- use the project's exact terms, paths, and commands;
- state each fact once in the file that maintains it;
- link to detailed material instead of copying it;
- separate current facts, plans, assumptions, and test results;
- remove filler, promotion, vague advice, and private process terms.

Preserve exact legal, safety, protocol, accessibility, and approval wording when the wording itself matters.

Complete this step when every section helps the intended reader understand, decide, act, or verify.

### 5. Check the saved document

Run the project's document check when one exists.
Then run any other repository checks required for the task and read the saved file as its intended reader.

If no document check is configured, review the file against the matching contract.
State that no automated document check is configured.

Do not install a checker or copy CanonRail configuration unless the user explicitly requested that setup.

Check for misplaced content, approval errors, repeated facts, and unsupported claims.
Complete this step when the configured checks pass and the final read finds no remaining contract issues.

## Limits

- Tool integrations can catch errors early. When a project defines repository checks, those checks determine whether a saved file meets the enforced rules.
- A schema can check declared structure. It cannot prove that the content is true or useful.
- Project exceptions belong in the project and need a clear reason and scope.
- Do not add front matter to common root files when path rules can identify them.
- Do not weaken a shared rule to make an outdated document pass.

## Verification

- [ ] The target has the correct document type
- [ ] Current project sources were read
- [ ] The intended reader, purpose, and approval rules are clear
- [ ] Each fact and any current status has a clear source
- [ ] The document contains no private context or duplicated status
- [ ] The configured document check passed, or its absence was stated
- [ ] Required project checks passed
- [ ] The final document meets the intended reader's needs
