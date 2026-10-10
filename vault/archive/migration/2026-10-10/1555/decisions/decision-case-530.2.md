---
type: decision
case: "530.2"
status: archived
update: ["[[rule-bash-guard]]", "[[estimate-bash-guard]]"]
origin: raw/2026-09-29/2024/ledger.md#case-530.2
sprint: migration
created: 2026-09-29
tags: [hooks, harness]
---

## Problem

The librarian's list of allowed reads contradicts the brief section of its own frame, so every run breaks the list and `estimate-documentation-completes` cannot pass. When a hook refuses a write, the refusal text points to the scratchpad and not to `Write`, so the librarian worked around the refusal with `cp` instead of writing the file with the tool the hooks check.

## History

- 2026-09-30 created · raw/2026-09-29/2024/ledger.md#case-530.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
