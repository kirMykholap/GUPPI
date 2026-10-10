---
type: decision
case: "273.3"
status: archived
update: ["[[rule-claude-md]]", "[[estimate-claude-md-rendered]]"]
origin: raw/2026-09-20/1308/ledger.md#case-273.3
sprint: migration
created: 2026-09-20
tags: [harness, render]
---

## Context

The Case form is described twice: in `case-schema.md`, a Rule-class file edited by hand and imported into `CLAUDE.md`, and in the Render of `rule-case-protocol`, spliced into the same `CLAUDE.md`. Four of the nine paragraphs of the Render repeat the schema word for word — the form, the operands, the story sections, the sub-cases, the writing of the Spec; every change of the form was signed twice (267 changed both). Five paragraphs stand only in the Render — the Frontier, the acknowledging reply, the harness rendered from `rules/`, `ask-guppi` before a `create`, the ledger mechanics — and the schema does not know them. A session without `/hi` carries all that text although no Case is possible without `/hi`: the ledger hook refuses.
State of the pages: `rule-case-protocol` `built`, `governs: CLAUDE.md`, `partial`, parent `rule-claude-md`; its `estimate-case-protocol-loaded` `pending` from 270.2 — its Criterion is replaced once more here, the sentence of 270.2 inside; the three other Estimates of the rule read the behaviour, not the delivery, and are untouched. `rule-claude-md` `built`, its `estimate-claude-md-rendered` `pending` from 272.1 — replaced a second time here, the text of 272.1 whole. `rule-internal-context` `built`, `estimate-internal-context-loaded` `passed` in the shape before case 193. `rule-plan-mode` a MOC of four children, its Estimates untouched. The Rule-class files `glossary.md` and `index.md` call the schema "imported into CLAUDE.md" — changed by hand. Compaction and subagents are out of scope by the owner's decision.

## Problem

One text in two places, signed twice; a part of the protocol stands only in the system prompt, where nobody reads it as the schema. Where the one text on the Case lives, and when it reaches the session.

## History

- 2026-09-20 created · raw/2026-09-20/1308/ledger.md#case-273.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
