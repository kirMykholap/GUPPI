---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: An update of an Estimate changes the part it names alone, or replaces the Criterion whole
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` lifts the `update` item of an Estimate.

Then:
An item that carries `set.status` gets `sections.Criterion`, the text it writes under `sections: Criterion` or else the `when` and `then` of its Case, and keeps the status it set.
**＋** An item that writes `sections: Criterion` keeps that text and gets `set: {status: pending}` unless it set a status itself.
**＋** A written `sections.Criterion` beside any other part stands and sets `pending`.
**＋** An item that carries `change` alone gets no `sections.Criterion` and no `set`: `.guppi/guppi/generate.py` writes its History line, and the Criterion and the status of the page stand.
**＋** An item that names a part — `set` without `status`, a `replace` pair, `drop`, a section other than `Criterion` — and writes no Criterion carries that part alone: nothing is lifted and no status is set.
**＋** `names_a_part` of `.guppi/guppi/materialize.py` is the one judgment of an item that replaces a Criterion: `.guppi/guppi/prespec.py` imports it and `.guppi/guppi/casecheck.py` imports its notes, so an item with `change` alone counts as no promise and gets no note on the lines of the old Criterion.
**－** An item with `change` alone is not `incomplete`.
**－** An item whose `drop` names `Criterion` gets `incomplete: [criterion]`, by `drops_criterion` of `.guppi/guppi/materialize.py`, and the lift adds no `sections.Criterion` and no `set.status` to it, whatever else the item carries.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
