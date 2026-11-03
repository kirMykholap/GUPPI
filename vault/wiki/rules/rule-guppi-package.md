---
type: rule
kind: Leaf
purpose: Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in the repository of GUPPI
status: built
enforcement: check
implementation_ref: [.guppi/pyproject.toml, .guppi/tests/test_guppi_package.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-guppi-package-runs-from-its-own-folder]]", "[[estimate-guppi-package-is-ready-after-the-install]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, plugin]
ref: rule-harness
core: true
---

## Purpose

Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in the repository of GUPPI. The code of GUPPI, the package `guppi`, stands in `.guppi/guppi/`, with its `.guppi/pyproject.toml`, its lock file `.guppi/uv.lock`, its tests in `.guppi/tests/` and a `.guppi/.gitignore` that keeps its Python environment `.guppi/.venv/` out of git. Each caller runs the code as `uv run --project .guppi guppi …` — the hooks of `.claude/settings.json`, the skills and the agents — and the tests as `uv run --project .guppi pytest`. The key `test` of `guppi.toml` names the folder `.guppi/tests`, since pytest looks for its settings only in the folder it starts in and the folders above it, and skips a folder whose name starts with a dot: so it reads the settings of `.guppi/pyproject.toml` whatever the root of the project holds. `.guppi/pyproject.toml` declares the version of Python, the one runtime dependency PyYAML, and pytest and ruff for the tests. The code finds the project by the folder that Claude Code was opened in, so it reads the vault of the project from there. The test `.guppi/tests/test_guppi_package.py` fails on a command that runs the code or the tests through `uv run` without `--project .guppi`, in a file of `.claude/` or `.github/workflows/`, the `Makefile` where one stands, or a live rule, entity or Estimate, and on a path of the code or the tests outside `.guppi/` in such a page, found by the matching of `reword` of `guppi generate`. `guppi ship` writes no `pyproject.toml` and no `uv.lock` at the root of the clean version.

## History

- 2026-11-03 shipped with GUPPI
