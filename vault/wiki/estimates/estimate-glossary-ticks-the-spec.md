---
type: estimate
kind: QA
status: pending
target: "[[rule-glossary]]"
purpose: glossary, once it wrote glossary.md and exits 0, ticks the guppi glossary lines of every Spec under raw/ whose yaml is applied whole
method: pytest tests/test_glossary.py, plus one reading of this session's spec.md after the librarian's run
origin: raw/2026-09-22/0014/ledger.md#case-306.6
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Criterion

When:
`uv run guppi glossary` without a flag wrote `vault/wiki/glossary.md` and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

Then:
In the `spec.md` of every unit whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi glossary` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`. Nothing else in the file changes.
**＋** The form of the line in `vault/wiki/case-schema.md` is `` - [ ] `uv run guppi glossary` ``, the command in the first code span.
**－** A line that names `guppi glossary` only in a later code span, such as a `read` line, is not ticked.
**－** `--check` ticks nothing, and a run that exits 1 ticks nothing.
**－** A unit whose yaml is not applied whole is not touched.

## Result

2026-09-22, uv run pytest tests/test_glossary.py, 8 passed: the plain run ticks the unticked task lines opening with a code span holding guppi glossary in the spec.md of an applied unit, leaves a read line naming the command later, a sprint line and an unapplied unit alone; --check ticks nothing; the live reading of this session's spec.md after the librarian's run not taken

## History

- 2026-09-22 created · [[decision-case-306.6]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L63
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out (case 488.3) · [[decision-case-488.3]]
