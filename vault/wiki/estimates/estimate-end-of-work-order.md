---
type: estimate
kind: QA
status: pending
target: "[[rule-end-of-work]]"
purpose: "A session ends one of two ways, and the ordinary way keeps its order: the commit before /handoff, handoff.md before the librarian, no commit between the handoff and the librarian's"
method: "make test-end-of-work, plus by hand at the close of a later session: its folder, the day's event log and git log"
checked: 2026-09-16
origin: raw/2026-09-10/ledger.md#case-38
sprint: migration
created: 2026-09-10
tags: [session, workflow]
---

## Criterion

When:
A session ends, and someone reads its folder `vault/raw/<date>/<hi HHMM>/`, the day's event log `vault/raw/<date>/event_log.md` and `git log`.

Then:
The session ended one of two ways: Work Mode, Retro, the commit, the handoff and the librarian; or `/carry` straight after Plan Mode.
**＋** In the ordinary way the order holds: `/handoff` is refused while the tree is dirty; `handoff.md` exists before the librarian is dispatched; no other commit stands between the handoff and the librarian's commit.
**＋** On leaving Plan Mode the agent asks the person which of the two ends, and starts nothing until it is answered.
**＋** `rule-carry-over` is a child of `rule-end-of-work`, after `rule-handoff`.

## Result

2026-09-16, make test-end-of-work (30 passed) and the event log of session 1955: retro 22:14:35, commit 8fd804e 22:18:59, handoff 22:19:10 on a clean tree, handoff.md written 22:19:47 before the dispatch, the librarian's commit ebaef1e 22:25:58 with nothing between; rule-carry-over a child after rule-handoff

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L88
- 2026-09-16 updated: the Criterion replaced whole by this Case; its earlier blocks recut by point 1 at this touch (case 190.2) · [[decision-case-190.2]]
- 2026-09-16 updated: the Criterion replaced whole by case 196.2 — the head recut with the second end (case 196.2) · [[decision-case-196.2]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L2
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out, the green run of make test-end-of-work into method; purpose and method set, Context and Method out (case 499.1) · [[decision-case-499.1]]
