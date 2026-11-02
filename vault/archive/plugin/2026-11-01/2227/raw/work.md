# Work — session 2227

## Baseline

- `uv run --project .guppi guppi test`: exit 0 — 1898 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1 — 9 lines:
  - rules/rule-ask: status: a page with core: true that is draft
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-orchestration: status: a page with core: true that is draft
  - rules/rule-skill-approve-spec: status: a page with core: true that is draft
  - rules/rule-skill-hi: status: a page with core: true that is draft
  - rules/rule-spec-box: status: a page with core: true that is draft
  - rules/rule-synthesis: status: a page with core: true that is draft
  - estimates/estimate-case-build-reads-the-readers-of-a-new-files-folder: unread: failed

## Expected red
