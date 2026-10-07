---
type: decision
case: "706"
status: current
update: ["[[insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out]]"]
origin: raw/2026-10-07/0636/ledger.md#case-706
sprint: migration
created: 2026-10-07
tags: [hooks, workflow, orchestration]
---

## Problem

The Insight `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` stands `actioned` with no `addressed_by`, and `make lint` reports it as a missing field.

## Recommend

- **Which decision the field `addressed_by` links to**
  - Recommended: (a) the part that set the status, `decision-case-701.1`, the decision its History line names.
  - Answer: agreed, (a).
- **Whether this Case also adds a check for this mistake**
  - Recommended: (a) fix the page only; `make lint` still catches the mistake at the librarian's run, and the Case says the check is left not done.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/0636/ledger.md#case-706
