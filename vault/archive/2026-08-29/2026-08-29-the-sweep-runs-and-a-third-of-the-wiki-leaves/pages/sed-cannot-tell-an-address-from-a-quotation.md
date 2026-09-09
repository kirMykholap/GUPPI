---
title: "`sed` cannot tell an address from a quotation, and a rename sweep made a sentence say the opposite of what it meant"
type: lesson
status: archived
authority: rename-sweep-over-reach
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md"]
tags: [vault, retrieval, process]
---

# What happened, 2026-08-19

The rename sweep substituted sixteen old slugs for sixteen new ones across `wiki/`, `archive/` and
the registers, with one `sed -f` script ([[a-page-rename-is-sed-and-verify]]). **Two of those slugs
were being quoted by other pages as *examples* of counting names** — the pages were arguing about
the rule, not linking to the page — and the sweep rewrote the examples along with the addresses.

**One sentence came to say the opposite of what it was written to say**: a page illustrating what a
counting filename looks like ended up illustrating it with a name that does not count.

# Why nothing can distinguish the two uses

**A slug in a body is one string with two jobs.** As an address it is what a `[[wikilink]]` resolves
to and it must move when the page moves. As a mention it is *the name that was wrong*, quoted as
evidence, and it must not move — the evidence is the old name.

Nothing in the text separates them:

- **not the wikilink brackets.** These pages quoted the bare slug precisely because they were not
  linking to it, so a rewriter matching only `[[...]]` would have left the addresses stranded and the
  quotations correct — the mirror image of the same defect
  ([[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]);
- **not a code span.** Some quotations were fenced in backticks and some were in italics, and the
  corpus has never had a convention that says which;
- **not the surrounding words**, without reading them.

**So the class is: a mechanical rewrite over a corpus that talks about itself.** A store whose pages
argue about its own naming will always hold names it quotes rather than uses, and the more it does
that the more a sweep can damage.

# What the verification pass has to be, and what it is not

**`vault-check.sh` reports neither error.** Rules 4 and 5 ask whether every link resolves and whether
any page is unreachable, and both hold perfectly after a sweep that rewrote a quotation — the text is
wrong and the graph is fine. **The gate is green in exactly the case that needs a reader.**

**The pass that catches it is a `git diff` read by a human for meaning**, not a grep for the old
slug returning zero. Both over-reaches this session were caught that way, and each was corrected in
place ([[a-title-corrected-in-place-is-not-a-supersession]]).

# What it does not argue

**It is not an argument against the sed sweep.** The sweep moved 148 inbound links across sixteen
renames in ten seconds, and the alternative on the record — a rewriter-and-detector pair — was
priced, never built, and would have had this same blindness
([[a-page-rename-is-sed-and-verify]], [[a-rewriter-must-be-paired-with-a-detector]]). A tool that
reads meaning is not what is missing; **a reading of the diff is.**
