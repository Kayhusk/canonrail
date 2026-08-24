# Agent instructions contract

Agent instruction files give coding agents project rules they cannot infer reliably from the repository.
Keep only rules that prevent a concrete mistake.

CanonRail chose the sections and review rules below.
Each coding tool still controls how it finds and prioritizes instruction files.

## Include

- Setup, build, test, and validation commands that differ from common defaults.
- Who can approve or authorize work, safety limits, conventions, and protected paths that an agent cannot reliably infer.
- Short links to project documents an agent must read for specific work.
- Completion checks that apply throughout the instruction file's scope in the current tool.

## Keep elsewhere

- Agent identity, user preferences, credentials, and private profile details.
- Changing task status, issue history, test records, and release history.
- File-by-file repository tours and facts already clear in manifests or source code.
- Copies of architecture documents, plans, runbooks, and contribution guides.
- Vague or self-evident advice that would not prevent a specific mistake.

## Review

- Verify every command and path against the current repository.
- If the current tool supports nested instruction files, verify which file applies at each changed path.
- Remove repeated explanations and changing status.
- Make each link specific enough that an agent knows when to follow it.
- Run the repository's document check and the project checks required for the change.
