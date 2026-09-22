---
type: estimate
kind: QA
status: pending
target: "[[rule-synthesis]]"
purpose: An Insight stays or is born actioned by the mark — an existing actioned Insight keeps its status and takes the new addressed_by; a new Insight from a marked lesson is set actioned right after its create
method: one reading by hand of the yaml and the brief after the librarian's run on the first marked lesson clustered under an actioned Insight; no date
origin: raw/2026-09-20/2106/ledger.md#case-284.4
sprint: migration
created: 2026-09-20
tags: [harness, workflow, librarian]
---

## Criterion

Given:
`rule-synthesis`: on an Insight of the same pattern the librarian appends an `update` with `children` plus the lesson and `set: {status: open}` when it was `actioned`; on two lessons with one cause and no Insight a `create` of the Insight and an `update` of each lesson; the entries it adds carry `librarian: synthesis`.
**＋** `insights/schema.md`: `addressed_by` is one decision; `generate` sets a new Insight `open`; the cascade of `generate` archives the children of an `actioned` Insight.
**＋** The lesson entry carries `addressed_by: decision-case-N` when a decision line of the unit marked it (284.3).
**－** An `open` Insight stays as today; the librarian sets `actioned` by the mark alone, never on his own.

When:
The librarian, at synthesis, finds an Insight of the same pattern that is `actioned`, or creates an Insight, and the lesson entry carries `addressed_by`.

Then:
On an existing `actioned` Insight the `update` carries `children` plus the lesson and `set: {addressed_by: decision-case-N}` — the bare slug, `generate` writes the wikilink — with `status` kept `actioned`; the lesson is `clustered` with `insight` set, the cascade archives it; the brief reports the pair beside the synthesis, as it reports a clustering.
**＋** On a new Insight an `update` of its slug follows the `create` with `set: {status: actioned, addressed_by: decision-case-N}`; the Insight stands `actioned`, both lessons `clustered` go to the archive by the cascade; the brief reports the pair (302.2).
**＋** Without `addressed_by` — `set: {status: open}` on an existing Insight, a new one `open`, as today.
**＋** The schema of Insights, the schema of Insights and the glossary name the exception: a new Lesson reopens `actioned` unless its entry carries `addressed_by`; the schema names the birth by the mark too.

## History

- 2026-09-21 created · [[decision-case-284.4]]
- 2026-09-22 updated: the Criterion replaced whole — the second case of the mark, an Insight born from a marked lesson (case 302.2) · [[decision-case-302.2]]
- 2026-09-22 updated: the exception is named by the schema and the glossary, not by §8 (case 318) · [[decision-case-318]]
