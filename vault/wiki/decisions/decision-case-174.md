---
type: decision
case: "174"
status: current
update: ["[[estimate-generate-writes]]", "[[estimate-cleanup-moves]]", "[[rule-ledger-write]]"]
origin: raw/2026-09-15/1809/ledger.md#case-174
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger, session, hooks]
---

## Context

`estimate-generate-writes` and `estimate-cleanup-moves` are the Estimate pages of `rule-page-generation` and `rule-cleanup`. Their Criterion is a head text — the criterion signed at creation (cases 32, 33) and edited directly in case 57 — and `### case N` blocks, one per contract change. A `supersedes` removes a block only; nobody touches the head. `rule-ledger-write` describes the second refusal of `guppi gate` — a Spec item without its ledger line — and quotes its text whole. Since 169.1 the gate has two texts: for the agent "end this reply in text with the LEDGER block, then call /<skill> in the next reply", for the person "Ask the agent to end its reply with the LEDGER block, then type /<skill> again".

## Problem

Three texts contradict ratified contracts. The head of `estimate-generate-writes` asks for `## Children` and `## Estimates`, which 166.2 removed. The head of `estimate-cleanup-moves` asks for "their sections" when a slug leaves (removed by 166.4) and "the four category indexes are rewritten" (removed by 147.6). `rule-ledger-write` quotes one refusal text where the gate has two. The readings of 166.2 and 166.4 stand in F1 and read the whole page; the reader meets a head that says one thing and a block that says the opposite. This is the pattern of `insight-workflow-contract-change-leaves-its-derived-text-stale` (`actioned`), left in the handoff of session R as F17.

## Given

`estimate-generate-writes`, head Criterion: "the parent's children and ## Children in order, the target's estimates and ## Estimates" — once on the page; block 166.2 says no section is derived from a ref field.
**＋** `estimate-cleanup-moves`, head Criterion: "its slug leaves the children lists of live pages and the estimates lists of entities and rules, and their sections, with a History line there" and "the four category indexes are rewritten without the moved page, and an archived Estimate leaves no line anywhere" — once each; block 147.6: no index is written; block 166.4: the field only, no section rebuilt.
**＋** `rule-ledger-write`, How it works: one quoted refusal text — the advice to the agent; `guppi/gate.py` prints `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B).` and then one of two advices by `typed(payload)`.
**＋** `generate` applies `replace` on a page of any category: `old` matched whitespace-insensitive over every section but History, exactly one hit (case 57 edited `estimate-cleanup-moves` the same way).
**＋** Both Estimates are `pending` already (blocks 166.2, 166.3, 172 and 166.4); their reading is F1, over the whole page.
**－** No contract changes: an Estimate page has none, `rule-ledger-write` is `contract: same`; no `### case 174` block appears.

## History

- 2026-09-15 created · raw/2026-09-15/1809/ledger.md#case-174
