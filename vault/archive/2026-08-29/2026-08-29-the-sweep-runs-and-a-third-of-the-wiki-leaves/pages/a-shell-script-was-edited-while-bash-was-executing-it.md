---
title: "DIVERGENCE: a shell script was edited while bash was executing it"
type: decision
status: archived
authority: running-script-edit-divergence
basis: human
binding: divergence
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "scripts/vault-check-selftest.sh"]
tags: [process, testing, harness]
---

# The divergence, recorded 2026-08-20

**What the rule says:** do not change a working file mid-work
([[do-not-change-a-working-file-mid-work]]) — recorded against this session's own predecessor, the
day before.

**What was done:** `scripts/vault-check-selftest.sh` was edited while bash was executing it. **The
run collapsed mid-suite with missing result files, and the failure looked like a suite defect.**

**Why it looked unnecessary at the time:** the file was not being *worked on* by anyone — it was
being *run*, and a script that is merely running did not read as a working file.

**It is one in the most literal sense the phrase has.** Bash reads a script incrementally, so an
edit lands in the middle of a program that is still being read.

**Rejected: wait for the run.**

# What this instance adds to the class

**The rule was written about two parties touching one file, and this is one party touching a file
an interpreter is reading.** The recurrence one day after the rule was recorded is the evidence
that *working file* was the wrong boundary: what matters is whether **anything** is holding the file
open, and `bash script.sh` is the cheapest way in this repository to be that something
([[failing-loudly-with-the-wrong-diagnosis]]).
