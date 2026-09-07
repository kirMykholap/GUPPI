---
title: "`git check-ignore --stdin` receives nothing through a Windows PowerShell pipe, and it fails towards nothing-is-ignored"
type: lesson
status: archived
authority: check-ignore-stdin
basis: measurement
sprint: S3
created: 2026-08-26
sources: [".claude/hooks/gate-the-handoff.ps1", "scripts/hook-selftest.ps1"]
tags: [harness, testing, process]
---

# The measurement, 2026-08-26

**In a fresh repository whose `.gitignore` holds `.superpowers/`, under Windows PowerShell 5.1:**

| form | exit | output |
|---|---|---|
| `git check-ignore <path>` | `0` | the path |
| the same paths piped into `git check-ignore --stdin` | `1` | nothing |

**`1` from `check-ignore` means *no path was ignored*.** It is the same code the command returns
when the answer is genuinely no, so there is no way to tell an empty answer from an empty input by
reading the exit code alone.

# Why it matters more than a quoting bug

**It fails in the direction that opens a gate.** The consumer here is
[[the-gate-on-handoff-refuses-and-is-argued-against-the-refusal-test]], which reads the ledger for
the latest `write:` row **naming a path git does not ignore**. If nothing is ever ignored, every
write into `.superpowers/` counts as a real write, the smoke row is always stale against it, and
`/handoff` is refused for ever.

**A refusal that can never be cleared is worse than no gate**, and it arrives at the end of a
session, at the point of no return ([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).
The hook's own page argues that the condition must be **measured rather than judged**
([[a-hook-refuses-on-a-measured-condition-a-reliable-measurement-and-a-refusal-that-says-how-to-clear-it]]);
this is the case where the measurement is taken correctly and the *instrument* returns a wrong
answer silently, in the dangerous direction ([[an-instrument-that-fails-towards-nothing-to-do]]).

# What found it

**A selftest case, not a review.** The argument form and the `--stdin` form look interchangeable in
the documentation and the defect is invisible in the diff; what separated them was running both and
comparing ([[knowing-a-rule-is-not-a-mechanism]]).

**The repair is to use the argument form**, which is one process per batch of paths rather than one
per path and needs no pipe at all.

# What this does not say

**It is not a claim about `git check-ignore` on other hosts.** The reading is Windows PowerShell 5.1,
which is the only shell on this machine ([[a-hook-is-measured-from-powershell-or-not-at-all]]). What
generalises is the shape: **a native command reading standard input through a PowerShell pipeline is
a thing to measure rather than assume**, and `Add-Content -Encoding UTF8` writing a BOM is the same
class from the writing side ([[add-content-utf8-writes-a-bom-in-front-of-the-first-field]]).
