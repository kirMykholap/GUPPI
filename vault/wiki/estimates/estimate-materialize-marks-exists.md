---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A create whose slug is on disk is exists only when the page was born of the same Case
method: pytest in .guppi/tests/test_materialize.py, the tests of the exists mark
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, librarian]
---

## Criterion

When:
`uv run --project .guppi guppi materialize` reads a `create` line whose slug is already on disk — live
or archived.

Then:
The entry is marked `exists` only when the `origin` of the page carries the `#case-N`
of this line.
**＋** Otherwise the entry stays an ordinary `create`.
**－** A placeholder (no `kind`) is not a collision: 101.1 fills it.

## Result

2026-09-16, `pytest tests/test_materialize.py`: 51 green; a create is marked exists only when the page on disk carries this line's #case-N in its origin, otherwise it stays a create; live, `materialize --show` over raw/2026-09-16/1034 and 1651: no exists mark, every create a create

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L31
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
