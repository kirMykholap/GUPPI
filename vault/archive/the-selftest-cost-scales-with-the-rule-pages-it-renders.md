---
title: "The selftest's cost is now a function of how many rule pages exist, and each migration adds to it"
type: lesson
status: deprecated
superseded_by: \"[[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]\"
authority: selftest-cost
basis: measurement
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check-selftest.sh", "scripts/vault-inject.sh", "archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md"]
tags: [testing, harness, process]
---

# Measured 2026-08-17, at `814472a`

**`bash scripts/vault-check-selftest.sh` takes 8m04s** — user 2m31, sys 3m00 — against the **201
seconds** recorded before rule 9 was retired, and the **~158** that were expected to be left once its
43-second wrapper went with it.

**The cause was measured, not guessed:**

| Component | Figure |
|---|---|
| cases | **89**, each running a full check |
| one full `bash scripts/vault-check.sh` | **4.9 s** |
| of which `bash scripts/vault-inject.sh --check` | **1.98 s**, about **40%** |
| 89 × 4.9 s | **436 s**, plus the tree copy per case |
| rule pages today | **nine** |
| **each further migrated rule** | **roughly fifteen seconds of suite** |

**Why it scales with rule pages: rule 12 asks its question by running the injector**
([[a-check-asks-by-running-the-writer-it-checks]]), **and the injector spawns two `awk` processes per
page** — `slice_of` and `region_of`. Nine pages is eighteen process spawns inside every one of 89 checks.

## The projection, which is the actionable half

**Marking up the remaining twelve governed files takes the suite past fifteen minutes.** That is not a
guess from the trend; it is the per-rule figure above times the rules those files would carry
([[a-governed-file-with-no-region-is-an-advisory]]).

**A suite nobody runs catches nothing**, and this project has already measured what an expensive suite
does to a session: the first run of one day cost five minutes to report a failure that had nothing to do
with the change under test ([[hand-probe-a-new-mechanism-before-running-the-suite]]).

## The fix, when it is wanted

**One `awk` pass over all rule pages instead of two processes each.** Deferred with the cost stated
([[what-the-harness-build-waits-on]]).

## What this replaces, and what it does not

**The numbers this vault carried for the selftest are now the numbers of a different script.** The 201
seconds and the 43-second `regen_catalogue` wrapper belong to rule 9, which is retired
([[a-rule-over-every-page-makes-every-test-fragile]], [[vault-scripts]]). What carries over unchanged is
the shape: **a rule whose input is the whole store couples every test to itself**, and rule 12 is that
shape again — its cost was invisible while no region existed and arrived with the first migration.

**Not the same lesson as [[test-suite-wall-clock]]**, which is about `pytest` under contention. This one
is about a cost that grows with the corpus rather than with the machine's load.

## The unit was wrong, and the deferred `awk` pass was not the precondition it looked like

**Measured 2026-08-18.** Widening the injector's walk from 9 pages to 258 was expected to dominate;
it does not. `vault-inject.sh --check` runs **1837 ms** over every folder against **1898 ms** over
`wiki/rules/` alone — the wider walk is *faster* — and the pre-filter costs **113 ms**. The real
cost was **processes per page**, about 40 ms per spawn on this platform
([[measure-before-optimising-and-count-processes-not-pages]]).

**So the deferred one-`awk`-pass row is still worth having and is not a blocker for anything.** What
it removes is processes, which is the quantity that governs; it was filed as the precondition for
the wider walk and it was not one.

**The case count moved and the wall clock did not.** The suite ran **106 caught, 0 missed** after
`e83ce28`, **107, 0** after `b311f0f`, up from 99 at the start of the session. **Wall clock was not
timed**, so the 8m04s figure above stands unrevised rather than restated from memory
([[an-unsourced-number-is-dropped-not-chosen]]).

**Read again after the filename half — 2026-08-18, second session: 112 caught, 0 missed**, up from
107, and **re-run after a change that looked cosmetic**, because a case greps the advisory's output
([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]). Of the five cases added, one
discriminates and four assert absence
([[reverting-the-code-tells-you-whether-a-test-tests-anything]]). Wall clock was again not timed.

## Wall clock re-measured, and the components are separated — 2026-08-19

**Roughly five minutes on an idle machine**, against the 8m04s of 2026-08-17 that had stood unrevised
through two sessions that did not time it. The suite runs **120 cases**, each copying the tree and
running the whole gate.

**The components were measured rather than apportioned:**

| component | figure |
|---|---|
| files copied per case | **401** |
| the copy | **~0.25 s** |
| the diff | **~0.14 s** |
| the gate | **the rest**, and it is nearly all of it |

**So the two things that grow are the corpus and the case count**, and the copy — the obvious suspect and
the thing a reader assumes is expensive — is under a tenth of a second.

**Named as a candidate and not a task, on the owner's reading**: *a faster suite that silently stops
checking is the worse failure*. This store has already retired a rule for costing 71 seconds at 75 pages
and growing as the square ([[a-rule-over-every-page-makes-every-test-fragile]]), which is the precedent
for acting — and the precedent for acting **on a measured cause**, which is what the table above is for
rather than an optimisation nobody priced
([[measure-before-optimising-and-count-processes-not-pages]]).

# The figure in circulation is at least half the truth — 2026-08-19

**A run this session exceeded a 600-second timeout and finished in the background**, against the
*roughly five minutes* this page and [[vault-scripts]] both carry.

**That is a lower bound rather than a reading.** Nothing timed it end to end, so the number owed is
a real one and is not this. What it establishes is only that the figure in circulation is at least
double-optimistic, and that quoting it again without re-measuring would be quoting a figure measured
before the tree moved ([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

**The cause is the one this page already names**: each case copies the whole tree, so the cost grows
with the corpus — and the corpus grew by 22 pages at one ingest and by more at the next. **Cases
were also added**: the suite went from 120 to 130 in one session.

**Owed as a `measure:` line, and deliberately not converted into a plan.** Timing it properly is one
command with a wrapper; deciding what to do about the number is the owner's, on the reading this
page already records — *a faster suite that silently stops checking is the worse failure*.

# Superseded 2026-08-20, on a measurement rather than a correction

**The wall clock owed above was measured end to end: 1093 s, 18m13s**, and the decomposition names
the corpus rather than the rule pages as the dominant term — about 50 ms of gate per page against
~10 s of suite per rule page ([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]).

**This page is not wrong; it is narrower than it reads.** Its per-rule figure holds and its
reasoning about rule 12's shape holds. What it claimed as the cost's governing quantity is the
smaller of two, and the title says the governing quantity, which is why this is a supersession and
not an annotation.

**Read it for why the suite is coupled to the whole store.** Read the successor for what the cost
is made of.
