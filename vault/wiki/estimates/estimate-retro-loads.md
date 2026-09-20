---
type: estimate
kind: QA
status: pending
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
Retro takes the readings of this session's Estimates whose work is finished and writes their lines; `generate` applies the entries of the yaml in ledger order — an `estimate` entry sets `status` and overwrites the Result (case 53.2); `built` is computed once every Estimate is `passed`.
**＋** An `update` of an Estimate replaces its Criterion whole and sets `pending`; the render of a Rule comes with the librarian, after Retro.
**＋** `estimate-retro-loads` is read by hand at the first `/retro` after the render.

When:
The person invokes `/retro`, and the agent takes the readings of the session's Estimates.

Then:
A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built — rendered, written, run.
**＋** An Estimate whose Criterion a Case of this session replaced, and whose build is not finished at Retro, gets no reading in this session: the `read` line of the old Criterion in an earlier Spec is not debt and is not read; the reading of the new Criterion closes it, at the moment its `method` names; the handoff names the Estimate as one whose reading cannot be taken yet.
**－** Nothing in `generate` changes: an `update` and a reading of one slug in one session apply in ledger order, and the reading of a Criterion built in the session sets its status.
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
- 2026-09-21 updated: the Criterion replaced whole — a replaced Criterion is not read at the Retro of its session; the reading of 270.3 written after 282 undone by this pending (case 283) · [[decision-case-283]]
