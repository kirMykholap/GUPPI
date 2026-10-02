---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
method: one reading by hand at the first /retro, and one at the first /retro of a session that /box runs, recorded in the estimate line
checked: 2026-09-30
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

Then:
A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built — rendered, written, run.
**＋** An Estimate that this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — gets no reading in this session, built or not; the handoff names it as a reading of a later session.
**＋** The `read` line of its old Criterion in an earlier Spec is not read; the reading of the new Criterion closes it in a later session, at the moment its `method` names.
**＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec of this session is the `spec.md` of the folder that section names: Retro sorts its boxes, and the decision lines of that folder's `ledger.md` count as this session's for those boxes, for the scope of an edit and for the readings above.
**－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

## Result

2026-09-30, the /retro of session 2042 by hand: it read no Estimate that a decision line of this session creates or updates, the new four and estimate-retro-onward-sends-the-agent-to-the-handoff left to a later session, and took readings only of Estimates whose work is built

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
- 2026-09-21 status: pending → passed · raw/2026-09-21/0019/ledger.md#L21
- 2026-09-25 updated: the Criterion replaced whole — an Estimate the session creates or updates gets no reading at its Retro, built or not (case 428.3) · [[decision-case-428.3]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L36
- 2026-09-30 updated: the Criterion replaced whole — the trigger is the agent's call at the end of /work or the typed /retro; the readings rule is unchanged (case 531.2) · [[decision-case-531.2]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/2042/ledger.md#L35
- 2026-10-02 updated: the Criterion replaced whole — in a session that /box runs, the conserved Spec counts as this session's work (case 591.8) · [[decision-case-591.8]]
