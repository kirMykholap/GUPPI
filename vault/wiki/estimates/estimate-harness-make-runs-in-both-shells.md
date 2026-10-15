---
type: estimate
kind: QA
status: passed
target: "[[rule-harness]]"
purpose: Whether the Makefile that this repository keeps for now runs its targets help, style, test and lint under a POSIX sh from PowerShell as from Git Bash, its target lint runs guppi check alone, and it stops with a message when no sh is found
method: "uv run --project .guppi pytest .guppi/tests/test_lint.py -k makefile; by hand, after the Work Mode that builds this change: make with the targets help, style, test and lint from PowerShell and from Git Bash on Windows, read against the Criterion"
checked: 2026-10-15
origin: raw/2026-09-27/1819/ledger.md#case-457
sprint: migration
created: 2026-09-27
tags: [harness, workflow]
---

## Criterion

When:
On Windows, someone runs make with each of the targets `help`, `style`, `test` and `lint` of the `Makefile` from PowerShell and from Git Bash. `C:/ProgramData/chocolatey/bin/make.exe` reads the `Makefile`.
**＋** Or `.guppi/tests/test_lint.py` runs make with the target `lint` of the `Makefile` in a temporary folder, with a fake `uv` first on the search path that records each call.

Then:
Make runs each recipe under a POSIX `sh`, with stdin read from `/dev/null`, and each target gives the same exit code from PowerShell as from Git Bash.
**＋** The target `lint` runs `uv run --project .guppi guppi check` and nothing else.
**＋** The target `test` runs pytest over the tests of `.guppi/tests/`, and the target `style` runs ruff, both as they did before this change.
**＋** The targets of the pipelines of the MOCs stand as before.
**＋** When make finds no POSIX `sh` on Windows, it stops before any recipe runs, with one message that names the missing shell and the places it searched.
**－** Make never runs a recipe of the `Makefile` under `cmd.exe`.
**－** Running a target changes no file of the working tree.
**－** Outside Windows, the `SHELL` of the `Makefile` stays `/usr/bin/sh`.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_lint.py -k makefile: 2 passed; by hand on Windows, make help/style/test/lint from PowerShell and from Git Bash: exit 0/0/2/2 in both shells, the same in each, test and lint red on the expected red of work.md; git status the same before and after

## History

- 2026-09-27 created · [[decision-case-457]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L18
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-15 updated: the Criterion replaced whole — the Makefile stays for now, and its target lint runs guppi check · [[decision-case-820.7]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L11
