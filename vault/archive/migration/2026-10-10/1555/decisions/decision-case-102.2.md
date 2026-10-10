---
type: decision
case: "102.2"
status: archived
update: ["[[rule-cleanup]]"]
origin: raw/2026-09-13/ledger.md#case-102.2
sprint: migration
created: 2026-09-13
tags: [harness, workflow]
---

## Context

Two archive roots in the vault. `vault/archive/`: 49 folders of August (`2026-08-12`…`2026-08-31`, 4.9 MB), the handoffs and pages of the model before the migration, whose fate sat in Slice 5. `vault/archived/`: the new one, where `cleanup` puts pages with `status: archived` — `migration/2026-09-11/estimates/` (21) and `migration/2026-09-12/lessons/` (1). `vault/wiki/archive/` is an empty folder git does not know. Case 100 puts the archive of `raw/` under the same root.

## Problem

Two places for one notion, and the name that was wanted taken by what is not needed. Renaming now is cheap: three places in the code, five test files, four pages, one `git mv`. Later every `cleanup` run and every archived session add paths.

## Given

Code reading `vault/archived`: `cleanup.py:29` (`archive_root`, writes and restores), `lint.py:207` (`archived_slugs`, `rglob` over the archive — a reference to an archived slug is not a finding), `materialize.py:339` (`page_exists`, the `exists` mark). Tests: `test_cleanup.py:1,37`, `test_lint.py:257,517,597,623`, `test_pretask.py:473` — path strings in fixtures.
**＋** Pages naming the path: `rule-cleanup` (How it works: `vault/archived/<sprint>/<date>/<category>/<slug>.md`, "A page under `vault/archived/`"), `rule-documentation` (Render, the frame: "Never read … `vault/archived/`"), `index.md` §1 line 32, the glossary row `archived`. Neither `log.md` nor the History of pages carries a path — slugs only.
**＋** The 22 archived pages hold no paths; their slugs sit in `decision-case-53.1`, `decision-case-70`, the `children` of `insight-ledger-hook-reads-only-the-final-text`. After the `git mv`, `lint.archived_slugs` finds them under the new root.
**＋** The old `vault/archive/` is read by no script, test or Rule page; only its own handoffs and `raw/notes/` (100.6) point at it. `sprint.md` Slice 5 names it among the old folders.
**＋** The layout under the root: `vault/archive/<sprint>/<date>/<HHMM>/` is the base — a session; inside, `raw/` (its ledger, yaml, Spec, Frontier, handoff) and `<category>/<slug>.md` (the pages its cleanup archived). `vault/archive/<sprint>/<date>/raw/` holds a date-level ledger of the shape before case 103. A date before 2026-09-12 held one session without a `<HHMM>/` folder (case 73.1); its pages sit at `<date>/<category>/`.
**＋** `cleanup` learns the session of the run as the latest `<HHMM>/` folder under `raw/<day of the run>/`, and without one the latest of the nearest date back (a session across midnight).
**－** `vault/parked/` (2 folders, Slice 4) and `docs/` are not touched.
**－** `estimate-cleanup-moves` (`passed`) gets a block: the path is part of its criterion. `page_exists` in `materialize` is implementation; the `exists` contract does not change — a task without a line. 102.3 and 102.5 as first shown are folded into 103.5 and 103.6.

## Criterion

- [[estimate-cleanup-moves]] § case 102.2

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-102.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
