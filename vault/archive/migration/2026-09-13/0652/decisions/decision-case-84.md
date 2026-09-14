---
type: decision
case: "84"
status: archived
defer: ["[[rule-claude-md]]", "[[rule-render-harness]]"]
superseded_by: ["[[decision-case-88.1]]", "[[decision-case-88.2]]"]
origin: raw/2026-09-12/ledger.md#case-84
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Context

`estimate-claude-md-rendered` (case 59.8) says the first render leaves a `git diff` of
marker lines only; `estimate-render-harness-reproduces` (case 59.7) says `git diff
--stat` shows only the two dropped marker lines of `hi/SKILL.md`. A full render drops
the outer markers by design, and the librarian's run of session I wrote Cases 59.2,
59.5, 59.6, 59.7, 62 and 66 into the Rule pages after the clauses were written; at the
render of session J both readings failed on those clauses and on nothing else
(`lesson-estimates-live-clause-stale-at-first-render`). `rule-claude-md` and
`rule-render-harness` stay `draft`.

## Problem

The live clauses have to say what a render of the current pages leaves in the tree:
`render --check` exits 0, the diff equals the Renders of the pages that changed since
the last render, no more. An `update` of the two Estimates through their Rules; the
next Plan Mode, under the derived-Criterion scheme of case 72.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-84
- 2026-09-12 superseded by decision-case-88.1 · [[decision-case-88.1]]
- 2026-09-12 superseded by decision-case-88.2 · [[decision-case-88.2]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
