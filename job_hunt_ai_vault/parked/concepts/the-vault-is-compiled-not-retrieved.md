---
title: "The store is compiled, not retrieved — which is what makes grep plus links enough"
type: concept
status: current
authority: compilation-vs-retrieval
basis: human
sprint: S1
created: 2026-08-15
sources: ["raw/notes/2026-08-13-owners-note-second-brain-info.md", ".claude/agents/vault-librarian.md", ".claude/skills/ingest/SKILL.md"]
tags: [vault, retrieval]
---

# Compilation, not RAG

The owner's method note opens on this and calls it the philosophy: *«В отличие от стандартных
систем RAG …, данная система основана на компиляции»*. It is the one claim in that note from which
most of the rest of the vault's shape follows, so it is worth stating on its own.

**A RAG store answers a question by searching the raw material afresh every time.** The raw
material never changes shape; the retrieval does all the work; and two questions about the same
subject each pay for the same reading. **A compiled store answers it by having already done the
reading.** The raw material is turned, once, into pages that state the conclusion — and the next
question reads a page rather than a transcript.

Four consequences, all of them visible in the store as it stands:

- **knowledge is fused in, not appended.** «Вплавляется» is the note's word. A new decision does
  not arrive as another document beside the old one: it edits the page that carried the old claim,
  or it supersedes it and the retired page names its successor. That is why nothing is deleted and
  why `superseded_by:` is written in both directions;
- **synthesis, not summarisation.** The librarian's own definition says it in those words —
  *«Synthesise. Never dump page contents»* — and a page's own wording is quoted only where the
  wording carries the weight, a measured number or the exact boundary of a rule;
- **the links are the structure**, because a compiled store is only as good as the walk between
  its pages. An orphan is therefore a defect and not an untidiness ([[vault-scripts]] rule 5);
- **an agent writes it for an agent to read.** The note says so, and the whole retrieval design
  assumes it: an isolated context that greps, opens five pages and is thrown away.

## Why this is the argument under the retrieval decisions, and not a restatement of them

**It is what makes grep plus links sufficient at this size.** The cost of a query is the size of
the *question*, not of the corpus, because the compilation already happened
([[the-index-is-a-map-not-a-catalogue]]). That is a property of a compiled store; a RAG store over
the same material would have to be tuned instead.

It also fixes what vectors would be *for*, if they arrive: **not to find the answer but to find the
page**, over a corpus that has already been compiled. [[vectors-are-deferred-not-rejected]] is the
decision and states its own reopening condition; this page is only the reason the deferral is
cheap.

## Where it is not built, and it is worth knowing which half

The compilation is real and mechanical — `/ingest` splits a source into units and every unit gets
a verdict ([[ingest-is-units-and-verdicts]]), so "was this document compiled" is a question a
script answers. **What no script can answer is whether the compiled page says what the source
said.** Coverage is not fidelity, and a page compiled from a note of *intent* can be well-formed,
sourced and false ([[an-intent-note-compiled-as-testimony-describes-things-nobody-built]]).

So: compiled, yes; and the compiler is checked on its accounting and trusted on its reading.
