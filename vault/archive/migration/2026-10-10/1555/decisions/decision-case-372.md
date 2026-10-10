---
type: decision
case: "372"
status: archived
update: ["[[rule-rules-schema]]", "[[estimate-rules-schema-checked]]"]
origin: raw/2026-09-23/1126/ledger.md#case-372
sprint: migration
created: 2026-09-23
tags: [harness, render, schema]
---

## Context

The rules schema (`rule-rules-schema`, its Render `vault/wiki/rules/schema.yaml`) asks of a Rule a guard that refuses a case; Enforcement says "A constraint that no hook, check or render can detect is not a Rule at all", and the same schema counts "a render that refuses drift" as a guard. The rules on the agent's own conduct — `rule-one-judgment-one-implementation`, created by Case 360, `rule-agent-writing`, `rule-language`, `rule-atomicity` — stand on the text in a file the agent reads, `CLAUDE.md` or `case-schema.md`; the render refuses the drift of that text, not a case in substance, and the Estimate of 360 says "No script refuses a second copy". The pre-spec of session 0034 named this a known contradiction.
`rule-rules-schema` stands `draft`; the Case touches `estimate-rules-schema-checked` (`pending`), whose Then promises the prose of Enforcement verbatim with one added sentence after 240.2; the four rules of the class do not change; no `create`.

## Problem

The rules schema does not admit a Rule without a guard that refuses the case, while four rules on the agent's conduct stand on the text in the context alone; either the schema is wrong or these pages are not Rules.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-372
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
