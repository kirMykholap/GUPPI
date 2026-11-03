---
type: estimate
kind: QA
status: passed
target: "[[entity-guppi]]"
purpose: uv run --project .guppi guppi test is green on the branch — the whole suite of the harness
method: "by hand, after each Work Mode: uv run --project .guppi guppi test, read against the Criterion, 0 failed"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, tests]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi test` runs `uv run --project .guppi pytest -q` over `.guppi/tests/` on the working branch, after a Work Mode.

Then:
pytest reports no failed test and no error, and `uv run --project .guppi guppi test` exits 0.
**－** A skipped test is not a failure.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
