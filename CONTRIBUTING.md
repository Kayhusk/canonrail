# Contributing

Changes should clarify CanonRail's document contracts or make them easier to check.
They should remain usable across projects and compatible agent tools.

## Before changing a contract

1. Explain the recurring mistake that the rule would prevent.
2. Confirm that the rule applies across projects rather than to one repository.
3. Add one example that should pass and one that differs only in the rule that should fail.
4. Keep writing requirements separate from checks that a tool can run.
5. Update the [source audit](docs/research/foundation-sources.md) when a claim about an external standard or tool changes.
6. Run both repository checks.

## Verification

```bash
python -m unittest discover -s tests -v
npx --yes @mdsmith/cli@0.54.0 check .
```

Do not add a dependency or another checker when mdsmith or the Python standard library already covers the requirement.
