---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A decision line's {addresses:<lesson slug>} lands on the lesson's entry as addressed_by, at the entry's level; a mark without its lesson is incomplete
method: pytest tests/test_materialize.py on a temp ledger; the live reading the librarian's run on the first marked lesson
checked: 2026-09-21
origin: raw/2026-09-20/2106/ledger.md#case-284.3
sprint: migration
created: 2026-09-20
tags: [harness, workflow, ledger]
---

## Criterion

Given:
`materialize` lifts `source`, `supersedes` and `tags` from the braces of a line and ignores the other keys; `superseded_by` it sets on the entries of Case N from a later `{supersedes}` of any unit.
**＋** `tests/test_materialize.py` fixes the behaviour on a temp ledger.

When:
`guppi materialize` assembles the yaml of a unit.

Then:
A decision entry carries `addresses: [<slug>, …]`; the lesson entry of that slug in the same unit carries `addressed_by: decision-case-N` at the entry's level, not among the page's fields — the lesson page gets no field.
**－** A mark naming a lesson not in the unit is `incomplete: [addresses]` on the decision entry, not an error.

## Result

2026-09-21, uv run pytest tests/test_materialize.py green; live — raw/2026-09-21/1315/materialize.yaml: the decision entries of 291.1 and 296 carry addresses: [lesson-estimate-purpose-update-replaced-the-signed-criterion]; the lesson entry of L3 carries addressed_by: decision-case-296 at the entry's level beside tags and near, not under fields; the lesson page has no such field

## History

- 2026-09-21 created · [[decision-case-284.3]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L6
