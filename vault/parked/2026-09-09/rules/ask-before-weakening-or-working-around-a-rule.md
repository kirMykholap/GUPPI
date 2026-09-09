---
title: "Ask before you weaken, remove or work around a rule"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "scripts/vault-check.sh", "[[the-turn-that-explains-a-rule-adds-exceptions-to-it]]", "[[hand-edits-of-the-wiki-are-a-recorded-divergence]]"]
decided_by: [[the-ask-before-weakening-rule-is-ratified-after-being-enforced-without-a-decision]]
tags: [harness, process, vault]
---

# What travels

<!-- text -->
**Ask before you weaken, remove or work around any rule** — here, in the code, or in the vault.
Every recorded divergence in this project began with the rule looking unnecessary.
<!-- /text -->

**That is the paragraph of the repository's `CLAUDE.md`, to the byte** — cut out at `e478c19` by
line number and diffed against the slice above rather than read against it. The diff is empty.

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it cannot wait for a question

**A work-around is finished before the question forms.** That is the whole of the argument, and it
is the same shape as the boundary-test rule: by the time you would think to ask, the thing is
already done ([[claude-md-is-a-map-and-four-rules]]). Weakening a rule is not an act with a pause in
it — the flag gets added, the assertion gets loosened, the directory gets created by hand — and
afterwards there is nothing left to ask about, only something to report.

**Its scope is deliberately all three places at once**: here, in the code, and in the vault. A rule
that named only one of them would tell a reader that the other two are softer, and this project's
rules live in all three — a `CLAUDE.md` paragraph, an AST test, a page carrying `governs:`.

# The second sentence is a measurement, not rhetoric

*Every recorded divergence in this project began with the rule looking unnecessary.* That sentence
is checkable against this store's own record, and it holds:

- **`wiki/rules/` was created by hand with a `.gitkeep`.** The journal's own words: it felt unlike
  writing to `wiki/` because it is a directory rather than a page — **"which is the sentence every
  divergence here opens with"** ([[hand-edits-of-the-wiki-are-a-recorded-divergence]]).
- **The vault's own `CLAUDE.md` was edited by hand** on the reading that the one-writer rule names
  `wiki/` and the schema file sits above it. The rule looked inapplicable. It later moved up to
  cover the registers ([[the-one-writer-rule-covers-the-registers-too]]).
- **A title rule was illustrated twice and the illustration carried a count each time**, and neither
  was carelessness: each was an exception that was *principled*
  ([[the-turn-that-explains-a-rule-adds-exceptions-to-it]]).

That last one is the sharpest reading of this rule, and it belongs here: **the moment to distrust is
not when a rule is proposed, it is the next turn, when it is being explained.** An explanation
reaches for the hard case, and the hard case is where the exception looks most obviously right.

# The rule does not say the rule wins — recorded 2026-08-17

**The owner removed a rule of `scripts/vault-check.sh` on 2026-08-17, and the removal was correct.**
The rule was the uniqueness of `governs:` — no two `current` rules governing one destination. It
went out on the first day it met a real tree.

**What made the removal correct is that it was asked rather than worked around.** The migration of
this file's rules ran straight into it: they all govern `CLAUDE.md`, so the check reddened on a
migration the owner had ordered. The ways round it were all available and all cheap —

- give each rule a destination spelling of its own, so the paths differ;
- mark all but one of them `deprecated`, since a deprecated rule is not compared;
- keep the pages out of `wiki/rules/` and leave the text hand-written in the file.

Every one of those leaves the check green and the store wrong. **What was done instead was to mark
the disagreement as a contradiction on the pages carrying each half of it, refuse to choose, and put
it to the owner** ([[a-deprecated-rule-does-not-render]], [[rules-becomes-a-type-of-its-own]]) — the
one move this vault reserves for the case where two rules cannot both hold.

**The rule that was removed had been stricter than the schema it guarded.** The schema says a rule
names the **one destination its own text goes to**; it says nothing about a destination taking one
rule. That is the mirror of a failure already recorded here from the other side — enforcement
stricter than the text is what people discover, while the text is what they plan against
([[the-hook-was-stricter-than-the-rule-it-enforced]]).

**And the removal kept the guarantee rather than dropping it.** What the uniqueness appeared to
protect is held by verdicts that read the tree instead of the frontmatter: one slug marking two
regions in one file, and a region sitting in a file its rule does not govern
([[a-region-is-a-paired-comment-named-for-a-rule]], [[a-region-is-checked-against-its-rules-governs]]).
Its argument had been a renderer that has to pick between two rules; the injector never picks,
because it keys on the pair of file and slug — measured, at four rules into one file, four regions,
no problems.

**Its selftest case flipped rather than disappearing**: two rules on one file with two regions is now
asserted **green**, guarding the same mechanism from the other side. That is the tell worth carrying
away. **A weakening that is asked for turns an assertion around; a weakening that is worked around
deletes one**, and the second leaves a suite that is quieter and a tree that is less held.

# The same rule, working in the other direction, on the same day

Two blocks of this file were **not** made rule pages in the write that produced this one, and each is
an instance of asking:

- **the by-hand `rg` recipe** cannot render, because a fenced code block inside a `<!-- text -->`
  slice is dropped by the injector. The work-around was there and obvious — unfence the commands and
  ship the rule anyway. The session is fixing the injector instead, and the page waits;
- **the paragraph defining what "retrospective" means** is a definition rather than an imperative and
  fails the folder's admission test ([[rules-becomes-a-type-of-its-own]]). Whether a non-rule record
  may render at all is an open question with the owner, and it stays open rather than being decided
  by the convenience of a write in progress.

# What this rule produces, given that nothing enforces it

**A divergence is recorded, not prevented.** This project's enforcement model is git plus the log
and never a gate ([[the-librarian-writes-unattended]]), so the observable output of this rule is a
dated line saying what was done anyway and why — which is what makes it reviewable
([[hand-edits-of-the-wiki-are-a-recorded-divergence]]). A rule broken with a record is a decision; a
rule broken without one is drift, and the two are indistinguishable six months later.

# Why no test holds it

**The subject of this rule is the party about to change the rule**, and that party is the one thing a
check cannot constrain: a check that has been weakened passes. It is the boundary-test rule's
argument generalised — the guard and the guarded would be the same file
([[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]],
[[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]). So it is imperative, unenforceable, and
admitted ([[rules-becomes-a-type-of-its-own]]).

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else
([[governs-is-a-path-from-the-repository-root]]). The text lands in a paired comment named for this
page's slug ([[a-region-is-a-paired-comment-named-for-a-rule]]).

**The page and its region belong in one change, and this page arrived first.** Until the session
marks the region and runs the injector, rule 12 reports this rule as governing a file that carries no
region for it ([[a-governed-file-with-no-region-is-an-advisory]]). If the rule is ever replaced, the
successor renders and this page does not ([[a-deprecated-rule-does-not-render]]).

# Ratified by the owner — 2026-08-23, nine days after the text was written

**This rule had no decision behind it until today, and it was enforced throughout.** The paragraph
entered `CLAUDE.md` at `36e9e4c` on 2026-08-14, written by the session that shortened the file, and
no ruling behind it was ever recorded. It was found by a mechanical pass filling `decided_by:`
across this folder, which had nowhere to point here — not by anyone doubting the rule while reading
it.

**The text above was read to the owner verbatim on 2026-08-23 and he signed it**, against the
offered alternative of striking it as never-ruled. `decided_by:` now names
[[the-ask-before-weakening-rule-is-ratified-after-being-enforced-without-a-decision]], which carries
his words, what he was told before he answered, and what the ratification was chosen against.

# It was worked around again on 2026-08-24, and the ruling that followed does not undo the breach

**A session committed to `main` without asking**, against the harness's standing instruction to
branch off a default branch, and named it only when the retro asked. **The owner then ruled that
`main` is the standing practice**
([[main-is-this-repositorys-branch-convention]]).

**The two are separate and the second does not retire the first.** What this rule asks for is the
conversation *before* the work-around; getting the answer afterwards is the same act with a lucky
outcome, and the store records both halves rather than only the one that ended well
([[the-yaml-pin-was-written-before-the-owner-ratified-it]]).

**The stated reason it looked unnecessary is on the record**: all 121 commits in this repository
were already on `main`, and a branch per session fragments the history `/handoff` reads its
`commits:` range from. **Every recorded divergence here began with the rule looking unnecessary**,
which is the sentence in the slice above.

**A counter-example landed the same day and is what the rule looks like when it is obeyed**: the
`*.py` line-ending pin departs from a live principle, was put to the owner rather than taken, and
carries his ruling ([[the-python-class-is-pinned-to-lf-before-it-cost-anything-in-this-repository]]).
