---
type: estimate
kind: QA
status: pending
target: "[[rule-synthesis]]"
purpose: An actioned Insight of the same pattern stays actioned when the new lesson's entry carries addressed_by, and its addressed_by moves to that decision
method: one reading by hand of the yaml and the brief after the librarian's run on the first marked lesson clustered under an actioned Insight; no date
origin: raw/2026-09-20/2106/ledger.md#case-284.4
sprint: migration
created: 2026-09-20
tags: [harness, workflow, librarian]
---

## Criterion

Given:
`rule-synthesis`: on an Insight of the same pattern the librarian appends an `update` with `children` plus the lesson and `set: {status: open}` when it was `actioned`; the entries it adds carry `librarian: synthesis`.
**＋** `insights/schema.md`: `addressed_by` is one decision; the cascade of `generate` archives the children of an `actioned` Insight.
**＋** The lesson entry carries `addressed_by: decision-case-N` when a decision line of the unit marked it (284.3).
**－** An `open` Insight stays as today; the librarian never sets `actioned` himself.

When:
The librarian, at synthesis, finds an Insight of the same pattern, it is `actioned`, and the lesson entry carries `addressed_by`.

Then:
The `update` of the Insight carries `children` plus the lesson and `set: {addressed_by: decision-case-N}` — the bare slug, `generate` writes the wikilink — with `status` kept `actioned`; the lesson is `clustered` with `insight` set, the cascade archives it; the brief reports the pair beside the synthesis, as it reports a clustering.
**＋** Without `addressed_by` — `set: {status: open}`, as today.
**＋** The schema of Insights, §8 of the map and the glossary name the exception: a new Lesson reopens `actioned` unless its entry carries `addressed_by`.

## History

- 2026-09-21 created · [[decision-case-284.4]]
