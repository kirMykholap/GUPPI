---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A create whose slug is on disk is exists only when the page was born of the same Case
method: pytest in .guppi/tests/test_materialize.py, the tests of the exists mark
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger, librarian]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` reads a `create` line whose slug is already on disk — live or archived.

Then:
The entry is marked `exists` only when the `origin` of the page carries the `#case-N` of this line.
**＋** Otherwise the entry stays an ordinary `create`.
**－** A placeholder, a page with no `kind`, is not a collision: `uv run --project .guppi guppi generate` fills it.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
