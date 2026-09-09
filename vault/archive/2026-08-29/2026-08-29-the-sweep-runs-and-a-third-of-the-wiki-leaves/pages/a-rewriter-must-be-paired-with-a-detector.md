---
title: "A path rewriter need not be complete where its detector is, but it must be paired with one"
type: lesson
status: archived
authority: rewriter-and-detector
basis: measurement
sprint: S1
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", "scripts/vault-check.sh"]
tags: [vault, testing, process]
---

# A file moved, and the gate answered the owner's question for him

On 2026-08-16 the owner moved `.claude/agents/vault-librarian.md` to a directory of its own. The
move left **eight files in the vault and three outside it** naming the old path.

**`vault-check.sh` went red immediately and named three of them** — the three carrying the path in
`sources:`. It said nothing about the other five, which mention it in prose, nor about the
repository's `CLAUDE.md`, nor about two plans under `docs/`.

**So the detector is complete for citations and blind everywhere else** — the same boundary as
every other check here, which reads frontmatter and link structure and not meaning
([[vault-scripts]]).

## The answer to *can a script fix paths after a move*

**A rewriter does not have to be perfect where a detector is complete; it has to be paired with
one.** Where `sources:` is concerned, a rewriter can be mechanical and its misses are caught by the
gate on the next run. Where prose is concerned, neither exists, and a rewrite there is a change
nothing will check.

**This move had no rewriter at all**, which is why the correction was done by hand, in the same
session, once the gate named the first three.

## What was rewritten, and what was deliberately left

The directory was first created misspelled — `vault-libranian` — and the agent still resolved,
because `name:` in its frontmatter was correct. That was corrected the same session, and the owner
then authorised a mechanical path rewrite:

- **six pages in `wiki/` and the repository's `CLAUDE.md`** now name
  `.claude/agents/vault-librarian/AGENT.md`;
- **`raw/` was left alone**, because a journal is testimony about its own date and is never edited;
- **the two plans under `docs/` were left naming the old path**, for the same reason.

The gate is green again. The general form of *why the immutable copy is not corrected* is
[[fidelity-to-a-source-and-fidelity-to-the-tree]]; the general form of *a claim in a `CLAUDE.md`
that nothing reads* is [[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]].

## The pair was priced, and half of it already exists — measured 2026-08-18

**All six standing renames were done in an isolated worktree in 10.1 seconds**, including a full
gate run, across 51 files, with the gate returning to exactly its baseline. **The detector half is
already built for the link set**: a half-done rename leaves a broken wikilink and an orphan, and
rules 4 and 5 print both ([[a-page-rename-is-sed-and-verify]]).

**What is genuinely missing is smaller and more specific than "a rewriter"**: `log.md` is outside
the set those rules read, and a rename strands it silently — demonstrated, 13 dangling links and a
green gate ([[log-md-is-outside-the-link-set-the-check-reads]]).

**And no `proposals/` page designs the rewriter the renames were said to wait on.** The blocker was
prose in several places with nothing behind it
([[a-blocker-can-be-dissolved-instead-of-answered]]). This lesson stands — the pairing rule is
right — but *this* rename was not the case that needed it built first.

# One of the ones left is still pointing at nothing, three days later — found 2026-08-19

**`.claude/agents/vault-librarian.md` is named in `wiki/` bodies**, and the file has been at
`.claude/agents/vault-librarian/AGENT.md` since the move this page records — the sweep that rewrote
six pages and `CLAUDE.md` **while leaving prose alone**.

**This page's own claim, demonstrated on itself.** Nothing checked the prose, so nothing reported
it, and it took a prototype built for a different purpose to find it
([[a-path-detector-for-prose-references]]).

**The detector half is now measured rather than assumed impossible.** Over the bodies of `wiki/`:
299 backtick spans shaped like paths resolve and 168 do not; after excluding globs and score
fractions, and after trying the vault root as a second base, **the residual is 65 across 41 pages**,
of which roughly 24 are illustrations. **So a prose detector is buildable and can only ever be an
advisory**, because a page recording history is supposed to name a path that no longer exists
([[fidelity-to-a-source-and-fidelity-to-the-tree]]).

# The file moved back on 2026-08-20, and both mentions above stay exactly as they are

**`.claude/agents/vault-librarian.md` is the live path again**, so the dangling reference this page
found on 2026-08-19 has resolved itself — by the file returning, not by anything reporting it.

**Neither mention here is repointed.** The list names what the 2026-08-16 sweep wrote; the section
below it says *"since the move this page records"*. **Both are claims about where the file was at a
time**, and repointing either makes the sentence assert the opposite of what it meant while the gate
stays green.

**The ratio this page argues for is now measured on a live rename**: of nine wiki pages naming the
moved path, the gate saw **four** in `sources:` and was blind to **five** in prose — and four of
those five were correct as written ([[a-path-detector-for-prose-references]]).

**And the rewriter half now has a rule rather than a habit.** A session may repoint a citation in
the same change that renames what it points at — `sources:` lines only, prose never
([[the-one-writer-clause-reaches-a-citation-and-not-only-a-register]]).
