---
type: estimate
kind: QA
status: pending
target: "[[rule-materialize]]"
purpose: The Criterion materialize lifts from a Case is its when and then, never its given
method: pytest tests/test_materialize.py on a temp Spec
origin: raw/2026-09-23/1355/ledger.md#case-378.2
sprint: migration
created: 2026-09-23
tags: [harness, workflow, ledger]
---

## Criterion

When:
`guppi materialize` assembles the `create` entry of an Estimate, or an `update` entry whose item carries `set.status`, whose Case has `given`, `when` and `then` and whose item writes no `sections: Criterion`.

Then:
The entry's `sections.Criterion` is the `When:` and `Then:` of the Case, verbatim with their operands.
**－** The Criterion holds no `Given:`.
**＋** The decision record of the Case still carries `given` in its `case_text`; a sub-case without its own `given` carries its parent's.

## Result

2026-09-23, uv run pytest tests/test_materialize.py -k "criterion or sub_case_lifts": 9 passed — the lifted Criterion of a create, an update and a sub-case is When and Then with no Given; a written Criterion stands

## History

- 2026-09-23 created · [[decision-case-378.2]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1355/ledger.md#L39
- 2026-10-02 updated: the Criterion replaced whole — the lift covers a create and an update that carries set.status, not an update with change alone (case 588.3) · [[decision-case-588.3]]
