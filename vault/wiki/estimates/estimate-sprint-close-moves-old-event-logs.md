---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether the close of a sprint moves the event logs that the open session no longer reads to the archive, outside git, and keeps the logs that session reads in raw/
method: uv run --project .guppi pytest .guppi/tests/test_sprint_close.py -k event_log; the lines of vault/.gitignore read in the tree at Retro
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow, librarian]
core: true
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

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
