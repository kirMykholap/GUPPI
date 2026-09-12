---
type: rule
kind: MOC
purpose: Prevents the tools of the harness from drifting apart from the pages that describe them
status: built
children: [rule-render-harness, rule-hook-registry, rule-lint, rule-index, rule-governed-files-hook, rule-claude-md]
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
the indexes, the indexes before the pages. Two more belong here and run in no
pipeline: the hook that refuses a hand edit of a rendered file, and the page
`CLAUDE.md` is rendered from (cases 59.6, 59.8).

## Estimates

- [[estimate-harness-pipeline]]

## Children

1. [[rule-render-harness]]
2. [[rule-hook-registry]]
3. [[rule-lint]]
4. [[rule-index]]
5. [[rule-governed-files-hook]]
6. [[rule-claude-md]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 estimate estimate-harness-pipeline added · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 child rule-governed-files-hook added · [[decision-case-59.6]]
- 2026-09-12 child rule-claude-md added · [[decision-case-59.8]]
- 2026-09-12 updated: two children outside the make lint pipeline — the guard hook and the CLAUDE.md page (case 66) · [[decision-case-66]]
