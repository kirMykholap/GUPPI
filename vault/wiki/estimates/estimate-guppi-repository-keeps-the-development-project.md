---
type: estimate
kind: QA
status: passed
target: "[[entity-guppi-repository]]"
purpose: Whether the repository of GUPPI keeps the files of a development project around the package in .guppi/, its Makefile and its workflow prod.yml run the code through uv run --project .guppi, and the clean version holds no pyproject.toml at its root
method: "uv run --project .guppi pytest .guppi/tests/test_guppi_package.py; by hand: the Makefile, .github/workflows/prod.yml and the root of the repository read against the Criterion, written into the estimate line"
origin: raw/2026-10-17/1805/ledger.md#case-880.9
sprint: plugin
created: 2026-10-17
tags: [harness, plugin]
---

## Criterion

When:
In the repository of GUPPI, the `Makefile` and `.github/workflows/prod.yml` run the code of GUPPI or its tests, `uv run --project .guppi pytest` runs `.guppi/tests/test_guppi_package.py`, and `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it.

Then:
Each command of the `Makefile` and of `.github/workflows/prod.yml` that runs the code of GUPPI or its tests runs it through `uv run --project .guppi`.
**＋** `.guppi/tests/test_guppi_package.py` fails on a command of the `Makefile` that runs that code or those tests through `uv run` without `--project .guppi`.
**＋** The repository keeps at its root, until a Case of a later session removes them, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so a command without `--project .guppi` still runs at its root and no hook of a running session fails.
**＋** The clean version holds no `pyproject.toml` and no `uv.lock` at its root.
**－** The Decision pages, the lessons and the Insights keep the commands and the paths from before the code moved under `.guppi/`, since they are records.

## Result

2026-10-17, Retro of session 1805: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py 12 passed; each command of the Makefile that runs the code or the tests and the ship step of .github/workflows/prod.yml run through uv run --project .guppi; the root holds pyproject.toml and uv.lock; the clean version that guppi ship --allow-draft wrote at this session's /hi holds neither at its root

## History

- 2026-10-17 created · [[decision-case-880.9]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L66
