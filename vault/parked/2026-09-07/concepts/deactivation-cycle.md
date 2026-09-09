---
title: "The deactivation cycle: every condition guarded by a test that fails when its guard is removed"
type: concept
status: current
authority: deactivation-rules
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [deactivation, testing]
---

# The deactivation cycle

**This is the most dangerous logic in the project.** It was repaired five times across two
iterations, and every defect was of one class: something quietly stopped being judged, or was
judged without grounds.

## Four conditions for a pair to be a miss candidate

All must hold: the vacancy belongs to this source and is active; it is linked to at least one tag
that **actually ran** in this pass; it falls inside the current collection frame; and at least 20
hours have passed since the last counted miss.

**"Actually ran" is not "enabled".** A tag whose request failed does not count as having run.

## Four rules about the marking itself

Misses are marked once per source per profile pass, over the union of all queries. A failure of
any query cancels the marking for the whole source. An empty result set is not a miss. An
incomplete set of identifiers forbids marking misses at all.

## Rebuilding links must never orphan a pair

A link is removed only if the pair keeps a link to **another tag that ran in this pass**.
Otherwise the pair falls out from under condition 2 forever, the threshold of two misses becomes
unreachable, and a vacancy that has disappeared hangs in the list for ever.

**This defect occurred twice in a row**: first with the predicate "has any link at all", then when
it turned out that a link to a *disabled* tag does not save it either.

## How to change this code

Each of the eight rules is closed by a test that **fails when that specific guard is removed**. If
you edit this code, re-check by removing the guard — not merely by a green run. **Twice in one
iteration an edit silently voided the tests' evidential power and they passed for an unrelated
reason**: a pair was created without a link and was filtered out by a newer condition before the
guard under test could fire.

See [[a-test-green-under-any-implementation]] for the general form of that failure, and
[[orphan-pairs-never-deactivate]] for the known gap this cycle still has.

Two things this cycle judges against, both recorded separately: the frame is compared with what we stored rather than with the site's current text ([[frame-checked-against-the-stored-string]]), and an empty listing from work.ua silences the whole source ([[empty-listing-silences-deactivation]]).
