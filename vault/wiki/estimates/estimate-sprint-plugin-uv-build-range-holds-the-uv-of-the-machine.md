---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-plugin]]"
purpose: Whether uv sync builds the package guppi from a fresh copy of .guppi/ with no warning that the build line of .guppi/pyproject.toml does not hold the version of uv, on a uv from 0.11 to before 0.14
method: "by hand, in Work Mode of the session that sets this Criterion, after the edit of .guppi/pyproject.toml: .guppi/ copied without .venv/ into an empty folder under the scratchpad of the session, and the output of uv --version and of uv sync --project on that folder, read against the Criterion, the outputs in the estimate line"
origin: raw/2026-11-25/2003/ledger.md#case-1059
sprint: plugin
created: 2026-11-25
tags: [sprint, plugin]
once: true
---

## Criterion

When:
The agent copies `.guppi/` without `.guppi/.venv/` into an empty folder and runs `uv sync --project` on that folder, with a `uv` whose version is 0.11 or later and before 0.14.

Then:
`uv sync` builds the package `guppi` into the Python environment of that folder and exits 0.
**＋** Its output holds no warning that the `build-system.requires` of `.guppi/pyproject.toml` does not hold the version of `uv`.
**－** The range of `uv_build` in `.guppi/pyproject.toml` does not lose its upper bound.

## Result

2026-11-25, Retro of session 2003, `.guppi/` copied without `.venv/` into the scratchpad folder `uvbuild/`, `uv --version` and `uv sync --project <copy>/.guppi`: uv 0.13.10; `uv sync` created the venv, built and installed `guppi==0.1.0` with 9 packages, exit 0, and printed no warning on `build-system.requires`; `.guppi/pyproject.toml` reads `requires = ["uv_build>=0.11,<0.14"]`, the upper bound kept

## History

- 2026-11-26 created · [[decision-case-1059]]
- 2026-11-26 status: pending → passed · raw/2026-11-25/2003/ledger.md#L20
