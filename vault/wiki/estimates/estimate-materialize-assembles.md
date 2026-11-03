---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: One entry per record line of a ledger, its content lifted from the then block of its Case, nothing invented
method: pytest in .guppi/tests/test_materialize.py against a temp vault; the live reading once by hand
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` lifts the record lines of a unit's `ledger.md` against the `then` blocks of its `spec.md`.

Then:
`materialize.yaml` holds one entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `addresses`, `origin`, `line`, `text`, `decision`; from the `then` item found by its slug — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `drop`, `impact`; what the block lacks is `incomplete`, never invented.
**＋** `reword` is carried as a list of `{old, new}` pairs; a mapping or a scalar under it is `incomplete: [reword]`.
**＋** An Estimate has its own line and its own entry, the `ref` of the line the Estimate itself; the entry of its `create` keeps `kind`, `purpose`, `method` and `tags` as fields.
**＋** One decision record per Case: `decision`, `case_text`, `targets`; a sub-case reads a missing `context` and `given` from its parent, never `problem`, `recommend` or `when`, and carries `parent`, the `decision` of its parent.
**＋** A Case whose sub-cases have decision lines in the unit gets one decision record of its own: its `decision` and its `origin` named by the id of the Case, `case_text` with its `context`, `problem` and `recommend`, and its `given` when it has one, `children` the `decision` of each of its sub-cases in ledger order, and no `targets`.
**＋** An `estimate` line whose slug has a `create` in the same unit is folded into it; one for a page of an earlier unit is an `estimate` entry of its own.
**＋** The `new_tags` of any Case reach the yaml once each; an existing `materialize.yaml` is extended with the lines it does not hold, never rewritten.
**＋** A line the grammar does not parse goes under `unparsed`, and the run goes on.
**－** No entry of an Estimate is derived from a key of the item of a rule or an entity: an Estimate comes only from its own line.
**－** A sub-case record without `problem` carries no `incomplete: [problem]`.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
