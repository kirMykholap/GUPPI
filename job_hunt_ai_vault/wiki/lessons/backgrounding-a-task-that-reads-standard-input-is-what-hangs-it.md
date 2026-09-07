---
title: "Backgrounding a task that reads standard input is what hangs it, not what hides it"
type: lesson
status: current
authority: background-launch-stdin-hang
basis: measurement
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/hook-selftest.ps1"]
tags: [testing, harness, process]
---

# The incident, 2026-08-30

**`scripts/hook-selftest.ps1` launched as a background task did not finish.** Two PowerShell
processes lived **330 minutes on 0.125 s and 0.344 s of CPU**: blocked, not slow.

**The same suite, launched the same way with `< /dev/null`, finished in seven minutes at
`caught 224, missed 0`.** The same suite in the foreground finished in seven minutes earlier the same
day.

**A backgrounded task leaves standard input open, and this suite reads it.** The suite spawns on the
order of a hundred and seventy children through pipes; a child holding a handle to an input nobody
will ever close does not exit.

**The owner lost most of a day to it, twice.**

# It is a cause, and the store had only recorded a symptom

**`a-background-job-with-buffered-output-cannot-be-told-from-a-dead-one` says the observable evidence
is empty in both directions and the honest report is *I do not know whether it is running*.** Its
repairs are a heartbeat and a launch timestamp — instruments for **seeing** a hang. That page is
correct and it is in `archive/`, so this is not a correction of it.

**The claim here is stronger and it is causal: the backgrounding is not hiding the hang, it is
producing it.** A heartbeat would have shown the hang sooner and would not have prevented it. Closing
the descriptor does.

# The class, which is wider than one suite

**This is the third reading of the same descriptor in this repository.** A command in a `make` recipe
hangs on inherited standard input and finishes with `< /dev/null`
(`a-command-in-a-make-recipe-hangs-while-it-inherits-standard-input`, 2026-08-26, now in `archive/`);
a hook measured without stdin is measured three times too cheap
([[a-process-is-measured-with-the-stdin-it-will-have]]); and a background launch hangs it outright.
**The launcher changes and the descriptor does not.**

**So the rule is about the descriptor rather than about `make` or about backgrounding:** anything in
this repository that spawns this suite closes standard input on it, whichever launcher it uses.

**And zero CPU is still the observable that separates hung from slow** — it was the diagnosis both
times, and it takes one look.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
