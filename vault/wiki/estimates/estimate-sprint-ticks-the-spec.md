---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint]]"
purpose: sprint, once it wrote sprint.md and exits 0, ticks the guppi sprint lines of every Spec under raw/ whose yaml is applied whole
method: pytest tests/test_sprint.py, plus one reading of this session's spec.md and the 1957 Spec after the librarian's run
checked: 2026-09-18
origin: raw/2026-09-18/2054/ledger.md#case-250.2
sprint: migration
created: 2026-09-18
tags: [harness, sprint]
---

## Criterion

When:
`guppi sprint` without a flag wrote `vault/wiki/sprint.md` and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

Then:
In the `spec.md` of every unit whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi sprint` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`. Nothing else in the file changes.
**－** A line where `guppi sprint` sits in a later code span, such as a `read` line or a description, is not ticked.
**－** `--check` ticks nothing, and a run that exits 1 ticks nothing.
**－** A unit without a yaml, with an entry not applied, with a `failed` entry, or marked by `carry.md`, is not touched.

## Result

2026-09-18, pytest tests/test_sprint.py (3 tests of the tick, 429 green) and the librarian's `uv run guppi sprint` of commit 3e1251f: the `uv run guppi sprint` lines 37, 103, 137 of the 1957 Spec — a yaml with two `superseded_by` entries — and line 94 of the 2054 Spec ticked; the `read` line that names the command later, the page lines and the render lines untouched; `--check` and exit 1 tick nothing in the tests

## History

- 2026-09-18 created · [[decision-case-250.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-18/2253/ledger.md#L4
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the yaml applied whole stated (case 491.1) · [[decision-case-491.1]]
