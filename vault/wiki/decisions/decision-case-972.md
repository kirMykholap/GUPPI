---
type: decision
case: "972"
status: current
create: ["[[estimate-prespec-hook-reports-a-wait-off-its-form]]"]
origin: raw/2026-10-31/2307/ledger.md#case-972
sprint: plugin
created: 2026-10-31
tags: [harness, workflow]
---

## Problem

A `method` that writes its wait for an event behind another word, such as `and by hand, after`, waits for nothing in lint and in pre-spec, and no check says so while the Case can still be fixed.

## Recommend

- **How the wait form is fixed**
  - Recommended: (b) pre-spec reports the near miss — a new predicate in `.guppi/guppi/lint.py`, imported by pre-spec, finds a part that holds the form but does not open with it; the form stays as it is.
  - Answer: (b).
- **How pre-spec reports the near miss**
  - Recommended: (a) pre-spec prints it as a `note:` line, which sets no exit code, and the main agent answers it in one line in the chat: rewritten into the form, or a moment of the Case's own session that is no wait.
  - Answer: (a).

## History

- 2026-11-01 created · raw/2026-10-31/2307/ledger.md#case-972
