---
type: decision
case: "110"
status: archived
update: ["[[rule-page-generation]]"]
origin: raw/2026-09-14/0747/ledger.md#case-110
sprint: migration
created: 2026-09-14
tags: [harness, workflow, ledger]
---

## Context

Case 104.3 made the cascade of `generate` recount the `severity` of every Insight and archive an `open` one with no live child. The brief of session L flags the same page a second time: `insight-ledger-hook-reads-only-the-final-text` says `severity: 3` with three children, one of them — `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` — `status: archived` in `vault/archive/migration/2026-09-12/1156/lessons/`. The brief ranks the deferred list by Insight severity, so a wrong count moves items.

## Problem

The recount reads the status of a child from `wiki/lessons/` only. A child whose page `cleanup` moved into the archive has no page there; the code gives it an empty Page with no status and counts it as live (`generate.py:711`). The count is wrong the moment a child is archived, which is exactly the moment the count matters.

## Given

`generate.cascade` (`generate.py:688-721`) reads `wiki/lessons/*.md` into a dict and counts a child live when `lessons.get(s, Page(...)).status != "archived"`; a slug absent from the dict is an empty Page, status `None`, counted live.
**＋** `Vault.find` and `archived_paths` (`generate.py:207-258`) already reach a page in the archive by slug, in a category folder, `raw/` excluded (case 105.3).
**＋** The contract of 104.3, block `### case 104.3` of `estimate-generate-writes`: `severity` 0 — every child `archived` — gives `status: archived`; 1 or more — as it is. `insights/schema.md:19`: `severity` = `count(children where status != archived)`. Neither says where the status is read.
**＋** The page today: `severity: 3`, three children, one archived; the right count is 2. `estimate-generate-writes` is `pending` with five blocks (101.1, 104.1, 104.2, 104.3, 105.3); `rule-page-generation` is `draft` on it.
**＋** The branch for an `actioned` Insight (104.2) skips a child absent from the dict; a child already in the archive is already `archived`, so that branch is right as it is.
**－** `insights/schema.md:30` and `rule-synthesis:22` say "the archive is not read" — of synthesis, which matches lessons by meaning. Resolving a known slug is what `find` does since 105.3, not a search.
**－** `insights/schema.md:19` says the count is "recomputed by lint"; no code in `lint.py` recounts it, `generate` alone does: Case 110.1.
**－** The Frontier line F6 closes on this Case.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-110
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
