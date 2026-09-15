---
type: decision
case: "182"
status: current
defer: ["[[rule-plan-mode]]", "[[rule-page-generation]]", "[[rule-materialize]]", "[[rule-lint]]", "[[rule-pretask]]"]
supersedes: ["[[decision-case-178]]"]
origin: raw/2026-09-15/2225/ledger.md#case-182
sprint: migration
created: 2026-09-15
tags: [session, workflow, harness, ledger]
---

## Context

An Estimate today is one page per rule: a head Criterion from the moment of `create`, plus one `### case N` block per `contract: changed`, appended by the script; only `{supersedes:case N}` removes a block; `Result` is overwritten by the last reading of any block; `Method` is one per page although the blocks are checked by a test here and by a reading there. The promise of a rule is written three times — How it works, Render, the blocks — and the copies drift apart (174, 179/181). `rule-page-generation` holds 10 blocks, `rule-materialize` 9. Question 178 — who names the block a new contract removes — is a symptom.

## Problem

Nobody judges an Estimate page as a whole: it is stitched from deltas, and "what the rule promises now" is written nowhere. Session 2225 took this apart down to a model that changes `estimates/schema.md`, `rules/schema.md`, `case-schema.md`, `index.md` §6–§7, `materialize`, `generate`, `lint`, pre-task and the form of Plan Mode — the size of a Slice, not of a Case. The model must be kept whole and run as the Plan Mode of the next session, before 3b: Work Mode leans on "an Estimate is the red test".

## History

- 2026-09-16 created · raw/2026-09-15/2225/ledger.md#case-182
