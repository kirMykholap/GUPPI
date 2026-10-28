# Work — 2026-10-26, session 0118

## Baseline

- `uv run --project .guppi guppi test`: exit 0 — 1768 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1 — 15 lines:
  - backlog: vault/wiki/backlog.md differs from its sources
  - entities/entity-sprint: status: a page with core: true that is draft
  - rules/rule-case-build: status: a page with core: true that is draft
  - rules/rule-close: status: a page with core: true that is draft
  - rules/rule-git-context: status: a page with core: true that is draft
  - rules/rule-guppi-package: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-orchestration: status: a page with core: true that is draft
  - rules/rule-ratification: status: a page with core: true that is draft
  - rules/rule-skill-hi: status: a page with core: true that is draft
  - rules/rule-spec-write: status: a page with core: true that is draft
  - rules/rule-work-mode: status: a page with core: true that is draft
  - estimates/estimate-clean-branch-ships-neutral-texts: unread: failed
  - estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with
  - estimates/estimate-spec-write-writes-a-defer: unread: failed

## Expected red
