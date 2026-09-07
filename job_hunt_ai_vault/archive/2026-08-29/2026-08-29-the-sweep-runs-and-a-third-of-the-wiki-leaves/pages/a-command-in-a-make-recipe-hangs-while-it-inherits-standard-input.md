---
title: "A command in a `make` recipe hangs while it inherits standard input, and the redirect belongs on the command rather than on the recipe"
type: lesson
status: archived
authority: make-recipe-stdin
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["Makefile", "scripts/hook-selftest.ps1"]
tags: [harness, testing, process]
---

# The incident, measured 2026-08-26

**`powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/hook-selftest.ps1`, run from a
`make` recipe with standard input inherited, does not return.** The first attempt sat **forty-nine
minutes at zero CPU** before anyone looked at it; two further attempts were killed at 100 s and at
200 s, both at zero CPU.

**The same command with `< /dev/null` written on it finishes in 43 s** and reports its score. Zero
CPU is the whole diagnosis: nothing was slow, something was waiting.

**What it waits on** is an inherited console handle that never closes. The suite spawns on the order
of a hundred and seventy child processes and feeds them through pipes, and a child holding a handle
to a standard input nobody will ever close is a child that does not exit.

# Three repairs that look right and are not

**`exec < /dev/null` at the head of the recipe does not work, and it was tried twice.** It reads as
the tidier form — one redirection for the whole block — and the run hung at the same step with it in
place, against three runs that finished with the redirect written on each command. Whatever `exec`
does to the recipe shell's own descriptor is not what the spawned process inherits.

**Recursion through `$(MAKE)` was the first suspect and was measured innocent.** The selftest
invoked from a recipe that had just run a sub-make finished in 42 s, exactly as one invoked with no
recursion at all did. The jobserver was a plausible cause and it was the wrong one.

**A timeout is not the fix and made it worse.** `timeout 330` returned having killed `make` and
`bash` and left two `powershell` processes running: an MSYS signal does not reach a native Windows
process, which this repository has now measured more than once
([[an-msys-signal-does-not-reach-a-native-windows-process]]).

# What follows

**Close standard input on every command in a recipe, not on the one that bit.** No check in this
repository's `Makefile` reads standard input, so the redirect is correct everywhere, and one rule
that always holds is worth more than an exemption list somebody has to keep true — the same ground
on which the governed set is swept rather than listed
([[the-governed-set-is-swept-and-markdown-by-property]]).

**And zero CPU is the observable that separates hung from slow.** The session before this one spent
an hour on a starved-machine theory about a process that was hung, and the repair there was the
same shape: look at what the process is doing before theorising about the machine
([[a-trace-answered-in-ninety-seconds-what-an-hour-of-process-archaeology-did-not]]).

**A later reader tempted to collapse the per-command redirects into one should collapse them and
time the result.** The per-command form is the one with a measurement behind it.
