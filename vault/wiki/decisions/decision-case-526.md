---
type: decision
case: "526"
status: current
update: ["[[rule-case-protocol]]", "[[rule-spec-write]]", "[[rule-materialize]]"]
origin: raw/2026-09-29/2024/ledger.md#case-526
sprint: migration
created: 2026-09-29
tags: [session, workflow, ledger, hooks, harness]
---

## Problem

Three rule pages, `case-schema.md`, the code and one test say that YAML cuts an unquoted value at a `#` after a tab. PyYAML refuses the block there instead. A reader of the pages, the code or the test learns a false fact about the parser the harness runs.

## History

- 2026-09-30 created · raw/2026-09-29/2024/ledger.md#case-526
