---
title: "Fidelity to a source and fidelity to the tree are different properties, and only the first has ever been checked"
type: concept
status: current
authority: fidelity-axes
basis: measurement
sprint: S1
created: 2026-08-15
sources: ["archive/2026-08-15/2026-08-15-the-vault-checked-whole/handoffs/2026-08-15-the-vault-checked-whole.md", "scripts/vault-coverage.sh", "log.md"]
tags: [vault, testing]
---

# Two questions that sound like one

A page can be wrong in two unrelated ways, and this store has an instrument for one of them.

*(The title read "Fidelity to a source and fidelity to the tree are two different properties, and
only the first has ever been checked" until 2026-08-18. It names both properties in its own first
clause, so the count was never carrying anything the title did not already say. The `quantity:`
line it carried argued that the pair was the page's subject and that a third would make this page
wrong rather than stale. **A third arrived anyway**: the section "A third kind, proved on
2026-08-17" below was added while the declaration stood, and the count in the title was stale from
that day until this one. That reasoning went with the field when it was rejected and the rule was
made unconditional in both halves ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[a-title-names-what-is-counted-instead-of-counting-it]]).)*

| | **Fidelity to the source** | **Fidelity to the tree** |
|---|---|---|
| Question | does the page still say what the lines its sidecar names actually said? | does the page still describe what the repository does now? |
| Checked by | sampling the sidecar's line numbers against their pages — the fidelity sample every ingest owes | nothing |
| Fails when | the compiler paraphrased, merged two sources, or read a later passage as replacing an earlier one | the code moved and nobody re-read the page |
| Measured 2026-08-15 | **10 of the 10 most-cited pages still say what the source said** | **6 pages said what the repository no longer does** |

**Neither is coverage.** `INGEST COMPLETE` says every unit carries a verdict; a page describing
behaviour a later slice replaced passes both coverage modes, identifiers and all, and the script's
own header says so ([[vault-scripts]]).

## Why the second one has no instrument, and what it would need

The first is checkable because both sides are text that does not move: the source is in `raw/` and
`raw/` is immutable ([[the-handoff-template-maps-onto-the-categories]]), so a line number is a
stable address and a sample is cheap. **The second has a moving right-hand side.** `sources:` rule
11 of `vault-check.sh` proves only that a cited path *exists* — never that the file still holds the
claim — and that gap has already been met at scale, when 24 pages cited a `docs/HANDOFF.md` that
had become a pointer.

So a `basis: code` page is an assertion about a tree, made on a day, with nothing watching it. The
only discipline that has ever caught the second kind here is a human reading, and the audit of
2026-08-15 is the first time anyone did it deliberately.

## The consequence for how a page's claim is weighted

`basis` already ranks a conflict — `code` loses to the code itself. This page is why that ranking
is not enough on its own: **a `basis: code` page is only as current as the last time somebody
opened the code beside it**, and the vault records that date nowhere except in prose. Where a
number is involved, the discipline that works is the commit stamp —
[[a-stated-count-drifts-from-the-list-it-heads]] measured that *"N at `<commit>`"* survived every
time and *"it is now N"* failed every time.

The related failure, on the source axis rather than the tree axis, is
[[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]]: fidelity to *a* passage of a
source is not fidelity to the source.

## The missing instrument was designed on 2026-08-16

*Fidelity to the tree: checked by nothing* now has a design, and its inputs already exist:
[[a-staleness-detector-from-updated-against-a-pages-sources]] compares `updated` (else `created`)
against the last commit of every source that is a live file of the tree, in one
`git log --name-only` pass. **Coverage would be 91 pages of 142** — the other 51 cite only the
immutable `raw/` and are invisible to it, which is a limit and not an omission.

**The `updated` field it needs is now part of the core** and is stamped by a script
([[the-frontmatter-core-is-fixed-and-updated-joins-it]]). The trap it must not fall into is on this
page's own axis: **a stamp means bytes moved, not that anyone re-read the sources**, so it may not
clear a suspicion — a typo fix would clear one silently, in the dangerous direction.

**Nothing is built.** The freezing half of the same problem — thirteen pages citing a mutable spec —
is answered separately by [[raw-holds-testimony-and-artefacts-are-frozen]].

## A third kind, proved on 2026-08-17: fidelity of a *move*

**The rules of the repository's `CLAUDE.md` were migrated into pages, and the migration was verified to
have changed no words.** Two measurements, in both directions:

- **the rendered regions were diffed against the list items they replaced** — nine diffs, all empty;
- **every non-marker line of the previous file was checked for presence** in the new one. What is gone:
  the deleted section, two headings, and the counting phrase. Nothing else.

**That is a question neither of the two fidelities above asks.** Fidelity to a source asks whether a page
says what its journal said; fidelity to the tree asks whether it still describes the code. **Fidelity of a
move asks whether a byte-preserving operation preserved bytes** — and it is answerable exactly and cheaply,
which is why it was answered rather than asserted ([[a-gate-guarantees-agreement-never-truth]]).

**Once it is verified, the gate takes over**: rule 12 keeps the region and the page equal from then on
([[a-check-asks-by-running-the-writer-it-checks]]). **The verification is needed precisely once per move**,
at the moment the two copies exist and nothing yet compares them
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).
