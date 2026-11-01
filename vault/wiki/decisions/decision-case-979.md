---
type: decision
case: "979"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-reads-each-list-of-a-new-member]]"]
supersedes: ["[[decision-case-971]]", "[[decision-case-976]]"]
origin: raw/2026-11-01/0141/ledger.md#case-979
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, case-build]
---

## Problem

The builder misses the search for a member already in a list when the list is not one of the four named kinds, and nothing in the Case shows that the search was skipped.

## Recommend

- **What changes so the search runs**
  - Recommended: (b) name the missed kinds of list (a hook of an event, a command, a list in a comment or docstring of code), and have `context` report the search.
  - Answer: agreed, (b).
- **Where the step stands**
  - Recommended: (a) it stays in the check before the summary.
  - Answer: agreed, (a).
- **When the check is read again**
  - Recommended: (a) read it after the first later build that adds a member to a list.
  - Answer: agreed, (a).

## History

- 2026-11-01 created · raw/2026-11-01/0141/ledger.md#case-979
