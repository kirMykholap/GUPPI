---
type: insight
pattern: "An edit pair — a `reword` or a `replace` — is signed from a grep fragment: the matched words are copied out as the anchor, and neither the sentence they sit in nor what an earlier Case of the same Spec leaves of it is read before the Case is ratified."
status: open
children: ["[[lesson-reword-pairs-signed-before-the-places-were-read]]", "[[lesson-replace-anchors-overlap-in-one-spec]]"]
severity: 2
origin: raw/2026-09-22/1121/ledger.md#L96
sprint: migration
created: 2026-09-22
tags: [workflow, harness, librarian]
---

## Pattern

A Case that changes an existing page names the text it changes with a pair — `reword` with
`{old, new}`, or `replace` with `{old, new}`. The pair is composed from the output of a grep:
the matched words are copied out of the hit line and signed as the anchor. Two things stay
unknown to the Case.

What the words mean where they stand. One word names different things in different places, so a
pair written for one of them rewrites the others wrongly, or produces text that reads as
nonsense. Case 274.2 signed `pre-task → pre-spec` across the live pages by a grep count; five of
the places meant the vault query, not the check of the set, and one would have produced "at
pre-spec and at pre-spec".

What the page will hold when the pair is applied. The pairs of one Spec land in entry order at
the librarian's run, so an earlier Case of the same Spec can have rewritten the span a later
anchor names. Case 314.2's `old` was a span of `rule-prespec` that Case 310.6 of the same Spec
replaces first; three other anchors of that Spec named text that was never on the page.

Both are found late. Pre-spec catches them at best, `generate` fails the entry at worst, and the
pair is repaired by hand or superseded — after ratification either way.

## Proposal

Bind the pair to a read of its place, in two halves, one for each unknown.

The procedure half: a `reword` or `replace` pair is signed only after the whole sentence around
every match is in context with its meaning named. The regulated procedure the first lesson
names already asks this before a `reword` is signed; it does not reach a `replace`.

The mechanical half: the pairs of a Spec can be simulated in entry order against the pages on
disk before Work Mode ends — whitespace collapsed as `generate` collapses it, the matches
counted, an anchor that misses or is not unique reported with its Case. This moves the pre-spec
check of anchors off the page as it stands today and onto the page as the Spec leaves it, which
is the half pre-spec cannot see now.

Neither half is decided here.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#L96
