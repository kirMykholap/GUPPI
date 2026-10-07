---
type: lesson
kind: error
root_cause: Case 596 was ratified again around 21:32 with the decision lines the ledger already held, so the ledger kept 21:10:50 as the time of its last decision line while case-596.md was written after it; the hook reads the decision lines of ledger.md and of the reply that ended, and case 597.2 widens that only to the replies of the stretch, so a Case ratified again with unchanged lines stays out for the rest of the session once the stretch of its re-ratification has passed
status: archived
insight: "[[insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out]]"
origin: raw/2026-10-02/2049/ledger.md#L31
sprint: migration
created: 2026-10-02
tags: [hooks, workflow]
---

## Trigger

in session 2049, after the reply at 22:26 that closed the last open line under Cases with a LEDGER block, uv run guppi onward --plan stayed silent and the person had to ask the agent to go on to /pre-spec

## Root cause

Case 596 was ratified again around 21:32 with the decision lines the ledger already held, so the ledger kept 21:10:50 as the time of its last decision line while case-596.md was written after it; the hook reads the decision lines of ledger.md and of the reply that ended, and case 597.2 widens that only to the replies of the stretch, so a Case ratified again with unchanged lines stays out for the rest of the session once the stretch of its re-ratification has passed

## History

- 2026-10-02 created · raw/2026-10-02/2049/ledger.md#L31
- 2026-10-07 updated: clustered under insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out (synthesis) · raw/2026-10-07/0211/ledger.md#L48
- 2026-10-07 archived · insight actioned
- 2026-10-07 archived · cleanup
