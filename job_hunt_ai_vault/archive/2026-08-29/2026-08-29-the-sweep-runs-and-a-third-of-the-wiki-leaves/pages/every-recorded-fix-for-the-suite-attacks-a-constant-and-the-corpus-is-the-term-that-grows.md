---
title: "Every recorded fix for the suite attacks a constant, and the corpus is the term that grows"
type: lesson
status: archived
authority: suite-cost-growth-term
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["scripts/vault-check-selftest.sh", "scripts/vault-check.sh", "Makefile"]
tags: [testing, harness, vault]
---

# The readings, in the order they were taken

| date | corpus, as each reading recorded it | `bash scripts/vault-check-selftest.sh` |
|---|---|---|
| 2026-08-20 | 379 pages under `wiki/` | **18m13s** serial, 368 s parallel |
| 2026-08-23 | 543 pages under `wiki/` | **27m15s** |
| 2026-08-24 | 562 files | **34m08s** |
| 2026-08-26 | 682 files | **about an hour** |

**The units are not the same across the four rows and that is how they were recorded.** The first two
count `wiki/` pages, the last two count files in the set the gate walks. Nobody has ever taken the two
counts on one day, so the series cannot be turned into a rate — **what it shows is a direction, and
the direction is the whole finding** ([[an-unsourced-number-is-dropped-not-chosen]]).

**Read off the tree on 2026-08-26 for the next reader: 725 pages under `wiki/`**, counted with
`find wiki -mindepth 2 -maxdepth 2 -name '*.md' | wc -l`. The command is given because the number is
stale the day after it is written ([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

**The last row is not a clean measurement.** *About an hour* is what two attempts produced — one run
launched and never returned, the other killed unfinished at 56 minutes
([[a-background-job-with-buffered-output-cannot-be-told-from-a-dead-one]]). It is offered as a lower
bound rather than a figure.

# The finding: every proposal on record attacks a constant

**Three fixes have been proposed or ordered for this suite, and each of them multiplies the total by
a factor smaller than one. None of them touches the quantity that is growing.**

| proposal | what it attacks | shape of the term |
|---|---|---|
| exclude the sandbox from the virus scanner | the per-file I/O cost | a constant factor |
| narrow the gate so a case evaluates one rule | the rules evaluated per case | a constant factor |
| the one-`awk`-pass rendering fix | processes per rule page | a constant, and the **minor** one |

**A constant factor bought once is spent once.** The scanner exclusion was applied on 2026-08-24 and
the measurement gave nothing ([[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]); the
narrowed gate is measured against, because the gate's shared pass over the corpus is two thirds of
its cost and does not narrow ([[the-gate-is-a-shared-pass-over-the-corpus-plus-the-scripts-it-delegates-to]]).
**Even if both had worked in full, the series above would still be a series that rises.**

# Why the cost grows with the corpus, structurally

**`scripts/vault-check-selftest.sh` copies the whole corpus per case and runs a full gate over it.**
Both factors of the product are functions of the corpus:

- **the per-case sandbox copy** is a copy of the tree, so it costs what the tree costs;
- **the gate run inside it** is one shared pass over every page, so it costs what the corpus costs —
  4.9 s in 2026-08-17, 8.5 s in 2026-08-20, about 13 s in 2026-08-23, 21.5 s in 2026-08-26.

**And the case count rises with the corpus too**, because a new rule brings a new case: 130 cases in
2026-08-20, 158 in 2026-08-23, about 178 in 2026-08-26.

**So the total is (cases) × (per-case corpus work), with both terms growing** — which is the
superlinear shape the readings show, and it is a consequence of the suite being a mutation test
rather than an inefficiency inside one ([[the-selftest-is-a-mutation-test-of-the-gate]]).

**The corpus only grows.** Nothing in this store shrinks it: pages are never deleted, a retired one
moves to `archive/` and stays on disk, and every ingest adds. The one quantity nobody chose is the
one that governs the total.

# What this page does not do

**It does not design the fix, and that is deliberate rather than an omission.** Naming the term is a
different act from choosing what to do about it, and the readings above are not sufficient for the
second: nobody has measured what fraction of the sandbox copy is the corpus, whether the gate inside
a case needs the whole corpus at all, or what a case would lose if it ran against a fixture the size
of its own fixture.

**It does not overturn any of the three proposals.** A constant factor is worth buying if it is cheap;
what this page refuses is the reading in which buying one **answers** the cost.

**It does not say the suite is too expensive.** That is a judgement about what the project is willing
to pay, and it is the owner's — he has already changed the cadence rather than the cost, and the suite
now runs at a sprint's close instead of every session
([[the-suite-stops-running-every-session]]).

# What it obliges of the next proposal

**Any further proposal about this suite's cost states which term it attacks, before its price.** The
three above did not, and the effect was three sessions of work priced against the wrong bottleneck
([[measure-before-optimising-and-count-processes-not-pages]],
[[a-negative-measurement-that-is-not-written-down-gets-proposed-again]]).

**Measurement conditions:** the four readings were taken on four different days against four different
trees, and two of them were taken while other work ran against the same disk
([[a-measurement-taken-while-other-work-runs-against-the-same-disk-measures-nothing]]). They are a
series of point readings and not a controlled experiment; the shape survives that and no individual
figure should be quoted as this suite's cost today.
