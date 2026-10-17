---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-package]]"
purpose: Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook, skill, agent, workflow and page runs them through uv run --project .guppi, and the modules and the guards take that form
method: "by hand, after a render of the harness: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py, then a session opened in the project, /hi typed there, and the output of its hooks read against the Criterion"
checked: 2026-10-17
origin: raw/2026-10-15/0553/ledger.md#case-819.1
sprint: plugin
created: 2026-10-15
tags: [harness, plugin]
---

## Criterion

When:
In the project, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.

Then:
The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
**＋** Each hook of `.claude/settings.json`, and each command of a skill, an agent or a workflow of `.github/workflows/` that runs the code of GUPPI or its tests, runs it through `uv run --project .guppi`, and no hook prints an error.
**＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
**＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
**＋** Each module that finds its own refusals in the transcript by the command of its hook finds them under the command with `--project .guppi` and under the command without it.
**＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
**－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.

## Result

2026-10-17, Retro of session 1805: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py 12 passed; .guppi/ holds guppi, pyproject.toml, uv.lock, tests and a .gitignore of .venv/, and .guppi/pyproject.toml declares pytest and ruff; this session opened after the render --sync of its /hi, and its hooks printed no error

## History

- 2026-10-15 created · [[decision-case-819.1]]
- 2026-10-15 status: pending → failed · raw/2026-10-15/1959/ledger.md#L5
- 2026-10-15 deferred · [[decision-case-837]]
- 2026-10-16 defer by decision-case-837 superseded · [[decision-case-840.2]]
- 2026-10-16 updated: read again after the example of a path pair changes in rule-page-generation and estimate-generate-rewords; the Criterion stands, the method waits for the librarian's run that writes the new example · [[decision-case-840.2]]
- 2026-10-16 status: pending → passed · raw/2026-10-16/0342/ledger.md#L1
- 2026-10-17 updated: the purpose names no Makefile, and the method waits for a render, with no past moment · [[decision-case-875]]
- 2026-10-17 updated: the Criterion replaced whole — the Makefile, prod.yml, the root pyproject.toml, the clean version and the records of the repository of GUPPI moved to estimate-guppi-repository-keeps-the-development-project · [[decision-case-880.8]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L65
