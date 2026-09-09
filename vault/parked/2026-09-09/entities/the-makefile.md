---
title: "The `Makefile`, and what each of its targets actually runs"
type: entity
status: current
authority: makefile-targets
basis: code
sprint: S3
created: 2026-08-26
sources: ["Makefile", "archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [harness, testing, process]
---

# What it is

**The single entry point for every check in this repository**, at the repository root, built
2026-08-26. Before it, running "the checks" was four commands typed by hand and the fourth was the
one somebody forgot ([[the-checks-get-a-single-entry-point-and-make-is-the-revived-candidate]]).

**GNU Make 4.4.1 (Built for Windows32)**, installed by chocolatey. `SHELL := /usr/bin/sh`, so a
recipe runs under MINGW64, and both `uv` and `powershell.exe` resolve from inside one.
`.DEFAULT_GOAL := help`.

# The targets

| target | what it runs |
|---|---|
| `help` | an `awk` sweep of `$(MAKEFILE_LIST)` for `## ` comments — the default goal |
| `gate` | `bash scripts/vault-check.sh` against the live corpus |
| `style` | `uv run ruff check src tests` and `uv run ruff format --check src tests` |
| `test` | `uv run pytest -q` |
| `smoke` | `gate`, `style`, the three cheap selftests, and `vault-check-selftest.sh --only` under `ONLY=` |
| `suite` | `smoke` plus `scripts/vault-check-selftest.sh` whole |

**What each target costs and what a red one obliges is decided elsewhere** and is not restated
here ([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

# Four properties of the file that are decisions rather than style

**`smoke` uses no prerequisites, and that is the point.** `smoke: gate style` reads better and is
wrong: make aborts a target when a prerequisite fails, so a red gate would hide whether the
selftests pass. Each step is invoked through `$(MAKE)` or directly, its failure caught with `||`,
and the accumulated code is what the target exits with. A run taken before handing work over has to
report every verdict it has, not the first one it hits.

**Every recipe line closes its own standard input, and the rule is every line rather than the one
that bit.** No check in this file reads standard input, so closing it is correct everywhere, and one
rule that always holds beats an exemption list somebody has to keep true. The measurement behind it
is a forty-nine-minute hang at zero CPU
([[a-command-in-a-make-recipe-hangs-while-it-inherits-standard-input]]).

**`smoke` and `suite` each print `SMOKE-EXIT: <n>` or `SUITE-EXIT: <n>` immediately before exiting
with the same number.** That line is written for a reader that is not a shell — the recorder hook
observes somebody else's tool call and cannot claim the exit code as its own
([[a-hook-that-observes-another-tools-run-reads-a-printed-marker-and-not-an-exit-code]]).

**No target here writes.** `style` runs `ruff format --check` rather than `ruff format`, and there
is no target for `scripts/vault-inject.sh`, which edits tracked files. Nothing in this project
decides that a build target may perform the injector-then-gate ritual, so the ritual stays typed.

# `ONLY=` is optional, and its absence is a legal run

**The narrowed slice of the gate's own selftest is named by the session and never inferred from a
diff** — a session that edited one rule and ran another rule's case proves nothing, and nothing
would catch it. With no `ONLY=` the floor still runs, which is the floor clause of
[[the-smoke-runner-is-built-first-thing-next-session]] holding rather than a degraded run
([[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]]).

# `make help` is swept, and the owner ruled the sweep acceptable

**The target list is derived from the file and each description is typed beside its target.** The
arrangement the owner ruled says `help` is typed and generation is carried, and whether a swept list
of typed descriptions is the generation he ruled out was put back to him: **he selected it as
acceptable on 2026-08-26, on the ground that nothing is stored twice so nothing can drift.**

# The file is pinned to LF

`.gitattributes` had it before the checkout that would have converted it, on the owner's «да,
прибиваем сейчас» — announced by git while the file was being committed
([[a-file-class-is-pinned-after-it-costs-something]]).

# Readings

**`make smoke`, no `ONLY=`: `SMOKE-EXIT: 0` in 66-70 s across three runs on 2026-08-26.** The last
of them, at 70 s, is the run that stands behind that session's `/handoff`, with the gate at
`9 of 15` and the three cheap selftests at 180, 52 and 59 cases, all `missed 0`.

**None of those readings includes a suite slice.** `ONLY=` was empty in all three, and the slice
costs about two minutes more ([[an-estimate-can-be-wrong-in-its-reasoning-and-not-only-in-its-number]]).

**`make test` has never run.** Docker was not answering on the day the file was built, so the
fixture could not build the test database
([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]).

# `style` widened on 2026-08-31, and the two halves of it no longer cover the same set

**`style` now runs `ruff check src tests scripts`.** The line above stating its scope as `src tests` was
true until this day and is corrected here rather than deleted.

**`ruff format --check` still covers `src tests` only**, deliberately: it would fail on six existing
files in `scripts/`, and reformatting scripts nobody is reviewing belongs in a diff someone reads
([[scripts-joins-make-style-and-only-the-check-half]]). **So the check half and the format half of one
target now read different sets**, and that asymmetry is decided rather than accidental.

**Ten findings were fixed before the widening landed**, so the target was green the first time it ran
wide — four `subprocess.run` calls given an explicit `check=False` with the reason on each, two
`date.today()` calls kept as the local date under a `noqa`, one unused import, one implicit
concatenation, one enumerate loop, one open alias.

**The folder had never been linted by any target**, which is the finding worth more than the change
([[a-target-that-covers-part-of-a-repository-reports-clean-about-that-part]]).

*(Extended at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
