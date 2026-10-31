# Work — session 2307

## Baseline

- `uv run --project .guppi guppi test`: exit 0 — 1853 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1 — 19 lines:
  - backlog: vault/wiki/backlog.md differs from its sources
  - estimates/estimate-link-graph-prints-the-neighbours: ref: body names slug, which no live or archived page carries
  - rules/rule-ask: status: a page with core: true that is draft
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-close: status: a page with core: true that is draft
  - rules/rule-estimates-schema: status: a page with core: true that is draft
  - rules/rule-handoff: status: a page with core: true that is draft
  - rules/rule-link-graph-at-session-start: status: a page with core: true that is draft
  - rules/rule-materialize: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-orchestration: status: a page with core: true that is draft
  - rules/rule-ratification: status: a page with core: true that is draft
  - rules/rule-skill-hi: status: a page with core: true that is draft
  - rules/rule-spec-box: status: a page with core: true that is draft
  - rules/rule-synthesis: status: a page with core: true that is draft
  - estimates/estimate-case-build-reads-each-list-of-a-new-member: unread: failed
  - estimates/estimate-link-graph-at-session-start-writes-the-file: unread: pending
  - estimates/estimate-orchestration-names-related-cases-in-the-dispatch: unread: failed
  - estimates/estimate-orchestration-shows-the-built-case: unread: failed

## Expected red
