---
title: "`entities/` will describe the application, one page per package, after the detector that keeps it honest"
type: decision
status: current
authority: entity-coverage
binding: deferral
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [vault, architecture]
---

# Decided 2026-08-16: yes, and not yet

**The application gets entity pages** — the codebase, the harness, the pipeline and the tests.
Today all fifteen pages in `entities/` describe tooling and environment and **none describes the
application**, while `src/jobhunt/` is 42 files under five packages with 40 test files. That gap is
already a row of [[structure-work-agreed-and-not-executed]].

**Sequenced after `asserts:` and the staleness detector exist.** Before them it is a second "Where
things are" — the block of the repository's `CLAUDE.md` that has already gone stale, most recently
inside one hour of a file move — and it would rot on exactly that schedule
([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

## The objection, and why it is answered rather than dismissed

**A module map has no source in `raw/`**, which is the same ground `tasks/` was refused on
([[the-wiki-has-five-folders-and-tasks-is-not-one]]), and a hand-maintained map is the artefact
this project has watched rot.

**Two mechanisms answer it and neither would answer alone.** `asserts:` catches the structure
moving ([[asserts-is-a-closed-predicate-set-with-a-flat-syntax]]); `sources:` plus the staleness
detector flags the prose when the code it describes gets a commit
([[a-staleness-detector-from-updated-against-a-pages-sources]]). For pages about the application
that detector's coverage is **total**, because their sources are code — which is the one part of
the corpus where the instrument has no blind half.

## Three bounds, so it stays a map and not a second codebase

1. **One page per package, not per file.**
2. **Written when that area is worked on**, never as one cartography pass.
3. **No coverage numbers** — name the test files, which `asserts:` can check, because a stated
  count drifts from the list it heads ([[a-stated-count-drifts-from-the-list-it-heads]]).

The reconciliation this would finally make possible is
[[reconciling-entities-against-the-decision-register]].

# What this page does NOT block — measured 2026-08-18

**It gates *one page per package* of `src/jobhunt/` behind `asserts:`. It does not gate a
one-paragraph description of what the tool is.**

The project description has been deferred twice with this page cited as its blocker, and the
citation is wider than the page. A description of the product — what it collects, from where, and
what the two pages are for — asserts nothing about the module layout, so **none of the three bounds
above applies to it** and neither does the objection they answer: there is no map to rot.

**Consequence of not writing this narrowing down**, and it is why it is written here: the next
session reads the blocker widely again and defers again
([[what-the-harness-build-waits-on]]). **The folder for that description is to be decided when it is
built**, and it may render, since a definition and a sourced assertion both may
([[a-definition-may-render-into-the-repository-claude-md]],
[[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]).

**What still waits on `asserts:` is exactly what this page's title says**: the per-package pages
([[asserts-is-a-closed-predicate-set-with-a-flat-syntax]]).
