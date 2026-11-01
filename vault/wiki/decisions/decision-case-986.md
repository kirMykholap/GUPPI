---
type: decision
case: "986"
status: current
update: ["[[rule-case-build]]", "[[rule-link-graph-at-session-start]]", "[[estimate-case-build-reads-the-link-graph-of-what-it-changes]]"]
origin: raw/2026-11-01/1721/ledger.md#case-986
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, case-build]
---

## Problem

The builder reads the graph of links once, early, so a page or file added to the Case later is never looked up, a long block is cut short, and a created page is held to a duty it cannot meet.

## Recommend

- **When does the builder read the blocks?**
  - Recommended: (a) again at the final check, for each page and file the tasks change whose block was not read.
  - Answer: agreed, (a).
- **What about a page or file the Case creates?**
  - Recommended: (a) no block expected, nothing said.
  - Answer: agreed, (a).
- **How does the builder read a long block whole?**
  - Recommended: (a) find the line, then read to the next heading.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) rewrite that check whole.
  - Answer: agreed, (a).

## History

- 2026-11-01 created · raw/2026-11-01/1721/ledger.md#case-986
