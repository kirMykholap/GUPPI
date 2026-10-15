---
type: lesson
kind: error
root_cause: the Case named the file of the pytest settings from where the package lives, without checking which config file a run from the root of the repository reads
status: clustered
insight: "[[insight-case-build-rests-on-an-unchecked-fact-of-a-tool]]"
origin: raw/2026-10-15/1959/ledger.md#L73
sprint: plugin
created: 2026-10-15
tags: [tests, case-build]
---

## Trigger

Case 823.1 set the marker live and its addopts in .guppi/pyproject.toml; the first full `uv run --project .guppi guppi test` after the task ran the live test anyway and warned of an unknown mark, since pytest from the root reads the [tool.pytest.ini_options] of the root pyproject.toml; Work Mode added the same two lines there

## Root cause

the Case named the file of the pytest settings from where the package lives, without checking which config file a run from the root of the repository reads

## History

- 2026-10-15 created · raw/2026-10-15/1959/ledger.md#L73
- 2026-10-15 updated: clustered under insight-case-build-rests-on-an-unchecked-fact-of-a-tool (synthesis) · raw/2026-10-15/1959/ledger.md#L73
