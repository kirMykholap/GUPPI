---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: Whether generate leaves every line of the sprint page in place, a milestone item put off in many sessions in a row included, so that a line moves only by a Case
method: "uv run --project .guppi pytest .guppi/tests/test_generate.py -k moves_no_line; then by hand, the History of entity-sprint-<id> after the librarian's run of a later session: no line of generate on a move"
checked: 2026-09-30
origin: raw/2026-09-23/0034/ledger.md#case-354.1
sprint: migration
created: 2026-09-23
tags: [sprint, harness]
---

## Criterion

When:
`uv run --project .guppi guppi generate` runs over the vault with one live page `entity-sprint-<id>`, and the `frontier.md` of three or more sessions in a row, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names an item of its `## Milestones` in a code span.

Then:
After the run, `## Milestones` and `## Backlog` of `entity-sprint-<id>` stand as before it, each line in its place, unless an entry of the run changes the page.
**＋** A milestone whose items were all put off keeps its heading under `## Milestones`.
**＋** `.guppi/guppi/generate.py` writes no line about a move into the History of `entity-sprint-<id>`, and it prints no such line on stdout.
**＋** A line of `entity-sprint-<id>` moves only through an entry of a Case the person ratified, an `update` that `generate` applies like any other.
**－** `rule-sprint` and `rule-page-generation` name no move of a sprint line by `generate`.

## Result

2026-09-30, uv run pytest -q tests/test_generate.py -k moves_no_line: 1 passed, 95 deselected; git blame of the History of entity-sprint-migration: the four move lines come from 519c5bc, the librarian run before 417ceaa built case 539.3; the librarian run cfcfb09 after it added one line, the update of case 539.3, and no move line; ## Milestones keeps Slice 5 and its item

## History

- 2026-09-23 created · [[decision-case-354.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L35
- 2026-09-27 updated: the Criterion replaced whole — a line put off under the closers of case 451, Given lifted into When and Then (case 451.7) · [[decision-case-451.7]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L29
- 2026-09-30 renamed from `estimate-sprint-moves-a-passed-over-item` · [[decision-case-539.1]]
- 2026-09-30 updated: renamed from estimate-sprint-moves-a-passed-over-item and the Criterion replaced whole — generate moves no line of the sprint page (case 539.1) · [[decision-case-539.1]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1306/ledger.md#L2
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
