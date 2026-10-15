---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: The Criterion materialize lifts from a Case is its when and then, never its given
method: pytest .guppi/tests/test_materialize.py on a temp Spec
checked: 2026-10-02
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

2026-10-02, uv run pytest tests/test_materialize.py: 123 passed

## History

- 2026-09-23 created · [[decision-case-378.2]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1355/ledger.md#L39
- 2026-10-02 updated: the Criterion replaced whole — the lift covers a create and an update that carries set.status, not an update with change alone (case 588.3) · [[decision-case-588.3]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1834/ledger.md#L34
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
