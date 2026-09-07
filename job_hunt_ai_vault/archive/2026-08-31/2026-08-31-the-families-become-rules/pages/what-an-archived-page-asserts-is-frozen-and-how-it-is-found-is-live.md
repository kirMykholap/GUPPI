---
title: "What an archived page asserts is frozen, and how it is found is live"
type: decision
status: archived
authority: archive-rule-reach
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
supersedes: [[what-archive-is-stays-undecided-and-the-rules-reading-wiki-disagree-about-it]]
sources: ["archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "scripts/vault-check.sh", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [record-schema, vault, harness]
---

# The ruling, 2026-08-19, and it is neither of the two options it was asked with

> **owner: what an archived page *asserts* is frozen; how it is *found* is live.**

**Rejected: `archive/` as frozen testimony like `raw/`** ([[raw-holds-testimony-and-artefacts-are-frozen]]).
**Rejected: `archive/` as live retired content.** The question was framed as a choice between those
two and the answer refuses the frame: the two rules that disagree about `archive/` are not both
answered by one widening.

**The value of the ruling is that it is a predicate rather than a verdict.** Every rule written
against `wiki/` from now on is answered by asking **which of the two halves it governs**, instead of
inheriting the question the way rules 6 and 10 both did.

# How the two rules fall out of it

| rule | which half | verdict |
|---|---|---|
| rule 6 — every tag on a page is defined in `tags.md` | findability | **widens to `archive/`** |
| rule 10 — no title or filename carries a measurable quantity | what the page asserts | **does not widen** |

**Rule 6 widens** because an archived page carrying a word the dictionary no longer defines is a
real defect — the page becomes unreachable through the one handle a reader has for it. **Found live**
rather than reasoned: the `schema` tag split would have left three archived pages holding a word that
no longer exists, and it was caught because the librarian went looking, not because anything printed
([[the-schema-tag-splits-into-db-schema-and-record-schema]]).

**Rule 10 does not widen** because a title is what the page asserts.
[[the-wiki-has-five-folders-and-tasks-is-not-one]] is archived **because** its count went stale;
repairing the title now erases the evidence of why the page was retired
([[the-no-quantity-rule-reads-the-title-and-the-filename-and-never-the-body]]).

# Recorded and not built

**The owner deferred the check change** so it would not eat the session's chosen body of work. Rule 6
still reads `wiki/` only.

*Consequence while it stands:* an archived page carrying a tag the dictionary does not define passes
in silence, which is how the `schema` split nearly stranded three of them.

*The size of the change is already measured*, on the page this one supersedes: four archived pages
carry a count today, three were touched by the tag rename. That measurement is what makes this a
one-sitting change rather than an investigation.

## Applied 2026-08-20, and it is what settled a question that had been open

**The owner used this page's predicate to rule that a path move rewrites `archive/`**
([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]): a `sources:` line is an **address**,
so it is *how a page is found*, and it moves.

**And the same predicate does not reach `log.md`**, which is different in kind — what a log entry
records is not only what happened but **how it was recorded**, so a wrong entry is evidence and
correcting it destroys the evidence.

**Measured on the day it was applied:** the probe scaffolding was cited by nine pages, two of them
in `archive/`. **Rule 2 of the gate reads `wiki/` only, so an archived citation never reddens — it
dangles silently.** That is the practical reason the question could not be left open.

# The predicate meets an immutable source, and there it decides against the sweep — 2026-08-23

**Step 12 of `/ingest` moved a journal from `raw/` into `archive/` and the gate went red on one
line of it.** The journal quotes the owner asking for a script that reads *все `[[викиссылки]]`
внутри записи*, and rule 5's link sweep reads `wiki/` and `archive/` alike. In `raw/` that line was
outside the sweep; in `archive/` it is a broken wikilink, and the gate exits 1 on it.

**Nothing about the journal may be changed to fix it.** `raw/` is immutable and an archived journal
is the same artefact moved; the coverage sidecar is keyed by its line numbers, and a sentence a
source asserted is never rewritten ([[raw-holds-testimony-and-artefacts-are-frozen]],
[[fidelity-to-a-source-and-fidelity-to-the-tree]]).

**Read through this page's own predicate, the sweep is on the wrong side of it.** A `[[wikilink]]`
inside a **quotation** is not *how the document is found*: nobody navigates by it, it addresses
nothing, and the owner was naming the syntax rather than pointing at a page. It is part of what the
document **asserts**, and what a document asserts is frozen. **Rule 5 widened to `archive/` for
pages, where a link is an address; a journal's links are testimony.**

**So the move was reversed and the journal is back in `raw/` with its sidecar**, the twelve
`sources:` lines rewritten back with the script's own narrowing — `^sources:` only, literal, `wiki/`
and `archive/` only — and the gate exits 0. **The ingest is complete and its source is not
archived**, which is a stated shortfall rather than a silent one.

**The repair is a change to `scripts/vault-check.sh` and is the session's**
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]). The shape it points at: the
link sweep's page set should be the pages, not every markdown file under `archive/` — a journal, a
plan, a spec and a note are testimony, and only `archive/*/*/pages/` holds records that address
each other. **Until it lands, every journal quoting wikilink syntax is unarchivable**, and the one
of 2026-08-23 is the first.

**The wiki page that compiles the same quotation is unaffected and shows why**: it writes his
`[[викиссылки]]` inside a code span, which the sweep strips, and says so in a note beside it
([[a-links-field-carries-the-bodys-wikilinks-and-sources-keeps-provenance]]). **A page may be
marked up and a source may not** — which is the same frozen-versus-live line this page draws, seen
from the other end.

# The repair landed, and it follows the four RAW kinds rather than the whole of `archive/` — 2026-08-23, later the same day

**`scripts/vault-check.sh` now excludes `handoffs`, `plans`, `specs` and `notes` under `archive/`
from the set whose outbound links must resolve, and leaves them resolvable as targets.** That is
exactly the shape the section above named as owed, and it is the change that unblocked the archive
step the previous ingest could not finish.

**The exemption follows the file rather than the directory**, on the ground the `raw/` exclusion
already states: archiving does not make a file mutable. A journal quoting `[[викиссылки]]` as an
illustration is testimony in `raw/` and is still testimony after it moves.

## It was proved in both directions, and the second direction is the one that matters

| what was planted | what the gate did |
|---|---|
| a **journal** under `archive/` with an unresolvable wikilink | exits 0 |
| a retired **page** under `archive/` with the same wikilink | red |

**Without the second half the pair would only prove the sweep got quieter**, which is the direction
a defect hides in: an exclusion written too wide and a correct exclusion look identical from the
green side ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
[[a-green-gate-can-be-no-evidence-about-the-branch-just-changed]]).

**It has a selftest case in both directions**, so the reading survives the next change to that sweep
([[a-local-proof-that-a-new-verdict-fires-is-not-a-regression-run-of-the-old-ones]]).

**Decided and applied after the previous ingest had closed**, so no page written that day records
the repair itself — this section is the first.
