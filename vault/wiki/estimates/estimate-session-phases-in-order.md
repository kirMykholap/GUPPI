---
type: estimate
kind: QA
status: pending
target: "[[rule-session]]"
purpose: The five phases of a finished session left their marks in the session folder and in git log, ascending in time; a conserved session ends at carry.md
method: by hand at the close of a session — the hi line of the day's log, frontier.md, the approved stamp of spec.md, the Retro commit, handoff.md, the librarian's commit, read in that order
origin: raw/2026-09-22/1121/ledger.md#case-316
sprint: migration
created: 2026-09-22
tags: [session, workflow]
---

## Criterion

Given:
A Rule MOC is a workflow: its children are ordered, the order is the content, and the MOC's Estimate promises the order itself (`rule-rules-schema`).
**＋** A session leaves its marks in `raw/<date>/<hi HHMM>/`: the `hi` line in the day's log, `frontier.md`, `spec.md` with its approved stamp, `handoff.md`; the Retro commit and the librarian's commit in `git log`.
**＋** A session conserved by `/carry` leaves `carry.md` in place of the last three marks (case 190.3).

When:
A session has ended, and someone reads its folder and `git log`.

Then:
All five phases left a mark, and the marks ascend in time: `hi` → `frontier.md` → `spec.md` approved → the Retro commit → `handoff.md` → the librarian's commit.
**＋** `rule-session` is the parent of the five phases, its children in that order.
**－** A session conserved by `/carry` ends at `carry.md`: the marks of Work Mode, End of Work and Documentation are absent, and that is not a failure.

## History

- 2026-09-22 created · [[decision-case-316]]
