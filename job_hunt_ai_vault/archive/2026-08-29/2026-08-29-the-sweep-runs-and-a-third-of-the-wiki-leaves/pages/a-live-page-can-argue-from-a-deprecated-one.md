---
title: "A live page can argue from a deprecated one, and no rule catches it — a link into archive/ resolves perfectly"
type: lesson
status: archived
authority: archive-link-blindness
basis: code
sprint: S1
created: 2026-08-15
sources: ["scripts/vault-check.sh", "archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", "log.md"]
tags: [vault, retrieval]
---

# The link resolves, so nothing complains

`vault-check.sh` rule 4 fails a `[[wikilink]]` that resolves to nothing, or to an empty file. It
does not look at what it resolved **to**. A page in `archive/` is a real, non-empty file, so a
`current` page may cite a `deprecated` one as its ground and the gate stays green.

**Found by reading, in the first audit — 2026-08-15.** There is no mechanical trace of it: the
citation looks identical to a healthy one at every level a script here can see.

## Why it is worse than a broken link

A broken link is loud and is fixed in seconds. This one is silent and it **inverts the point of
supersession**. The whole retirement protocol exists so that a reader arriving at an outdated claim
is pushed forward to its successor:

1. successor gets `supersedes:`;
2. old page gets `status: deprecated` and `superseded_by:`;
3. old page moves to `archive/`.

The link is written in both directions *on purpose*, because a deprecated page that does not name
its successor is a dead end. **A live page linking backwards into `archive/` is that dead end
rebuilt from the other side**: the reader is walked from current knowledge into retired knowledge
with no marker at the boundary, and the deprecation notice arrives after they have already accepted
the argument.

There is one legitimate case, and it is narrow: quoting a deprecated page to answer *why did we
change this*. That is what the retired page is kept for. The failure is quoting it for what it
says, not for the fact that it was once said.

## What it would take to catch

Cheap, and not built: for every `[[link]]` in `wiki/`, resolve it and report when the target lives
under `archive/` — an advisory rather than an error, because of the legitimate case above. The
resolver already exists inside rule 4 and already knows both directories.

Recorded here rather than fixed, because adding a rule is not an ingest's act and this one belongs
with the rest of the audit's outcomes ([[the-audits-findings-are-owed-to-the-owner]]). Until it
exists, the discipline is the manual one: **before citing a page, look at which folder it is in.**

The same blindness, one level up, is [[vault-scripts]]'s `sources:` rule — a path that exists is
not a path that still holds the claim
([[fidelity-to-a-source-and-fidelity-to-the-tree]]).

## It happened again on 2026-08-17, and this time a write caused it

Retiring [[ingest-is-batched-at-the-retrospective]] left **four live citations arguing from an
archived page**: [[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]] row 6,
[[no-rule-reads-a-harness-file]] row 5, [[agent-round-trip-cost]] for the cost arithmetic, and
`tags.md` in a definition. **None is a broken link — `archive/` resolves — so the gate stayed
green.**

**The difference from the 2026-08-15 instance is the direction.** That one was *found* in a corpus
nobody had swept. This one was *created*, by a supersession performed correctly: the successor was
written, the old page deprecated and moved, and every inbound link was left pointing where it always
had. **A supersession is a link-rewriting event and nothing in this vault treats it as one**
([[a-rewriter-must-be-paired-with-a-detector]]).

Each of the four was annotated where it stands, rather than repointed, because two of them cite the
retired page for a claim that survives — the cost arithmetic, and a divergence whose other half is
still true. **Annotating beside the citation is the only move that keeps the argument readable**;
repointing would have made the rows say something their sources never said.

Until the advisory proposed above exists, **a supersession owes a sweep**: grep the retired page's
name across `wiki/` before the ingest ends, and annotate every hit.

## The largest instance so far, and it was caused by two writes — 2026-08-17

Two decisions were superseded in one ingest, and both were heavily cited:

| Retired page | `current` pages still citing it |
|---|---|
| [[the-catalogue-is-generated-not-maintained]] | **eighteen** |
| [[the-wiki-has-five-folders-and-tasks-is-not-one]] | **eleven** |

Counted with `grep -rl` over `wiki/` immediately after the move, and both figures include the
successor pages, which cite their predecessors on purpose.

**Not one is a broken link**, because `archive/` resolves — which is the blind spot this page is
about, now at a scale where it is no longer a curiosity. `index.md` was repointed at both
successors, per the rule that a supersession is a link-rewriting event. **The rest were left where
they stand**, and only four were annotated by hand
([[the-index-is-a-map-not-a-catalogue]], [[index-md-stays-at-the-vault-root]],
[[proposals-are-a-folder-not-a-status]], [[vault-scripts]]).

**That is the librarian reporting rather than repairing**, and the reason is the one already on
this page: most of these citations are still true about the day they were written, and rewriting
twenty-nine of them unattended would edit pages this ingest has no other business touching. The
alternative — a detector that names live citations of archived pages — is the pairing this store
already knows it owes ([[a-rewriter-must-be-paired-with-a-detector]]).

## The instance that lands inside a rendered file — 2026-08-17

Two more pages were archived, and one of them is cited **from six of the nine rule pages**:

| Retired page | `current` pages in `wiki/` still citing it |
|---|---|
| [[claude-md-is-a-map-and-four-rules]] | **sixteen**, including its successor and six rule pages |
| [[a-region-is-checked-against-its-rules-governs]] | **six**, including its successor |

**What is new here is the destination, not the count.** A rule page's text is *rendered into the
repository's `CLAUDE.md`* ([[what-travels-from-a-rule-page-is-a-marked-slice]]), so a citation of an
archived page on a rule page could in principle travel out of the vault and into a file where `[[…]]`
is inert and unresolvable — the exact reason that file refuses wikilinks.

**It does not, and that was measured rather than assumed**: every one of those citations sits *outside*
the `<!-- text -->` slice, on the justification half of the page. Checked on all nine rule pages —
**no wikilink appears inside any slice**.

**So the rule holds for a new reason**: a rule page is two documents, and only one of them is exported.
The other is a vault page like any other and may argue from history. **What is owed is a verdict** — a
wikilink inside a `<!-- text -->` slice should be red, because it would render into a file that cannot
resolve it, and nothing checks that today.

**The detector this page keeps asking for was deferred by the owner twice in the same session**
([[a-rewriter-must-be-paired-with-a-detector]], [[what-the-harness-build-waits-on]]).
