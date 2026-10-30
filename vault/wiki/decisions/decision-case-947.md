---
type: decision
case: "947"
status: current
update: ["[[estimate-prespec-checks-the-frontier]]"]
origin: raw/2026-10-30/2345/ledger.md#case-947
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness]
---

## Problem

`guppi prespec --check` reports a backlog line that a Case of the conserved Spec puts off again, closed `[-] … · backlog · defer case N` as the `/box` closer sets it, because it looks for the decision lines of that Case only in the session's window. The finding stops the exit from Plan Mode of a session that cannot fix it.

## Recommend

- **What the check reads for a backlog line put off by a Case of the saved Spec**
  - Recommended: (a) also read the saved Spec's own ledger, and judge the line as for a Case of the current session, marks included.
  - Answer: agreed, (a).

## History

- 2026-10-31 created · raw/2026-10-30/2345/ledger.md#case-947
