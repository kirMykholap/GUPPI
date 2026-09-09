---
title: "\"The file stops carrying assertions\" means no *unsourced* assertions, so a record may render into `CLAUDE.md`"
type: decision
status: current
authority: claude-md-assertions
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md"]
tags: [harness, process, vault]
---

# Decided by the owner on 2026-08-17, reading his own earlier decision

The dispatch-table decision says the repository's `CLAUDE.md` *"stops carrying assertions and carries
entry points"* ([[the-repository-claude-md-becomes-a-dispatch-table]]). **He read that as: no
*unsourced* assertions.**

**Why the earlier wording was narrower than the intent: it was written on 2026-08-16, before a
renderer existed.** At that moment the file had exactly two options for a fact — a hand-written
assertion, or a pointer at a page. The third did not exist. A rendered assertion **has a page behind
it, is corrected in one place, and reddens the gate when it drifts**, so the disease the dispatch-table
decision was written against is *cured* rather than renamed
([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

**Rejected: reading the earlier decision literally** and moving the project description out to a page
the file merely points at. That would have made the first thing every session reads a pointer to what
the project is.

## What it obliges

- **The project description stays in `CLAUDE.md`**, and its destination is a rendered region rather
  than typed prose. That region does not exist yet: the marker mechanism only carries rules, so a
  non-rule record cannot render until `governs:` is read as a field
  ([[governs-becomes-a-property-of-any-page]], [[the-marker-carries-a-type-and-governs-is-read-as-a-field]]).
- **The test for the file is now the source, not the sentence type.** *Is there a page behind this
  paragraph, and does the gate compare them?* — not *is this a statement or a pointer*.
- **Rule 5b's vacuous pass is unchanged by this.** It checks that a wikilink in that file names a
  page that exists; there are no wikilinks in it and there will be none
  ([[claude-md-may-point-and-may-not-assert]]).

## What this does not license

**Prose typed into that file is still the failure this project has recorded most.** Two blocks in it
are unsourced today and both are recorded as such rather than tolerated quietly: the first sentence,
which describes a map that was deleted, and `## Commands`, whose stated `~2 s` is measured at `4.9 s`
([[the-repository-claude-md-after-the-rules-left-it]]). *Sourced* is the whole of the licence.
