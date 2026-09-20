---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
method: one reading by hand at the first /retro, recorded in the estimate line
checked: 2026-09-20
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Criterion

Given:
Retro runs before the librarian; `generate` after it ticks the page lines and the `read` lines whose reading stands in the ledger, `render` and `sprint` the render and sprint lines (cases 226, 250, 270.1).
**＋** A ledger line `{supersedes:case N}` marks every entry of Case N `superseded_by`; `generate` neither applies nor ticks them (200.2).

When:
The person invokes `/retro`, and the agent counts the unticked `tasks` of the Spec.

Then:
A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the ledger of this session are listed as waiting for the librarian and end in none of the four ways; every other unticked line is debt, as today.
**＋** The lines of a Case a `{supersedes:case N}` line of this session's ledger names are not counted: its work stands under the superseding Case.
**－** A `read` line without its line in the ledger is debt: the reading was not done.
**－** Nothing else in Retro changes.

## Result

2026-09-20, the /retro of session 1749 read by hand, the Criterion of 270.3 — the SKILL rendered before 282: the unticked lines of raw/2026-09-20/1749/spec.md counted per Case; the update, create, defer and uv run guppi render lines and the read lines whose estimate[...] stands in the Tail (129, 220) listed as waiting for the librarian, ending in none of the four ways; the read lines without a line in the Tail (88, 179) counted as debt and carried to the handoff; the two lines of the superseded 278 (38, 39) left out of the count by 282, ratified this session and not yet rendered — the one departure from the text of 270.3; nothing else of Retro changed

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L86
- 2026-09-11 updated: the frontier, the four outcomes, the readings and the red-test paths added; pending until the next live /retro · [[decision-case-56]]
- 2026-09-12 updated: the Deferred heading (cases 59.5, 66) · [[decision-case-66]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L106
- 2026-09-12 criterion: case 73.6 added · [[decision-case-73.6]]
- 2026-09-13 criterion: case 109.1 added · [[decision-case-109.1]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/0747/ledger.md#L50
- 2026-09-14 criterion: case 126 added · [[decision-case-126]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/1029/ledger.md#L41
- 2026-09-14 status: failed → passed · raw/2026-09-14/1229/ledger.md#L30
- 2026-09-14 criterion: case 150 added · [[decision-case-150]]
- 2026-09-15 status: pending → failed · raw/2026-09-15/1110/ledger.md#L26
- 2026-09-15 criterion: case 169.3 added · [[decision-case-169.3]]
- 2026-09-15 criterion: case 150 removed · [[decision-case-169.3]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L14
- 2026-09-18 updated: the Criterion replaced whole — the page and render lines are not debt (case 233.2) · [[decision-case-233.2]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L37
- 2026-09-18 updated: the Criterion replaced whole — a guppi sprint line waits for the librarian too (case 253.2) · [[decision-case-253.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0527/ledger.md#L22
- 2026-09-20 updated: the Criterion replaced whole — the read line with its ledger line waits for the librarian (case 270.3) · [[decision-case-270.3]]
- 2026-09-20 updated: the Criterion replaced whole — the lines of a superseded Case are not counted (case 282) · [[decision-case-282]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L20
