---
type: rule
kind: MOC
purpose: Prevents the tools of the harness from drifting apart from the pages that describe them
status: built
children: [rule-render-harness, rule-hook-registry, rule-lint, rule-index]
estimates: [estimate-harness-pipeline]
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Purpose

Prevents the tools of the harness from drifting apart from the pages that describe
them. Four rules belong to no phase of the session: the renderer, the hook
registry, lint and the indexes. They run together in `make lint`, in this order, and
the order is the content: the harness files are checked against their pages before
the indexes, the indexes before the pages.

## Estimates

- [[estimate-harness-pipeline]]

## Children

1. [[rule-render-harness]]
2. [[rule-hook-registry]]
3. [[rule-lint]]
4. [[rule-index]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 estimate estimate-harness-pipeline added · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
