---
title: "A bare slug mention is an inbound reference no wikilink counter sees, and in `log.md` the bare ones outnumbered the linked"
type: lesson
status: archived
authority: bare-slug-inbound-links
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "scripts/vault-check.sh"]
tags: [vault, retrieval, harness]
---

# The measurement, taken with two instruments on 2026-08-19

Before the rename sweep, the sixteen pages to be renamed were counted twice, independently:

| instrument | what it counted | total across the sixteen |
|---|---|---|
| the session's | `[[wikilinks]]` only | **148** inside the set rules 4 and 5 read |
| the librarian's | wikilinks **and bare slug mentions** | the same 148, **plus 14 in `log.md`** — and in `log.md`, **28 bare against 14 linked** |

**They agreed on every one of the sixteen counts inside the checked set.** The agreement is what makes
the disagreement outside it readable: the second instrument saw a whole class the first was blind to,
and the class is larger than the one both could see.

# What it would have cost

**A rewriter matching only the linked form would have left two thirds of `log.md`'s references
dangling with a green gate.** `log.md` is outside the set rules 4 and 5 read, so nothing would have
printed ([[log-md-is-outside-the-link-set-the-check-reads]]) — and the bare mentions are the majority
there, because a log entry names a page as a subject far more often than it links to it.

**The rewriter-and-detector pair that the renames were said to be blocked on would have had exactly
this blindness**, since it was designed around the link graph
([[a-rewriter-must-be-paired-with-a-detector]], [[a-page-rename-is-sed-and-verify]]). The `sed -f`
sweep that replaced it substitutes a **string**, which is what caught both forms — and is also what
made it rewrite two quotations it should not have
([[sed-cannot-tell-an-address-from-a-quotation]]). **The same property is the strength and the
weakness.**

# The general point about counting a link

**"Inbound links" is not one number, it is a number per definition of link**, and the definitions
differ by more than a rounding. The corpus already carries an inbound-link figure that does not
reproduce at any commit checked, quoted across several pages
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]); part of the spread is exactly
this — whether `log.md` and bare mentions are counted.

**So a rename is priced with the definition attached**, and the wider definition is the one the sweep
has to satisfy, because a stranded bare mention is a page a reader cannot find and no gate reports.

# The wide definition became a precondition, and it was measured before it shipped — 2026-08-23

**`scripts/vault-archive.sh` refuses to move a page under `kind = pages` while no live `wiki/` page
names its slug, and *names* is the wide definition** — the bare slug matched anywhere in the file,
which catches a `[[wikilink]]` and a bare mention alike ([[vault-archive-sh]]).

**The safety of the wide match was measured rather than argued. Over all 530 slugs, exactly one page
would be refused, and it is the corpus's single orphan** — a true positive, and no false one at all.
**A hyphenated slug does not occur in ordinary prose**, which is why the looseness costs nothing
here.

**That measurement is of this corpus on this date and is not a property of the definition.** It is
the same standing as everything else on this page: which number *inbound links* is depends on which
definition you picked, and the wide one is chosen because a stranded bare mention is what nothing
else reports.

**The exact answer is designed and not built** — a `Links:` field a script fills from the body's
wikilinks, which would make the precondition ask a field instead of scanning text
([[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]],
[[links-is-filled-by-a-script-from-the-bodys-wikilinks]]). **It would also narrow *cited* back to
wikilinks**, and this page is the argument for deciding that deliberately rather than by
implementation.
