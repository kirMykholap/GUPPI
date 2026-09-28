## Case 457 — `make` runs its recipes under a POSIX shell from PowerShell too

> **context:**
> The `Makefile` sets `SHELL := /usr/bin/sh`. Its header comment says that every recipe closes its own stdin, because a PowerShell child that inherits stdin from make hangs. Every recipe but `help` ends in `< /dev/null`. `help` runs awk over `$(MAKEFILE_LIST)` and has no redirect. On this machine, `make` is the native Windows GNU make at `C:/ProgramData/chocolatey/bin/make.exe`. Windows has no `/usr/bin/sh` path, so make looks for `sh.exe` on `PATH`. Under Git Bash, `PATH` holds Git's `usr/bin`, so every target runs. Under PowerShell, `sh` is not on `PATH` (the main agent read `(Get-Command sh).Source` as empty). Make then falls back to `cmd.exe`. There `< /dev/null` names no file, and the single quotes of the awk program of `help` do not quote. The handoff of session 1255 saw the failure on `make style`. Nobody has reproduced it yet, because Plan Mode runs no make.
> The person chose these answers in the rounds: the Makefile finds a POSIX shell by itself, a new Estimate on `rule-harness` holds the promise, and make stops with a message when it finds no such shell. `help` gets `< /dev/null` because the header comment already requires it of every recipe, not because of a new choice. No page governs the Makefile as a whole. `rule-lint` names it in `implementation_ref`, and its Purpose sentence that no target writes to the tree stays true. `estimate-harness-pipeline` is about the order and the exit of `make lint` and `make test-harness`, not their shell, so it stays as it is. The Criterion of `estimate-tests-clock-pinned` stands. Its line "The `Makefile` does not change" belongs to the fixture of case 145.1 and means that the fixture needed no new target. This Case does not touch that fixture or what `make test` collects, and replacing that Criterion would set a sound promise `pending` again. The skills `retro` and `carry` call `make` and need no change of text. The slug `estimate-harness-make-runs-in-both-shells` is free. The `create` carries a `ref`, so no vault query ran.

> **problem:**
> From PowerShell, make runs its recipes under `cmd.exe`. That shell cannot read `< /dev/null` or the quoted awk program of `help`. So `make style` fails there, and every other target should fail the same way. The agent can run the checks only through Bash, and nothing says so.

> **recommend:**
> Change the `Makefile` on Windows so that make finds a POSIX `sh` itself and never falls back to `cmd.exe`. If no such shell exists, make stops with a message that names the cause. The recipes keep their `< /dev/null`, and `help` gets one too, as the header comment requires. A new Estimate on `rule-harness` keeps the promise in view. The rejected option was a written rule that `make` runs only through Bash, which leaves a trap for any caller who does not read it.

> **given:**
> `Makefile` — the shell its recipes run under; its header comment requires every recipe to close stdin
> **＋** `/usr/bin/sh` — the `SHELL` of the `Makefile` outside Windows
> **＋** `/dev/null` — the device each recipe of the `Makefile` reads its stdin from
> **＋** `C:/ProgramData/chocolatey/bin/make.exe` — the native Windows GNU make that reads it
> **＋** `estimate-harness-make-runs-in-both-shells` — the new promise
> **＋** `rule-harness` — the MOC of the harness tools, the target of the promise

> **when:**
> On Windows, someone runs `make help`, `make style`, `make test` or `make lint` of the `Makefile` from PowerShell and from Git Bash. `C:/ProgramData/chocolatey/bin/make.exe` reads the `Makefile`.

> **then:**
> Make runs each recipe under a POSIX `sh`, with stdin read from `/dev/null`. Each target gives the same exit code from PowerShell as from Git Bash.
> **＋** When make finds no POSIX `sh` on Windows, it stops before any recipe runs, with one message that names the missing shell and the places it searched.
> **－** Make never runs a recipe of the `Makefile` under `cmd.exe`.
> **－** No recipe of the `Makefile` reads the stdin of its caller, and no target writes to the working tree.
> **－** Outside Windows, the `SHELL` of the `Makefile` stays `/usr/bin/sh`.

> **tasks:**
> - [ ] create `estimate-harness-make-runs-in-both-shells`
>   - type: `estimate`
>   - kind: `QA`
>   - purpose: `make help, make style, make test and make lint run their recipes under a POSIX sh from PowerShell as from Git Bash, and stop with a message when no sh is found`
>   - method: `by hand, make help, make style, make test and make lint from PowerShell and from Git Bash on Windows, at the first session after the change`
>   - tags: `[harness, workflow]`
> - [ ] `Makefile` — reproduce the failure of `make style` from PowerShell first. Then, on Windows only, set `SHELL` to a POSIX `sh` that make finds without Git's `usr/bin` on `PATH`, and stop with one message when none is found. Keep `/usr/bin/sh` elsewhere and every stdin redirect from `/dev/null`. Add the redirect to the `help` recipe. Add one sentence to the header comment on the shell.
> - [ ] by hand — `make help`, `make style`, `make test` and `make lint` from PowerShell and from Git Bash: the same exit code in both, no `cmd.exe` error
> - [ ] read `estimate-harness-make-runs-in-both-shells` — by hand, at the first session after the change

> **ratification:**
> ```
> - decision[case 457][create][estimate-harness-make-runs-in-both-shells]{ref:rule-harness}{tags:harness,workflow}
> ```
