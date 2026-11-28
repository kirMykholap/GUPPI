---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-package]]"
purpose: Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook runs them through .guppi under the folder that Claude Code was opened in, so that a cd in a Bash call cannot break it, every skill, agent, workflow and page runs them through uv run --project .guppi, and the modules and the guards take those forms
method: "by hand, after the render of the harness by the librarian's run of the session that ratifies this Criterion: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py, then a session opened in the project, /hi typed there, a Bash call that runs cd vault/wiki, and a later tool call and reply; the output of its hooks in the transcript of that session under ~/.claude/projects/ read against the Criterion, recorded in the estimate line"
checked: 2026-11-23
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [harness, plugin]
core: true
---

## Criterion

When:
In the project, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.
**＋** A Bash call of that session runs a `cd` into a folder of the project, and the shell stays there.

Then:
The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
**＋** Each hook of `.claude/settings.json`, and the hook in the frontmatter of `.claude/agents/librarian-guppi.md`, runs the code through `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi"`, so it finds `.guppi/` wherever the shell stands.
**＋** After the `cd`, the hooks of the next tool call and of the next reply run, and none prints an error or refuses for want of `.guppi/`.
**＋** Each command of a skill, an agent or a workflow of `.github/workflows/` that runs the code of GUPPI or its tests runs it through `uv run --project .guppi`.
**＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` with no `--project` that names `.guppi`, outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
**＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
**＋** Each `Stop` hook that finds its own refusals in the transcript finds them as `estimate-ledger-write-finds-a-refusal-by-the-name-of-its-hook` sets it, whatever the start of its command.
**＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
**－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.

## Result

2026-11-23, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
