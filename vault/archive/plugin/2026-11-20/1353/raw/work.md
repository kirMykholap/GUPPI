# Work — session 1353

## Baseline

- `uv run --project .guppi guppi test`: exit code 0 — 1976 passed, 6 skipped, 2 deselected; no failing test.
- `uv run --project .guppi guppi check`: exit code 1
  - rules/rule-ask: status: a page with core: true that is draft
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - estimates/estimate-ask-searches-at-prespec: unread: failed
  - estimates/estimate-case-build-offers-a-page-for-code-no-page-covers: unread: failed
  - estimates/estimate-case-build-searches-the-names-of-what-it-changes: unread: failed
  - estimates/estimate-sprint-plugin-frontierguard-build-read-its-folders-readers: unread: failed

## Expected red
