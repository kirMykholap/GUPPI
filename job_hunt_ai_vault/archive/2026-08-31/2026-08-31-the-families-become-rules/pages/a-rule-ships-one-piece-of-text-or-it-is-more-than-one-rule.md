---
title: "A rule ships one piece of text or it is more than one rule, which is why `## Language` is one page"
type: decision
status: archived
authority: one-slice-per-rule
binding: prohibition
basis: code
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-inject.sh"]
tags: [harness, vault, process]
---

# A session decision, taken without asking and reviewed at the retro

The `## Language` section of the repository's `CLAUDE.md` is two paragraphs — English for everything
written into the repository, Russian only with the owner and in the product's own output. **It became
one rule page, not two** ([[english-in-the-repository-russian-with-the-owner]]).

**The criterion was the injector's own, and it is already in the code**: `slice_of` refuses a page with
two `<!-- text -->` slices, with the message *"two text slices; a rule ships one piece of text or it is
two rules"*. So the question *is this one rule or two* has a mechanical answer — **count the contiguous
blocks of text the destination needs** — and `## Language` needs one.

*(The title read "A rule ships one piece of text or it is two rules, which is why `## Language` is
one page" until 2026-08-18, and the injector's message quoted above is where the number now lives.
**It was never a count of the world**: the "two" is the consequent of a conditional and it is the
injector's own wording — a third block of text would make it three rules by the same sentence, so
nothing can arrive that leaves the title stale. That reasoning stood in a `quantity:` line on this
page until the field was rejected and the rule made unconditional over titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). **The quote keeps its
number**, because there it is the injector's word and not the title's claim; the title states the
boundary instead of counting past it ([[a-title-names-what-is-counted-instead-of-counting-it]]).
The **filename** still counts and waits for its rename, which moves an address
([[the-title-rule-extends-to-filenames]], [[a-page-rename-is-sed-and-verify]]). A title corrected
in place is not a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]).
**Closed 2026-08-19: the rename landed and the name counts nothing.** The sentence above was
written on 2026-08-18 and stood for one day; the wait is the record rather than an oversight,
because a filename is an address and the repair was scheduled as one sweep of sixteen names in a
single change, not taken by whichever session happened to open this page next.)*

**Rejected: two pages, one per paragraph.** They would render into two regions that must stay adjacent
and in order, and nothing in the mechanism can express *adjacent* — regions do not nest, do not
overlap, and carry no ordering ([[a-region-is-a-paired-comment-named-for-a-rule]]). Two pages would
have made the section's shape a property of where somebody happened to put the markers.

## What it obliges

- **The slice carries markdown hard breaks** — trailing double spaces on two of its lines — and they
  are *content*, not whitespace. They survived the round trip and were diffed byte for byte. **An
  editor that trims trailing whitespace reddens rule 12 on a change nobody typed**, which is recorded
  on the rule page itself.
- **A rule page's boundary is the destination's, not the subject's.** A subject can be as large as it
  likes; what may not be split is a run of text the destination needs whole.
- **The refusal is a real verdict and not a comment**: a page with two slices is red, so this decision
  cannot silently be broken later ([[what-travels-from-a-rule-page-is-a-marked-slice]]).
