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
line and a log.md line; its slug leaves the children lists of live pages and the estimates lists of entities and rules, and their sections, with a History line there; an Insight's children keep
it; body wikilinks stay; pages with any other status stay; a page in the archive
whose status is not archived moves back with History restored; the four category indexes are rewritten without the moved page, and an archived Estimate leaves no line anywhere; a live page whose parent or target
is archived is reported; a rerun moves nothing and exits 0; an unmovable file or a
taken name is reported with exit 1 and the rest still move. Live: one run over the
vault with nothing to move exits 0 and leaves git diff empty.

## Method

pytest in tests/test_cleanup.py against a temp vault; the live reading once by hand

## Result

tests/test_cleanup.py 5 green with the estimates lists of entities and rules only; live 2026-09-11: uv run guppi cleanup with nothing archived printed 0 page(s) moved, exit 0, rewrote the four indexes unchanged, git status clean afterwards

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-33
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L72
- 2026-09-11 updated: four indexes; estimates lists of entities and rules only; pending until the live run · [[decision-case-57]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L70
