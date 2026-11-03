---
type: estimate
kind: QA
status: passed
target: "[[rule-raw-archive]]"
purpose: guppi archive moves a done unit of raw whole into the archive of its date, keeps an undone one with its reason, and never touches the session of the run
method: "pytest .guppi/tests/test_archive.py, plus by hand on the archive step of a later librarian's run: its stdout, the raw folder and the origin findings of uv run --project .guppi guppi check before and after"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, librarian, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi archive` runs, as a step of the librarian's run or by hand, over the units under `vault/raw/<date>/`.

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

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
