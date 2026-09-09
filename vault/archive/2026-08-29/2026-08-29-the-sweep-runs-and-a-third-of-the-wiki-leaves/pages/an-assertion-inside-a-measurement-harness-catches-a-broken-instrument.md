---
title: "An assertion inside a measurement harness catches a broken instrument before it produces a number"
type: lesson
status: archived
authority: assertion-inside-a-measurement-harness
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [testing, process, harness]
---

# What it caught

**The first latency run was about to time a hook that had never received its payload.** The harness
**proved the branch fired before timing it**, and threw instead of reporting
([[a-hook-is-measured-from-powershell-or-not-at-all]]).

**Without the assertion the run would have produced a number.** A plausible one: a hook that reads
an empty payload and exits immediately is fast, and the figure would have said the guard is cheap —
which is even the conclusion the measurement eventually reached, by a route that means something.

# Why a figure from a silent instrument is worse than no figure

**A stand that cannot fail loudly produces figures nobody can trust**, and the store already holds
the cost of the alternative: a claim labelled *measured* that came from an instrument reporting its
own exit code ([[a-claim-labelled-measured-came-from-an-instrument-reporting-its-own-exit-code]]),
and a runbook carrying the nonce it was supposed to measure the delivery of
([[a-runbook-that-carries-the-nonce-cannot-be-read-by-what-it-measures]]).

**The common property of all three is that the instrument answers a different question and the
answer is well-formed.** Nothing in the output says which question was answered.

# The shape to build

**An assertion that the subject did the thing, run before the timing loop and fatal if it fails.**
It is one extra case, it costs one run, and it converts the whole family of *the harness was not
wired up* failures from a silent wrong number into a stop.

**It is the measurement-side twin of proving a case fails before the change**
([[a-case-that-passes-before-the-change-tests-nothing]],
[[a-case-that-fails-for-its-own-reason-tests-nothing-either]]): in both, what is established first
is that the apparatus can distinguish the two outcomes at all.

## Second instance, and it is why the assertion is now on the score line — 2026-08-20

**A measurement wrapper reported success about a run that never executed.** It grepped the suite's
output for `MISSED`, found none, and printed *no misses* about a suite killed by a syntax error
before its first case ran ([[a-script-must-not-be-edited-while-it-is-running]]).

**Fixed by requiring the score line to exist before reading anything off the run.** Absence of a
failure marker is not evidence of success when the run may not have produced any markers at all.

**The general form, and it is the shape this page already carries:** assert that the instrument
*ran* before believing what it *says*. Applied to the setup step it is the same rule —
a planted offender is proved by reading the planted file back
([[a-planted-offender-is-proved-by-reading-it-back]]), and a counter that lives in a backgrounded
subshell prints zero and exits green
([[no-verdict-lives-in-a-variable-in-a-parallel-suite]]).
