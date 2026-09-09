---
title: "A background job with buffered output cannot be told from a dead one, and the session promised a notification from neither"
type: lesson
status: archived
authority: background-job-liveness
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md"]
tags: [harness, process, testing]
---

# What happened, 2026-08-26

**A proof script was left running for 40 minutes while the session told the owner a notification was
coming.** Python buffered its stdout, so the output file stayed empty; the process list showed the
processes alive at zero CPU.

**The claim that something was running was made without checking that anything was running.** An
empty output file and a live-looking process are exactly what a finished, a hung and a dead job all
produce.

# Why the two states are indistinguishable from outside

**Buffered stdout means the file is empty until the buffer flushes or the process exits**, so
file size carries no information about progress. **Zero CPU** is what a blocked process and a
finished-but-unreaped one both show.

**So the observable evidence is empty in both directions**, and the honest report is *I do not know
whether it is running*, not *it is running*.

# What would have made it checkable

- **Unbuffered output**, or a heartbeat line the job writes on a timer, turns an empty file into a
  positive signal rather than an absence of one.
- **A timestamp taken at launch.** The same session launched
  `bash scripts/vault-check-selftest.sh` into the background without one, so its `caught 178,
  missed 0` carries no wall clock and cannot be compared against the recorded 34m8s and 37m44s
  ([[a-control-nothing-touched-separates-a-change-from-the-machine]]).

**This is the shape the owner has named before**: when a thing cannot be checked, build the check
rather than explain harder ([[a-chain-proved-in-halves-is-not-proved]]).

# The separate failure it stands beside, and why it is not merged with it

**The owner ruled on 2026-08-26 that this one stays a lesson**, because it has no checkable form,
while the class it was reported next to — file content passed through an intermediary that rewrote
it — earns a mechanical guard
([[file-content-is-written-with-the-tool-and-never-through-a-shell]]). Two failures in one session
are not thereby one class.

# `stdbuf -oL -eL` does not repair it, and the timestamp rule answers only half — 2026-08-26

**Measured twice on one day, by two sessions, on the same run.** `stdbuf -oL -eL` was applied to
`bash scripts/vault-check-selftest.sh` and **28 minutes in the log held one line**: the suite
accumulates its own output, so line buffering on the pipe changes nothing.

**Liveness had to be inferred indirectly, from 37 shell processes.**

**The timestamp requirement solves half the problem it was written for.** A start time answers *when
it began* and does not answer *whether it is alive*, which is the question a reader of a background
run actually has ([[the-suite-stops-running-every-session]]).

**And the run cannot be told dead by having been stopped either.** `TaskStop` reaches the tracked
parent and not the tree ([[an-msys-signal-does-not-reach-a-native-windows-process]]).

**The run in question was killed unfinished at 56 minutes and produced no reading at all**, which is
part of what took the full suite out of the session loop.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md` and `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*
