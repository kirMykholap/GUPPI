---
type: lesson
kind: error
root_cause: the clean version writes no ignore file that covers `__pycache__/`; its only ignore files are `.guppi/.gitignore` for `.venv/` and `vault/.gitignore` for the event logs
status: new
origin: raw/2026-11-04/0358/ledger.md#L35
sprint: plugin
created: 2026-11-04
tags: [git, plugin]
---

## Trigger

2026-11-04, the trial session in C:/PROJECTS/guppi-trial-0358/empty-git (transcript 93058e9a, L838 to L862): the gate refused /handoff four times on `.guppi/guppi/__pycache__/` and `.guppi/tests/__pycache__/` until the agent added `__pycache__/` to .git/info/exclude

## Root cause

the clean version writes no ignore file that covers `__pycache__/`; its only ignore files are `.guppi/.gitignore` for `.venv/` and `vault/.gitignore` for the event logs

## History

- 2026-11-04 created · raw/2026-11-04/0358/ledger.md#L35
