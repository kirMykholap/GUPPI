---
type: decision
case: "110.1"
status: current
update: [insights-schema]
origin: raw/2026-09-14/0747/ledger.md#case-110.1
sprint: migration
created: 2026-09-14
tags: []
---

## Context

Case 104.3 made the cascade of `generate` recount the `severity` of every Insight and archive an `open` one with no live child. The brief of session L flags the same page a second time: `insight-ledger-hook-reads-only-the-final-text` says `severity: 3` with three children, one of them — `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` — `status: archived` in `vault/archive/migration/2026-09-12/1156/lessons/`. The brief ranks the deferred list by Insight severity, so a wrong count moves items.

## Problem

The recount reads the status of a child from `wiki/lessons/` only. A child whose page `cleanup` moved into the archive has no page there; the code gives it an empty Page with no status and counts it as live (`generate.py:711`). The count is wrong the moment a child is archived, which is exactly the moment the count matters.

## Given

`insights/schema.md:19`: "`count(children where status != archived)`. Recomputed by lint, never written by hand." No code in `lint.py` recounts `severity`; `generate.cascade` does (case 104.3). A Rule-class file, slug `insights-schema`, applied by hand.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-110.1
