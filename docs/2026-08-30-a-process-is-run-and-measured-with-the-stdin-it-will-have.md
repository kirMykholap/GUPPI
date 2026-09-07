---
title: "A process is run and measured with the stdin it will actually have"
type: proposal
status: current
authority: stdin-shape-fidelity
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["job_hunt_ai_vault/raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/hook-selftest.ps1", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, testing, process]
---

# What it would be

**Two rules about one file descriptor, and one helper that makes both cheap.**

1. **A hook is timed through a pipe**, because a pipe is how the harness always invokes it. A bare
   spawn is a different subject.
2. **A background task is launched with stdin closed** — `< /dev/null` on the Bash side, the
   equivalent redirect on the PowerShell side — because a backgrounded task leaves stdin open and a
   suite that reads it waits forever.

**The helper is a one-line launch form** written into the harness files that launch things, so the
redirect is what an author copies rather than what an author remembers
([[knowing-a-rule-is-not-a-mechanism]]).

# The two incidents, and why one file descriptor produced both

**They are the same oversight measured from opposite ends: a wrong number and a five-hour hang.**

**The measurement, taken in a shape the subject never runs in.** A new hook was measured at 99 ms
and 141 ms and designed on those figures. Through a pipe — the only shape the harness ever uses — a
bare spawn alone is 359 ms and the hook is 750–930 ms, against 941 ms for the existing
`ask-the-vault.ps1` under the same load. **The design's whole argument was that the new hook was
cheap beside the old one, and at the real shape it is not.** A measurement taken in a shape the
subject never runs in is worse than none, because it is trusted.

**The run, launched in a shape that blocks.** `scripts/hook-selftest.ps1` launched as a background
task lived **330 minutes on 0.125 s and 0.344 s of CPU** — blocked, not slow. With `< /dev/null` it
finished in seven minutes at `caught 224, missed 0`, and the same suite in the foreground finished
in seven minutes earlier the same day. **The owner lost most of a day to it, twice.**

# What the store already says, and what is stronger here

**[[a-background-job-with-buffered-output-cannot-be-told-from-a-dead-one]] says the two states are
indistinguishable from outside** and that the honest report is *I do not know whether it is running*.
It offers a heartbeat and a launch timestamp as the repairs, and records that `stdbuf -oL -eL` does
not help.

**The stronger claim is that backgrounding is not merely opaque — it is the cause.** The job was not
running slowly behind a buffer; it was blocked on a descriptor the launch left open, and the CPU
figures prove it. That page's repairs make a hang visible. This one stops it happening.

# What it would take

- A launch form with the redirect, written into the files that launch suites and probes.
- A measurement form for hooks: `<payload> | <hook>`, with a bare-spawn control taken in the same
  run so the spawn cost can be subtracted ([[a-control-nothing-touched-separates-a-change-from-the-machine]]).
- **Re-measure every hook figure this store carries that was taken without a pipe.** Which of them
  those are is not known and is part of the work.

# What is open

- **Whether the PowerShell redirect is equivalent.** `< /dev/null` was measured on the Bash side; the
  PowerShell form is untested here, and an MSYS-shaped assumption about a native Windows process has
  already cost this project a page ([[an-msys-signal-does-not-reach-a-native-windows-process]]).
- **Whether any harness path launches a suite where the redirect cannot be added**, which would make
  this a convention with a hole in it rather than a rule.
- **Whether the new hook survives its true cost at all.** At 750–930 ms against 941 ms it is not the
  cheap addition it was approved as, and that is the owner's question and not this page's.

# What it would oblige

**A hook's page carries the shape its figure was taken in**, or the figure is not a measurement of the
hook. The store already ranks a claim by what it rests on; this says a `measurement` basis is
incomplete without the invocation shape.

**A background launch with an open stdin is a defect, not a style.** That is a sentence a reviewer can
apply, unlike *check whether it is really running*.
