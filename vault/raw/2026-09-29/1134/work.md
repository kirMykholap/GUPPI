# Work — session 1134, 2026-09-29

## Baseline

Branch `migration`, before the first change.

- `make test`: exit 0 — 900 passed, 2 skipped.
- `make lint`: exit 2 — it stops at the `backlog --check` step; the steps after it did not run:
  - `backlog: vault/wiki/backlog.md differs from its sources`
  - `make: *** [Makefile:49: lint] Error 1`
- `uv run guppi lint`, the step `make lint` did not reach, run alone: exit 1, 161 findings — 89 `unread` (the `pending` Estimates), 62 `schema` on `decision-case-1` to `decision-case-28` (missing `## Context` and `## Problem`), 2 `schema` and 1 `orphan` on `rule-spec-box`, 1 `fence` on `decision-case-13`, 6 `deferred`, 0 `unmigrated`.

## Expected red
