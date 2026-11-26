# Work — session 0605 (2026-11-25)

## Baseline

- `uv run --project .guppi guppi test`: exit code 0 (1978 passed, 6 skipped, 2 deselected)
- `uv run --project .guppi guppi check`: exit code 1

rules/rule-ask: status: a page with core: true that is draft
rules/rule-case-build: status: a page with core: true that is draft
rules/rule-morph: status: a page with core: true that is draft
estimates/estimate-ask-searches-at-prespec: unread: failed
estimates/estimate-case-build-searches-the-names-of-what-it-changes: unread: failed
estimates/estimate-sprint-plugin-frontierguard-build-read-its-folders-readers: unread: failed

## Expected red

- `guppi sprint --check` (a step of `guppi check`): `sprint: vault/wiki/sprint.md differs from entity-sprint-plugin` until the librarian's `guppi sprint` renders `vault/wiki/sprint.md` with the tick of the read one-off Estimate (Case 1051, `.guppi/guppi/sprint.py`).
