---
title: "A journal is judged against the template only while it is uncompiled"
type: concept
status: current
authority: journal-section-rule
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "scripts/vault-check.sh", ".claude/templates/handoff.md"]
tags: [vault, testing]
---

# The rule, and the window it applies in

Rule 8 of `vault-check.sh` asks that a journal carry every section of the form it was written from.
Two properties changed on 2026-08-17 and both are load-bearing.

**It reads the section set from `.claude/templates/handoff.md`**, never from a list inside the
script — regenerate and compare, the same shape as `catalogue.md`
([[the-catalogue-is-generated-not-maintained]]). The numbers it used to count are gone; the cut is
by heading text ([[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]]). What that costs
is stated in the rule rather than hidden: **a renamed heading is indistinguishable from a dropped
one plus a new one**, and the rule reports it as exactly that, which is the loudest it can be.

**It judges a journal only while no `.coverage.tsv` sidecar sits beside it.** The rule exists to
protect the ingest that is about to read the journal, so it applies to what that ingest has not yet
read. Afterwards the form is history: `raw/` is immutable, the journal can never be corrected, and
**a rule that fails forever on a file nobody may edit is an alarm you learn not to read**.

## This is what let the template change at all

Journals written to the older numbered form left the rule's scope **the moment they were compiled**.
Nothing had to be moved, renumbered or rewritten to make the new form legal — the migration cost of
changing the template was zero, because the rule's scope is the uncompiled set.

**The hole is named in the rule's own comment**: a journal written malformed and compiled before
anyone runs the check is never judged. `/handoff` closes it by running the gate as its last step,
and [[the-journal-gate-hook]] closes it again the moment the file lands.

## Two details it was corrected on the same day

- **A journal is told from a form by a property, not by a filename** —
  [[a-journal-is-told-from-a-form-by-a-property-not-a-filename]].
- **It prints only the half that has content.** It used to print `unexpected [none]` when nothing was
  unexpected, and *none* is the exact word the template tells a writer to put in an empty section
  ([[a-placeholder-that-collides-with-real-data]]).
