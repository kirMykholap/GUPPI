---
type: estimate
kind: QA
status: pending
target: "[[rule-clean-branch]]"
purpose: Whether the workflow prod.yml runs the tests of test_ship.py selected by -k own_style and by -m live -k own_tests, which check the style and the tests of a clean version, on its Linux runner before it commits, and writes nothing to prod when one of them fails
method: "by hand: .github/workflows/prod.yml read against the Criterion; by hand, after a run of .github/workflows/prod.yml on GitHub whose step guppi ship exits 0: the output of gh run view --log of that run read against the Criterion, written into the estimate line"
origin: raw/2026-11-20/1353/ledger.md#case-1042.1
sprint: plugin
created: 2026-11-20
tags: [ci, plugin, tests]
---

## Criterion

When:
A push to `main`, or a push of a tag `prod-*` on a commit of another branch, starts a run of `.github/workflows/prod.yml` on GitHub, as `rule-clean-branch` sets it, and its step `uv run --project .guppi guppi ship` exits 0.

Then:
Before its step that commits to `prod`, the job runs `uv run --project .guppi pytest .guppi/tests/test_ship.py -k own_style` and `uv run --project .guppi pytest .guppi/tests/test_ship.py -m live -k own_tests` on its runner `ubuntu-latest`.
**＋** Each of the two exits 0 there on a commit whose clean version passes the commands of the keys `style` and `test` of `guppi.toml`.
**－** A run where either of the two exits non-zero fails and writes nothing to `prod`.
**－** `.github/workflows/checks.yml` does not change.

## History

- 2026-11-23 created · [[decision-case-1042.1]]
