---
type: estimate
kind: QA
status: passed
target: "[[rule-session]]"
purpose: The five phases of a finished session left their marks in the session folder and in git log, ascending in time; a conserved session ends at carry.md
method: make test-session, the pipeline over the tests of rule-session's children; then by hand at the close of a session — the hi line of the day's log, frontier.md, the approved stamp of spec.md, the Retro commit, handoff.md, the librarian's commit, read in that order
checked: 2026-10-01
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

2026-10-01, by hand, session 2356: hi at 2026-09-30 23:56:52 in raw/2026-09-30/event_log.md, frontier.md written at 23:58:19, spec.md stamped approved at 02:58:08 on 2026-10-01, the Retro commits f7581b07 at 03:10:35 and 0e65b085 at 03:11:00, handoff.md written at 03:11:35, the librarian's commit 1f43cf1c at 03:18:18, in ascending order; rule-session lists its children rule-session-start, rule-plan-mode, rule-work-mode, rule-end-of-work, rule-documentation in that order

## History

- 2026-09-22 created · [[decision-case-316]]
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out (case 493.4) · [[decision-case-493.4]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L7
- 2026-10-05 updated: the method names make test-session before the reading by hand; the lint finding on a MOC's reading clears (case 641) · [[decision-case-641]]
