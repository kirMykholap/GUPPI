---
title: "Source filters only reduce volume — the local re-check is the truth"
type: concept
status: current
authority: collection-modes
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [collection, data]
---

# Source filters reduce volume; the local re-check decides

A profile has a collection frame: cities, a remote flag, and a depth in days.

**The filters we send to a source are only a way to fetch less. The truth is the local re-check** —
because work.ua's promotional block arrives past any filter at all. A vacancy that the site chose
to show us regardless of our query still has to be judged here.

That is why [[collection-frame-city-check]] matters: the frame is applied by us, to every city in
the raw string, after the fetch.

## Two modes

| Mode | What it does |
|---|---|
| full check | judges, and rebuilds the tag links |
| quick update | collects only |

The difference has a consequence recorded elsewhere: a quick run marks its id set incomplete, which
is what "does not touch the disappeared" means — and that is why an unconditional summary clause
about truncation always said the same thing. See [[name-only-non-zero-counters]].
