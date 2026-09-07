---
title: "The filename advisory prints one name per line, and only its first line carries the word that counts it"
type: decision
status: current
authority: advisory-line-shape
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# Three clauses, all the owner's, all on 2026-08-18

1. **One name per line**, not a comma-run on a single line.
2. **Every line carries the `VAULT-CHECK:` prefix**, continuations included.
3. **No continuation line carries the word `advisory:`** — only the heading line does.

Landed at `c521a10`, correcting the shape shipped at `2772439`.

## Why each clause is load-bearing

**The prefix keeps the output greppable line by line**, which is what a line-oriented tool owes a
caller. A continuation without it is a line that no filter matches and no reader can select.

**Withholding the second word keeps `grep -c 'advisory:'` counting advisories rather than names.**
The brief reports that number every ingest, and six continuation lines would have turned twenty
into twenty-five overnight with nothing in the corpus having changed. A count that moves when only
the formatting moved is the same class of noise as an advisory that reorders between two runs
([[an-advisory-prints-one-line-and-sorts-what-it-names]]).

**One name per line is right for a list that shrinks one name at a time.** Each rename removes a
line and the diff of two runs says exactly which. That is the opposite case from rule 11's coverage
advisory, whose set is read whole and whose membership moves for reasons other than work being done
([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]) — and it is why the
two advisories of one script legitimately have two shapes.

## The shape was changed under an approved one, and that is a divergence

The owner chose the filename verdict from a **multi-line preview** and received a single comma-run,
because the house style of the two advisories beside it won silently. Replacing an approved shape is
a question ([[narrowing-a-scope-notifies-and-widening-it-asks]]); neither a question nor a
notification happened. Confessed unprompted at the retrospective and corrected the same session. The
general form is [[a-replaced-shape-reads-as-no-replacement-when-only-the-shape-moved]].

## The format is load-bearing for a test, which is why the suite was re-run

A selftest case greps this output, so the reformat was not cosmetic and the suite was run again
after it — **112 caught, 0 missed** ([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]).
