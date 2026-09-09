---
title: "A case that passes before the change tests nothing, and running the suite against the pre-change scripts is what made every new case evidence"
type: lesson
status: archived
authority: pre-change-suite-run
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The procedure, and what it returned on 2026-08-19

**Check out the scripts as they were before the change, run the new suite against them, and read
which cases fail.** A case that passes against the old code is testing something the old code already
did — it is not evidence for the change.

Measured: five new cases and one changed message. **Against the pre-change scripts, exactly six were
missed and nothing else.** Every new case is therefore evidence, and nothing else in the suite moved.

# The sixth is the finding

**One of the six is the changed message**, not a new verdict — the `ruleclaim` branch's wording moved,
and an existing case greps it
([[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]],
[[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]).

**No reasoning had flagged that as testable.** It was found because the procedure asks the *code* what
moved rather than asking the author what he changed — which is the same argument as measuring rather
than arguing, applied to a suite ([[measurement-settled-what-argument-could-not]]).

# Why this is not obvious, and why it is skipped

**A new case that passes feels like confirmation.** It is green, the change is in, and green after a
change reads as *the change works*. The information it actually carries is zero unless it was red
before — and the failure mode is silent: a case written slightly beside the verdict it meant to test
passes both before and after, and stands in the suite forever, costing time and asserting nothing.

**The cost of the procedure is one checkout and one suite run**, against a suite that costs eight
minutes ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]). That is the whole price, and
it buys the only proof that the cases are about the change.

# The relation to the other two instruments

**It complements the plant-and-revert proof, which shows a verdict firing today**
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]), and it is what
turns *the suite is green* into *the suite is green and the cases are about this*. It also caught, in
the same run, the fixtures that had gone red for an unrelated reason
([[the-fixture-corpus-goes-red-before-the-rule-it-was-never-written-for]]) — the pre-change run is how
that was proved to be new damage rather than pre-existing.

## Applied again on 2026-08-20, and it caught nothing because it was done first

**The new selftest case for an absent `render:` was run against the unchanged injector before the
change** and read `MISSED` — `134 caught, 1 missed`, the miss being that case and nothing else.
After the change it is `CAUGHT` and the suite is `135 / 0`.

**Without that run it would have been a case that passes before the change and therefore tests
nothing** ([[an-absent-render-is-red-on-a-page-that-renders]]). It is recorded as a success of the
rule rather than as an incident: the run costs one invocation, and it is the only thing that
distinguishes a guard from a decoration.

**Its sibling the same session** is the no-op run that proved the translation tool did not itself
corrupt line endings ([[a-planted-offender-is-proved-by-reading-it-back]],
[[a-gap-named-by-a-reviewer-is-closed-by-a-mechanism-rather-than-by-care]]) — **proving the
instrument before the measurement, twice, and both paid.**
