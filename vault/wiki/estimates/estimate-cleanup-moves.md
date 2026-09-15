---
type: estimate
kind: QA
status: passed
target: "[[rule-cleanup]]"
origin: raw/2026-09-10/ledger.md#case-33
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Context

A page left live after archival keeps its index line and its findings. A page moved without its History line loses the trace of when it left.

## Criterion

Against a temp vault: every live page with status archived moves to
vault/archive/<sprint>/<date>/<HHMM>/<category>/ under the same file name with a History
line and a log.md line; its slug leaves the children lists of live pages and the estimates lists of entities and rules, the field only and no section rebuilt, with a History line there (case 174); an Insight's children keep
it; body wikilinks stay; pages with any other status stay; a page in the archive
whose status is not archived moves back with History restored; no index file is written (case 174); a live page whose parent or target
is archived is reported; a rerun moves nothing and exits 0; an unmovable file or a
taken name is reported with exit 1 and the rest still move. Live: one run over the
vault with nothing to move exits 0 and leaves git diff empty.

### case 102.2

When:
`uv run guppi cleanup` moves or restores a page.

Then:
A page with `status: archived` goes to `vault/archive/<sprint>/<date>/<HHMM>/<category>/<slug>.md`: `<date>` the day of the run, `<HHMM>` the latest session folder under `raw/<date>/`, and without one the latest of the nearest date back.
**＋** A page under `vault/archive/` whose status is no longer `archived` comes back to `wiki/<category>/` from any depth.
**＋** Migration in Work Mode, one commit: `archived/migration/2026-09-11/estimates/` → `archive/migration/2026-09-11/estimates/` (a date without a session); the lesson of 2026-09-12 → `2026-09-12/<HHMM>/lessons/` of the session whose cleanup moved it, by the time of its line in `log.md`. The History of the pages does not change.
**＋** `estimate-cleanup-moves` gets a `### case 102.2` block, `pending`.
**－** A date without `<HHMM>/` folders is one session; the page goes to `<date>/<category>/`.

### case 147.6

When:
`guppi cleanup` runs.

Then:
The sentence "Then the four indexes are rewritten …" removed; purpose — "Prevents an archived page from staying among the live ones"; `cleanup.py` without the call of the index writer; the tests without the index checks.

### case 166.4

When:
`guppi cleanup` moves a page to the archive and removes its slug from the lists of the live pages.

Then:
`unlink` removes the slug from `children` and `estimates` and writes History `child <slug> archived` / `estimate <slug> archived`; it rebuilds no section and touches none.
**－** What goes to the archive, what comes back and where — as today.

## Method

pytest in tests/test_cleanup.py against a temp vault; the live reading once by hand

## Result

block 166.4: tests green (377 passed, 2026-09-15 session S); live — the librarian's run of session R moved decision-case-164, decision-case-114 and decision-case-165.2 to vault/archive/migration/2026-09-15/1448/decisions/ with five more decisions and one lesson; the pages that lost a slug carry no rebuilt section — a Grep of the seven derived headings over rules/, entities/, lessons/ and insights/ gives 0 hits

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-33
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L72
- 2026-09-11 updated: four indexes; estimates lists of entities and rules only; pending until the live run · [[decision-case-57]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L70
- 2026-09-13 criterion: case 102.2 added · [[decision-case-102.2]]
- 2026-09-14 updated: the prose Criterion names the path of case 102 (case 112.5) · [[decision-case-112.5]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L41
- 2026-09-14 criterion: case 147.6 added · [[decision-case-147.6]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L2
- 2026-09-15 criterion: case 166.4 added · [[decision-case-166.4]]
- 2026-09-15 updated: head Criterion: the field only, no section rebuilt (166.4); no index file (147.6) (case 174) · [[decision-case-174]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L8
