---
type: decision
case: "90.1"
status: current
update: [rule-materialize]
origin: raw/2026-09-12/ledger.md#case-90.1
sprint: migration
created: 2026-09-12
tags: [harness, workflow, ledger]
---

## Context

Today's reading of `estimate-documentation-completes` failed on one clause: the librarian
edited yaml entries by hand. There were three, and the handoff asked for all of them. Two
were needed because of a defect of `materialize`: the derived entry takes the first
Estimate of the page, and `None` when the page has none. The third is gone with case 87.

## Problem

Two things. A script guesses which Estimate a Case changes instead of asking. And an
instruction of the handoff that the librarian's own Rule forbids reaches it with the
authority of the person's session, and is carried out.

## Given

`derived_entries`, the `update` branch: `"slug": estimates[0] if estimates else None`. The
`create` branch beside it already reads `item.get("estimate_slug")`, and `DERIVED_KEYS`
already keeps that key off the target page — on an `update` it is simply not read.
**＋** Both of the librarian's repairs are of this class: case 73.10 had `slug: null`
(`rule-claude-md` had an empty `estimates` list when materialize ran) and case 73.3 had
`estimate-hi-no-read-calls` where the Case changed `estimate-hi-writes-frontier`, because
the first of `rule-skill-hi`'s two Estimates is not the one that moved.
**＋** Four pages carry two Estimates: `rule-materialize`, `rule-page-generation`,
`rule-render-harness`, `rule-skill-hi`. Three contracts of this session hit two of them —
case 87 on `rule-materialize`, 88.1 and 89.4 on `rule-render-harness` — and each time the
first of the list was the right one by chance, not by guarantee.
**＋** `pretask --check` already carries the four form findings of case 72.5: a Leaf
`create` without `method`, a Leaf `update` without `contract`, two contracts in one Case,
a colliding derived slug. This is the fifth of that family.
**＋** The criterion of `estimate-documentation-completes` says the librarian edits the
yaml only as the index check and the synthesis say; case 44 put yaml repairs in the
forbidden set by name. The librarian takes the handoff as its first input and as its list
of instructions, and nothing checks the handoff against that criterion.
**－** The repairs were useful in themselves: without them two pages would be wrong. After
90.1 and 90.2 they are not needed; until then the price of a refusal is a wrong entry that
the next Plan Mode fixes, instead of a hand nobody signed.

## Criterion

- [[estimate-materialize-assembles]] § case 90.1

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-90.1
