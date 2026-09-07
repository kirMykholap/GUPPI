---
title: "The index is a map, not a catalogue, because retrieval is grep plus links"
type: concept
status: current
authority: index-purpose
basis: inference
sprint: S0
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md", "raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "scripts/vault-catalogue.sh"]
tags: [retrieval, vault]
---

# A map, not a catalogue

An earlier draft made `index.md` a table with one row per page, carrying `authority` and `status`.
It was withdrawn, and for the more fundamental of its two reasons: **it is a second copy of what
the files already say, and second copies diverge.** (The other: at a thousand pages that table
becomes the problem it was meant to solve.) A `grep` derives the same answer, and deriving is
cheaper than maintaining.

## Whose conclusion this is — and what it overrode

**The owner's own note asked for the opposite.** Both of his working notes on the method say
«wiki/index.md — автоматически обновляемый каталог всех страниц»: an automatically maintained
catalogue of every page. This page is the reasoning for not building that, and the spec's decision
table records the row — "`index.md` is a map, not a per-page table | a per-page table is a second
copy, and it grows; grep plus links does not" — **without owner attribution**, unlike the rows
beside it that carry "owner's call".

So this is the designer's conclusion, not his, and it is marked `basis: inference` for that reason;
it said `human` until 2026-08-13, which would have let it outrank the note it overrode. The
argument may still be the right one — but "the owner asked for a catalogue and got a map" is a
thing he is entitled to revisit, and a `human` marking would have hidden that there was anything to
revisit.

**One of the two notes has now been compiled, on 2026-08-14** — the instructions one, line by line,
in [[the-owners-instructions-note-and-what-was-built-from-it]]. The reading above survived the
accounting unchanged: the note asks for the catalogue in the same words, and nothing later in it
argues for a map. *(The paragraph this replaced said both notes were uningested and that nothing in
the vault had been checked against them. The method note still has not been.)*

**Both are compiled as of 2026-08-15** — [[the-owners-method-note-and-what-was-built-from-it]] —
and the sentence above survives the second accounting too, verbatim: line 31 of the method note and
line 14 of the instructions note ask for the catalogue in identical words, and neither argues
anywhere for a map. *(The clause "the method note still has not been" was true when it was written
and is not now.)*

> [!NOTE] CONTRADICTION — RESOLVED 2026-08-15 BY THE OWNER
> **What stood here from 2026-08-14 to 2026-08-15**, and is kept because a resolved contradiction
> is still a thing that happened: *«Catalogue or map — unresolved. The owner's instructions note
> ([[the-owners-instructions-note-and-what-was-built-from-it]]) asks for «автоматически обновляемый
> каталог всех страниц» and is `basis: human`; this page declines to build one and is
> `basis: inference`. On the ranking the schema itself defines, the source outranks the page, and
> the page is the one that was built. The librarian does not choose between them, and asking in
> chat would leave no artefact — this marking is the artefact. Both pages carry it.»*
>
> **How it was settled: by building the option neither page had considered.** The catalogue exists
> and is *generated* — `scripts/vault-catalogue.sh` writes `catalogue.md` from the frontmatter of
> every page, and rule 9 of `vault-check.sh` fails while that file differs from what the script
> produces. **The argument this page rests on is that a second copy diverges; it does not reach a
> copy nobody types.** The map keeps its shape and the reasoning below stands unaltered — what was
> wrong was only the inference that the ask had to be refused.
> [[the-catalogue-is-generated-not-maintained]] is the decision, `b58ec48` the commit.
>
> **Resolved by the owner, which is the only party that may resolve one**
> ([[the-librarian-writes-unattended]]). Where it lives rather than what it holds was settled the
> same day and separately: [[index-md-stays-at-the-vault-root]].

## What retrieval actually is

Grep the corpus for the question's terms, open the hits, then **follow the `[[links]]` out of
whatever was found**. The cost is the size of the *query*, not the size of the corpus, and it does
not grow.

**You do not need to find every relevant page — only one, and walk from there.** That is what
makes wikilinks load-bearing rather than decorative, and it is why an orphan page is a defect: a
page nothing links to is reachable only by an exact grep hit, which is the one retrieval path we
know fails across languages. `vault-check.sh` refuses orphans for that reason
([[vault-scripts]]).

## So `index.md` holds only what grep cannot supply

The categories and what belongs in each; the naming convention, so grep lands; where the current
sprint's boundary is; and links to a few **hub pages**, the entry points into large subjects.

**A hundred new pages do not lengthen it.** A fifth category would, and categories appear about
once a year.

## The rule is being obeyed and the file is failing anyway — measured 2026-08-15

The first `/vault-lint` checked `index.md` against exactly the sentence above and found **no
per-page row**, which is the thing this page was written against. And it found the file had grown
**883 → 3750 bytes, 4.2×, while the corpus grew 29 → 108 pages, 3.7×.** Near-proportional growth is
what *"a hundred new pages do not lengthen it"* forbids, so the prohibition is being kept in the
letter and broken in the outcome.

Two components, and neither is a per-page row:

- **hub rows 0 → 13.** Each is defensible on its own, which is how this failure always arrives.
- **two five-line paragraphs restating [[proposals-are-a-folder-not-a-status]] and
  [[the-catalogue-is-generated-not-maintained]]** instead of linking them — a second copy of a
  page's substance, in the file whose founding argument is that second copies diverge.

**The prediction above also has a measured error.** "A fifth category would [lengthen it], and
categories appear about once a year": the fifth arrived **two days later**. The mechanism held and
the rate did not — and *a rate nobody re-measures is how a ceiling stops being one.*

**Nothing was removed.** Trimming a map is deleting text and the map's shape is the owner's, so it
is one of the six findings owed to him: [[the-audits-findings-are-owed-to-the-owner]]. What
this page can say without him is the reading: **the failure this file was designed against arrives
by prose rather than by rows**, and a growth rule stated as "no per-page rows" does not catch it.
Bytes against pages is the measurement that does.

## The cost, stated honestly

Grep finds only what shares vocabulary with the question. Ask about «внешний вид» when the page is
called `vacancy-table-layout` and you miss — which has already happened once, in the vault's first
recorded miss. Three things carry that weight, and all three are structural rather than cosmetic:
descriptive filenames, the links, and the dictionary's aliases
([[aliases-carry-the-question-across-languages]]).

## The resolution above was itself superseded on 2026-08-17

**The generated file is gone.** `catalogue.md` is deleted, rule 9 is retired, and the list of every
page is `pages.base` — an Obsidian base, evaluated when it is opened
([[pages-base]], [[the-page-list-is-a-query-not-a-generated-file]]).

**Nothing in this page's argument moves.** It rested on *a second copy of what the files already say
diverges*, and the blockquote above already recorded that the argument does not reach a copy nobody
types. A query is the limit case of that: there is no copy at all. The two citations of
[[the-catalogue-is-generated-not-maintained]] above are left where they stand, because both are
about how the question was **settled on 2026-08-15**, which is what that page is now kept for.
