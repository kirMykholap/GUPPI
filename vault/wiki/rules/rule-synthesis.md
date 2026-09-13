---
type: rule
kind: Leaf
purpose: Prevents a pattern of failures from staying a list of unrelated incidents
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: rule-documentation
estimates: [estimate-synthesis-clusters]
deferred_by: [decision-case-108]
origin: raw/2026-09-10/ledger.md#case-35.2
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Purpose

Prevents a pattern of failures from staying a list of unrelated incidents. One
lesson is an incident; two with one root cause are a pattern, and a pattern is what
a later Case can fix. The archive is not read: a lesson is archived only when its
Insight was actioned, and that Insight stays live with its pattern in the index, so
a recurrence is caught there at the cost of one index line.

## Render

<!-- rule-synthesis -->
Synthesis. For each `lesson` entry, compare its `root_cause` with every line of
`lessons-index.md` and of `insights-index.md`, by meaning.
- A live lesson has the same cause and no Insight exists: append to the yaml a
  `create` in `insights` with `slug` (`insight-<area>-<pattern>`), `pattern`,
  `children` (both lessons), `tags` (the union), and `sections` `Pattern` and
  `Proposal`; and an `update` for each lesson with `set: {status: clustered,
  insight: <slug>}`.
- An Insight has the same pattern: append an `update` of it with `children` plus
  the new lesson, and `set: {status: open}` when it was `actioned`; and an `update`
  for the lesson.
Mark each entry you add with `librarian: synthesis`. One lesson without a pair
stays `new`; that needs no flag. `Proposal` is a suggestion, never a decision. When an index line does not settle whether a lesson shares a root cause, read the
Trigger and Root cause of the candidate and name the page in the report with the
outcome, clustered or not. Do not read the archive and do not write pages yourself.
<!-- /rule-synthesis -->

## Estimates

- [[estimate-synthesis-clusters]]

## Parent

- [[rule-documentation]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.2
- 2026-09-10 estimate estimate-synthesis-clusters added · raw/2026-09-10/ledger.md#case-35.2
- 2026-09-10 updated: the lessons of a cluster are read before the Insight is written, and named · raw/2026-09-10/ledger.md#case-44
- 2026-09-11 updated: a candidate lesson is read when the index line is not enough, clustered or not, and named with the outcome · [[decision-case-54]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 deferred · [[decision-case-96]]
- 2026-09-12 deferred · [[decision-case-97]]
- 2026-09-13 defer by decision-case-97 superseded · [[decision-case-104.3]]
- 2026-09-13 defer by decision-case-96 superseded · [[decision-case-108]]
- 2026-09-13 deferred · [[decision-case-108]]
