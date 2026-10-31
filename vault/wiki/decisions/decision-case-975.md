---
type: decision
case: "975"
status: current
update: ["[[rule-rules-schema]]", "[[entity-glossary]]", "[[estimate-rules-schema-checked]]"]
origin: raw/2026-10-31/2307/ledger.md#case-975
sprint: plugin
created: 2026-10-31
tags: [harness, render, schema, session]
---

## Problem

The rules schema says a Rule's guard refuses a case, while hook Rules of the vault, such as the one that writes the graph of links at the start of a session, refuse nothing and only keep a file in place, so the schema and those pages contradict each other.

## Recommend

- **What the rules schema says about a hook that refuses nothing**
  - Recommended: (b) name any hook that makes a state hold instead of refusing a call: a guard refuses the case or prevents it, and a hook prevents it when it writes a file or gives the agent a text, in the opening of the schema, its Enforcement paragraph and the glossary row of Rule.
  - Answer: (b), as recommended.
- **How the change is checked**
  - Recommended: (a) replace the Criterion of `estimate-rules-schema-checked` whole, with a new line on the opening and the Enforcement paragraph; the glossary row stays with its own Estimate.
  - Answer: (a), as recommended.

## History

- 2026-11-01 created · raw/2026-10-31/2307/ledger.md#case-975
