---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: Whether materialize gives a create item with no type the type of its category, and marks no incomplete type
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py -k type_from_the_category
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` lifts a `create` item of a page of `rules`, `entities`, `estimates` or `insights` from the `then` block of its Case.

Then:
When the item writes no `type`, the `fields` of the entry hold the `type` of its category: `rule`, `entity`, `estimate` or `insight`.
**＋** The entry carries no `incomplete: [type]`.
**＋** The type of each category is one map of `.guppi/guppi/materialize.py`, which the lift, `.guppi/guppi/generate.py` and `.guppi/guppi/prespec.py` read.
**＋** A missing `kind`, `purpose`, `tags`, `method`, `pattern` or `children` is still named under `incomplete`, as before.
**－** A `type` that the item writes stands as written.
**－** The `type` of a `defer` item is its own key and is not filled.

## Result

2026-10-09, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
