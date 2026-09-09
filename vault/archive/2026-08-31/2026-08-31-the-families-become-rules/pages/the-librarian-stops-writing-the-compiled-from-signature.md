---
title: "The librarian stops writing the *Compiled from* signature, because `sources:` already carries it"
type: decision
status: archived
authority: page-provenance-signature
basis: human
binding: prohibition
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/handoffs/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate.md"]
tags: [vault, process, harness]
---

# The ruling

> **owner:** «Полностью с тобой согласен. Отметь плиз»

Answering the session's finding: *"настоящая правка дешевле и в другом месте: librarian должен
перестать писать эту подпись вообще; `sources:` уже несёт то же самое, машинно и точно, а рукописная
копия расходится с оригиналом"*.

**No page written from here on carries a closing line of the form
`*(Compiled from raw/handoffs/….md.)*`.** Pages that already carry one keep it.

# What it was and why it goes

**It was a hand-typed copy of `sources:`.** The frontmatter field is written by the same pass, is
machine-readable, holds any number of entries, and is what every script here reads. The signature
held one path, in prose, at the foot of the page.

**A copy drifts from what it copies, and this one drifted in a day.** When `raw/handoffs/` was swept
into `archive/`, the `sources:` lines were rewritten mechanically — 584 of them across 22 journals —
and the signatures were not. **183 lines of prose in 124 pages now name a path that moved**, of which
111 are these signatures ([[a-copied-list-drifts-and-a-sweep-cannot]],
[[raw-handoffs-is-swept-whole-today-and-the-forward-only-clause-is-overturned]]).

# The rejected alternative

**Sweep the 183 stale lines.** Refused on the same day and for a reason of its own: `sed` cannot tell
an address from a quotation, 72 of the lines are prose inside a claim, and part of the population is
**correct as written** — the address moved, not the claim
([[the-prose-path-detector-is-refused-on-its-own-measurement]]).

**So the repair is at the writer and not at the text.** Stop producing the copy; leave what exists.

# What it obliges

**`sources:` has to be right, because nothing else says where a page came from.** It was always the
authority; the signature made it look like there were two.

**A reader who wants the source of an existing page reads its frontmatter.** A page with a signature
and a `sources:` line that disagree is a page whose signature is stale, and the frontmatter wins
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

**Nothing renders this into the librarian's own instructions.** It is written here and nowhere else,
so a librarian that has not read this page will keep typing the signature — which is the general
weakness of an agent-facing rule that no `wiki/rules/` page carries
([[a-rule-reaches-a-session-by-several-routes-and-only-one-transition-had-a-gate]]).
