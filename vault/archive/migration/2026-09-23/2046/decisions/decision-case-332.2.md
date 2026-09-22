---
type: decision
case: "332.2"
status: archived
create: ["[[estimate-prespec-simulates-the-pairs]]"]
update: ["[[rule-prespec]]", "[[insight-workflow-edit-pair-signed-from-a-grep-fragment]]"]
superseded_by: ["[[decision-case-345]]"]
origin: raw/2026-09-22/1724/ledger.md#case-332.2
sprint: migration
created: 2026-09-22
tags: [harness, workflow, session, librarian]
---

## Context

A Case that changes an existing page names the text with a pair — `replace` or `reword`. The pair is composed from the output of a grep: the matched words are copied out of the line and signed as the anchor. Two things stay unknown to the Case: what the words mean where they stand — case 274.2 signed `pre-task → pre-spec` by a count of grep hits, and in five places the word meant the vault query, not the check of the set — and what the page will hold when the pair lands, since the pairs of one Spec are applied in entry order and an earlier Case rewrites the span a later anchor names (case 314.2). Today this is caught by eye alone: at `/pre-spec` the `ask-guppi` agent reads the `then` blocks, but against the page as it stands, not as the Spec leaves it, and the librarian of session 1121 simulated 71 anchors by hand.
The Insight stands `open`, severity 2, with `lesson-reword-pairs-signed-before-the-places-were-read` and `lesson-replace-anchors-overlap-in-one-spec` as its `clustered` children. `rule-case-protocol` stands `draft` and renders `case-schema.md`, where `replace` is described; `rule-prespec` stands `built`, and three Cases of this session already change its Render in three places that meet nowhere. This Spec carries eight pairs over six pages, three of them on one.

## Problem

A pair is signed blind twice over: without the meaning of the words in their place, and without what the Spec itself leaves of that place. It is caught late — by eye at pre-spec at best, by a refusal of `generate` at worst, after ratification either way.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-332.2
- 2026-09-23 superseded by decision-case-345 · [[decision-case-345]]
- 2026-09-23 archived · superseded
- 2026-09-23 archived · cleanup
