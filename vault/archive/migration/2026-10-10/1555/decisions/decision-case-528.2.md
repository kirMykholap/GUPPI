---
type: decision
case: "528.2"
status: archived
update: ["[[entity-glossary]]", "[[rule-ledger-tail]]"]
delete: ["[[rule-github-issues]]", "[[estimate-github-issues-listed]]"]
supersedes: ["[[decision-case-220]]", "[[decision-case-243]]"]
origin: raw/2026-09-29/2024/ledger.md#case-528.2
sprint: migration
created: 2026-09-29
tags: [session, harness, github, ledger]
---

## Problem

`/hi` runs two commands against a remote that is not this project, and both fail at every session start. The note that keeps them off the Frontier goes away with the sprint. After the merge, `main` would pull from the product repository. The promise on the raw date folders asks that folders git does not track be gone, but `rule-raw-archive` keeps their logs on purpose.

## History

- 2026-09-30 created · raw/2026-09-29/2024/ledger.md#case-528.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
