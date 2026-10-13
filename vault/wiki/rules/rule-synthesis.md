---
type: rule
kind: Leaf
purpose: Prevents a pattern of failures from staying a list of unrelated incidents
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: ["[[estimate-synthesis-clusters]]", "[[estimate-synthesis-keeps-actioned-by-the-mark]]", "[[estimate-synthesis-reads-the-status-its-yaml-sets]]"]
origin: raw/2026-09-10/ledger.md#case-35.2
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
core: true
---

## Purpose

Prevents a pattern of failures from staying a list of unrelated incidents. One
lesson is an incident; two with one root cause are a pattern, and a pattern is what
a later Case can fix. The archive is not needed: a lesson is archived when its Insight was actioned, and that Insight stays live with its pattern in its index line until the close of its sprint, so a recurrence inside the sprint is caught there at the cost of one Grep line; the close of a sprint archives its actioned Insights and its `error` lessons that joined no Insight (`rule-sprint-close`, case 627.5).

## Render

<!-- rule-synthesis -->
Synthesis. For each `lesson` entry, compare its `root_cause` with every index line of `vault/wiki/lessons/` and of `vault/wiki/insights/` — the Greps `^(root_cause|deferred_by):` and `^(pattern|deferred_by):`, run by you — by meaning (case 147.4).
- A live lesson has the same cause and no Insight exists: append to the yaml a `create` in `insights` with `slug` (`insight-<area>-<pattern>`), `pattern`, `children` (both lessons), `tags` (the union), and `sections` `Pattern` and `Proposal`; and an `update` for each lesson with `set: {status: clustered, insight: <slug>}`. When the lesson entry carries `addressed_by: decision-case-N` — the Case of this unit that closed its cause — append right after the `create` an `update` of the new Insight with `set: {status: actioned, addressed_by: decision-case-N}`: the Insight is born closed, its lessons go to the archive by the cascade, and the pair is reported in the brief beside the synthesis (case 302.2).
- An Insight has the same pattern: append an `update` of it with `children` plus
  the new lesson, and — when it was `actioned`, on disk or by an `update` entry of a decision in this yaml that sets it `actioned`, whose `addressed_by` is then the one the Insight names (case 668) — `set: {status: open}`, or `set: {addressed_by: decision-case-N}` with `status` kept when the lesson entry carries `addressed_by: decision-case-N`, the Case of this unit that closed its cause, and case N is later than the case the Insight's `addressed_by` names — compared number by number, `378.5` after `378.4`; when it is not later, the `update` carries no `addressed_by` and the field stands (case 385); the pair reported in the brief beside the synthesis (case 284.4); and an `update`
  for the lesson.
Mark each entry you add with `librarian: synthesis`. The entries of the synthesis have these forms, so no earlier entry and no `materialize.yaml` other than the ones `guppi materialize` names is needed (case 474.1); when you still need one, read it and flag the read as the frame says (case 558.2).

```yaml
# a new Insight from two lessons of one cause
- kind: create
  category: insights
  slug: insight-<area>-<pattern>
  origin: <the origin of the new lesson entry>
  fields: {type: insight, pattern: <the shared cause>, children: [<lesson-a>, <lesson-b>]}
  tags: [<the union of the tags of both lessons>]
  sections: {Pattern: <text>, Proposal: <text>}
  librarian: synthesis
# right after the create, only when the lesson entry carries addressed_by
- kind: update
  category: insights
  slug: insight-<area>-<pattern>
  origin: <the origin of the new lesson entry>
  set: {status: actioned, addressed_by: decision-case-N}
  change: born actioned, its cause closed by case N (synthesis)
  librarian: synthesis
# an existing Insight of the same pattern
- kind: update
  category: insights
  slug: <the live Insight>
  origin: <the origin of the new lesson entry>
  set: {children: [<its children>, <the new lesson>]}
  change: child <the new lesson> added (synthesis)
  librarian: synthesis
# set also takes status: open, or addressed_by: decision-case-N, as the rule above says
# each lesson that joins an Insight
- kind: update
  category: lessons
  slug: <lesson-a>
  origin: <the origin of the new lesson entry>
  set: {status: clustered, insight: <the Insight>}
  change: clustered under <the Insight> (synthesis)
  librarian: synthesis
```

Write the synthesis into the brief: the two Greps with the number of lines each printed, then one line for each `lesson` entry — its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause (case 602). One lesson without a pair stays `new`; its line in the brief is no flag. `Proposal` is a suggestion, never a decision. When an index line does not settle whether a lesson shares a root cause, read the
Trigger and Root cause of the candidate and name the page in the report with the
outcome, clustered or not. The archive is not needed: an actioned Insight stays live with its pattern in its index line until the close of its sprint; when you still need an archived page, read it and flag the read as the frame says (case 558.2). Do not write pages yourself.
<!-- /rule-synthesis -->

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
- 2026-09-14 defer by decision-case-108 superseded · [[decision-case-114]]
- 2026-09-14 updated: the index lines come from the librarian's own Greps of lessons and insights (case 147.4) · [[decision-case-147.4]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 status: draft → built · cascade
- 2026-09-21 updated: an actioned Insight stays actioned when the lesson entry carries addressed_by from a decision of the same unit; addressed_by moves to that decision (case 284.4) · [[decision-case-284.4]]
- 2026-09-21 estimate estimate-synthesis-keeps-actioned-by-the-mark added · [[decision-case-284.4]]
- 2026-09-21 status: built → draft · cascade
- 2026-09-22 updated: an Insight born from a lesson whose entry carries addressed_by is set actioned by an update right after its create (case 302.2) · [[decision-case-302.2]]
- 2026-09-24 updated: addressed_by moves to the lesson's decision only when it is the later case (case 385) · [[decision-case-385]]
- 2026-09-27 status: draft → built · cascade
- 2026-09-28 updated: the synthesis shows the form of each of its entries and reads no yaml that materialize did not name (case 474.1) · [[decision-case-474.1]]
- 2026-09-28 status: built → draft · cascade
- 2026-09-29 updated: the closing fence of the sample entries stands alone on its line, and the sentence after it follows as its own paragraph (case 487.3) · [[decision-case-487.3]]
- 2026-09-29 status: draft → built · cascade
- 2026-09-30 updated: the synthesis forbids no read; another session's yaml or an archived page it still needs is read and flagged (case 558.2) · [[decision-case-558.2]]
- 2026-09-30 status: built → draft · cascade
- 2026-10-03 updated: the synthesis gives one line per lesson entry in the brief, a lesson that joins nothing with the reason (case 602) · [[decision-case-602]]
- 2026-10-03 status: draft → built · cascade
- 2026-10-04 updated: an actioned Insight stays live until the close of its sprint (case 627.5) · [[decision-case-627.5]]
- 2026-10-04 status: built → draft · cascade
- 2026-10-05 estimate estimate-synthesis-reads-the-status-its-yaml-sets added · [[decision-case-668]]
- 2026-10-05 updated: an Insight that a decision entry of the same yaml sets actioned counts as actioned at synthesis (case 668) · [[decision-case-668]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
