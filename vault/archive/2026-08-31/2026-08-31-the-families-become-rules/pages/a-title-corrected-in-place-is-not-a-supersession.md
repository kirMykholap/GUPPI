---
title: "A title corrected in place is not a supersession"
type: decision
status: archived
authority: title-corrections
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "CLAUDE.md", "scripts/vault-check.sh"]
tags: [vault, process]
---

# Decided 2026-08-17 by the owner

**Supersession is for a changed claim.** Striking a stale number out of a title is not one: in this
vault **the filename is the identity** — it is the search surface, and it is what every
`[[wikilink]]` resolves to — so a corrected title moves no address and strands nothing.
Superseding on a title change would mean a page is identified by its title, which is not how
anything here addresses a page.

**Rejected: full supersession for each of the retitles**, priced at a new page and an archived page
per title, plus every inbound link rewritten. That price bought nothing: the pages' claims had not
changed, only the counting in their names had, and the rule that forbade the counting was written
the day before ([[a-title-names-what-is-counted-instead-of-counting-it]]).

**Renaming the *file* is the other operation and is explicitly not this one.** A rename moves an
address, so it needs the rewriter-and-detector pair first
([[a-rewriter-must-be-paired-with-a-detector]]).

## What it obliges

- **The compliance pass is unblocked.** The retitles it was waiting on are edits, not supersessions,
  which is what made thirty-seven of them affordable in one session
  ([[the-title-check-asks-and-does-not-judge]]).
- **The correction is stated on the page, not hidden.** This corpus writes *(this line read X until
  DATE)* beside the text it replaces; a title corrected silently is a claim changed silently.
- **It says nothing about a changed claim.** A page whose argument moves is still superseded per the
  schema — successor first, `superseded_by:` on the old page, and the old page into `archive/`.

The clause is written into the vault's own `CLAUDE.md` under `status` and supersession, and into
rule 10's comment in `vault-check.sh`, by the owner's session rather than by the librarian
([[hand-edits-of-the-wiki-are-a-recorded-divergence]]).

## The other side of the boundary, exercised 2026-08-17

**A count inside a page's *claim* is the claim, and changing it is a supersession.**
`the-wiki-has-five-folders-and-tasks-is-not-one` said *five* in its H1 and in its first line, and
`wiki/rules/` made six. It was retired rather than corrected, and its successor is
[[the-folder-set-is-closed-and-tasks-is-not-in-it]]. Its own history is the precedent: it retired a
predecessor that said *four*, for exactly this reason.

**The distinction is where the number sits, not that there is one.** A stale number in the
`title:` field moves no address and strands nothing, so it is struck out in place. A stale number in
what the page *asserts* means the page is now false, and a reader arriving at it must be told what
replaced it.

The same day produced a second supersession of the same shape, where a page's **conclusion survived
its mechanism** ([[the-page-list-is-a-query-not-a-generated-file]]) — which is the other reliable
signal that a successor is owed rather than an edit.
