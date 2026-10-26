---
type: decision
case: "888"
status: current
update: ["[[rule-page-generation]]", "[[estimate-generate-writes-the-decision-page]]", "[[rule-decisions-schema]]", "[[entity-glossary]]"]
origin: raw/2026-10-26/0118/ledger.md#case-888
sprint: plugin
created: 2026-10-26
tags: [harness, workflow, ledger, render, schema, session]
---

## Problem

A Case that a later Case replaced before its entries applied keeps a Decision page that stands `current` and names no Case that replaced it, when the Case that replaced it is retired in turn, though nothing of it applied.

## Recommend

- **Which Case does A's page name as the one that replaced it?**
  - Recommended: (a) B, the Case the mark on A's record names; nothing is invented and no chain is walked.
  - Answer: agreed, (a).
- **Does A's page date that change in its history?**
  - Recommended: (a) one History line, and one line of the log, at once, as for any page that goes superseded.
  - Answer: agreed, (a).
- **How do the texts that define the page status read?**
  - Recommended: (a) add one clause to both texts for a page whose own entries never applied.
  - Answer: agreed, (a).

## History

- 2026-10-26 created · raw/2026-10-26/0118/ledger.md#case-888
