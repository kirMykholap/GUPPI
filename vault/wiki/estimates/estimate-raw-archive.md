---
type: estimate
kind: QA
status: passed
target: rule-raw-archive
origin: raw/2026-09-13/ledger.md#case-100.1
sprint: migration
created: 2026-09-13
tags: [harness, librarian, ledger]
---

## Context

Nothing says when a unit of `raw/` is done with, and nothing takes it away. The `origin` of every page (`raw/<date>/ledger.md#case-N`) points in, lint checks it, `rule-cleanup` and `index.md` §1 say "`raw/` stays". The migration plan meant a move "by run stamp with every path rewritten": 82 pages point at 2026-09-09 alone, plus History lines and `log.md`.

## Criterion

### case 100.1

When:
`uv run guppi archive` runs — the librarian's fifth step, or by hand.

Then:
A unit is a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`, or a date-level `raw/<date>/ledger.md` with its yaml. A unit is done when its yaml exists, every entry under `entries` carries `applied` or `superseded_by`, and the number of every line of its `ledger.md` that `materialize.parse_line` reads as a record is in the `line` or `folded` of some entry or under `unparsed`.
**＋** Only units whose date is before the day of the run are looked at; the session of the run never — found as `cleanup` finds it, the latest `<HHMM>/` folder of the run day, else the nearest date back, and skipped even when dated before the run day.
**＋** A done session moves whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. A done date-level ledger moves with its yaml and everything else at the date root to `vault/archive/<sprint>/<date>/raw/`, and with it every `<HHMM>/` folder of the date that has no ledger of its own, each to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. No file is cut.
**＋** `event_log.md` stays in `vault/raw/<date>/`.
**＋** Stdout, one line per unit: `archive: raw/<date>/<HHMM> → archive/<sprint>/<date>/<HHMM>/raw`, `archive: raw/<date> → archive/<sprint>/<date>/raw`, or `archive: raw/<date>[/<HHMM>] kept: <reason>` — `no yaml`, `N entries not applied`, `N ledger lines outside the yaml`.
**＋** Exit 0; a name already taken in the archive or a move that fails is a line on stderr, exit 1, the other units still move. A rerun moves nothing and exits 0.
**－** `origin`, History, `log.md` and the yaml are not rewritten.
**－** A folder without `ledger.md` is not a unit; a date-level unit dated the day of the run is not looked at.
**－** An entry that a supersedes from another unit did not mark keeps its unit in `raw/`; that gap is `rule-materialize`'s, not this rule's.

## Method

Unit, `tests/test_archive.py`: a fixture vault with a date-level date applied to the
last entry and fully covered, holding a `<HHMM>/` folder without a ledger; a session
folder applied and covered; a session with a `failed` entry; a session with a record
line outside its yaml; a session dated today; and a folder without `ledger.md`. One
run moves the date-level unit to `<date>/raw/` and its session folder to
`<date>/<HHMM>/raw/`, the done session to `<date>/<HHMM>/raw/`, leaves every
`event_log.md` behind, keeps the other three with the reason on stdout, exits 0; a
name already taken in the archive is a stderr line and exit 1 while the other units
move; a rerun moves nothing and exits 0. Live, 2026-09-13: `uv run guppi archive`
over the four date-level dates of `raw/`, then `make lint` — the four dates under
`vault/archive/migration/<date>/raw/` with their session folders beside, `raw/`
holding only today and the four `event_log.md`, lint's `origin` findings unchanged
from before the move; a change in lint's count fails the reading and the move is
reverted with `git checkout`.

## Result

unit: tests/test_archive.py 7 green — a date-level unit and a done session move whole with the ledger-less session folder beside, event_log.md stays, a failed entry, a line outside the yaml, today's unit and the session of the run stay with the reason on stdout, a taken name is stderr and exit 1 while the rest moves, a rerun moves nothing; live 2026-09-13 session L: uv run guppi archive moved raw/2026-09-09, 09-10, 09-11 and 09-12 to vault/archive/migration/<date>/raw/ with the three session folders of 09-12 beside as <HHMM>/raw/, raw/ holds today and the four event_log.md, guppi lint 133 findings before and after the move with no origin finding, a rerun printed nothing and exited 0, guppi tail then printed the 49 lines of today's date-level ledger and nothing of the archived dates

## History

- 2026-09-13 created · [[decision-case-100.1]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/0652/ledger.md#L1
