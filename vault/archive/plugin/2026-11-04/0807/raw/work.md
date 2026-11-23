# Work — session 0807

## Baseline

- `uv run --project .guppi guppi test`: exit code 0 (1956 passed, 6 skipped, 1 deselected); no failing test.
- `uv run --project .guppi guppi check`: exit code 1; the lint finding lines:
  - rules/rule-ask: status: a page with core: true that is draft
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-git-context: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - estimates/estimate-ask-searches-at-prespec: unread: failed
  - estimates/estimate-case-build-searches-the-names-of-what-it-changes: unread: failed
  - estimates/estimate-git-context-offers-git-init: unread: failed
  - estimates/estimate-morph-sets-up-the-project-at-the-first-hi: unread: failed
  - estimates/estimate-sprint-plugin-frontierguard-build-read-its-folders-readers: unread: failed

## Expected red
