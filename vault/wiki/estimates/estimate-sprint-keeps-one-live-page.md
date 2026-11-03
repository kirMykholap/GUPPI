---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint]]"
purpose: Whether the vault holds at most one live sprint page and each other sprint page stands in the archive
method: "uv run --project .guppi pytest .guppi/tests/test_sprint.py -k two_sprint_pages; by hand, at Retro: a Glob of vault/wiki/entities/entity-sprint-*.md and of vault/archive/**/entities/entity-sprint-*.md read against the Criterion"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow]
core: true
---

## Criterion

When:
At the Retro of a session, the sprint pages `entity-sprint-<id>` under `vault/wiki/entities/` and under `vault/archive/` are read.

Then:
At most one sprint page `entity-sprint-<id>` stands under `vault/wiki/entities/`.
**＋** Each other sprint page `entity-sprint-<id>` stands under `vault/archive/`.
**－** A vault with no live sprint page, between the close of one sprint and the opening of the next, does not fail this.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
