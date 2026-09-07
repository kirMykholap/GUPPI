---
title: "The checks get a single entry point, and `make` is revived as the candidate"
type: decision
status: current
authority: check-entry-point
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "CLAUDE.md"]
tags: [harness, testing, process]
---

# The ruling, 2026-08-26, in his own words

> **owner:** «И да, делаем единую точку входа. Мы когда-то обсуждали make. Можем воскресить вопрос.»

**Both `smoke` and `suite` become one command each**, or the naming buys nothing
([[gate-smoke-and-suite-name-different-things-and-gate-keeps-its-meaning]]).

# The gap it closes

**There is no single command today.** Running "the checks" is four commands typed by hand, and the
fourth is the one somebody forgets.

# `make` is present here, measured

**GNU Make 4.4.1 at `/c/ProgramData/chocolatey/bin/make`**, installed through chocolatey, measured
2026-08-26.

**The no-new-dependencies rule does not reach it.** That rule names Python packages and npm, and
`make` is neither — and it is already on the machine.

**Two pages already carry the design** and are revived rather than rewritten:
[[a-makefile-holds-the-projects-pipelines]] and [[the-command-list-moves-into-a-makefile]].

# What is open

**Whether `make` is the answer**, as against a shell script or a skill. The owner reopened the
question rather than settling it — «можем воскресить вопрос» — and it is bound into the proposal that
settles the check system as a whole
([[a-proposal-page-settles-who-runs-which-check-and-when]]).

# The open clause is closed: it is `make` — 2026-08-26

**The owner settled it the same day, by approving the plan the arrangement was written into.** The
entry point is `make`; **a shell script and a skill were both rejected.** GNU Make 4.4.1 at
`/c/ProgramData/chocolatey/bin/make`, measured present that day.

**The section above is left standing**, because what it records is that the question was open when
this page was written. It is answered on
[[make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation]], which is the
proposal [[a-proposal-page-settles-who-runs-which-check-and-when]] ordered.

# The entry point exists and was run, measured 2026-08-26

**`make smoke` with no `ONLY=` slice reported `SMOKE-EXIT 0` in 67 s.** That is the whole floor:
gate, style, hooks and dialogue, each with standard input closed on its own command
([[a-command-in-a-make-recipe-hangs-while-it-inherits-standard-input]]).

**What the number does not mean.** It is not the suite — `bash scripts/vault-check-selftest.sh` is
not in `smoke` and is measured in tens of minutes ([[the-suite-stops-running-every-session]]). It is
one reading on one machine that was otherwise idle; a reading taken beside other work against the
same disk measures nothing
([[a-measurement-taken-while-other-work-runs-against-the-same-disk-measures-nothing]]).

**The component readings of that run**, same day: `scripts/hook-selftest.ps1` **caught 175, missed
0, in 42 s**, and `bash scripts/vault-check.sh` exited 0 with its region-coverage advisory at
**8 of 15** harness markdown files.
