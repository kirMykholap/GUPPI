---
title: "The no-quantity rule reads the title and the filename, and never the body: a counting subheading is prose"
type: decision
status: archived
authority: quantity-rule-subject
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["log.md", "scripts/vault-check.sh"]
tags: [retrieval, vault, harness]
---

# Decided 2026-08-19: the subject of the rule is `title:` and the filename

**A counting heading inside a page's body is out of scope, and that is a decision rather than an
omission.** The rule itself is unchanged — [[a-title-names-what-is-counted-instead-of-counting-it]],
extended to the address by [[the-title-rule-extends-to-filenames]] and given its word list by
[[ordinals-count-and-first-does-not]]. What is settled here is **which strings the rule is about**,
which nothing had said, and which three agents in one session each assumed differently.

**What asked the question.** The corpus clean-up of 2026-08-18 and 2026-08-19 repaired the titles
and then the addresses under them. Reading those pages, three separate agents reported the same
class of finding: headings like *"The two hooks"* or *"Three artefacts, three owners"* sitting in
bodies the rule had never touched. Each report read as a gap. It is not one.

# Why the boundary sits exactly there

**The title and the filename are the two strings this store addresses and retrieves a page by.
A subheading is prose.**

- Every `[[wikilink]]` resolves to a **filename**, and rules 4 and 5 of the check are built on that
  set alone.
- The narrowings a reader is told to apply before opening anything are `rg --files` over names and
  a grep of `^tags:` or `^title:` over frontmatter — both of them addressed strings
  ([[the-folder-is-the-first-narrowing]]).
- `pages.base` and `bash scripts/vault-catalogue.sh` list pages by `title:`; the brief quotes
  titles. A reader deciding whether to open a page has the title and the name in front of them and
  nothing else.

**So a false title is asserted to someone who has not opened the page**, and there is no way for
them to find out it is false without doing the work the title was supposed to save. A false
subheading is read by someone already inside the page, with the list it heads in the same glance —
the contradiction is on screen, in one view, and it costs a scroll rather than a retrieval.

# The code already says this more exactly than the prose did

Rule 10's `awk` in `scripts/vault-check.sh` stops evaluating a page at the closing `---` of its
frontmatter — `done { next }` — and its `verdict()` is called with `title` and `FILENAME` and
nothing else. **The body is not scanned at all**, so this was never a word list that had failed to
reach headings; it is an instrument pointed at two strings. What the ruling does is make that
aiming deliberate, so the next reader of the script finds a boundary instead of a hole.

# What was ruled in, and the test is contradiction rather than counting

**Exactly the headings our own retitles had left contradicting the titles above them were ruled in
scope, and both are repaired.** The defect there was ours and it was made by the repair pass: a
page whose title stopped counting while the heading under it went on doing so states two different
things about itself, and the reader cannot tell which one the page means.

**So the test a reader applies to a body heading is not *does it count*. It is *does it contradict
the title above it*.** That test is bounded — it can only fire on a page whose title was just
changed — where *does it count* is not.

# What was rejected, and the list is what was refused

Three ways to keep the agents' findings from being lost were put to the owner: **a line in
`sprint.md`**, **a proposal page**, and **a written boundary**. He took the boundary, on the ground
that the other two produce a list which has to be extended every time anyone writes a page with a
number in a subheading — **work without end, and a list that is stale the day after it is written**
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
[[a-copied-list-drifts-and-a-sweep-cannot]]).

**The pages the agents named are deliberately not listed here.** Naming them would be the list he
refused, in the one place a future session would find it and treat it as a queue.

# The size of the list that was refused, measured rather than argued

The agents named roughly a dozen between them. Under rule 10's own predicate — its word list, its
exemptions — applied to markdown headings instead of to frontmatter, the corpus reads
**201 counting headings across 128 of 308 pages**, on the working tree of 2026-08-19. A cruder
one-liner, with a shortened word list and no exemptions, reads 122 pages:

```
rg -l --glob '*.md' -i '^#{1,6} .*\b(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|dozen|both|twice|thrice|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)\b' wiki | wc -l
```

**The figure is not the point and is not maintained** — it grows with the corpus, which is the
argument ([[an-unsourced-number-is-dropped-not-chosen]]). The point is the order of magnitude: what
was offered as a list of a dozen is a standing property of two pages in five, and every page written
from here can add to it.

# What this does not say

**It does not say a count in a body never drifts.** It does, and it is the most-recorded defect in
this project — [[a-stated-count-drifts-from-the-list-it-heads]] has instances in the repository's
own `CLAUDE.md`, in this vault's registers and in pages diagnosing the disease. What the boundary
says is that the **gate is not the instrument for it**: a stated count is checked against the list
beneath it by a reader, in place, and the repair is an edit like any other.

**And it does not close the question of a different check.** A rule comparing a stated count
against the list it heads is designed and unbuilt ([[a-rule-comparing-a-stated-count-against-its-list]]);
that proposal reads a number *against its own list*, which is a comparison, where rule 10 reads a
string for a word, which is a lexical guess. They are different mechanisms and only one of them is
being bounded here.

# What it obliges

**Nothing.** No sweep, no list, no task, no advisory. Writing the boundary down is the whole of the
work, and it exists so that the next session that notices a counting heading finds a decision
instead of a gap — and does not open a task for it.
