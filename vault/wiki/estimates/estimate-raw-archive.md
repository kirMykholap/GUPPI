---
type: estimate
kind: QA
status: pending
target: "[[rule-raw-archive]]"
purpose: guppi archive moves a done unit of raw whole into the archive of its date, keeps an undone one with its reason, and never touches the session of the run
method: "pytest tests/test_archive.py, plus by hand on the archive step of a later librarian's run: its stdout, the raw folder and the origin findings of make lint before and after"
origin: raw/2026-09-13/ledger.md#case-100.1
sprint: migration
created: 2026-09-13
tags: [harness, librarian, ledger]
---

## Criterion

When:
`uv run guppi archive` runs, as a step of the librarian's run or by hand, over the units under `vault/raw/<date>/`.

Then:
A unit is a session folder `vault/raw/<date>/<HHMM>/` that holds a `ledger.md`, or a date-level `ledger.md` at the root of `vault/raw/<date>/` with its yaml. A unit is done when its yaml exists, every entry under `entries` carries `applied` or `superseded_by`, and the number of every line of its `ledger.md` that `materialize.parse_line` reads as a record stands in the `line` or `folded` of an entry or under `unparsed`.
**＋** Only units dated before the day of the run are looked at. The session of the run is never looked at, even when it is dated before the run day: it is the latest session folder of the run day, else of the nearest date back.
**＋** A done session moves whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. A done date-level ledger moves with its yaml and everything else at the date root to `vault/archive/<sprint>/<date>/raw/`. With it goes every session folder of the date that has no ledger of its own, each to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. No file is cut.
**＋** `event_log.md` stays in `vault/raw/<date>/`.
**＋** Stdout holds one line per unit: "archive: raw/<date>/<HHMM> → archive/<sprint>/<date>/<HHMM>/raw", "archive: raw/<date> → archive/<sprint>/<date>/raw", or "archive: raw/<date>[/<HHMM>] kept: <reason>". The reason is `no yaml`, `N entries not applied` or `N ledger lines outside the yaml`.
**＋** The exit is 0. A name already taken in the archive, or a move that fails, is a line on stderr and exit 1, and the other units still move. A rerun moves nothing and exits 0.
**－** `origin`, History, `log.md` and the yaml are not rewritten.
**－** A folder without `ledger.md` is not a unit.
**－** An entry that a supersedes from another unit did not mark keeps its unit in `vault/raw/<date>/`.

## Result

unit: tests/test_archive.py 7 green — a date-level unit and a done session move whole with the ledger-less session folder beside, event_log.md stays, a failed entry, a line outside the yaml, today's unit and the session of the run stay with the reason on stdout, a taken name is stderr and exit 1 while the rest moves, a rerun moves nothing; live 2026-09-13 session L: uv run guppi archive moved raw/2026-09-09, 09-10, 09-11 and 09-12 to vault/archive/migration/<date>/raw/ with the three session folders of 09-12 beside as <HHMM>/raw/, raw/ holds today and the four event_log.md, guppi lint 133 findings before and after the move with no origin finding, a rerun printed nothing and exited 0, guppi tail then printed the 49 lines of today's date-level ledger and nothing of the archived dates

## History

- 2026-09-13 created · [[decision-case-100.1]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/0652/ledger.md#L1
- 2026-09-22 updated: the layout named by its rules (case 318) · [[decision-case-318]]
- 2026-09-29 updated: the Criterion replaced whole — the block 100.1 as When and Then, the pointer to rule-materialize out; purpose and method set, Context and Method out (case 500.4) · [[decision-case-500.4]]
