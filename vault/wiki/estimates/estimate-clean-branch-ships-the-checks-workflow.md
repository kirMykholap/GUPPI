---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether guppi ship writes .github/workflows/checks.yml, judged and cleaned, and no other file of .github/, and whether --check judges it in place
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k checks_workflow
checked: 2026-10-15
origin: raw/2026-10-15/0553/ledger.md#case-822.6
sprint: plugin
created: 2026-10-15
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
**＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.

Then:
It writes `.github/workflows/checks.yml`, judged and cleaned like each other file it writes.
**＋** `--check` judges `.github/workflows/checks.yml` in place.
**＋** The comment of `.github/workflows/checks.yml` names no page that the clean version does not hold.
**－** It writes no other file of `.github/`, `.github/workflows/prod.yml` included.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_ship.py -k checks_workflow: 3 passed, exit 0

## History

- 2026-10-15 created · [[decision-case-822.6]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L4
