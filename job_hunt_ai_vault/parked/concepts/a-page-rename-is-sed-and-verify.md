---
title: "A page rename is sed-and-verify, and the blocked framing was overpriced"
type: concept
status: current
authority: rename-cost
basis: measurement
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check.sh", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [vault, retrieval, harness]
---

# Measured on 2026-08-18, on all six standing renames at once

**In an isolated worktree: 10.1 seconds of wall clock including a full gate run, 51 files touched,
and the gate came back at exactly the baseline.** That is the whole operation — a substitution over
the link set, then `vault-check.sh`.

**The detector is complete for the link set it reads.** A half-done rename cannot pass quietly: the
old address is a broken wikilink and the new page is an orphan, and rules 4 and 5 print both
([[a-rewriter-must-be-paired-with-a-detector]]). The pair that the renames were said to be waiting
on is, for `wiki/`, already half-built and the half that exists is the half that catches the error.

**Except for `log.md`**, which is outside that set and is stranded silently
([[log-md-is-outside-the-link-set-the-check-reads]]). That is the real hole, and it is a smaller and
more specific one than "blocked on a rewriter".

# Two figures on the record that do not reproduce

**The "23 inbound links" price does not reproduce at any commit checked.** Re-measured here at
`c521a10` over the link set — `wiki/`, `archive/` and the three registers — the highest inbound
count of the six is **20**, on `the-audits-findings-are-owed-to-the-owner`; the page the figure
was originally written about, `the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here`, carries
**14**, or 20 with `log.md` counted as well. The figure travelled from a `miss:` line into two
decision pages and `index.md` without anyone counting
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

**And no `proposals/` page designs the rewriter the renames were said to wait on.** The blocker was
carried in prose across several pages and had no design behind it anywhere — which is what makes
"blocked" the wrong word rather than a cautious one
([[a-blocker-can-be-dissolved-instead-of-answered]], [[a-proposal-misprices-by-overcharging-one-row-and-undercharging-another]]).

# What is still true about renaming

**It moves an address**, and an address is what every `[[wikilink]]` resolves to, so it is a sweep
scheduled as work rather than a repair a session performs because a check went red
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]). What the measurement
changes is the price, not the category.

# The sweep it priced was run on 2026-08-19, and the price held

**Sixteen renames, executed as `git mv`, one `sed -f` and a verification pass.** They moved **148**
inbound wikilinks inside the set rules 4 and 5 read, and **14** more in `log.md`, which is outside it
and was swept by hand ([[log-md-is-outside-the-link-set-the-check-reads]]).

**The rewriter-and-detector pair the renames were said to be blocked on was never built and was never
needed** ([[a-rewriter-must-be-paired-with-a-detector]]). That is the claim on this page, executed
rather than argued.

**Two things the measurement did not predict, and both are the substitution being a substitution:**

- **`sed` cannot tell an address from a quotation.** The sweep rewrote two slugs that other pages
  were quoting as *examples* of counting names, and one sentence came to say the opposite of what it
  was written to say. Nothing in a slug distinguishes the two uses, and the gate is green either way
  ([[sed-cannot-tell-an-address-from-a-quotation]]).
- **A string substitution catches the bare mentions a link-graph rewriter would have missed.** In
  `log.md` the bare slugs outnumbered the linked ones two to one, and a rewriter matching `[[...]]`
  alone would have left the majority dangling with nothing printing
  ([[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]).

**The same property is the strength and the weakness**, and the verification pass that answers it is a
`git diff` read for meaning — not a grep of the old slug returning zero.

# A folder move is not a rename here, and it was measured before it was agreed to — 2026-08-21

**The link check resolves a `[[wikilink]]` by *filename*, anywhere under `wiki/` or `archive/`.** So
moving a page from one folder to another strands nothing: no inbound link changes, no register entry
changes, and the rewriter-and-detector pair a rename needs is not in play. **The address this store
uses is the filename and not the path.**

**It turned an expensive-looking ruling cheap.** «governs уходит из concepts» looked like it needed
the full rename apparatus over 26 inbound links; reading the resolver took minutes and the ruling
went from blocked to half an hour of work
([[governs-is-a-property-of-wiki-rules-alone]], [[measurement-settled-what-argument-could-not]]).

**What a folder move *does* change is the marker's type word**, because the injector derives it from
the folder — four markers in the repository's `CLAUDE.md` had to be retyped
([[the-marker-carries-the-records-type]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

# A path in `sources:` and a name in `decided_by:` behave in opposite ways — 2026-08-23

**The link sweep resolves a wikilink by filename alone.** Its `resolvable` set is built by stripping
the directory from every `.md` under `wiki/` and `archive/`, so a page can move anywhere in either
tree and every inbound `[[wikilink]]` still resolves. **Renaming one breaks all of them.** That is
the mechanism behind the section above, stated from the sweep's end rather than from the rename's.

**It splits the two provenance-shaped fields cleanly**, which is worth knowing before either is
touched:

| field | what it addresses | what a move does to it | what a rename does to it |
|---|---|---|---|
| `sources:` | a **place** — a path | rewritten by `scripts/vault-archive.sh` | nothing |
| `decided_by:` | a **name** — a slug | nothing at all | breaks it |

**So the archiver's rewrite pass and the rename sweep are answers to different problems** and
neither substitutes for the other ([[vault-archive-sh]],
[[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).

**And a filename is therefore an address in a way a title is not**, which is why a title may be
corrected in place and a filename may not
([[a-title-corrected-in-place-is-not-a-supersession]]).
