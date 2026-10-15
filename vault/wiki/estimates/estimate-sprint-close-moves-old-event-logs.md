---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether the close of a sprint moves the event logs that the open session no longer reads to the archive, outside git, and keeps the logs that session reads in raw/
method: uv run --project .guppi pytest .guppi/tests/test_sprint_close.py -k event_log; the line of .gitignore read in the tree at Retro
origin: raw/2026-10-08/2352/ledger.md#case-743.3
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, librarian]
---

## Criterion

When:
`uv run --project .guppi guppi sprint-close --sprint <id> --apply` of `.guppi/guppi/sprint_close.py` closes a sprint, in the librarian's run or in `.guppi/tests/test_sprint_close.py` over a made-up vault.

Then:
After a close whose run of `guppi cleanup` exits 0, each `vault/raw/<date>/event_log.md` dated before the day before the date of the session of the run moves to `vault/archive/<id>/<date>/event_log.md`.
**＋** A date folder that the moves leave empty is removed.
**＋** `.gitignore` leaves out each moved log, so git tracks none.
**＋** Stdout holds one line per log moved.
**－** The log of the date of the session of the run, of each later date and of the day before it stays where it is, since the hooks of that session read them.
**－** A log whose target exists does not move: one line on stderr, and the close exits 1 after the other moves.
**－** A refused close moves no log.

## Result

2026-10-09, uv run pytest tests/test_sprint_close.py -k event_log; 3 passed; .gitignore line 48 reads vault/archive/*/*/event_log.md and git check-ignore matches vault/archive/x/2026-01-01/event_log.md by it

## History

- 2026-10-09 created · [[decision-case-743.3]]
- 2026-10-09 status: pending → passed · raw/2026-10-08/2352/ledger.md#L31
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
