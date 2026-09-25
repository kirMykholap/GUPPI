---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: Every decision line of the session has its item under its own Case in the plan, and every item its line
method: uv run pytest tests/test_prespec.py
checked: 2026-09-24
origin: raw/2026-09-24/1916/ledger.md#case-399.2
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run guppi prespec --check <plan>` compares the decision lines of the session's window with the items of the plan's `then` blocks.

Then:
A decision line whose Case has no heading in the plan is the finding `case N: line [kind][slug]: no Case N heading in the plan`; one whose Case holds no item of its kind and slug is `case N: line [kind][slug] has no item in the plan`.
**＋** An item with no decision line of its kind and slug under its own Case heading — a sub-case's heading included — is the finding `case N: item [kind][slug] has no decision line`.
**＋** A nested `estimate` of a `create` needs no line of its own: the line of its parent covers it.
**＋** A second item of one kind and slug under one Case heading — in the same fence tagged `then` or in another one — is the finding `case N: item [kind][slug] stands twice — one entry per target`: one decision line covers one item.
**－** A `create` and an `update` of one slug, or items of one slug under two Case headings — sub-cases included — are no finding of this kind.

## Result

2026-09-24, `uv run pytest tests/test_prespec.py`: 108 passed

## History

- 2026-09-25 created · [[decision-case-399.2]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L38
- 2026-09-25 updated: the Criterion replaced whole — a second item of one kind and slug under one Case is a finding (case 426) · [[decision-case-426]]
