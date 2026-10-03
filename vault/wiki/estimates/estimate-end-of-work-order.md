---
type: estimate
kind: QA
status: passed
target: "[[rule-end-of-work]]"
purpose: "A session ends one of two ways, and the ordinary way keeps its order: the commit before /handoff, handoff.md before the librarian, no commit between the handoff and the librarian's"
method: "make test-end-of-work, plus by hand at the close of a later session: its folder, the day's event log and git log"
checked: 2026-10-03
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
**＋** A session that took a conserved Spec at the Frontier is asked nothing on leaving Plan Mode: `/box` runs the ordinary way on the branch of that Spec, and the shared branch takes that branch by a fast-forward after `handoff.md` exists and before the librarian is dispatched.
**＋** `rule-carry-over` is a child of `rule-end-of-work`, after `rule-handoff`.
**＋** `rule-spec-box` is a child of `rule-end-of-work`, after `rule-retro-onward`.

## Result

2026-10-03, `make test-end-of-work` 30 passed; by hand, the close of session 0115 read in vault/raw/2026-10-03/0115/, the event log vault/raw/2026-10-03/event_log.md and git log: ExitPlanMode 02:59:42, AskUserQuestion 02:59:48, then /work, retro 03:05:39, the work commit f510fb46 03:06:37 and the session-folder commit 2f0591a3 03:07:01, handoff 03:07:02 on a clean tree, handoff.md written 03:07:39 before the librarian's run, the librarian's commits f1a46df1 03:13:32 and 9b821b2b 03:14:09 with no other commit between the handoff and them; `rule-end-of-work` children hold rule-carry-over after rule-handoff and rule-spec-box after rule-retro-onward; not exercised: a /handoff refused on a dirty tree, and a session that took a conserved Spec

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L88
- 2026-09-16 updated: the Criterion replaced whole by this Case; its earlier blocks recut by point 1 at this touch (case 190.2) · [[decision-case-190.2]]
- 2026-09-16 updated: the Criterion replaced whole by case 196.2 — the head recut with the second end (case 196.2) · [[decision-case-196.2]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L2
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out, the green run of make test-end-of-work into method; purpose and method set, Context and Method out (case 499.1) · [[decision-case-499.1]]
- 2026-10-02 updated: the Criterion replaced whole — a box session is asked nothing on leaving Plan Mode, its branch merged back by a fast-forward before the librarian; rule-spec-box the last child (case 591.4) · [[decision-case-591.4]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/0317/ledger.md#L53
