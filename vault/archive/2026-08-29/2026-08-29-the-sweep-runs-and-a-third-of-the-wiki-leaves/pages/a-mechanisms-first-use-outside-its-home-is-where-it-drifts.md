---
title: "A mechanism's first use outside the folder it was built for is where it drifts, and the anti-duplication mechanism produced a duplicate"
type: lesson
status: archived
authority: first-use-outside-home
basis: human
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "CLAUDE.md"]
tags: [harness, process, vault]
---

# The incident

**The map's slice restated two claims that were hand-written prose in `CLAUDE.md` five lines above
it.** The region mechanism exists to end exactly that — one text, one owner, rendered rather than
retyped — and its first use outside `wiki/rules/` created a duplication rather than removing one
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]).

**Two readers found it independently, and neither found it while designing the page.** Both found it
while *placing* it. The design was read whole, approved and cited; the overlap only exists in the
destination, and the destination is not where a design is read.

# Why the first use outside the home folder is the moment

**Inside `wiki/rules/` the mechanism carried an invariant nobody had to state**: a rule page's text
came *out* of `CLAUDE.md` in the migration, so there was never prose left behind for it to duplicate
— the migration deleted the source lines by construction
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).

**A `concepts/` page has no such history.** It is written fresh, alongside prose that already exists,
and nothing about the mechanism notices. The invariant was a property of how the first nine pages
arrived, not of the mechanism — and it expired silently the first time a page arrived any other way.

# The check to run, and where it has to be run

> **Read the rendered slice against the destination file, in the destination, before the region
> lands.**

Not against the page, and not while designing: the duplication is invisible on the page and obvious
in the file. The gate cannot see it — it compares a region to its page and guarantees agreement,
never that the file around the region says something different
([[a-gate-guarantees-agreement-never-truth]],
[[marked-regions-and-the-prose-outside-them]], whose fourth verdict row is exactly *text outside
every region is allowed and unchecked*).

**What was done with it here** is the placement decision
([[the-maps-region-replaces-the-prose-it-duplicated]]) — the prose was removed after the rendered
text was verified present, which is the only safe order
([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

# The repair has a procedure now, and it was used on 2026-08-22

**A region landing where the same text already stands as prose lands in this order: render, verify,
then delete.** The destination file already carried the shared reading discipline as hand-written
prose, which is the same setup that produced the duplicate above.

1. **Place the markers empty** and run `bash scripts/vault-inject.sh`.
2. **Diff the rendered region against the prose it duplicates** — 73 lines, 3757 bytes, `diff`
   empty.
3. **Only then delete the prose.**

**The order is what does the work.** Deleting first and rendering after leaves a window where the
file asserts nothing, and — worse — leaves the diff unavailable at exactly the moment it would have
caught a slice that is off by a heading ([[a-check-asks-by-running-the-writer-it-checks]],
[[the-maps-region-replaces-the-prose-it-duplicated]]).

**Verified before deleting, not after.** A comparison run after the prose is gone compares the region
against nothing; the whole value is in having both texts in the tree at once
([[the-shared-reading-discipline-renders-into-every-agent-that-reads-the-vault]]).
