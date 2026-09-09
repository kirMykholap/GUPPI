---
title: "A migrating rule leaves the numbered list for a block of its own, and ships no ordinal"
type: decision
status: archived
authority: rule-ordinals
binding: prohibition
basis: code
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md", "scripts/vault-check.sh"]
tags: [harness, vault, process]
---

# A session decision, taken without asking and reviewed at the retro

**When a rule of the repository's `CLAUDE.md` becomes a page, it stops being item *n* of a list.** Two
independent reasons, and either alone is sufficient:

1. **A marker must stand alone on its line at column zero**, which breaks a list item. Rule 11 names
   *"not a marker alone on its line at column zero"* as malformed, and the requirement is not
   negotiable at the margin — it is what makes the pattern unambiguous
   ([[a-region-is-a-paired-comment-named-for-a-rule]]).
2. **Shipping the ordinal inside the page would put a number in the wiki that drifts** as the remaining
   rules migrate. Rule 4 becomes rule 3 the moment rule 1 leaves, and the page would be wrong without
   being touched ([[a-stated-count-drifts-from-the-list-it-heads]]).

**Rejected: renumbering the list at each migration.** That is a copy being corrected rather than
removed, which this project refuses on principle
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

## What it obliges

- **The heading over the list stops counting.** *"Four rules that cannot wait for a question"* was
  about to head nine, and the repair was to delete the count from the heading rather than to update it
  ([[the-repository-claude-md-after-the-rules-left-it]]).
- **A page's identity is its slug, and never its position.** Every reference to a rule of that file in
  this corpus now names the page, not the number
  ([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).
- **The mixed state is legal and was legal for one commit**: three rules numbered, one marked, under a
  heading that still read *Four rules* and was still true. A migration that has to be atomic to be
  correct is a migration nobody starts.
