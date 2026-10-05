---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
method: by hand, the text of .claude/skills/retro/SKILL.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-retro in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-10-04
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

Then:
A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built.
**＋** Each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — is read in the reply that ends Retro, on the Criterion of `raw/<date>/<hi HHMM>/spec.md`: the `when` and `then` of its Case, or the Criterion its item writes.
**＋** For an Estimate of a rule whose Render a Case of the Spec changes, the reading reads the new text of the Render in `raw/<date>/<hi HHMM>/spec.md` against that Criterion.
**＋** Each such Estimate that Retro cannot read gets a `failed` line in the same `LEDGER` block, whose result opens with the date and says that Retro did not read it and why.
**＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as this session's for its boxes, for the scope of an edit and for the readings above.
**＋** Retro closes the open `W` line of each Estimate it reads or sets `failed` `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`.
**－** An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`.
**－** A reading whose `method` names the person's word is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question, and its `read` line is neither debt nor the librarian's.
**－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

## Result

2026-10-04, at the /hi of session 0004, by hand: the /retro of session 0317 (transcript 5b311f89, 05:04:23 to 05:05:59): its two readings, `estimate-case-build-writes-the-case` and `estimate-end-of-work-order`, are Estimates no decision line of raw/2026-10-03/0317/ledger.md names, while 27 of the 35 open W lines of its frontier.md name an Estimate a decision line of that ledger updates and none of them got a reading; handoff.md names the `read` lines of the session's own slugs under Debt and the 37 method rewrites of 613.3 as readings of later sessions; the /retro of session 1416 (transcript 682b0e2f, 14:39:41 to 14:40:43), work.md naming vault/raw/2026-10-03/1341/ under `## Conserved Spec`: handoff.md sorts the boxes of that folder's spec.md — one box waiting for the librarian, the `create` of `entity-reading-probe`, and no `read` line of a slug the session creates or updates —, and its two readings, `estimate-hi-takes-a-conserved-spec` and `estimate-spec-capture-offers-the-fork`, are Estimates no decision line of the 1341 or 1416 ledger names

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
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L2
- 2026-10-05 updated: the Criterion replaced whole — Retro reads each Estimate the session creates or updates on the Criterion of the Spec, or sets it failed (case 670.2) · [[decision-case-670.2]]
