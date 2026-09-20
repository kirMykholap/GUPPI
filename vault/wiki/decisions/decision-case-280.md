---
type: decision
case: "280"
status: current
update: ["[[rule-page-generation]]", "[[estimate-generate-ticks-the-spec]]"]
origin: raw/2026-09-20/1749/ledger.md#case-280
sprint: migration
created: 2026-09-20
tags: [harness, workflow, ledger]
---

## Context

`generate`, once it applied an `estimate` entry of the yaml, ticks the first unticked line `- [ ] read `<slug>`` — in the Spec beside the yaml first, then in the Specs of the other sessions of `raw/`, oldest first (270.1). "Own Spec first" is right when the reading came after the Case that set the Estimate `pending`. It goes wrong when the reading stands earlier in the ledger: in 1308 the reading of `estimate-documentation-completes` was line 8, Case 271 of the same session later replaced the Criterion and added its own `read` line (188) — and `generate` ticked that one, not 0958:308, the line the reading was made for. The Estimate stayed `pending` by 271 and line 308 open: the count held, but the ticked line belongs to a Case whose Criterion nobody read, and the debt left the Retro of 1308 for another session's Spec. This session repeats it: the reading of `estimate-case-protocol-loaded` (`failed`, ledger line 6) precedes 279.1, and the Spec beside the yaml carries the `read` line of 279.1 — today's run would tick it instead of 1308:98.
`rule-page-generation` `draft` (`estimate-generate-rewords` pending); `estimate-generate-ticks-the-spec` (`passed`) touched, the other seven Estimates of the rule not. A yaml entry carries `line` — the number of its ledger line — and a decision entry `case`; an `update` with a `ref`, no vault query due.

## Problem

A reading recorded before a Case closes the line of that Case. `generate` needs a mark by which it tells the line of a Case ratified after the reading.

## History

- 2026-09-20 created · raw/2026-09-20/1749/ledger.md#case-280
