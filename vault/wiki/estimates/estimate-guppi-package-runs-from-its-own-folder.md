---
type: estimate
kind: QA
status: pending
target: "[[rule-guppi-package]]"
purpose: Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook, skill, agent, Makefile line and page runs them through uv run --project .guppi, the modules and the guards take that form, and the clean version holds no pyproject.toml at its root
method: "uv run --project .guppi pytest .guppi/tests/test_guppi_package.py; by hand, after the librarian's run of the session whose Work Mode moves the code: a session opened in this repository, /hi typed there, and the output of its hooks read against the Criterion"
origin: raw/2026-10-15/0553/ledger.md#case-819.1
sprint: plugin
created: 2026-10-15
tags: [harness, plugin]
---

## Criterion

When:
In the repository of GUPPI, after the move of the code and the render of the harness, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.
**＋** `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it.

Then:
The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
**＋** Each hook of `.claude/settings.json`, and each command of a skill, an agent, the `Makefile` and `.github/workflows/prod.yml` that runs the code of GUPPI or its tests, runs it through `uv run --project .guppi`, and no hook prints an error.
**＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
**＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, the `Makefile`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
**＋** Each module that finds its own refusals in the transcript by the command of its hook finds them under the command with `--project .guppi` and under the command without it.
**＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
**＋** The clean version holds no `pyproject.toml` and no `uv.lock` at its root.
**－** The repository of GUPPI keeps at its root, until a Case of a later session removes them, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so a command without `--project .guppi` still runs at its root and no hook of a running session fails.
**－** The Decision pages, the lessons and the Insights keep the old command and the old paths, since they are records.
**－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.

## History

- 2026-10-15 created · [[decision-case-819.1]]
