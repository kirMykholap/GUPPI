---
title: "What travels from a rule page is a marked slice, and everything outside the mark stays home"
type: decision
status: archived
authority: rule-text-boundary
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-inject.sh", "job_hunt_ai_vault/CLAUDE.md"]
tags: [harness, vault]
---

# Decided by the owner on 2026-08-17

A `rules` page carries **exactly one `<!-- text -->` … `<!-- /text -->` slice**, and that slice is
what `scripts/vault-inject.sh` renders into the region the page governs. The justification, the
measurements and the links stay on the page and reach nothing.

**Rejected: rendering the whole body**, with rule pages written short enough to survive it.

## The argument that decided it was already on the record

**Prose does not stop an agent.** The repository's `CLAUDE.md` went from 218 lines to about 110
once, and only structure keeps it there — nothing about the file's own good intentions did. A rule
saying *keep rule pages short so the whole body can travel* is exactly that kind of prose: an
instruction with no mechanism behind it, in a store that has recorded seven harness divergences
none of which was caught by anything mechanical ([[no-rule-reads-a-harness-file]]).

Marking the slice moves the constraint from the author's discipline into the file's syntax. What
ships is what the author marked, and the rest of the page can be as long as the argument needs.

## What it obliges

- **A current rule page with no slice is red.** The gate cannot render a rule that does not say
  what travels, and silently rendering nothing is the failure mode this project keeps meeting.
- **Exactly one slice, never two.** Two would make the page's own order the delivery order and put
  the reader of the destination at the mercy of an editing accident.
- **A deprecated rule does not render at all** — [[a-deprecated-rule-does-not-render]].
- The rendered end is checked by running the renderer rather than by a second comparison
  ([[a-check-asks-by-running-the-writer-it-checks]]), and what that guarantees is agreement and
  never truth ([[a-gate-guarantees-agreement-never-truth]]).

**No rule page exists yet.** The first migration is the next session's work, and rule 12 fails a
rule page whose destination carries no region — so the page and the region are written in the same
change ([[a-region-is-a-paired-comment-named-for-a-rule]]).

## Measured against nine real slices on 2026-08-17, and one thing a slice cannot carry

**Nine rule pages ship nine slices and every one of them is byte-equal to the block it replaced** — the
lines were cut out of `CLAUDE.md` by number, the ordinal and list indent stripped mechanically, and the
result diffed against the slice. Nine diffs, all empty
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).

**Trailing whitespace is content.** The language slice carries markdown hard breaks — trailing double
spaces on two of its lines — and they survived the round trip. **An editor that trims trailing whitespace
reddens rule 12 on a change nobody typed**, which is recorded on that rule page itself.

**A slice cannot carry a fenced code block.** The injector strips fences on both sides of the comparison,
so a code block inside a slice is silently dropped and success is still reported — measured at three lines
in and one line out ([[the-injector-drops-a-fenced-block-inside-a-slice]]). That is why the by-hand `rg`
recipe of the repository's `CLAUDE.md` is still hand-written prose.

**And a slice may not carry a `[[wikilink]]`**, though nothing enforces it: the destination is a file
where Obsidian syntax is inert, which is why that file refuses links at all. Measured on all nine pages —
every citation sits outside the slice ([[a-live-page-can-argue-from-a-deprecated-one]]).

**One slice per page, and the refusal is a verdict**: `slice_of` reports *"two text slices; a rule ships
one piece of text or it is two rules"* ([[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]).

# This page is suspended for the cleanup — 2026-08-30, and it is not deprecated

**[[the-cleanup-suspends-the-rules-that-would-refuse-it]] lifts this page for the cleanup**, with
three others, on one ratification.

**What is lifted is the requirement that a live rule page carry a marked slice at all.** A page under
`render: authority` is written into no file, so there is nothing for a slice to travel to: it carries
an `authority:` slug, no `governs:`, and no `<!-- text -->` markers
([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).

**Everything above stays true of the two rendering modes.** Fifteen pages render into a region and two
render whole, and for every one of them the slice is still what travels and everything outside it
still stays home. **The lift narrows the rule's subject rather than contradicting its claim.**

**And the sibling rule was checked and needs no lift.**
[[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]] refuses a page carrying **two** slices;
a lookup rule carries none, which that verdict does not object to. It is named here so its absence
from the repeal reads as a check rather than as an omission.

**This page stays `current`, is not `deprecated` and carries no `superseded_by:`.** A repeal is not a
supersession, ruled 2026-08-30. **The suspension has no stated end.**
