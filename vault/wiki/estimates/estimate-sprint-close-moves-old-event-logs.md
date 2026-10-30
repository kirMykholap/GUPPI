---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether the close of a sprint moves the event logs that the open session no longer reads to the archive, outside git, and keeps the logs that session reads in raw/
method: uv run --project .guppi pytest .guppi/tests/test_sprint_close.py -k event_log; the lines of vault/.gitignore read in the tree at Retro
checked: 2026-10-30
origin: raw/2026-10-08/2352/ledger.md#case-743.3
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, librarian]
---

## Criterion

When:
`uv run --project .guppi guppi sprint-close --sprint <id> --apply` of `.guppi/guppi/sprint_close.py` closes a sprint, in the librarian's run or in `.guppi/tests/test_sprint_close.py` over a made-up vault, and the session of the run is the stamp whose `hi` line `session_dir` of `.guppi/guppi/ledger.py` takes to the newest session folder of `vault/raw/`.

Then:
After a close whose run of `guppi cleanup` exits 0, each `vault/raw/<date>/event_log.md` dated before the start date of the session of the run, the first date that `session_event_logs` of `.guppi/guppi/ledger.py` gives for its stamp, moves to `vault/archive/<id>/<date>/event_log.md`.
**＋** A date folder that the moves leave empty is removed.
**＋** `vault/.gitignore` leaves out each moved log, so git tracks none.
**＋** Stdout holds one line per log moved.
**－** The log of the start date and of each later date stays where it is, since the hooks of that session read them, the start date two or more days before the date of the session folder included.
**－** With no session folder in `vault/raw/`, or with no stamp or more than one whose `hi` line `session_dir` takes to the newest session folder, no log moves, and stdout holds one line that says why.
**－** A log whose target exists does not move: one line on stderr, and the close exits 1 after the other moves.
**－** A refused close moves no log.

## Result

2026-10-30, Retro of session 2341: uv run --project .guppi pytest .guppi/tests/test_sprint_close.py -k event_log 7 passed, 15 deselected; vault/.gitignore holds raw/*/event_log.md and archive/*/*/event_log.md, and git check-ignore -v reports vault/archive/plugin/2026-10-29/event_log.md ignored by vault/.gitignore:3; .guppi/guppi/sprint_close.py names vault/.gitignore

## History

- 2026-10-09 created · [[decision-case-743.3]]
- 2026-10-09 status: pending → passed · raw/2026-10-08/2352/ledger.md#L31
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-26 updated: the Criterion replaced whole — the close keeps the event logs from the start date of the open session, found by the window of the hooks · [[decision-case-886]]
- 2026-10-26 status: pending → passed · raw/2026-10-17/2307/ledger.md#L54
- 2026-10-30 updated: the Criterion replaced whole — the moved logs are left out of git by vault/.gitignore, and the method reads that file · [[decision-case-917.1]]
- 2026-10-30 status: pending → passed · raw/2026-10-29/2341/ledger.md#L35
