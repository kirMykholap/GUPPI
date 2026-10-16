# Work — session 1959

## Baseline

`uv run --project .guppi guppi test`: exit 1 — 1 failed, 1699 passed, 6 skipped

- FAILED .guppi/tests/test_guppi_package.py::test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]

`uv run --project .guppi guppi check`: exit 1

- backlog: vault/wiki/backlog.md differs from its sources
- entities/entity-sprint: status: a page with core: true that is draft
- rules/rule-claude-md: status: a page with core: true that is draft
- rules/rule-guppi-config: status: a page with core: true that is draft
- rules/rule-guppi-package: status: a page with core: true that is draft
- rules/rule-harness: status: a page with core: true that is draft
- rules/rule-lint: status: a page with core: true that is draft
- rules/rule-morph: status: a page with core: true that is draft
- rules/rule-page-generation: status: a page with core: true that is draft
- rules/rule-skill-hi: status: a page with core: true that is draft
- rules/rule-work-mode: status: a page with core: true that is draft
- estimates/estimate-clean-branch-installs-as-a-plugin: unread: failed
- estimates/estimate-guppi-tests-green: method: a MOC's Estimate names no `make <target>` or `pytest` with test files
- estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with
- estimates/estimate-harness-pipeline: unread: failed
- estimates/estimate-page-schemas-one-file-per-rule: method: says by hand while estimate-entities-schema-checked names a test file
- estimates/estimate-plugin-install-writes-guppi-into-an-empty-project: unread: failed

## Expected red
