---
title: "The address verdict joins the rule that already holds every region, instead of becoming a rule of its own"
type: decision
status: archived
authority: address-verdict-home
binding: prohibition
basis: inference
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# A session decision, taken without asking and reviewed at the retro

**The verdict comparing a region's file against its rule's `governs:` was written into rule 11**, not
added as a rule 13 of `scripts/vault-check.sh`.

*(The title read "The address verdict joins rule 11 instead of becoming a rule of its own" until
2026-08-18, and the sentence above is now where the number is resolved. **11 was never a count**: it
is the identifier of a rule in `scripts/vault-check.sh`, and a retired rule number is never reused
([[a-retired-rule-number-is-never-reused]]), so it is a fixed address that cannot drift. That
reasoning stood in a `quantity:` line on this page until the field was rejected and the rule made
unconditional in both halves ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]);
the title now names the rule the verdict joined instead of numbering it
([[a-title-names-what-is-counted-instead-of-counting-it]]). The **filename** still carries the number
and waits for its rename, which moves an address ([[the-title-rule-extends-to-filenames]],
[[a-page-rename-is-sed-and-verify]]).
**Closed 2026-08-19: the rename landed and the name counts nothing.** The sentence above was
written on 2026-08-18 and stood for one day; the wait is the record rather than an oversight,
because a filename is an address and the repair was scheduled as one sweep of sixteen names in a
single change, not taken by whichever session happened to open this page next.)*

**The ground: it is the fifth of a set whose other four live there.** Rule 11 already holds every
region with its slug, its file and its line; the frontmatter pass already holds every current rule's
`governs:`. The comparison is a join between two tables the check already builds, and putting it in a
rule of its own would have meant a third pass over the swept tree to rebuild one of them.

**Rejected: a numbered rule 13.** Two costs, and the second is the real one. A number is an address
every page in this corpus cites, and a retired number is never reused
([[a-retired-rule-number-is-never-reused]]) — so a numbered rule is a permanent commitment for what is
one comparison. And a reader looking for *what does the check say about regions* would then have to
know that the answer is in two places.

**Rejected also: putting it in the injector**, which is where the proposal behind it said to put it.
The injector walks rule pages and opens only the destination each `governs:` names; it holds no table
of regions found elsewhere, and giving it one would put a second copy of the swept governed set in the
tree ([[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]],
[[a-copied-list-drifts-and-a-sweep-cannot]]).

## What it obliges

- **The rule numbering does not move**, so no page's citation of a rule number goes stale by this
  ([[vault-scripts]]).
- **Rule 11's own description grows**, and it is now four paragraphs of comment about one rule. That is
  the cost, and it is accepted: the alternative was a number that could never be given back.
- **The distinction the placement rests on is worth keeping**: rule 11 is about a region's *address*,
  which only a sweep can see; rule 12 is about its *content*, which the writer owns and which is why
  rule 12 asks by running the writer ([[a-check-asks-by-running-the-writer-it-checks]]).

**Two live pages called it "the fifth verdict of rule 12"** before it was built, which is what the
`/pre-task` corrected: rule 12 by design contains no logic of its own
([[a-proposal-can-be-wrong-about-the-hole-it-describes]]).
