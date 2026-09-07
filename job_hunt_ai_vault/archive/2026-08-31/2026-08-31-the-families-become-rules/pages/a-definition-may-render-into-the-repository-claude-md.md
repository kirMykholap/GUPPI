---
title: "A definition may render into the repository's `CLAUDE.md`, not only an imperative or a sourced assertion"
type: decision
status: archived
authority: renderable-shapes
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md"]
tags: [harness, record-schema, vault]
---

# Decided by the owner on 2026-08-18: yes

**Three shapes may now reach that file through a region, in the order he ruled them:**

| Shape | Ruled | Where it comes from |
|---|---|---|
| an imperative not held by a test | 2026-08-17 | `wiki/rules/` ([[the-harness-is-compiled-not-maintained]]) |
| a **sourced** assertion | 2026-08-17 | any page with `governs:` ([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]) |
| a **definition** | 2026-08-18 | any page with `governs:` |

**This is the plain reading of the second rather than an extension of it.** Its stated test is *is
there a page behind this paragraph*, not *is this a statement* — so a paragraph that defines a word
passes it the same way a fact about the tree does. The question was left open on the retired
[[the-marker-carries-a-type-and-governs-is-read-as-a-field]], which named the definition of
*retrospective* as the case that forced it.

## What it obliges

- **Three records become renderable**: the definition of *retrospective*, the project description,
  and the map. The map is the first of them built
  ([[the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint]]); the other two are on
  [[what-the-harness-build-waits-on]].
- **None of them may come from `wiki/rules/`.** That folder's admission test is *imperative and not
  enforced by a test*, and admitting a definition would empty it
  ([[rules-becomes-a-type-of-its-own]]). A definition renders from the folder its record belongs
  to, which is what makes the type in the marker load-bearing
  ([[a-marker-with-its-type-is-a-complete-address]]).

## Why the word *retrospective* is the case that made it urgent

The word meant two different things here for three days — the end of a session, and the
sprint-level ritual — and that ambiguity put two live, contradictory answers into this corpus about
when `/ingest` runs ([[ingest-runs-after-handoff-at-the-end-of-a-session]],
[[the-end-of-a-session-is-a-retrospective]]). The definition is what stops it happening again, and
until this ruling it had nowhere to render from.

## Executed on 2026-08-18 at `46b7c76`, and the move was verbatim

**The definition of *retrospective* renders**: it is the eleventh region in the repository's
`CLAUDE.md` and the second rendered from outside `wiki/rules/`
([[a-retrospective-is-a-sessions-end-not-a-sprints-ritual]]).

**The move was verbatim and was proved rather than asserted.** The slice was cut out of `CLAUDE.md`
with `sed` rather than retyped, both sides hashing the same, and the diff of the destination is
three insertions and no deletions — the two markers and the separator
([[the-injector-writes-the-separator-inside-the-region]]).

**Decided with it, and the rejections are worth keeping:** rewording while moving was refused,
because a change nobody decided is invisible in the diff of a move; deleting the paragraph instead
of rendering it was refused, because then no page owns the question. **What it obliges: the page is
the only place that text is corrected** ([[the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison]]).

**It is the first region whose source paragraph already stood in the destination**, so the prose was
deleted only after the render was verified present — the ratified order
([[the-maps-region-replaces-the-prose-it-duplicated]],
[[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).
