---
type: estimate
kind: QA
status: passed
target: "[[rule-harness]]"
purpose: make help, make style, make test and make lint run their recipes under a POSIX sh from PowerShell as from Git Bash, and stop with a message when no sh is found
method: by hand, make help, make style, make test and make lint from PowerShell and from Git Bash on Windows, in a session
checked: 2026-09-27
origin: raw/2026-09-27/1819/ledger.md#case-457
sprint: migration
created: 2026-09-27
tags: [harness, workflow]
---

## Criterion

When:
On Windows, someone runs `make help`, `make style`, `make test` or `make lint` of the `Makefile` from PowerShell and from Git Bash. `C:/ProgramData/chocolatey/bin/make.exe` reads the `Makefile`.

Then:
Make runs each recipe under a POSIX `sh`, with stdin read from `/dev/null`. Each target gives the same exit code from PowerShell as from Git Bash.
**＋** When make finds no POSIX `sh` on Windows, it stops before any recipe runs, with one message that names the missing shell and the places it searched.
**－** Make never runs a recipe of the `Makefile` under `cmd.exe`.
**－** No recipe of the `Makefile` reads the stdin of its caller, and no target writes to the working tree.
**－** Outside Windows, the `SHELL` of the `Makefile` stays `/usr/bin/sh`.

## Result

2026-09-27, make help/style/test/lint from Git Bash and from PowerShell; exit 0/0/0/2 in both shells (844 passed, 2 skipped), the same 105 lint lines, recipes under C:/Program Files/Git/usr/bin/sh.exe, and make POSIX_DIRS=C:/nowhere/usr/bin help stops with "no POSIX sh" at exit 2

## History

- 2026-09-27 created · [[decision-case-457]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L18
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
