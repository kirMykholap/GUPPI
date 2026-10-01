---
type: estimate
kind: QA
status: passed
target: "[[rule-brief]]"
method: one reading by hand after the first librarian run, recorded in the estimate line
checked: 2026-10-01
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
**＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
**＋** Where things stand, Readings due and Readings at the close are as before.
**＋** Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
**＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and add one kind: a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
**＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
**＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
**＋** An item stands in one list only. A list with no item is the line "none".
**＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
**－** The brief states no decision: the sort by kind is not a judgment of the work.

## Result

2026-10-01, by hand at the /hi of session 1725, vault/wiki/brief.md of the librarian's run a264476c over 1441, the first run whose .claude/agents/librarian-guppi.md held the Render of session 1237, read against raw/2026-10-01/1441/handoff.md: five sections in order, no Deferred list and no cap; Readings due 39 lines, each with slug, target and method, the failed one marked, 10 of the target rules checked by grep, all draft; Flags hold the incomplete and near marks, the failed Estimate, MOC candidates none, the 6 stale defers, the handoff's contradiction, the lint output and the line on reads outside the frame; Next session: Cases the 4 lines of For the next session and the handoff's Observation on guppi/casecheck.py; Work the 38 pending slugs of Readings due, the unticked read boxes of specs 1441 (14) and 1237 (4) and the unapplied ledger lines 22 to 27; Ask the person "none" as the handoff; no dirty tree; no decision stated; the lines it shares with the old brief are Readings due lines taken from the Estimate pages; estimate-estimates-schema-checked stands in Work by its reading and in Cases by the question on its test

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
