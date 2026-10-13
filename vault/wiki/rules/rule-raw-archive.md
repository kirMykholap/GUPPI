---
type: rule
kind: Leaf
purpose: Keeps raw/ to the sessions not yet turned into pages, by moving an applied session whole into the archive
status: built
enforcement: check
implementation_ref: [guppi/archive.py, tests/test_archive.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-raw-archive]]", "[[estimate-raw-archive-files-a-session-by-its-sprint]]"]
origin: raw/2026-09-13/ledger.md#case-100.1
sprint: migration
created: 2026-09-13
tags: [harness, librarian, ledger]
core: true
---

## Purpose

Keeps `raw/` to the sessions that are not yet fully turned into pages. A session
whose `materialize.yaml` is applied to the last entry and whose `ledger.md` has no
line outside the yaml is done; nothing reads it again, so it moves whole into the
archive of its date. A session with an entry still to apply stays, and is named
with the reason, so the debt is in view at every run until the entry is fixed in
Plan Mode.

## How it works

`uv run guppi archive` looks at every unit of `vault/raw/` whose date is before
the day of the run: a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`,
or a date-level `raw/<date>/ledger.md` with its yaml (the shape before case 103).
The session of the run is never looked at. At the close of a sprint, `guppi sprint-close` moves each done unit the same way whatever its date, the session of the run still left out (`rule-sprint-close`, case 743.1). A unit is done when its
`materialize.yaml` exists, every entry under `entries` carries `applied` or
`superseded_by`, and every line of its `ledger.md` that `materialize.parse_line`
reads as a record has its number in the `line` or `folded` of an entry or under
`unparsed`. A done session moves whole to
`vault/archive/<sprint>/<date>/<HHMM>/raw/`; a done date-level ledger moves with
its yaml and everything else at the date root to
`vault/archive/<sprint>/<date>/raw/`, and with it every `<HHMM>/` folder of the
date without a ledger of its own, each to
`vault/archive/<sprint>/<date>/<HHMM>/raw/`. `<sprint>` is the `sprint` field of the unit's own `materialize.yaml`, so a session that leaves after the next sprint opened goes to the folder of its own sprint; a unit whose yaml holds none takes the first `## <id>` heading of `sprint.md` (case 743.2). `event_log.md` stays in `vault/raw/<date>/`: it is gitignored and the ledger hook walks it for the `hi` window. The close of a sprint moves each log dated before the day before the session of its run to `vault/archive/<id>/<date>/`, `<id>` the sprint it closes, still gitignored (`rule-sprint-close`, case 743.3). No file is cut and no
pointer is rewritten: `raw/<date>/<HHMM>/ledger.md#case-N`, the date form and
`#L<n>` stay the name of a ledger, which lint resolves in `raw/` or in the archive.

Stdout carries one line per unit, `archive: raw/<date>/<HHMM> →
archive/<sprint>/<date>/<HHMM>/raw`, `archive: raw/<date> →
archive/<sprint>/<date>/raw`, or `archive: raw/<date>[/<HHMM>] kept: <reason>` —
`no yaml`, `N entries not applied`, `N ledger lines outside the yaml`. A name
already taken in the archive or a move that fails is a line on stderr and exit 1;
the other units still move. A rerun moves nothing and exits 0. A folder without
`ledger.md` is not a unit. An entry that a supersedes from another unit did not
mark keeps its unit in `raw/`; that gap belongs to `rule-materialize`. The
coverage of a line is the one function `guppi tail` uses ([[rule-ledger-tail]]).

## History

- 2026-09-13 created · [[decision-case-100.1]]
- 2026-09-13 estimate estimate-raw-archive added · [[decision-case-100.1]]
- 2026-09-13 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-09 updated: the close of a sprint moves each done unit whatever its date (case 743.1) · [[decision-case-743.1]]
- 2026-10-09 updated: a unit goes to the archive folder of the sprint its own yaml records (case 743.2) · [[decision-case-743.2]]
- 2026-10-09 estimate estimate-raw-archive-files-a-session-by-its-sprint added · [[decision-case-743.2]]
- 2026-10-09 updated: the close of a sprint moves the old event logs (case 743.3) · [[decision-case-743.3]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
