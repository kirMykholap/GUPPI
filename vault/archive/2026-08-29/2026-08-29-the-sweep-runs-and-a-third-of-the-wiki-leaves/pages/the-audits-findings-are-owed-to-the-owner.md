---
title: "The first audit reported and did not act: its findings were deferred to the owner on 2026-08-15"
type: decision
status: archived
authority: audit-outcomes
binding: deferral
basis: inference
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", "log.md", "sprint.md"]
tags: [vault, process]
---

# Six outcomes that are not fixes

The first `/vault-lint` this corpus has ever had ran on 2026-08-15 over 108 pages in `wiki/` and
three in `archive/` ([[lint-waits-for-an-open-sprint]]). Every finding it made carries an outcome
in `log.md`. **Six of those outcomes are "owed to the owner"**, and this page is the deferral: a
date, a reason per item, and one rejected alternative.

**Rejected: fixing them inside the run that found them.** Each of the six is either a supersession,
a deletion of text, a change to a file the librarian does not write, or a judgement about the
store's shape — and the librarian writes unattended precisely because none of those four are its
call ([[the-librarian-writes-unattended]]).

| # | Finding | Why it is not the librarian's | Consequence of leaving it |
|---|---|---|---|
| 1 | **Two retitles** — [[lint-waits-for-an-open-sprint]] (it *has* run) and [[staleness-checks-run-at-different-times-and-ask-different-questions]] (there are *three*) | A title carries the claim, so correcting one is supersession, not an edit — and the run that falsified a title is the wrong one to erase it, because the retired page is the record of *why* the deferral existed | Two `current` pages carry titles that are false today |
| 2 | **The three tag advisories** — acceptance criterion 3 of S1 | Re-tagging pages a session never touched is the judgement half of a lint | An advisory standing for a fourth day stops being read |
| 3 | **`index.md` is obeying its rule and failing anyway** | Trimming a map is deleting text, and the map's shape is the owner's | The failure arrives by prose instead of by rows ([[the-index-is-a-map-not-a-catalogue]]) |
| 4 | **`.gitattributes` pins only `*.sh`** | It is a change to the repository, and the fix is one commit that rewrites 59 files and nothing else | Every session reads `git status` twice ([[line-endings-make-git-status-overstate-what-changed]]) |
| 5 | **Three proposals that do not exist**, all three living as clauses inside other pages | Writing them *is* the librarian's, and was done — deciding them is not | Now three pages; see below |
| 6 | **`.claude/skills/vault-lint/SKILL.md` does not know about the fifth category**, nor about the `> [!NOTE] CONTRADICTION — RESOLVED` shape | A skill is not the vault and the librarian does not write one | The next audit classifies a `proposal` as a missing `concept` ([[proposals-are-a-folder-not-a-status]]) |

## The evidence each one already has

None of the six is a bare assertion — the measurements are on the pages and in `log.md`, which is
what separates a deferral with a reason from a finding nobody looked at. For #2:
[[dynamic-tag-classification-by-a-skill]] carries the strata, the 35%-against-14% growth and the
two thresholds. For #3 and #4 the numbers are on the pages named in the table.

## #2 was decided on 2026-08-16, and the row above is kept as the deferral it was

The owner took finding #2 rather than the librarian: **the three tags are not split**, tag density
is measured inside a folder against the reader's ceiling of ten, and the five lines the check
prints at `2036d98` are each named with a reason
([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]). The row's consequence column — *an
advisory standing for a fourth day stops being read* — was not repealed by that: **five lines stand
where three did**, and the decision says so in those terms. What the row said about *whose* call it
was held exactly: re-tagging pages a session never touched is still the judgement half of a lint,
and the decision defers it to a skill that brings a proposal rather than a hand cut
([[dynamic-tag-classification-by-a-skill]]).

*(The two thresholds this page cites under "the evidence each one already has" are now one; the
sentence is left as written, because it is the state of the evidence when the deferral was made.)*

## The three proposals of #5, written on 2026-08-15

Finding #5 is the one this ingest could discharge in part, and the split is the boundary
[[proposals-are-a-folder-not-a-status]] draws: **this page records *that* we said not now; each
proposal carries *what* we would build.**

- [[reconciling-entities-against-the-decision-register]] — the owner's note asked for it and
  nothing built it;
- [[a-check-for-missing-conceptual-pages]] — the other note's fourth lint check, and the only one
  of the five that no `grep` could answer;
- [[a-rule-comparing-a-stated-count-against-its-list]] — thirteen instances of the failure and no
  rule ([[a-stated-count-drifts-from-the-list-it-heads]]).

## Also deferred the same day, and not part of the six

- **The selftest's 201 s.** The one-`awk`-per-run optimisation would return about 30 s of it; the
  suite is 61 of 61 and slow rather than wrong ([[vault-scripts]]).
- **The module map, the CLI and the data model.** They are uncompiled, and the finding is that they
  **have no source in `raw/` to be compiled from** — negative space, not an unfinished ingest.
- **The English migration itself**, whose design is [[migrating-the-repository-to-english]] and
  whose decision half is [[english-is-the-rule-and-the-russian-past-is-deferred]].

## What it obliges

**Acceptance criterion 1 of S1 is not met while any of the six lacks a fix or a `decisions/` page.**
This page is that page for all six as a set; a per-item outcome that supersedes it replaces the
row rather than the page. Whether the criterion is met is read off `log.md` by the owner and is not
asserted here ([[a-sprint-closes-on-its-goal]]).

## Three more rows moved on 2026-08-16, and the rows above are kept as they were written

**#6 — the lint skill — is done.** `.claude/skills/vault-lint/SKILL.md` was changed on `94483b1`
by the owner's session, not by the librarian, which is what the row said had to happen: **item 3
now asks which folder a missing page belongs in before calling it a missing concept**, and **item 1
knows that a resolved contradiction is not a finding**. The consequence the row predicted — the
next audit classifying a `proposal` as a missing `concept` — cannot happen now.

**#4 — `.gitattributes` — is done, and the row's price was wrong.** `5e864f1` pinned `*.md
text eol=lf` ([[markdown-is-pinned-to-lf]]). The row prices the fix as *one commit that rewrites 59
files and nothing else*; measured at `86823e3` before doing it, **all 161 tracked `.md` were
already `i/lf` in the index and the commit changed exactly one file.** The 52-against-59 split was
the working copy only. The cause of the overstatement, which the row's page called unidentified, is
[[the-stale-stat-cache-behind-git-status]].

**#1 — the two retitles — now has a rule behind it and is still not executed.** A title carries no
measurable quantity, unconditionally ([[a-title-names-what-is-counted-instead-of-counting-it]]),
and its form follows the record's type ([[the-titles-form-follows-the-records-type]]). That turns
two named pages into a class: **eight titles are out of compliance**, three of which S2 will break
again on purpose. **The owner has decided only the first of the two retitles**, and the second is
undecided, so the row stands exactly as written and the librarian performs neither
([[structure-work-agreed-and-not-executed]]).

**#3 — `index.md` — gained a decision about what it is for** and no execution:
[[the-index-reads-and-the-schema-writes]] splits the reader's file from the writer's and names the
three duplications to remove. Trimming the map is still deleting text and still the owner's.

*Two of the six were rows about work the librarian may not do, and both were done by the owner's
own session on 2026-08-16. That is the deferral working as designed rather than a gap closing by
itself.*

## Finding #1 read again on 2026-08-19: one of the two is done, and it is not the decided one

**"Two `current` pages carry titles that are false today" is now one.**
[[staleness-checks-run-at-different-times-and-ask-different-questions]] was retitled at `b6fc6d8`
on 2026-08-17 and its filename renamed on 2026-08-19, so both halves of that entry are finished
([[a-page-rename-is-sed-and-verify]]). [[lint-waits-for-an-open-sprint]] still says *"/lint has
never run"*, and it has run — **the half the owner had decided is the half still standing**, which
is the honest state of a deferral that was closed by a general rule rather than by the decision it
was waiting on ([[a-title-names-what-is-counted-instead-of-counting-it]]).

**So the sentence "the owner has decided only the first of the two retitles, and the second is
undecided" describes a state that has inverted**, and both clauses are kept above: what a deferral
was waiting for is the record of why it waited.

**The "eight titles are out of compliance" figure is replaced by the command.** Eight was counted by
eye on 2026-08-16 against a rule with no written boundary; the boundary arrived as rule 10 and the
real number was **37 of 165** ([[the-title-check-asks-and-does-not-judge]]). The reading is:

```
bash scripts/vault-check.sh | grep -c 'the title counts'    # 0 on 2026-08-19
```

Run beside this sentence it returns 0, with the run exiting 0 and nineteen advisories standing.
**That command answers a narrower question than the row does**, and the difference is the finding:
it reads a title for *counting words* and never for truth, so it returns 0 on a corpus that still
contains the false title named above. A count drifts and can be checked; a claim goes stale and
cannot ([[a-stated-count-drifts-from-the-list-it-heads]]).

**The predicate behind that command has also moved since the row was written**: ordinals count now,
`first` does not, and with no way for a page to declare itself exempt every word in the list is a
promise that the word is always a count ([[ordinals-count-and-first-does-not]]).
