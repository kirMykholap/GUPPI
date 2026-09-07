---
title: "Vectors are deferred, not rejected — there is nothing to tune them on yet"
type: decision
status: current
authority: vector-retrieval
binding: deferral
basis: human
sprint: S0
decided: 2026-08-13
created: 2026-08-13
sources: ["docs/superpowers/specs/2026-08-13-second-brain-design.md", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md"]
tags: [retrieval, architecture]
---

# Vectors are deferred, not rejected

**The deferral is cheap because the store is compiled** ([[the-vault-is-compiled-not-retrieved]]):
the reading has already been done, so what a vector would buy here is a way to *find the page*, not
a way to answer the question. That is the frame the owner's method note states outright — «в
отличие от стандартных систем RAG … основана на компиляции» — and it is why the alternative below
is grep with tags rather than a worse index.

**Decided on 2026-08-13, and reframed mid-session** after the owner objected that the first draft
undersold them. The distinction is the whole point: "not yet, and here is what would reopen it" is
a different obligation from "no".

## Why not now

1. **The corpus does not exist.** At a few dozen pages, grep with tags is genuinely sufficient and
   vectors would be optimising nothing.
2. **We do not yet know how the questions get asked**, and that governs both the model and the
   granularity. Building the index now sets those guesses in concrete.
3. **The miss log is the data** that would make the eventual choice something other than a guess.
   One data point exists so far, and it was closed by a dictionary entry rather than by an index
   — see [[aliases-carry-the-question-across-languages]].

**Deferring costs nothing, because the layout is already vector-ready.** One entity per page makes
a page the ideal chunk: no splitting strategy, one vector per page over `title` + `tags` + body.
That fell out of the atomicity rule for free. The database side is equally ready and equally
unstarted: [[pgvector-extension-not-enabled]].

## Two claims of the first draft were wrong, and are corrected here

- **The token argument holds for the main context, not for the librarian's.** The main session
  receives 500–1500 tokens either way. The librarian's own context is different — grep returns
  paths, and the cost lies in the pages it *opens*, including the ones a word matched by accident.
  But its tokens are the cheap ones: an isolated context that is thrown away. **The real argument
  is quality, not cost — a librarian that reads forty pages answers worse than one that reads
  five.**
- **The maintenance surface is smaller than the draft claimed.** At a few hundred pages there is
  no vector database: a numpy array and a full cosine is instant, and the index cannot go stale
  because ingest knows exactly which pages it wrote. The real cost is a local embedding model and
  its dependency, and that cost lands hardest on a future plugin — one needing a local model
  installs far less easily than one needing `ripgrep`.

## Vectors and tags are not alternatives

A **vector** answers *what resembles this question* — ranked, approximate, **with no boundary**:
you get top-k and cannot know whether k was enough. A **tag** answers *what belongs to this class*
— exact, enumerable, **complete**.

**The rule: vectors search, tags guarantee.** "What exists on this subject" is a vector question.
"Am I about to break something" needs enumeration, because the decision a plan violates may rank
twelfth when k is eight.

## What would reopen this

Misses in `log.md` of the kind an alias cannot close — a question that found nothing although the
page existed and shared no vocabulary with it. **That log is the evidence, for or against.**
