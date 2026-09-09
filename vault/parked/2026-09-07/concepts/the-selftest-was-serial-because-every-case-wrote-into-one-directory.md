---
title: "The selftest was serial because every case wrote into one directory, not by design"
type: concept
status: current
authority: selftest-parallelism
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# What made it serial was one line

**Every helper wrote into the same `$SANDBOX/work`.** The cases were already independent by
construction — each starts from an untouched copy of `$PRISTINE`. Nothing about the suite's design
required them to run one after another; one shared path did.

Giving each case its own directory and a worker slot took the suite from **1093 s to 368 s**, with
`JOBS` defaulting to 8 on this host.

## Not the 8x the core count suggests, and the reason is measured

**Eight concurrent copies of a 462-file tree contend on disk where the gate itself does not.** The
apportionment is [[the-parallel-floor-bounds-any-further-speedup]]: roughly 63 s of the 368 does
not parallelise at all.

## The change is smaller than it looks, and that is what made it provable

**All 130 call sites are untouched.** The change is six helpers, eight section headings and the
tail.

**Proved by comparison rather than asserted: the parallel run is byte-identical to the serial one**
— 140 lines each, `diff` exit 0, `caught 130, missed 0` both ways.

**Order is the dispatch number, never the finish**, section headings included, or all eight workers
would print before the first result and two green runs would differ.

## Why byte-identical was the acceptance test and not a nicety

A suite whose output reorders under load cannot be diffed against its own previous run, and diffing
it against its previous run is how a change that *looks* cosmetic is shown to be
([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]). The invariant that makes the
counting safe is separate and stronger: [[no-verdict-lives-in-a-variable-in-a-parallel-suite]].
