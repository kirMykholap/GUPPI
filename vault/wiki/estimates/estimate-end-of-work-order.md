---
type: estimate
kind: QA
status: pending
target: "[[rule-end-of-work]]"
origin: raw/2026-09-10/ledger.md#case-38
sprint: migration
created: 2026-09-10
tags: [session, workflow]
---

## Context

The three steps only work in order: a handoff before the commit folds two layers into one diff; a librarian before the handoff has nothing to read.

## Criterion

Given:
The Spec is written by the hook `guppi spec` into the session folder `raw/<date>/<hi HHMM>/spec.md`; the `hi` and the folder are known from the context.
**＋** `generate` appends `rule-carry-over` to the `children` of `rule-end-of-work` from the `ref` of its `create`; the `update` of 190.2 writes no field.
**＋** The methods of the Estimates do not change: `estimate-carry-over-writes` — pytest over the skill's Render and one live reading; `-end-of-work-order` — `make test-end-of-work` and the live reading of the order; `-brief-written` — a reading of the brief by hand.
**－** The entries of 190.x apply before the entries of this Case, in ledger order.

When:
A session ends.

Then:
It ends one of two ways: Work Mode, Retro, the commit, handoff and the librarian — or `/carry` straight after Plan Mode.
**＋** In the ordinary way the order holds: `/handoff` is refused while the tree is dirty; `handoff.md` exists before the librarian is dispatched; no other commit stands between the handoff and the librarian's; `make test-end-of-work` is green.
**＋** On leaving Plan Mode the agent asks which of the two, and starts nothing until it is answered.
**＋** `rule-carry-over` is a child of this MOC, after `rule-handoff`.
**－** The order of the three steps of the ordinary way does not change.

## Method

`make test-end-of-work`, the pipeline over tests/test_gate.py; the live reading of the order by hand

## Result

make test-end-of-work green inside the 132; live 2026-09-10: the refusal on a dirty tree was read in session E at 11:18:24 (retro-commit-gates); this session the tree was clean at /handoff; handoff.md existed at 11:48:15 before the dispatch at 11:48:22; git log shows 893b3d9 (Retro) then 8bbfa10 (librarian) with nothing between

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L88
- 2026-09-16 updated: the Criterion replaced whole by this Case; its earlier blocks recut by point 1 at this touch (case 190.2) · [[decision-case-190.2]]
- 2026-09-16 updated: the Criterion replaced whole by case 196.2 — the head recut with the second end (case 196.2) · [[decision-case-196.2]]
