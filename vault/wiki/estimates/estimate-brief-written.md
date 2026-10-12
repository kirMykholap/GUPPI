---
type: estimate
kind: QA
status: passed
target: "[[rule-brief]]"
method: "by hand at the Retro of the session that changes it: the new Render of rule-brief in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-12
origin: raw/2026-09-10/ledger.md#case-35.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Criterion

When:
The librarian rewrites `vault/wiki/brief.md` at the end of its run.

Then:
The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
**＋** It holds no Deferred list and no cap on deferred items; they stand in `vault/wiki/backlog.md`. Where things stand, Readings due and Readings at the close are as before, and Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
**＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
**＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, an item in one list only, a list with no item the line "none". `Cases` is what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags, one between pages that stand in `vault/archive/` too, a defect the librarian found, with what and from where; and, for each line of `## Debt` of `handoff.md` that names an Estimate whose reading cannot be taken yet, but one of the live sprint page, one whose `method` names the close of a sprint and one whose `method` waits for an event the librarian has not seen, one line that names the Estimate by slug and proposes to defer it into `vault/wiki/backlog.md`.
**＋** `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, one whose `method` names the close of a sprint — the session that closes a sprint, its librarian's run or the session after it —, one whose `method` waits for an event the librarian has not seen, one that a line of `Cases` proposes to defer and one of an Estimate with `deferred_by`; the unticked boxes of the Specs but the `read` box of such a reading; a ledger line this run did not apply, a dirty tree.
**＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint. A check of the live sprint page whose `method` names the person's answer stands there once the Retro of the session that finished its work named it in `handoff.md`.
**＋** In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer.
**＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
**－** A reading left out of `Work` and `Ask the person` keeps its line under Readings due.
**－** A reading whose `method` waits for an event — a part of it between two `;` that opens with `after`, or with `by hand, after`, and names the event before a colon — stands in Readings due alone until the librarian sees that event in `git log`, in the ledger or `handoff.md` of the session, or in the files its `method` names; then it stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer.
**－** A contradiction of Flags that a line of `## For the next session` of `handoff.md` already carries gets no second line in `Cases`.
**－** The brief states no decision: the sort by kind is not a judgment of the work.

## Result

2026-10-12, by hand at the Retro of session 1604: the new Render of rule-brief in raw/2026-10-12/1604/spec.md (Case 781.5, three replace pairs) read against the Criterion — Cases gains one defer line per Debt Estimate whose reading cannot be taken but for the sprint page, the close of a sprint and an event not seen; Work leaves out an event not seen, a reading Cases proposes to defer and an Estimate with deferred_by; an event reading stands in Readings due alone until the librarian sees the event in git log, the ledger, handoff.md or the files its method names, then under Work or Ask the person.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L92
- 2026-09-14 criterion: case 124.1 added · [[decision-case-124.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L5
- 2026-09-14 status: passed → passed · raw/2026-09-14/1633/ledger.md#L1
- 2026-09-15 criterion: case 168 added · [[decision-case-168]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L3
- 2026-09-16 updated: the Criterion replaced whole by this Case; its earlier blocks recut by point 1 at this touch (case 190.4) · [[decision-case-190.4]]
- 2026-09-16 updated: the Criterion replaced whole by case 197 — the head, 124.1 and 168 recut into one; the short shape of /carry left to estimate-carry-over-writes (case 197) · [[decision-case-197]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L3
- 2026-09-17 updated: the last line of the Criterion — a change of the sprint is a Case, never the librarian's edit; the sprint flag lands in Flags (case 209.6) · [[decision-case-209.6]]
- 2026-09-18 updated: the Deferred line — never a target the sprint page names (case 229.4) · [[decision-case-229.4]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L3
- 2026-09-20 updated: the Criterion replaced whole — six sections, Next session with the lists Cases and Work (case 268.1) · [[decision-case-268.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L9
- 2026-09-23 updated: the Criterion names the Flags line of a move to the Backlog (case 354.4) · [[decision-case-354.4]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L38
- 2026-09-27 updated: the Criterion replaced whole — no Deferred list, the deferred items in backlog.md (case 451.8) · [[decision-case-451.8]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L25
- 2026-09-30 updated: the Criterion replaced whole — Next session holds Cases, Work and Ask the person; Cases take For the next session of handoff.md (case 531.10) · [[decision-case-531.10]]
- 2026-09-30 updated: the Criterion replaced whole — the brief of carry keeps Next session, Work and Ask the person from the open lines of frontier.md and Cases the line none; Flags no longer name the moves of generate that case 539 removes · [[decision-case-538.2]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L1
- 2026-09-30 updated: the Criterion replaced whole — Flags hold a line for each read of the librarian beyond the reads its frame names (case 558.3) · [[decision-case-558.3]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L1
- 2026-10-01 updated: the Criterion replaced whole — Flags hold a line for each read the frame says the job does not need; Readings due takes the status, target and method fields (case 567.2) · [[decision-case-567.2]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1725/ledger.md#L2
- 2026-10-04 updated: the Criterion replaced whole — after a close, the first Cases line opens the next sprint (case 628.8) · [[decision-case-628.8]]
- 2026-10-10 status: pending → failed · raw/2026-10-10/1713/ledger.md#L2
- 2026-10-10 updated: the Criterion replaced whole — Cases hold each contradiction of Flags, one between archived pages too, once; read by the person's answer on the brief after a sprint close (case 761) · [[decision-case-761]]
- 2026-10-10 updated: the Criterion replaced whole — Work and Ask the person leave out a reading that waits for a moment of the sprint, its read box included; the method reads it too · [[decision-case-772.1]]
- 2026-10-12 updated: the Criterion replaced whole — a reading that waits for an event stays in Readings due until the librarian sees it, a reading its session did not take is a Cases line that proposes a defer, and a deferred Estimate stays out of Work · [[decision-case-781.5]]
- 2026-10-12 status: pending → passed · raw/2026-10-12/1604/ledger.md#L25
