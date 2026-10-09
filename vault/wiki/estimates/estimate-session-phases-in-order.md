---
type: estimate
kind: QA
status: passed
target: "[[rule-session]]"
purpose: The five phases of a finished session left their marks in the session folder and in git log, ascending in time; a conserved session ends at carry.md
method: make test-session, the pipeline over the tests of rule-session's children; then by hand at the Retro of the session of case 746 — the marks of the last finished session, the hi line of the day's log, frontier.md, the approved stamp of spec.md, the Retro commit, handoff.md and the commit of its Documentation phase, read in that order, and the children of rule-session as the Spec of case 746 sets them
checked: 2026-10-09
origin: raw/2026-09-22/1121/ledger.md#case-316
sprint: migration
created: 2026-09-22
tags: [session, workflow]
---

## Criterion

When:
A session has ended, and someone reads its folder, the day's event log and `git log`.

Then:
All five phases left a mark, and the marks ascend in time: the `hi` line of the day's event log → `frontier.md` → `spec.md` with its approved stamp → the Retro commit → `handoff.md` → the librarian's commit.
**＋** `rule-session` is the parent of the five phases, its children in that order.
**－** A session conserved by `/carry` ends at `carry.md`: the marks of Work Mode, End of Work and Documentation are absent, and that is not a failure.

## Result

2026-10-09, Retro, make test-session and by hand: make test-session 257 passed; the marks of session 2352 ascend — hi 2026-10-08 23:52:45 (event_log), frontier.md written 23:53:19, spec.md approved 01:21:17, Retro commit 418b4000 01:32:37, handoff.md written 01:33:57, librarian commit 22b7613c 01:40:02; the Spec of case 746 sets the children of rule-session to the five phases in order: rule-session-start, rule-plan-mode, rule-work-mode, rule-end-of-work, rule-documentation

## History

- 2026-09-22 created · [[decision-case-316]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out (case 493.4) · [[decision-case-493.4]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L7
- 2026-10-05 updated: the method names make test-session before the reading by hand; the lint finding on a MOC's reading clears (case 641) · [[decision-case-641]]
- 2026-10-09 updated: sent back for a reading at the Retro of the session of case 746, the Criterion unchanged: rule-session listed the two sprint skill pages among its children (case 746.1) · [[decision-case-746.1]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/0200/ledger.md#L16
