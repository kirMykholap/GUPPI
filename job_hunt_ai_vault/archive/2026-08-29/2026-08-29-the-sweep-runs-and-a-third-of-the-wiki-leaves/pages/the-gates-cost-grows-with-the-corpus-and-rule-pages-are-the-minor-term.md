---
title: "The gate's cost grows with the corpus, and rule pages are the minor term"
type: lesson
status: archived
authority: selftest-cost
basis: measurement
sprint: S2
created: 2026-08-20
supersedes: "[[the-selftest-cost-scales-with-the-rule-pages-it-renders]]"
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check.sh", "scripts/vault-check-selftest.sh", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [testing, harness, process]
---

# The reading the store was owed — measured 2026-08-20, end to end

**`bash scripts/vault-check-selftest.sh` is 1093 s — 18m13s — serial**, exit 0, `caught 130, missed 0`.
The figure it replaces was *roughly five minutes*, with a `>600 s` lower bound recorded as
explicitly not a measurement.

**The decomposition was measured, not apportioned.** One full `bash scripts/vault-check.sh` is
**8512 ms**, and 130 x 8.5 s is 1107 s — the whole of it. The per-case tree copy and diff are noise,
as the superseded page had already found.

# Why the title changed, and it is a changed claim rather than a correction

The predecessor said the suite's cost is a function of **how many rule pages exist**, and priced
each further migrated rule at roughly fifteen seconds of suite. **That is still true and it is the
smaller term.**

| term | figure |
|---|---|
| gate, 2026-08-17 | 4.9 s |
| gate, 2026-08-20 | **8512 ms** |
| `wiki/` over the same span | ~306 pages to **379** |
| tree the suite copies | 401 files to **462** |
| **gate per page** | **~50 ms** |
| **suite per ingest of thirty pages** | **~3 minutes** |
| suite per rule page | ~10 s, nine of them today |

**So the dominant term is corpus growth**, and it is the one nobody chose: the vault grows every
ingest whether or not a rule migrates.

# What this changes about the deferred fix

**The deferred one-`awk`-pass fix attacks the minor term.** It removes processes per rule page,
which the store already established is the quantity that governs a *rendering* cost
([[measure-before-optimising-and-count-processes-not-pages]]) — and it does nothing about the
50 ms per corpus page. **That is worth knowing before it is spent.**

**The lever that is left is the gate itself**, not the suite's parallelism, which is already at its
floor ([[the-parallel-floor-bounds-any-further-speedup]],
[[the-selftest-was-serial-because-every-case-wrote-into-one-directory]]).

# What carries over unchanged from the page this replaces

- **A rule whose input is the whole store couples every test to itself**, and rule 12 is that shape
  ([[a-rule-over-every-page-makes-every-test-fragile]], [[a-check-asks-by-running-the-writer-it-checks]]).
- **A suite nobody runs catches nothing**, and the owner's reading stands: *a faster suite that
  silently stops checking is the worse failure*
  ([[no-verdict-lives-in-a-variable-in-a-parallel-suite]]).
- Not the same lesson as [[test-suite-wall-clock]], which is about `pytest` under contention.

# The number the previous journal left owed

**`caught 130, missed 0`** — unchanged after the coverage rewrite of criterion 6 and the advisory's
new wording, so both cost the suite nothing. It is recorded here rather than added to that journal:
`raw/` is immutable, and a figure that arrives after a journal is written belongs in the next one
([[fidelity-to-a-source-and-fidelity-to-the-tree]]).

**Measurement conditions:** machine otherwise idle, nothing else running, the tree held still for
the duration ([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

# Measured again on 2026-08-23: 1.43x the pages cost 4.4x the time

| reading | corpus | wall clock |
|---|---|---|
| 2026-08-20, carried on this page | 379 pages | 368 s, parallel |
| 2026-08-23 | 543 pages under `wiki/` | **1635 s** — 27m15s, `user` 15m11s, `sys` 32m51s |

**The suite reported `caught 158, missed 0`, exit 0.** Two later runs the same day, at 167 and 168
cases, took 29m50s and comparable.

**The superlinear shape is what this reading is for, not the number.** A number measured on one
day's corpus is stale the next; the shape — the total growing faster than the page count — is the
property that decides whether the suite survives another month.

## `sys` exceeding `user` says where the time went, and the sandbox is not the reason

**File I/O, not computation.** `sys` at 32m51s against `user` at 15m11s is a process spending twice
as long in the kernel as in its own code. **The sandbox is 6.3 MB and 733 files**, which is not a
size that explains it.

**Eleven workers reach only a 1.7x speedup**, so they are contending rather than scaling — the
parallel floor this store already measured, now visible from the other side
([[the-parallel-floor-bounds-any-further-speedup]]).

**The multiplied term is the gate itself.** It went from 8.5 s to about 13 s as the corpus grew, and
it runs **once per case** — because most cases break one thing and evaluate all twenty rules
([[the-selftest-is-a-mutation-test-of-the-gate]]).

**What to do about it is a proposal with an order**, and the first step is a measurement rather than
a change ([[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]).

**Measurement conditions**: taken against the exact tree that was committed, on 2026-08-23, in the
second session of that day.

# The series continued and nothing acted on the term it names — 2026-08-26

**Two more readings exist and the shape held**: 34m08s at 562 files on 2026-08-24, and about an hour
at 682 on 2026-08-26. **This page named corpus growth as the dominant term on 2026-08-20 and every
proposal written since has attacked a constant factor instead**, which is a separate finding and has
its own page ([[every-recorded-fix-for-the-suite-attacks-a-constant-and-the-corpus-is-the-term-that-grows]]).

**This page keeps the decomposition; that one keeps the consequence.** Nothing here is corrected —
what changed is that the conclusion has now been available for six days and unused.
