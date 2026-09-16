---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, tests]
purpose: One bad entry does not stop the run
method: pytest in tests/test_materialize.py, the tests of the failed and unreadable entries
---

## Criterion

When:
`guppi materialize` lifts a record line and the lift raises; or it meets an existing
entry in `materialize.yaml`.

Then:
The line becomes an entry `{line, text, failed: "<Type>: <message>"}` without `kind`;
one line on stderr, `materialize: line N: <message>`; the other lines are lifted; the
yaml is written; the unit's exit is 1; the walk goes on to the next unit.
**＋** On the next run an entry with `failed` and no `kind` is lifted again from its
line and replaced when the lift succeeds.
**＋** An existing entry is readable when it is a mapping with at least one of `line`,
`derived`, `librarian`; the librarian's own entry — `librarian: synthesis` or
`merged`, no `line` — is left as it is, with no line on stderr.
**＋** An unreadable one — not a mapping, or a mapping with none of the three — is
left as it is, named on stderr once, and the run goes on.
**＋** The field list in the docstring of `guppi/materialize.py` is complete, every
field with its writer; a key the code writes and the list does not name is a finding
of the reading.
**－** A `MaterializeError` — no `ledger.md`, a Case heading in two files — still
stops the walk with exit 1.
**－** `unparsed` does not change.

## Result

2026-09-16, `pytest tests/test_materialize.py`: 51 green — a raising lift becomes a {line, text, failed} entry, the unit exits 1, the walk goes on, the entry is lifted again on the next run, an unreadable existing entry is left alone and named once, the librarian's entry without a line is kept silently; the field list in the docstring of guppi/materialize.py rewritten whole with every writer, the keys of the old shape (derived, criterion_block, case_removed) named as kept on entries already written; no key the code writes is missing from it

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L32
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
