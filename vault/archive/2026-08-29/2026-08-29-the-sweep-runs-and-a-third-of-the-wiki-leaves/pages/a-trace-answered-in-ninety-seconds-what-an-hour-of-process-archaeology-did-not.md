---
title: "A trace answered in ninety seconds what an hour of process archaeology did not"
type: lesson
status: archived
authority: hang-diagnosis-order
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "scripts/vault-check.sh"]
tags: [testing, harness, process]
---

# The incident, 2026-08-26

**The gate did not return.** It was read as slow, then as contended, then as starved by the suite
running beside it. **An hour of machine time went into diagnosing a starved machine that was actually
a hung process.**

**`bash -x scripts/vault-check.sh` pointed at rule 15 and cost 90 seconds.** It was the first thing
that answered, and it was tried third
([[python3-on-this-machine-is-the-microsoft-store-stub]]).

# Why the two rounds before it were plausible and still wrong

**The suite genuinely was running**, so contention was a live hypothesis with evidence for it — 33
processes in its group and a machine under load. **Contention explains slow; it does not explain
never returning**, and nothing in the reasoning drew that line.

**The two hypotheses differ in one observable**: a contended run finishes eventually. Waiting is what
distinguishes them and waiting is what was being spent.

# What follows

**When a command does not return, trace it before theorising about the machine.** `bash -x` names the
line, costs a minute and a half, and needs no hypothesis to be worth running.

**A theory about the environment is the expensive kind**, because checking it means measuring the
environment ([[measure-before-optimising-and-count-processes-not-pages]],
[[a-measurement-taken-while-other-work-runs-against-the-same-disk-measures-nothing]]).
