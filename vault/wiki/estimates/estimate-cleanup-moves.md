---
type: estimate
kind: QA
status: passed
target: "[[rule-cleanup]]"
purpose: guppi cleanup moves an archived page into the archive of the session of the run and a restored one back, and unlinks its slug from the live lists without rebuilding a section
method: pytest .guppi/tests/test_cleanup.py, plus by hand on the cleanup of a later librarian's run
checked: 2026-09-29
origin: raw/2026-09-10/ledger.md#case-33
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi cleanup` runs over the live pages of `vault/wiki/` and the pages under the archive.

Then:
A live page with `status: archived` moves under the same file name to `vault/archive/<sprint>/<date>/<HHMM>/<category>/`. The date is the day of the run, and the session is the latest session folder of `vault/raw/<date>/`, else the latest of the nearest date back. With no session folder at all, the page goes into the category folder under the date, with no session level.
**＋** The moved page gets the History line "- <date> archived · cleanup", and a page moved back gets "- <date> restored · cleanup". Each History line that cleanup writes also goes to `log.md` with the page's category and slug in front, such as "- <date> <category>/<slug> archived · cleanup".
**＋** Its slug leaves the `children` of live pages and the `estimates` of entities and rules, the field only, and that page gets the History line "- <date> child <slug> archived · cleanup" or "- <date> estimate <slug> archived · cleanup". No section is rebuilt, and an Insight's `children` keep the slug.
**＋** Wikilinks in page bodies stay, and a page with any other status stays.
**＋** A page under the archive, at any depth, whose status is no longer `archived` moves back to its category folder under `vault/wiki/`.
**＋** A live page whose `parent` or `target` is archived is reported on stderr and left.
**＋** A rerun moves nothing and exits 0. A file that cannot move, or a name already taken in the archive, is a line on stderr and exit 1, and the other pages still move.
**＋** Live, a run with nothing to move exits 0 and leaves `git diff` empty.

## Result

2026-09-29, uv run pytest tests/test_cleanup.py: 8 passed; live, the run of ff62585: cleanup moved 2 pages, exit 0, decision-case-495 and 496 to vault/archive/migration/2026-09-29/0137/decisions/ with "archived · cleanup" in History and log.md

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
- 2026-09-29 updated: the Criterion replaced whole — the head and the blocks 102.2, 147.6 and 166.4 into one When and Then, the one-time migration and the index files out, the History and log lines as the script writes them; purpose and method set, Context and Method out (case 500.3) · [[decision-case-500.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L50
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
