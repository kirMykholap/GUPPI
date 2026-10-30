# Note — Case 929 (C4, rule-guppi-package)

## Questions
- Round 1, Q1 **What this Case changes** — recommended (a) the key test names `.guppi/tests`, root files stay. Answer: agreed, (a).

## Read
- case-schema.md, ratification.md, case-example.md
- rules: rule-guppi-package, rule-guppi-config (whole), rule-morph 1-50
- decisions 834, 848; estimates guppi-package-* (both), guppi-config-* (both), guppi-tests-green
- pyproject.toml (root), .guppi/pyproject.toml, Makefile, guppi.toml, commands.py (whole), ship.py parts, test_guppi_package.py, conftest.py, checks.yml
- Docs: pytest customize + reference (offset 400000), uv cli

## Open forks
- none

## To do
- Case file written (case-929.md); answer with summary; fix findings by Edit.
- Done: casecheck findings (given names the command, .claude/); pre-spec finding: method says make test and make style (case-927.md read; lint.py MAKE_TARGET read). Cases 931, 932 built at the same time: read none of their files.
