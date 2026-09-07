---
title: "An advisory sorts what it names, so an unchanged tree prints unchanged output"
type: concept
status: current
authority: advisory-form
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh"]
tags: [harness, testing]
---

# One line, with the names on it

Rule 11's coverage advisory prints **one line** naming every governed file that carries no region —
not one line per file.

**Eighteen lines that never change is a way of teaching a reader to skip the advisories.** Five
already stand by decision ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]), and the tag
density advisories have since grown to ten. An alarm that fires every run and cannot be acted on is
one you learn not to read, which is the argument this store has already made about advisories that
stand forever ([[vault-scripts]]).

# The list is sorted, and that is load-bearing

`awk` walks `for (f in files)` in **hash order** — neither insertion order nor sorted order, and it
can change between runs for reasons that have nothing to do with the tree.

**An advisory whose text reorders between two runs over an unchanged tree reads as a change that
did not happen.** The reader diffs two runs, sees movement, and goes looking for what they broke.
It is the same class of noise as `git status` overstating a change
([[line-endings-make-git-status-overstate-what-changed]]), and the same reason this project
compares by regenerating rather than by mtime ([[staleness-checks-run-at-different-times-and-ask-different-questions]]).

**Deterministic output is a property of an instrument, not a nicety.** An instrument whose output
moves on its own cannot be diffed, and diffing two runs is how every check in this repository is
actually read.

# A second advisory arrived with the opposite shape, and the title above was corrected

**The owner ruled on 2026-08-18 that the filename advisory prints one name per line**, each line
carrying the `VAULT-CHECK:` prefix and none of the continuations carrying the word `advisory:`
([[the-filename-advisory-prints-one-name-per-line]]). So one script now prints two advisories in two
shapes, deliberately.

**The title of this page read *"An advisory prints one line and sorts what it names…"* until that
day**, and it is corrected in place rather than superseded — the claim that generalised was the
"one line" half, and it was only ever measured on rule 11's coverage advisory
([[a-title-corrected-in-place-is-not-a-supersession]]).

**What separates the two cases is how the list moves.** The coverage advisory names a set that is
read whole and whose membership changes for reasons other than work being done — the denominator
grew from 13 to 14 the moment a probe file landed
([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]],
[[the-conditional-delivery-probe]]). The filename list shrinks one name at a time as renames land,
so a line per name makes the diff of two runs say exactly which one went.

**Both halves of this page's actual mechanism survive unchanged**: the sorting, and the count. The
second is why no continuation line carries the word `advisory:` — the brief reports
`grep -c 'advisory:'` every ingest, and six continuations would have moved that number with nothing
in the corpus having changed.
