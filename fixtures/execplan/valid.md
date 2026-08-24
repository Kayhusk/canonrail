# Example execution plan

## Goal

Add and verify one document contract.

## Context

The repository already validates Markdown structure.

## Plan

Add the contract, example, and focused check.

## Validation

Run both commands from the repository root:

```bash
python -m unittest discover -s tests -v
npx --yes @mdsmith/cli@0.54.0 check .
```

## Recovery

Inspect the failing output and correct the affected file.
If the change must be abandoned, revert only files changed by this plan.
