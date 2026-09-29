---
type: estimate
kind: QA
status: pending
target: "[[rule-brief]]"
method: one reading by hand after the first librarian run, recorded in the estimate line
checked: 2026-09-27
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
**＋** Where things stand, Readings due, Flags and Readings at the close are as before. Flags also name every item `generate` moved to the sprint page's Backlog in the run, and every milestone it dropped.
**＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
**＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
**＋** An item stands in one list only. A list with no item is the line "none".
**－** The brief states no decision: the sort by kind is not a judgment of the work.
**－** The brief of the skill `carry` keeps its short shape, without Next session and without a Deferred list. `rule-brief` and `rule-carry-over` both say so.

## Result

2026-09-27, vault/wiki/brief.md of the librarian's run over 1819 (049458e) read by hand against raw/2026-09-27/1819/handoff.md; five sections in order, no Deferred list, Flags name no Backlog move and no dropped milestone; Next session: Cases 3, Work 33 Estimate slugs plus the 20 unticked read boxes, ledger lines 8–10 and the dirty tree, no item in both lists

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
