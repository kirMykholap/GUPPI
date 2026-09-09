---
title: "A marker is an address, and with the type in it the address is complete"
type: concept
status: current
authority: marker-as-address
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check.sh"]
tags: [harness, retrieval, vault]
---

# What a marker is, read as an address rather than as a label

`<!-- rule: some-slug -->` is not a name for a region. **It is a lookup**: the check resolves it to
`wiki/rules/some-slug.md` and reddens if that file is absent. The region's content is whatever the page
at that path says.

**Read that way, the present form is a partial address.** It carries the slug and hard-codes the folder,
so it resolves only while every renderable record lives in one folder. The moment a non-rule renders,
the hard-coded half is wrong ([[governs-becomes-a-property-of-any-page]]).

**With the type in it, the address is complete**: `<!-- entity: some-slug -->` resolves to exactly one
path, `wiki/entities/some-slug.md`, and nothing else has to be known
([[the-marker-carries-the-records-type]]).

## The objection that was withdrawn, and why the withdrawal is the useful part

The first objection was that this puts a **mutable field into an address** — the shape that makes a
rename expensive and that this project already pays for on filenames
([[a-rewriter-must-be-paired-with-a-detector]]).

**It was withdrawn on a fact about this vault: the type *is* the folder, and pages do not move between
folders.** `vault-check.sh` rule 2 requires `type:` to agree with the directory, so the field cannot
drift from the path without the gate going red. A field that cannot change independently of the address
is not a mutable component of it.

**And the design removes a lookup rather than adding a copy.** A field-driven injector that did not
carry the type in the marker would have to search all six folders for the slug — a cross-folder lookup
per region, and an ambiguity to resolve whenever two folders hold the same basename, which has already
happened once on purpose ([[the-slice-execution-rule-migrates-first]]).

## The general shape

**An address that omits a component is an address that only works while the omitted component has one
value.** The vault has met this before from the other side: `governs:` is read as a path from the
repository root and from nothing else, because a path meaning two files renders into the wrong one
([[governs-is-a-path-from-the-repository-root]]). Both are the same rule — **resolve narrowly, or do
not resolve**.

# Built at `e83ce28`, and the address is computed exactly once

*(This page was `basis: inference` while the design was unbuilt. It is `basis: code` from
2026-08-18.)*

**The type word is the singular** ([[the-marker-carries-the-records-type]]), so
`<!-- concept: some-slug -->` resolves to `wiki/concepts/some-slug.md`.

**The scanner computes `folder/slug` and everything downstream joins on it and opens it as a path.**
That is the property worth stating separately from the design: a second place computing the folder
from the word would be a second answer waiting to differ, and the region address, the pair table it
joins against, and the file the injector opens are all the same string
([[the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison]],
[[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]).

**The legal set of words is swept off the tree rather than listed**, so the address space is defined
by which folders exist ([[the-type-words-are-swept-off-the-tree-and-never-listed]]).

**The first address to point outside `wiki/rules/`** is the map's
([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]],
[[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]).
