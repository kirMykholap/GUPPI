---
title: "Failing loudly with the wrong diagnosis is worse in one specific way than failing silently"
type: lesson
status: archived
authority: wrong-diagnosis-failure
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The claim that was corrected by measuring it

**"Both cases die without saying so" was wrong.** Measured on an empty `raw/handoffs/`:

- the command substitution `$(find .../raw/handoffs -name '2026-*.md' | sort | head -1)` is the
  empty string;
- the redirect prints `: No such file or directory` **and exits 0**;
- the tree is left unmutated;
- so the helpers' own `diff -rq` guard catches it, and both cases report **MISSED** as
  *the mutation changed nothing*.

**They fail loudly, with the wrong diagnosis.**

# Which is worse, and which is better, and the difference is only visible because it was measured

**Better:** it is not silent. Something goes red, and a red suite is investigated.

**Worse, and this is the specific way:** the reader is told **the case is empty**, and *nothing
points at `raw/` having emptied*. The diagnosis leads away from the cause. A silent failure sends
you looking; a confident wrong one sends you somewhere else.

# What it is a hazard to

**Acceptance criterion 5 of the `raw/` migration — "`raw/` is an inbox that is empty between
sessions" — walks straight into breaking the suite that guards the migration**, and no page knew
([[moving-raw-into-a-dated-archive]],
[[archive-is-dated-by-session-and-holds-what-left-the-working-set]]). It is the sharpest
half-done-is-worse hazard in that plan.

**The repair is the fixture ruling**: a suite works in its own sandbox and never borrows a file
from the corpus ([[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

# And the correction itself is the method

**The first reading of this was "it fails silently", asserted rather than measured.** Running it on
an empty tree is what produced the true and more useful answer. A claim about how something fails
is a claim that can be tested by making it fail
([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

## Third instance, and this one cannot take the ruled repair — 2026-08-20

**`scripts/hook-selftest.ps1` prints `MISSED   lock allows the librarian on a green gate` when the
real tree is red.** It reads as *the lock is broken*; the truth is *the tree is red*. The case runs
against the real tree deliberately, because only a green tree tells a working lock from one that
refuses everything ([[the-librarian-lock-hook]]).

**So the repair named above — a suite works in its own fixture — cannot simply be applied**, since
this case's whole value is that it is not in a fixture. **Unbuilt, named, and deferred without a
known repair shape**
([[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]],
[[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]]).

**Which sharpens the claim this page makes.** The hazard is not that a suite borrows from the corpus;
it is that **a diagnosis is written for one cause and printed for another**. A fixture removes the
borrowing. It does not, on its own, make a case say which of two things went wrong.
