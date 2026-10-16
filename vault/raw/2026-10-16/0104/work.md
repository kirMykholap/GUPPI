# Work — session 0104

## Baseline

- `uv run --project .guppi guppi test`: exit 1 — 1 failed, 1714 passed, 6 skipped, 1 deselected
  - FAILED .guppi/tests/test_guppi_package.py::test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]
- `uv run --project .guppi guppi check`: exit 1
  - backlog: vault/wiki/backlog.md differs from its sources
  - entities/entity-sprint: status: a page with core: true that is draft
  - rules/rule-guppi-package: status: a page with core: true that is draft
  - rules/rule-harness: status: a page with core: true that is draft
  - rules/rule-morph: status: a page with core: true that is draft
  - rules/rule-ratification: status: a page with core: true that is draft
  - rules/rule-skill-hi: status: a page with core: true that is draft
  - rules/rule-work-mode: status: a page with core: true that is draft
  - estimates/estimate-clean-branch-installs-as-a-plugin: unread: failed
  - estimates/estimate-guppi-package-runs-from-its-own-folder: unread: failed
  - estimates/estimate-guppi-tests-green: method: a MOC's Estimate names no `make <target>` or `pytest` with test files
  - estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with
  - estimates/estimate-harness-pipeline: unread: failed
  - estimates/estimate-page-schemas-one-file-per-rule: method: says by hand while estimate-entities-schema-checked names a test file
  - estimates/estimate-plugin-install-writes-guppi-into-an-empty-project: unread: failed

## Expected red
