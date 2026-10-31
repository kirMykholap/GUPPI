---
type: decision
case: "973"
status: current
create: ["[[estimate-sprint-plugin-check-finds-no-bare-slug-link]]"]
update: ["[[estimate-link-graph-prints-the-neighbours]]"]
origin: raw/2026-10-31/2307/ledger.md#case-973
sprint: plugin
created: 2026-10-31
tags: [sprint, harness]
---

## Problem

A bare `[[slug]]` in the `## Result` of `estimate-link-graph-prints-the-neighbours` names no page, so `guppi check` reports a `ref` finding at each run.

## Recommend

- **What the Case fixes**
  - Recommended: (a) fix the page text only — the bare `[[slug]]` in the `## Result` of `estimate-link-graph-prints-the-neighbours` put in a code span.
  - Answer: agreed, (a).
- **How the fix is checked**
  - Recommended: (a) a one-time Estimate with `once: true` on `entity-sprint-plugin`, read by hand after the librarian's run by `guppi check`.
  - Answer: (a).

## History

- 2026-11-01 created · raw/2026-10-31/2307/ledger.md#case-973
