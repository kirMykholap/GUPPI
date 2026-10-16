# Work — session 0342

## Baseline

- `uv run --project .guppi guppi test`: exit 0 — 1715 passed, 6 skipped, 1 deselected
- `uv run --project .guppi guppi check`: exit 1
  - entities/entity-sprint: status: a page with core: true that is draft
  - rules/rule-guppi-package: status: a page with core: true that is draft
  - rules/rule-harness: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-ratification: status: a page with core: true that is draft
  - rules/rule-skill-hi: status: a page with core: true that is draft
  - rules/rule-work-mode: status: a page with core: true that is draft
  - estimates/estimate-clean-branch-ships-the-tests: unread: failed
  - estimates/estimate-clean-branch-writes-the-session-files: unread: failed
  - estimates/estimate-guppi-tests-green: method: a MOC's Estimate names no `make <target>` or `pytest` with test files
  - estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with
  - estimates/estimate-harness-pipeline: unread: failed
  - estimates/estimate-page-schemas-one-file-per-rule: method: says by hand while estimate-entities-schema-checked names a test file

## Expected red
