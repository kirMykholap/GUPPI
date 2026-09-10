---
type: estimate
kind: QA
status: passed
target: rule-cleanup
origin: raw/2026-09-10/ledger.md#case-33
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Context

A page left live after archival keeps its index line and its findings. A page moved without its History line loses the trace of when it left.

## Criterion

Against a temp vault: every live page with status archived moves to
vault/archived/<sprint>/<date>/<category>/ under the same file name with a History
line and a log.md line; its slug leaves the children and estimates lists of live
pages and their sections, with a History line there; an Insight's children keep
it; body wikilinks stay; pages with any other status stay; a page in the archive
whose status is not archived moves back with History restored; the category
indexes are rewritten without the moved page; a live page whose parent or target
is archived is reported; a rerun moves nothing and exits 0; an unmovable file or a
taken name is reported with exit 1 and the rest still move. Live: one run over the
vault with nothing to move exits 0 and leaves git diff empty.

## Method

pytest in tests/test_cleanup.py against a temp vault; the live reading once by hand

## Result

tests/test_cleanup.py 5 green; live: `uv run guppi cleanup` over the vault moved 0 pages, exit 0, the working tree unchanged by it

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-33
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L72
