---
type: estimate
kind: QA
status: passed
target: "[[rule-glossary]]"
purpose: glossary, once it wrote glossary.md and exits 0, ticks the guppi glossary lines of every Spec under raw/ whose yaml is applied whole
method: "pytest .guppi/tests/test_glossary.py; by hand, after a librarian's run: the spec.md of its session read against the Criterion"
checked: 2026-11-27
origin: raw/2026-09-22/0014/ledger.md#case-306.6
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Criterion

When:
`uv run --project .guppi guppi glossary` without a flag wrote `vault/wiki/glossary.md` and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

Then:
In the `spec.md` of every unit whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi glossary` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`. Nothing else in the file changes, but the map at the head of an approved document that holds one, which `rule-spec-write` rebuilds.
**＋** The form of the line in `vault/wiki/case-schema.md` is `` - [ ] `uv run --project .guppi guppi glossary` ``, the command in the first code span.
**－** A line that names `guppi glossary` only in a later code span, such as a `read` line, is not ticked.
**－** `--check` ticks nothing, and a run that exits 1 ticks nothing.
**－** A unit whose yaml is not applied whole is not touched.

## Result

2026-11-27, at the /hi of session 2214: uv run --project .guppi pytest .guppi/tests/test_glossary.py 8 passed; by hand, the librarian's run of session 1402 (commit def97898): no task line of vault/raw/2026-11-27/1402/spec.md or vault/raw/2026-11-27/0947/spec.md opens with a code span holding guppi glossary (grep), so the run ticked none, glossary.md unchanged, and the diff of both Specs in that commit is ticks of task lines and the rebuilt map only; the tick clause was not exercised live

## History

- 2026-09-22 created · [[decision-case-306.6]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L63
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out (case 488.3) · [[decision-case-488.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1753/ledger.md#L3
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the method waits for a librarian's run, with no past moment · [[decision-case-875]]
- 2026-11-27 updated: the Criterion replaced whole — nothing else in the file changes but the map of an approved document · [[decision-case-1085.8]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L3
