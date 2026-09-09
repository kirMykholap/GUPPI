---
title: "The rendered form is defined once and read by the writer and by the comparison"
type: concept
status: current
authority: rendered-form-definition
basis: code
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-inject.sh"]
tags: [harness, testing, vault]
---

# One variable, because both ways of splitting it fail silently

**What a region's body looks like — the slice plus the separator after it — is one definition in
`scripts/vault-inject.sh`, read by the writer and by the comparison.**

*(The title read "The rendered form is defined once and read by both the writer and the comparison"
until 2026-08-18, and it named the two ends in the same breath as counting them, so the count was
carrying nothing. **They were never a count of the world**: a shared format has a writer and a
checker because that is what makes it shared, and a third reader of the definition would make this
page wrong rather than stale. That reasoning stood in a `quantity:` line until the field was
rejected and the rule was made unconditional in both halves
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[a-title-names-what-is-counted-instead-of-counting-it]]). The **filename** still carries the word
and waits for its rename, which moves an address ([[the-title-rule-extends-to-filenames]],
[[a-page-rename-is-sed-and-verify]]).
**Closed 2026-08-19: the rename landed and the name counts nothing.** The sentence above was
written on 2026-08-18 and stood for one day; the wait is the record rather than an oversight,
because a filename is an address and the repair was scheduled as one sweep of sixteen names in a
single change, not taken by whichever session happened to open this page next.)*

| If it lives only in | What happens |
|---|---|
| the writer | the check reports a difference on **every** run, for good |
| the comparison | the separator is **never written**, and the check is happy |

**Both failures are silent in the way that matters**: the first is loud and wrong, and a reader
learns to ignore it; the second is quiet and wrong, and nobody learns anything. That is the whole
argument for one variable, and it is the same argument that keeps rule 12 from holding a second
implementation of the byte comparison ([[a-check-asks-by-running-the-writer-it-checks]],
[[a-command-substitution-strips-the-newline-a-gate-compares]]).

## The separator is idempotent because the writer replaces the body wholesale

The injector **drops the old region body entirely** and writes a new one between the markers, so one
blank line is written however many times it runs. Nothing accumulates, and no run has to know what a
previous run did.

**Emitting the separator after the close marker would accumulate** — one blank line per run, growing
in a file people also edit by hand, and looking exactly like an editor's doing. That, plus the fact
that the space between two regions is stripped before the file is read at all, is why it goes inside
([[the-injector-writes-the-separator-inside-the-region]],
[[block-comments-are-stripped-before-claude-md-reaches-the-model]]).

## The general shape

**A format shared by a writer and a checker is one definition or it is two formats.** The vault has
the same rule about addresses — the marker's `folder/slug` is computed once and everything
downstream joins on it ([[a-marker-with-its-type-is-a-complete-address]]) — and about mappings
between hops ([[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]). **Do not hand-write a
rendered region**: it is the writer's output, and anything hand-typed there is a third definition
nobody registered.
