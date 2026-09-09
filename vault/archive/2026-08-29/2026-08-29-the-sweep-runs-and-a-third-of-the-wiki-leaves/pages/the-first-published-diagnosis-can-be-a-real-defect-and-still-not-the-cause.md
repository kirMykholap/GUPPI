---
title: "The first published diagnosis of a failure can be a real defect and still not be the cause"
type: lesson
status: archived
authority: first-diagnosis-not-the-cause
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check-selftest.sh"]
tags: [testing, process, harness]
---

# The incident

**Loop ordering was published as the cause of `caught 24, missed 96`.** It was a genuine bug, it was
worth fixing on its own merits, and fixing it moved the suite from **24** caught to **86**
([[a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first]]).

**The cause was the renamed vault**, and the remaining thirty-four were behind it
([[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]]).

# Why a true first finding is the trap rather than a false one

**A false diagnosis is refuted by the next run.** A true one is *confirmed* by it — the number moves, and
a number moving is the strongest signal a debugging session has.

**Publishing the first true finding as *the* cause is the error**, not finding it. The finding is worth
having; the word *cause* is the claim that nothing else is behind it, and nothing about a partial
improvement supports that claim.

**The tell was available and was in the output**: 34 cases were still missed. A cause explains the whole
reading. A defect explains part of one, and the difference is arithmetic rather than judgement
([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]]).

# What was done about it, and it is the reusable half

**The correction was written into the same file that carried the first line, with the earlier line named**
rather than replaced ([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).
So the record carries both the finding and its demotion, and a reader who greps the ordering bug meets
the qualification in the same paragraph.

**The habit: say what the reading would be if this were the whole cause, before fixing it.** *"Ordering
explains the frontmatter cases"* is checkable and would have left 34 unexplained out loud; *"ordering is
the cause"* is not a claim about any particular number.
