---
type: estimate
kind: QA
status: passed
target: "[[rule-glossary]]"
purpose: glossary, once it wrote glossary.md and exits 0, ticks the guppi glossary lines of every Spec under raw/ whose yaml is applied whole
method: "pytest .guppi/tests/test_glossary.py; by hand, after a librarian's run: the spec.md of its session read against the Criterion"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, librarian, session]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi glossary` without a flag wrote `vault/wiki/glossary.md` and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

Then:
In the `spec.md` of every unit whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi glossary` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`. Nothing else in the file changes.
**＋** The form of the line in `vault/wiki/case-schema.md` is `` - [ ] `uv run --project .guppi guppi glossary` ``, the command in the first code span.
**－** A line that names `guppi glossary` only in a later code span, such as a `read` line, is not ticked.
**－** `--check` ticks nothing, and a run that exits 1 ticks nothing.
**－** A unit whose yaml is not applied whole is not touched.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
