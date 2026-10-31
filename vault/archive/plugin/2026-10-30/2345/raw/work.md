# Work — session 2345

## Baseline

- `uv run --project .guppi guppi test`: exit 0 — 1819 passed, 6 skipped, 1 deselected; no failing test.
- `uv run --project .guppi guppi check`: exit 1 — 13 lines:
  - entities/entity-sprint: status: a page with core: true that is draft
  - rules/rule-ask: status: a page with core: true that is draft
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-close: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-orchestration: status: a page with core: true that is draft
  - rules/rule-ratification: status: a page with core: true that is draft
  - rules/rule-rules-schema: status: a page with core: true that is draft
  - rules/rule-search-leaves-out-decisions: status: a page with core: true that is draft
  - rules/rule-skill-hi: status: a page with core: true that is draft
  - rules/rule-synthesis: status: a page with core: true that is draft
  - rules/rule-work-mode: status: a page with core: true that is draft
  - estimates/estimate-case-build-reads-the-readers-of-a-changed-step: unread: failed

## Expected red
