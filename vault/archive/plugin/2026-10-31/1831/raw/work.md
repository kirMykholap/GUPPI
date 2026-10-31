# Work — session 1831

## Baseline

- `uv run --project .guppi guppi test`: exit 0; 1830 passed, 6 skipped, 1 deselected; no failing test.
- `uv run --project .guppi guppi check`: exit 1; 16 lines:
  - rules/rule-ask: status: a page with core: true that is draft
  - rules/rule-backlog: status: a page with core: true that is draft
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-close: status: a page with core: true that is draft
  - rules/rule-handoff: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-orchestration: status: a page with core: true that is draft
  - rules/rule-ratification: status: a page with core: true that is draft
  - rules/rule-skill-hi: status: a page with core: true that is draft
  - rules/rule-spec-box: status: a page with core: true that is draft
  - rules/rule-synthesis: status: a page with core: true that is draft
  - estimates/estimate-ask-query-before-a-create: unread: failed
  - estimates/estimate-case-build-reads-each-list-of-a-new-member: unread: failed
  - estimates/estimate-case-build-reads-the-readers-of-a-changed-step: unread: failed
  - estimates/estimate-orchestration-names-related-cases-in-the-dispatch: unread: failed
  - estimates/estimate-orchestration-shows-the-built-case: unread: failed

## Expected red

