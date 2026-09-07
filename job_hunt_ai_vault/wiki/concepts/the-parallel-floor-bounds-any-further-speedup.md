---
title: "The parallel floor is measurable, and it bounds any further speedup of the suite"
type: concept
status: current
authority: selftest-parallel-floor
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, process]
---

# Measured 2026-08-20, against a stubbed gate

**63 s** — 130 tree copies and process spawns with no real work behind them.

So of the 368 s the parallel suite takes:

| part | figure |
|---|---|
| overhead that does not parallelise | **~63 s** |
| gate work, divided across workers | **~305 s** |
| the same gate work run serially | **~1030 s** |
| **speedup on the divisible part** | **3.4x** |

**That is the whole of the observed 2.97x, apportioned by measurement rather than by argument**,
and it is also **the ceiling on any further `JOBS` increase**: raising the worker count can only
attack the 305 s, and eight workers already contend on disk copying a 462-file tree
([[the-selftest-was-serial-because-every-case-wrote-into-one-directory]]).

## Where the remaining time actually goes

Into the gate, whose cost grows with the corpus rather than with the suite
([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]). **So the lever that
is left is the gate, not the parallelism** — which is the same conclusion the store reached the
last time it priced this suite: count processes, not pages
([[measure-before-optimising-and-count-processes-not-pages]]).

## The number came free from a run built for another purpose

The stubbed-gate run existed to prove the suite could report a failure
([[no-verdict-lives-in-a-variable-in-a-parallel-suite]]). Stubbing the expensive stage is what
isolates the fixed cost, and it is worth remembering as a technique: **a harness that can be
pointed at a null implementation measures its own overhead for nothing.**
