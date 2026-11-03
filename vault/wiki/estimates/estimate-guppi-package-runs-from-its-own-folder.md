---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-package]]"
purpose: Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook, skill, agent, workflow and page runs them through uv run --project .guppi, and the modules and the guards take that form
method: "by hand, after a render of the harness: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py, then a session opened in the project, /hi typed there, and the output of its hooks read against the Criterion"
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, plugin]
core: true
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

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
