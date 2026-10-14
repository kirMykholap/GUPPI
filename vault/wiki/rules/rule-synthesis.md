---
type: rule
kind: Leaf
purpose: Prevents a pattern of failures from staying a list of unrelated incidents
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, workflow, librarian]
core: true
---

## Purpose

Prevents a pattern of failures from staying a list of unrelated incidents. One
lesson is an incident; two with one root cause are a pattern, and a pattern is what
a later Case can fix. The archive is not needed: a lesson is archived when its Insight was actioned, and that Insight stays live with its pattern in its index line until the close of its sprint, so a recurrence inside the sprint is caught there at the cost of one Grep line; the close of a sprint archives its actioned Insights and its `error` lessons that joined no Insight, as `rule-sprint-close` sets it.

## Render

<!-- rule-synthesis -->
Synthesis. For each `lesson` entry, compare its `root_cause` with every index line of `vault/wiki/lessons/` and of `vault/wiki/insights/` — the Greps `^(root_cause|deferred_by):` and `^(pattern|deferred_by):`, run by you — by meaning.
- A live lesson has the same cause and no Insight exists: append to the yaml a `create` in `insights` with `slug` (`insight-<area>-<pattern>`), `pattern`, `children` (both lessons), `tags` (the union), and `sections` `Pattern` and `Proposal`; and an `update` for each lesson with `set: {status: clustered, insight: <slug>}`. When the lesson entry carries `addressed_by: decision-case-N` — the Case of this unit that closed its cause — append right after the `create` an `update` of the new Insight with `set: {status: actioned, addressed_by: decision-case-N}`: the Insight is born closed, its lessons go to the archive by the cascade, and the pair is reported in the brief beside the synthesis.
- An Insight has the same pattern: append an `update` of it with `children` plus
  the new lesson, and — when it was `actioned`, on disk or by an `update` entry of a decision in this yaml that sets it `actioned`, whose `addressed_by` is then the one the Insight names — `set: {status: open}`, or `set: {addressed_by: decision-case-N}` with `status` kept when the lesson entry carries `addressed_by: decision-case-N`, the Case of this unit that closed its cause, and case N is later than the case the Insight's `addressed_by` names — compared number by number, `378.5` after `378.4`; when it is not later, the `update` carries no `addressed_by` and the field stands; the pair reported in the brief beside the synthesis; and an `update`
  for the lesson.
Mark each entry you add with `librarian: synthesis`. The entries of the synthesis have these forms, so no earlier entry and no `materialize.yaml` other than the ones `guppi materialize` names is needed; when you still need one, read it and flag the read as the frame says.

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

Write the synthesis into the brief: the two Greps with the number of lines each printed, then one line for each `lesson` entry — its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause. One lesson without a pair stays `new`; its line in the brief is no flag. `Proposal` is a suggestion, never a decision. When an index line does not settle whether a lesson shares a root cause, read the
Trigger and Root cause of the candidate and name the page in the report with the
outcome, clustered or not. The archive is not needed: an actioned Insight stays live with its pattern in its index line until the close of its sprint; when you still need an archived page, read it and flag the read as the frame says. Do not write pages yourself.
<!-- /rule-synthesis -->

## History

- 2026-10-14 shipped with GUPPI
