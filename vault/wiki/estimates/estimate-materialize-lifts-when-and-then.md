---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: The Criterion materialize lifts from a Case is its when and then, never its given
method: pytest .guppi/tests/test_materialize.py on a temp Spec
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`guppi materialize` assembles the `create` entry of an Estimate, or an `update` entry whose item carries `set.status`, whose Case has `given`, `when` and `then` and whose item writes no `sections: Criterion`.

Then:
The entry's `sections.Criterion` is the `When:` and `Then:` of the Case, verbatim with their operands.
**－** The Criterion holds no `Given:`.
**＋** The decision record of the Case still carries `given` in its `case_text`; a sub-case without its own `given` carries its parent's.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
