---
type: decision
case: "1067"
status: current
update: ["[[rule-backlog]]", "[[estimate-backlog-renders]]"]
origin: raw/2026-11-26/1336/ledger.md#case-1067
sprint: plugin
created: 2026-11-26
tags: [session, workflow, harness, librarian, sprint]
---

## Problem

A line of a closed sprint's Backlog that names a page comes back into `backlog.md` each time its page gets a new Estimate and goes back to `draft`. It then shows work that nobody put off, with a count of put-offs from before the close.

## Recommend

- **What happens to a page line of a closed sprint's Backlog when its page goes back to draft?**
  - Recommended: (c) a page line leaves for good once its page has been finished since the close: `guppi backlog` reads the History of the page, and a line whose page stood `built`, `passed` or `archived` on or after the day its sprint closed does not come back.
  - Answer: agreed, (c).

## History

- 2026-11-26 created · raw/2026-11-26/1336/ledger.md#case-1067
