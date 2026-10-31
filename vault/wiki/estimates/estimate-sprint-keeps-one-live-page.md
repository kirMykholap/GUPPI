---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint]]"
purpose: Whether the vault holds at most one live sprint page and each other sprint page stands in the archive
method: "uv run --project .guppi pytest .guppi/tests/test_sprint.py -k two_sprint_pages; by hand, at Retro: a Glob of vault/wiki/entities/entity-sprint-*.md and of vault/archive/**/entities/entity-sprint-*.md read against the Criterion"
origin: raw/2026-10-31/0431/ledger.md#case-959
sprint: plugin
created: 2026-10-31
tags: [sprint, workflow]
---

## Criterion

When:
At the Retro of a session, the sprint pages `entity-sprint-<id>` under `vault/wiki/entities/` and under `vault/archive/` are read.

Then:
At most one sprint page `entity-sprint-<id>` stands under `vault/wiki/entities/`.
**＋** Each other sprint page `entity-sprint-<id>` stands under `vault/archive/`.
**－** A vault with no live sprint page, between the close of one sprint and the opening of the next, does not fail this.

## Result

2026-10-31, Retro of session 0431, uv run --project .guppi pytest .guppi/tests/test_sprint.py -k two_sprint_pages (1 passed) and a Glob of vault/wiki/entities/entity-sprint-*.md and vault/archive/**/entities/entity-sprint-*.md: one live sprint page, entity-sprint-plugin; the one other sprint page, entity-sprint-migration, stands under vault/archive/migration/2026-10-10/1555/entities/

## History

- 2026-10-31 created · [[decision-case-959]]
- 2026-10-31 status: pending → passed · raw/2026-10-31/0431/ledger.md#L40
