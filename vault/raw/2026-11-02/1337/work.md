## Baseline

- `uv run --project .guppi guppi test`: exit 0 — 1891 passed, 6 skipped, 1 deselected
- `uv run --project .guppi guppi check`: exit 1
  - rules/rule-orchestration: status: a page with core: true that is draft
  - rules/rule-skill-approve-spec: status: a page with core: true that is draft
  - estimates/estimate-orchestration-acknowledging-reply: unread: failed

## Expected red
