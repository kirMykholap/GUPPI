---
type: decision
case: "715"
status: archived
create: ["[[estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session]]"]
origin: raw/2026-10-07/1804/ledger.md#case-715
sprint: migration
created: 2026-10-07
tags: [harness, workflow]
---

## Problem

A Case that replaces the Criterion of an Estimate whole and keeps a `method` that waits for another session passes pre-spec with no report, and its own Retro leaves the Estimate `failed`.

## Recommend

- **What should the fix cover?**
  - Recommended: (b) a `/pre-spec` report for every check: a Case that replaces a Criterion with no new `method`, while the page's `method` waits for another session, gets a report; this Estimate's `method` stays until the next Case changes its Criterion.
  - Answer: agreed, (b).
- **Which check confirms the new report?**
  - Recommended: (a) a new check page, `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`, read by a test; the existing check page stays as it is.
  - Answer: agreed, (a).
- **Does a Case that sets a check passed or failed by your decision get the report?**
  - Recommended: (a) no report for it; only a Case that leaves the page `pending` gets the report.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#case-715
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
