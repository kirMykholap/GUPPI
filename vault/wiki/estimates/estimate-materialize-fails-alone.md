---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: One bad entry does not stop the run
method: pytest in .guppi/tests/test_materialize.py, the tests of the failed and unreadable entries
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger, tests]
core: true
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
**＋** The field list in the docstring of `.guppi/guppi/materialize.py` is complete, every
field with its writer; a key the code writes and the list does not name is a finding
of the reading.
**－** A `MaterializeError` — no `ledger.md`, a Case heading in two files — still
stops the walk with exit 1.
**－** `unparsed` does not change.

## Result

2026-09-16, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
