---
type: decision
case: "196.2"
status: current
update: ["[[rule-end-of-work]]", "[[estimate-end-of-work-order]]"]
origin: raw/2026-09-16/1651/ledger.md#case-196.2
sprint: migration
created: 2026-09-16
tags: [session, workflow]
---

## Context

Case 190 ratified a second end of a session: `rule-carry-over` — a new Leaf, `enforcement: render`, `governs: .claude/skills/carry/SKILL.md`, with the Estimate `estimate-carry-over-writes`; `rule-end-of-work` gets the second end and a new child; `rule-brief` a second writer; `rule-spec-capture` the fork in the context; `rule-materialize` the skip (closed by case 194). But the block of 190.1 carries no `sections: Render` — the text of the skill is signed by nobody; 190.2, 190.4 and 190.5 carry `change` only; `estimate-end-of-work-order` and `estimate-brief-written` stand `pending` with no new Criterion. The `status: draft` and `parent` in the block of 190.1 are overwritten by `generate` with its own values — no harm, nothing to fix. The skill is not typed by the person: the hook of `guppi spec` prints the fork, the agent asks, and on "conserve" the agent calls the skill. `carry.md` is a flag for `materialize`, not a document: its presence in the session folder tells the walk which unit to pass by (case 190.3). This Case touches `estimate-carry-over-writes` and `estimate-end-of-work-order`; it touches `estimate-brief-written` as the Estimate of the live reading of the Render of `rule-brief` without replacing its Criterion — that is Case 197; it does not touch `estimate-spec-capture-offers-the-fork` (its Criterion is 190.5), `estimate-spec-capture-appends` or `estimate-materialize-skips-a-carried-over-unit`.

## Problem

`/carry` is the first thing built in this session and the only exit if Work Mode does not fit in the context; without its Render text there is no skill, and without a Criterion the two `pending` Estimates cannot be read. The question: what text each of the four pages carries, and how the promises of the old Estimates read after the recut.

## Given

The Spec is written by the hook `guppi spec` into the session folder `raw/<date>/<hi HHMM>/spec.md`; the `hi` and the folder are known from the context.
**＋** `generate` appends `rule-carry-over` to the `children` of `rule-end-of-work` from the `ref` of its `create`; the `update` of 190.2 writes no field.
**＋** The methods of the Estimates do not change: `estimate-carry-over-writes` — pytest over the skill's Render and one live reading; `-end-of-work-order` — `make test-end-of-work` and the live reading of the order; `-brief-written` — a reading of the brief by hand.
**－** The entries of 190.x apply before the entries of this Case, in ledger order.

## History

- 2026-09-16 created · raw/2026-09-16/1651/ledger.md#case-196.2
