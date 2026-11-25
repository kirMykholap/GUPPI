---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether the sprint page says that an Estimate, a one-off one too, is done when it passes, and that a failed one-off reading is not done; read once
method: "by hand, after the librarian's run of session 0816: the Purpose of vault/wiki/entities/entity-sprint-plugin.md read against the Criterion, in the estimate line"
origin: raw/2026-11-25/0605/ledger.md#case-1046
sprint: plugin
created: 2026-11-25
tags: [sprint, workflow]
once: true
---

## Criterion

When:
Someone reads the Purpose of `entity-sprint-plugin` after the librarian's run.

Then:
An Estimate of the page is done when it passes, one with `once: true` too.
**＋** A one-off Estimate whose reading failed is not done, and it is worked on until one reading passes.
**－** A failed reading of a one-off Estimate is not called done or kept as its record of done.

## History

- 2026-11-25 created · [[decision-case-1046]]
- 2026-11-25 updated: the Criterion replaced whole — a one-off Estimate is done when one reading passes · [[decision-case-1057.1]]
