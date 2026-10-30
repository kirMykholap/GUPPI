---
type: rule
kind: Leaf
purpose: Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in the repository of GUPPI
status: draft
enforcement: check
implementation_ref: [.guppi/pyproject.toml, .guppi/tests/test_guppi_package.py]
parent: "[[rule-harness]]"
estimates: ["[[estimate-guppi-package-runs-from-its-own-folder]]", "[[estimate-guppi-package-is-ready-after-the-install]]"]
origin: raw/2026-10-15/0553/ledger.md#case-819.1
sprint: plugin
created: 2026-10-15
tags: [harness, plugin]
ref: rule-harness
core: true
---

## Purpose

Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in the repository of GUPPI. The code of GUPPI, the package `guppi`, stands in `.guppi/guppi/`, with its `.guppi/pyproject.toml`, its lock file `.guppi/uv.lock`, its tests in `.guppi/tests/` and a `.guppi/.gitignore` that keeps its Python environment `.guppi/.venv/` out of git. Each caller runs the code as `uv run --project .guppi guppi …` — the hooks of `.claude/settings.json`, the skills and the agents — and the tests as `uv run --project .guppi pytest`. The key `test` of `guppi.toml` names the folder `.guppi/tests`, since pytest looks for its settings only in the folder it starts in and the folders above it, and skips a folder whose name starts with a dot: so it reads the settings of `.guppi/pyproject.toml` whatever the root of the project holds (as set in case 929). `.guppi/pyproject.toml` declares the version of Python, the one runtime dependency PyYAML, and pytest and ruff for the tests. The code finds the project by the folder that Claude Code was opened in, so it reads the vault of the project from there. The test `.guppi/tests/test_guppi_package.py` fails on a command that runs the code or the tests through `uv run` without `--project .guppi`, in a file of `.claude/` or `.github/workflows/`, the `Makefile` where one stands, or a live rule, entity or Estimate, and on a path of the code or the tests outside `.guppi/` in such a page, found by the matching of `reword` of `guppi generate`. `guppi ship` writes no `pyproject.toml` and no `uv.lock` at the root of the clean version (the repository of GUPPI keeps at its root, for now, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so that a session whose hooks still name the command without `--project .guppi` keeps working, and a `Makefile` that runs the code the same way; a later Case removes them, as set in case 819).

## History

- 2026-10-15 created · [[decision-case-819.1]]
- 2026-10-15 estimate estimate-guppi-package-runs-from-its-own-folder added · [[decision-case-819.1]]
- 2026-10-15 updated: every live rule, entity and Estimate names the command, the code and the tests of GUPPI under .guppi/, and the page ships · [[decision-case-819.1]]
- 2026-10-15 estimate estimate-guppi-package-is-ready-after-the-install added · [[decision-case-819.4]]
- 2026-10-15 deferred · [[decision-case-834]]
- 2026-10-16 deferred · [[decision-case-848]]
- 2026-10-17 updated: the root files and the Makefile of the repository of GUPPI move into the bracket of their pointer · [[decision-case-875]]
- 2026-10-29 status: draft → built · cascade
- 2026-10-29 status: built → draft · cascade
- 2026-10-30 defer by decision-case-834 superseded · [[decision-case-929]]
- 2026-10-30 defer by decision-case-848 superseded · [[decision-case-929]]
- 2026-10-30 updated: taken up: the test command names .guppi/tests, so pytest finds the tests of GUPPI with no root pyproject.toml; the root pyproject.toml of the repository of GUPPI keeps its pytest settings until the Case that removes it · [[decision-case-929]]
