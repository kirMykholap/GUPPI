---
type: decision
case: "712"
status: archived
update: ["[[rule-insights-schema]]"]
origin: raw/2026-10-07/1804/ledger.md#case-712
sprint: migration
created: 2026-10-07
tags: [harness, render, schema]
---

## Problem

The schema asks a Case for a quoted wikilink in `addressed_by`, and the checks before ratification refuse that link when the decision is of the same session; a Case cannot follow both.

## Recommend

- **Which side changes so that a Case can name a decision of its own session**
  - Recommended: (a) change the words of the Insight schema: the field description says that the page holds the quoted wikilink, that a Case writes the bare decision slug, and that the page writer adds the brackets; no code changes.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#case-712
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
