---
title: "A retired rule number is never reused, because the corpus cites rules by number"
type: decision
status: archived
authority: rule-numbering
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-check.sh"]
tags: [harness, vault]
---

# Decided 2026-08-17, when rule 9 was retired

Rule 9 of `vault-check.sh` — *`catalogue.md` is what the generator produces* — was retired with the
file it guarded ([[the-page-list-is-a-query-not-a-generated-file]]). **Its number is dead. The next
rule was 11, then 12.**

**Rejected: renumbering 10, 11 and 12 down** to close the gap.

## The reason is a property of this corpus, not tidiness

**Pages in the vault cite these rules by number.** Taking the freed slot would repoint every such
citation without touching a word of any page: a sentence saying *rule 9 fails while the catalogue
is stale* would silently come to mean whatever rule 9 became. Nothing would be broken, nothing
would be flagged, and every affected page would still read as correct English.

That is the same failure the whole store is built against — a claim that changes meaning while its
text stands ([[a-stated-count-drifts-from-the-list-it-heads]]).

## The underlying failure was found live the same day

Two rule-numbering schemes for `vault-check.sh` are in the corpus at once:

- **[[vault-scripts]] numbers eighteen "failing conditions"** and enumerates them 1–18. That list is
  the *page's* enumeration of what can fail, and it has never matched the script's own rule numbers.
- **[[rules-becomes-a-type-of-its-own]] says "rule 4 (folder against `type:`)"**, where the script's
  rule 4 is the link rule and folder-against-`type:` is rule 2.

**Every other page in the corpus uses the script's numbering.** The gap was surfaced at a
`/pre-task` for the marked-region build, where the next rule's number had to be established before
anything could be written — which is a fair summary of what this decision costs when it is absent.

Both pages carry a correction note as of this ingest; neither had its text removed.

## What it obliges

A retired rule is struck from the script with its number left visible as a comment, and a page that
cites a retired rule is annotated rather than repointed — the citation is still true about the day
it was written.
