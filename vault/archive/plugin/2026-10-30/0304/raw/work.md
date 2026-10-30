## Baseline

- `uv run --project .guppi guppi test`: exit 0 — 1786 passed, 6 skipped, 1 deselected; no failing test.
- `uv run --project .guppi guppi check`: exit 1, 12 lines:
  - backlog: vault/wiki/backlog.md differs from its sources
  - entities/entity-sprint: status: a page with core: true that is draft
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-close: status: a page with core: true that is draft
  - rules/rule-guppi-package: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-orchestration: status: a page with core: true that is draft
  - rules/rule-ratification: status: a page with core: true that is draft
  - rules/rule-skill-hi: status: a page with core: true that is draft
  - rules/rule-work-mode: status: a page with core: true that is draft
  - estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with
  - ship: .guppi/tests/test_render.py:500: a reference to a case: Case 914

## Expected red
