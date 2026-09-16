---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
purpose: A Rule-class item is found by slug or by file
method: pytest in tests/test_materialize.py, the tests of the Rule-class item
---

## Criterion

When:
`guppi materialize` lifts a line `decision[case N][update][<rule-class slug>]` and
looks for its item in the `then` block of the Spec.

Then:
The item is found when its `slug` equals the slug of the line, or its `file` equals
`rule_class_path(slug)`; `change` is lifted, `incomplete` is empty, `category: file`,
`path` from `file`.
**＋** An item with both keys is found as before.
**－** A Rule-class slug with no item in `then` stays `incomplete: [then]`.

## Result

2026-09-16, `pytest tests/test_materialize.py`: 51 green; a Rule-class item is found by slug or by file equal to rule_class_path(slug), change lifted, category file with its path; live, `materialize --show` over raw/2026-09-16/1651: the nine Rule-class items of cases 193, 199 and 200.2 found by file, none incomplete

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L33
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
