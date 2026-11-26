## Baseline

- `uv run --project .guppi guppi test`: exit code 0 — 1983 passed, 6 skipped, 2 deselected; no failing test.
- `uv run --project .guppi guppi check`: exit code 1
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-orchestration: status: a page with core: true that is draft
  - estimates/estimate-case-build-settles-form-by-itself: unread: failed
  - estimates/estimate-orchestration-dispatches-case-guppi-at-a-level: unread: failed
  - estimates/estimate-sprint-plugin-frontierguard-build-read-its-folders-readers: unread: failed

## Expected red

- `uv run --project .guppi guppi check`, its step `guppi sprint --check`: `vault/wiki/sprint.md` differs from `entity-sprint-plugin`, since `.guppi/guppi/sprint.py` no longer ticks the failed one-off line of `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`; it waits for the render of `vault/wiki/sprint.md` at the librarian's run (case 1057.2).
