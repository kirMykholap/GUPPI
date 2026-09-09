---
title: "`Links:` is filled by a script from the body's wikilinks, and the checks read the field instead of the whole text"
type: proposal
status: refused
authority: links-field-design
basis: human
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-archive-becomes-history-and-three-refusals-land/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md", "scripts/vault-archive.sh", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "[[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]]"]
decided_by: [[the-links-field-and-the-script-that-would-fill-it-are-refused]]
tags: [vault, harness, record-schema]
---

# What would be built

**The design is the owner's, given whole in one sentence on 2026-08-23** — a script reads every
`[[wikilink]]` in a page's body and writes them into a frontmatter field, and the checks that want
the links read that field. The field is `Links:` rather than `sources:`, because the two meanings
may not share a line ([[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]]).

**Three pieces, in this order:**

1. **The field is admitted.** `Links:` joins the legal key set in every folder's `_schema.yaml`,
   the way any field does ([[the-per-folder-frontmatter-schema]],
   [[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).
2. **A writer fills it**, over `wiki/` and `archive/`, idempotently, from the body alone. It is the
   same shape as `scripts/vault-inject.sh`: a generator whose output is compared rather than
   trusted, so the check can ask by running the writer
   ([[a-check-asks-by-running-the-writer-it-checks]]).
3. **The readers switch.** The archive precondition stops matching a slug as a plain string and
   asks the field; anything else that counts inbound links does the same
   ([[vault-archive-sh]]).

# What it buys

**An exact answer to *who points at this page*.** Today there are two inexact ones in a single
script and they disagree: `pages_citing` matches a `sources:` path and misses a wikilink, and the
archive precondition matches a bare slug anywhere and cannot tell a pointer from a mention. On
2026-08-23 the first reported `cited by 0 page(s)` about a page five live pages name.

**And the orphan question becomes decidable.** A page carrying `status: implemented` waits in
`wiki/` until something names it; with a field, the advisory that lists the pages still waiting is
a one-line sweep rather than a grep over the corpus
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]).

# What is open

- **Whether `archive/` pages carry it.** A link *into* the archive is what makes an archived page
  reachable, and a link *out of* one is history pointing at history
  ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).
- **Whether a bare slug mention counts.** The field is filled from `[[wikilinks]]`, and a real
  pointer written as a bare slug would stop counting the day the field replaces the string match
  ([[a-bare-slug-mention-is-an-inbound-link-that-no-wikilink-counter-sees]]). That is a narrowing
  of what *cited* means, and it is a decision rather than an implementation detail.
- **Whether the field is per-page or a generated register.** A generated file has already been
  rejected once in this store for a list of pages, on the ground that a query cannot go stale
  ([[the-page-list-is-a-query-not-a-generated-file]]); the counter-argument here is that the writer
  is the check.
- **What it costs the diff.** Every page gains a frontmatter line that changes whenever its body's
  links change, so a prose edit now moves frontmatter.

# Why it is a proposal and not a task

**It is designed and nothing is built** — no schema declares the key, no script writes it, no check
reads it. The consequence of leaving it is written down where it bites: the archive precondition
stays a string match, safe on a measurement over 530 slugs rather than by construction.

# The field is legal in all six schemas and no script writes it — 2026-08-23, in the session after this page was written

**Half of this proposal landed and it is the half that changes nothing on its own.** `Links:` is
declared `optional` in every one of the six `wiki/*/_schema.yaml` files, so a page may carry it and
the gate will not object. **No page carries it and nothing fills it.**

**The writer was ruled to be a script rather than an agent, and the ground is the owner's own:**

> **owner: значет нужен скрипт, добавляем в спринт**

**An agent filling a field by reading its own page is a field that drifts** — it is written once, by
whoever happened to be there, and nothing re-reads it when the body changes. A script re-derives it
from the text every time it runs, which is the same property the injector has and the reason a
generated thing is trusted here at all
([[a-check-asks-by-running-the-writer-it-checks]], [[the-harness-is-compiled-not-maintained]]).

**It is optional everywhere and is promoted when the count of pages lacking it reaches zero** — the
order `basis:`, `authority:` and `decided_by:` all took
([[the-unknown-key-verdict-orders-a-schema-change-ahead-of-the-page-that-uses-the-field]]).

**So the open questions above are unchanged.** Nothing here decides what a script does with a
wikilink inside a code span, inside a quotation, or inside frontmatter.

# Refused — 2026-08-30

**The owner refused it after looking at his own graph.** Obsidian draws an edge from a
`[[wikilink]]` written in the body, which is what he saw on screen — so the reader this proposal
names first was already served, and the field would have cached something the tool derives for
itself. His words: *«Если это так работает, то тогда строить скрипт для поля Links не имеет
смысла, ровно как и это поле»*.

**The second reader falls to a measurement rather than to an argument.** An agent that wants one
page's outgoing links runs a single grep over that one file and gets them without loading the page
into context at all. So the saving the field was for — walking the graph without opening pages —
was available the whole time and needed no field, no script and no schema key.

**What was true and stays true** is everything above about *how* such a script would have to work,
and it is kept here rather than deleted, because the next person to propose caching a derived
property will need the reason this one failed: **it cached something two readers already computed
more cheaply than the cache.**

**`Links:` was removed from all six `_schema.yaml` files in the same change**, and no page ever
carried it — zero under `wiki/` and zero under `archive/`, measured that day. `decided_by:` above
now names the decision that refused this page, which is what
`scripts/vault-archive.sh` reads before releasing it; the decision that *caused* it moved into
`sources:` in the same edit rather than being dropped
([[a-decided-by-target-in-the-archive-is-kept-and-becomes-a-lesson-candidate]]).

# `decided_by:` was repointed at the ingest — 2026-08-30

**It named [[the-cleanup-suspends-the-rules-that-would-refuse-it]] when this page was written.** That
decision repeals four rules and says nothing about `Links:`; it was the only new decision the session
had, and the archiver refuses to release a refused proposal whose `decided_by:` is empty, so the field
was filled with the nearest page that existed.

**It now names [[the-links-field-and-the-script-that-would-fill-it-are-refused]]**, which is the
decision carrying the owner's words and the rejected alternative. Nothing else on this page changed.

**And this page is still in `wiki/proposals/`.** A refused proposal belongs in `archive/`;
`scripts/vault-archive.sh` is what moves it and it has not run.
