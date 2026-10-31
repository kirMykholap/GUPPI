---
type: decision
case: "969"
status: current
children: ["[[decision-case-969.1]]", "[[decision-case-969.2]]", "[[decision-case-969.3]]"]
origin: raw/2026-10-31/1831/ledger.md#case-969
sprint: plugin
created: 2026-10-31
tags: [harness, render, schema, session, workflow, ledger, sprint]
---

## Problem

No Case decides how a one-time Estimate is told apart from one that promises a lasting behaviour, so a one-time check keeps its page `draft` while it waits, stays live after its sprint and ships in the clean version.

## Recommend

- **How a one-time Estimate is told apart**
  - Recommended: (a) it targets the live sprint page, with no new field.
  - Answer: (c), both joined: it targets the live sprint page and carries a marker, and lint reports a marked Estimate whose target is not a sprint page.
- **Whether this Case also sorts the existing Estimates**
  - Recommended: (b) the two known one-time Estimates are archived too, with no full pass.
  - Answer: (b), as recommended.
- **The name of the marker**
  - Recommended: (a) `once: true`.
  - Answer: (a), as recommended.
- **Whether the Case form tells the builder about it**
  - Recommended: (a) one sentence in `case-schema.md`.
  - Answer: (a), as recommended.
- **How the new lint finding is checked**
  - Recommended: (a) a line added to `estimate-lint-checks-the-statuses`, its Criterion replaced whole.
  - Answer: (a), as recommended.
- **How the removal of the two old Estimates is checked**
  - Recommended: (a) `estimate-cleanup-moves` covers it, with no new Estimate.
  - Answer: (a), as recommended.

## History

- 2026-10-31 created · raw/2026-10-31/1831/ledger.md#case-969
