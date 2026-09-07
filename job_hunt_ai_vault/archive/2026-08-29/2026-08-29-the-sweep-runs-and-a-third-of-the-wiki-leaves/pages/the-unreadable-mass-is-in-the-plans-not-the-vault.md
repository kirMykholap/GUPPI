---
title: "The unreadable mass in this repository is in the plans, not in the vault"
type: lesson
status: archived
authority: document-size
basis: measurement
sprint: S1
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md"]
tags: [process, vault, testing]
---

# The complaint, in the owner's words

The owner named the problem the whole structure exists to solve, and it is worth quoting rather
than paraphrasing: **an agent writes large documents with no structure; they cannot realistically
be read, so they are trusted; details inside them are wrong; the agent goes and builds the wrong
thing; and the correction cycle repeats.**

# Where the mass actually is, measured 2026-08-16

| | documents | lines | largest |
|---|---|---|---|
| `wiki/` | 121 pages | 7,701 | nine pages over a hundred, averaging 63 lines a page |
| `docs/superpowers/` | 15 documents | **19,959** | **4,864 lines** — seventy-seven wiki pages in one file |

**The store is the thin half of this repository, by a factor of about two and a half.** The
complaint points at the plans; the session that measured it was spent restructuring the vault.

This is the second time a measurement has moved the subject of a complaint: the tag advisories were
also aimed at the wrong unit until the instrument changed
([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]]).

## The project already invented the answer and applied it in one place

**`sprint.md` gives every acceptance criterion the command that decides it**, so the owner does not
read to verify — he runs something. That is why criterion 4 of S1 is written as *decided by:
nothing*, which is the honest shape for one that cannot be mechanised
([[a-sprint-closes-on-its-goal]], [[the-owners-question-was-how-would-you-check-that]]).

**No plan or spec under `docs/superpowers/` has anything of the kind.** A plan step that cannot be
verified by running something is a step that has to be trusted, and being trusted is the whole
mechanism of the complaint above.

Nothing has been decided about the plans. The measurement and the pattern are recorded here so that
the next attempt to shrink documentation starts at the half that is 19,959 lines rather than the
half that is 7,701.
