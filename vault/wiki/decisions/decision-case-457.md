---
type: decision
case: "457"
status: current
create: ["[[estimate-harness-make-runs-in-both-shells]]"]
origin: raw/2026-09-27/1819/ledger.md#case-457
sprint: migration
created: 2026-09-27
tags: [harness, workflow]
---

## Context

The `Makefile` sets `SHELL := /usr/bin/sh`. Its header comment says that every recipe closes its own stdin, because a PowerShell child that inherits stdin from make hangs. Every recipe but `help` ends in `< /dev/null`. `help` runs awk over `$(MAKEFILE_LIST)` and has no redirect. On this machine, `make` is the native Windows GNU make at `C:/ProgramData/chocolatey/bin/make.exe`. Windows has no `/usr/bin/sh` path, so make looks for `sh.exe` on `PATH`. Under Git Bash, `PATH` holds Git's `usr/bin`, so every target runs. Under PowerShell, `sh` is not on `PATH` (the main agent read `(Get-Command sh).Source` as empty). Make then falls back to `cmd.exe`. There `< /dev/null` names no file, and the single quotes of the awk program of `help` do not quote. The handoff of session 1255 saw the failure on `make style`. Nobody has reproduced it yet, because Plan Mode runs no make.
The person chose these answers in the rounds: the Makefile finds a POSIX shell by itself, a new Estimate on `rule-harness` holds the promise, and make stops with a message when it finds no such shell. `help` gets `< /dev/null` because the header comment already requires it of every recipe, not because of a new choice. No page governs the Makefile as a whole. `rule-lint` names it in `implementation_ref`, and its Purpose sentence that no target writes to the tree stays true. `estimate-harness-pipeline` is about the order and the exit of `make lint` and `make test-harness`, not their shell, so it stays as it is. The Criterion of `estimate-tests-clock-pinned` stands. Its line "The `Makefile` does not change" belongs to the fixture of case 145.1 and means that the fixture needed no new target. This Case does not touch that fixture or what `make test` collects, and replacing that Criterion would set a sound promise `pending` again. The skills `retro` and `carry` call `make` and need no change of text. The slug `estimate-harness-make-runs-in-both-shells` is free. The `create` carries a `ref`, so no vault query ran.

## Problem

From PowerShell, make runs its recipes under `cmd.exe`. That shell cannot read `< /dev/null` or the quoted awk program of `help`. So `make style` fails there, and every other target should fail the same way. The agent can run the checks only through Bash, and nothing says so.

## Given

`Makefile` — the shell its recipes run under; its header comment requires every recipe to close stdin
**＋** `/usr/bin/sh` — the `SHELL` of the `Makefile` outside Windows
**＋** `/dev/null` — the device each recipe of the `Makefile` reads its stdin from
**＋** `C:/ProgramData/chocolatey/bin/make.exe` — the native Windows GNU make that reads it
**＋** `estimate-harness-make-runs-in-both-shells` — the new promise
**＋** `rule-harness` — the MOC of the harness tools, the target of the promise

## History

- 2026-09-27 created · raw/2026-09-27/1819/ledger.md#case-457
