# Work — session 1336 of 2026-11-26

## Baseline

- `uv run --project .guppi guppi test`: exit code 0 — 1994 passed, 6 skipped, 2 deselected; no failing test.
- `uv run --project .guppi guppi check`: exit code 0 — no finding line.

## Expected red

- `guppi backlog --check` (a step of `uv run --project .guppi guppi check`): names `vault/wiki/backlog.md`, waiting for it at the librarian's run, since `.guppi/guppi/backlog.py` now leaves out the line of `rule-work-mode` of the archived `entity-sprint-migration` (case 1067).
