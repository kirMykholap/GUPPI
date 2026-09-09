---
title: "A dictionary entry that points at a page or a folder, and not only at a tag"
type: proposal
status: current
authority: alias-target-kinds
basis: human
sprint: S1
created: 2026-08-16
sources: ["tags.md", "scripts/vault-check.sh", ".claude/agents/vault-librarian.md"]
decided_by: [[structure-work-agreed-and-not-executed]]
tags: [retrieval, vault]
---

# Let a word route straight to a page

**Designed 2026-08-16 and not taken.** The design, in one sentence:

> A dictionary entry today is *word → tag*, so every alias must attach to a tag. Let an entry
> instead point at a **target** that may be a tag, **a specific page**, or a folder.

## What it would win, which is the honest case for it

**The mechanism that inflates the big tags would stop.** `vault` has been extended **five times**
in `tags.md` at `2036d98` — the owner's note vocabulary, proposals, the audit, the compilation
method, the catalogue — and every extension records the same trigger in its own text: *a Russian
word reached nothing, and the fix was to add the word to `vault`'s alias list.*

That fix is correct for recall and wrong for classification, every single time, and the two are
welded together by the entry's shape. A word like `каталог` or `аудит` has to be hung on some tag,
so it is hung on the widest one — which is how `vault` arrived at 51 pages of 118 at `2036d98`
([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]]). **A direct route removes the
coupling**: the word lands on the page it means, and the tag keeps whatever selectivity it had.

It also matches how retrieval actually works here. You do not need to find every relevant page —
**only one, and walk the links from there** ([[the-index-is-a-map-not-a-catalogue]]). A pointer at
a page is a better instrument for that than a tag, which is an instrument for finding a set.

## Why it was not taken

1. **It plugs the leak and drains nothing.** `vault` stays at **51 pages at `2036d98`** until
   something re-cuts it. Every entry added from that day forward would be cheaper, and not one
   existing page would be reclassified.
2. **Folder-first narrowing, shipped the same day, shrinks the problem it solves**
   ([[the-folder-is-the-first-narrowing]]). A word that reaches too much is a smaller failure once
   the search runs inside one folder of `wiki/` — and the alias list is consulted *after* the
   folder and the filenames, not before them.
3. **A dictionary whose entries point at pages drifts toward being a catalogue of every page**,
   which is precisely what `index.md` in this vault refuses to be
   ([[the-index-is-a-map-not-a-catalogue]]) — and the refusal's own argument, that a second copy
   diverges, applies here word for word. The boundary that would prevent the drift — *only where a
   tag genuinely cannot carry the word* — is a soft rule, and this store has watched soft rules
   rot: `index.md` grew 4.2× while obeying the letter of its own growth prohibition.

## The known cost if it is ever taken

**An alias pointing at a page couples the dictionary to a filename, and a rename breaks it
silently** — the same class of failure as seventeen pages citing `vault/raw/handoffs/...` after the
vault was renamed, which nothing noticed ([[vault-scripts]]).

**That one is checkable, and the machinery already exists.** Rule 11 of `vault-check.sh` requires
every path in a page's `sources:` to resolve, and rule 4 requires every `[[wikilink]]` to resolve
to a non-empty file. A dictionary target would be one more thing in the same pass, written to the
same idiom, and it must be built **with** the feature rather than after it — an unchecked pointer
reads as provenance and is not.

## What it would oblige

- **A grammar for a target**, since `word → tag` is currently implicit in the entry's shape and a
  reader distinguishes nothing today;
- **the check above**, refusing a target that resolves to nothing;
- **a stated boundary** for when a page target is legitimate, knowing it is soft, plus whatever
  measurement would show the drift starting — a count of page-targeted entries against pages would
  do what bytes-against-pages did for `index.md`.

**Nothing here is decided**, and there is no decision page behind it: the design is the owner's, the
reasons against it are the session's, and it stands until it is built or refused
([[proposals-are-a-folder-not-a-status]]).
