---
type: insight
pattern: A Case is composed from what the agent has in view — the dialogue, the rule page, the code — and the pages it changes or runs beside are not read against it before it is shown, so a contradiction with them is found only by a later check, pre-task or pre-spec.
status: open
children: ["[[lesson-plan-mode-contract-change-skips-the-estimates-blocks]]", "[[lesson-case-designed-in-dialogue-not-checked-against-its-rules]]"]
severity: 2
origin: raw/2026-09-23/1859/ledger.md#L30
sprint: migration
created: 2026-09-23
tags: [workflow, harness, session]
---

## Pattern

A Case is composed from what the agent has in view — the dialogue, the rule page, the code — and the pages it changes or runs beside are not read against it before it is shown, so a contradiction with them is found only by a later check. In session 1809 of 2026-09-15 Cases 175 and 164 changed the contract of a rule without reading the Estimate pages that take the new block; ask-guppi at pre-task found the contradicting blocks (`lesson-plan-mode-contract-change-skips-the-estimates-blocks`). In session 1859 of 2026-09-23 Case 387 was written in one pass from the discussion; the rules it touches and the order in which its hooks run were not read against it, and pre-spec found eight contradictions (`lesson-case-designed-in-dialogue-not-checked-against-its-rules`).

## Proposal

A suggestion, not a decision: before a Case that changes a contract or adds a hook is shown, the agent could list the pages its tasks touch or run beside — the Estimates of the rule, the rules it names, the hooks on the same event — and read each against the Case, so the contradiction is found before the showing, not by the check after ratification.

## History

- 2026-09-24 created · raw/2026-09-23/1859/ledger.md#L30
