# Contributing

CanonRail accepts changes that make document contracts clearer, more portable, or easier to verify.

## Before changing a contract

1. State the recurring failure the rule prevents.
2. Confirm that the rule belongs in the shared contract rather than one project.
3. Add a valid and adjacent-invalid example.
4. Keep semantic guidance separate from deterministic checks.
5. Run the full local verification.

## Verification

```bash
python -m unittest discover -s tests -v
npx --yes @mdsmith/cli@0.54.0 check .
```

Do not add a new runtime or dependency when the existing validator or standard library covers the requirement.
