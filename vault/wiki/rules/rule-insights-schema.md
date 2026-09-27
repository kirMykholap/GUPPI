---
type: rule
kind: Leaf
purpose: Prevents an Insight page from carrying a field or section outside the shape lint checks, or lacking one it needs
status: built
enforcement: render
governs: vault/wiki/insights/schema.yaml
render_mode: full
parent: "[[rule-page-schemas]]"
estimates: ["[[estimate-insights-schema-checked]]"]
origin: raw/2026-09-22/0014/ledger.md#case-304.6
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Purpose

Prevents an Insight page from carrying a field or section outside the shape lint checks, or lacking one it needs. The Render is `vault/wiki/insights/schema.yaml`, the file `guppi lint` reads for every page of `wiki/insights/`. The lists are what lint reads; `description`, `fields`, `sections` and `examples` are the prose of the former `schema.md` as data — lint refuses a listed name without a description and a description without a name (case 304.8).

## Render

<!-- rule-insights-schema -->
type: insight
description: |
  Three blocks: properties, body, history. Always a MOC — a single unclustered lesson is just a Lesson.

  Insight is its own type, not a kind of Lesson. It shares no fields with one: no `trigger`, no `root_cause`, no `source`, no Estimate. It has `children`, `severity` and `addressed_by`, which a Lesson does not. Two schemas under one name would have meant a page where most fields are inapplicable whichever kind it is.

  Created by the librarian, never by a decision; an `update` actions or rejects it, a `defer` postpones it (case 124). It stands in `backlog.md` while `open`, and becomes an ordinary ratified Case when the person brings it onto a Frontier (case 451.4).

  Threshold. An Insight is created on the second Lesson sharing a root cause. One occurrence is an incident; two is a pattern. The archive is not searched. A Lesson is archived only when its Insight was actioned — its `clustered` children are archived by the cascade of `generate` (case 104.2) — and that Insight stays live with its `pattern` in its index line; a recurrence after the pattern was supposedly fixed is caught there, at the cost of one index line, and reopens the Insight.

  Reopening. `actioned` is not an end state. When a new Lesson matches the root cause of an `actioned` Insight, the Insight returns to `open` and the new Lesson becomes a child. Previously archived children stay archived, so `severity` counts only the current run. No separate recurrence counter — the fact is legible from History plus the retained `addressed_by`. One exception: a Lesson whose entry carries `addressed_by` — a decision line of its own session marked it with `{addresses:<its slug>}`, the Case that closed its cause. Then the Insight stays `actioned`, `addressed_by` moves to that decision when its case is later than the one the field names, and stands otherwise — one link, the latest (cases 361, 385) — the Lesson becomes a child and is archived with the other children by the cascade (case 284.4).

  Slug. Area + pattern, as for Lessons: `insight-hooks-lifecycle-assumptions`.

  No `## Children` or `## Addressed by` section: the fields are the links (case 166.1). `severity` is `count(children where status != archived)`, recomputed by the cascade of `generate`.
properties:
  required: [type, pattern, status, children, severity, origin, sprint, created, tags]
  optional: [addressed_by, deferred_by]
  single: [addressed_by]
  values:
    status: [open, actioned, archived]
  conditional:
    - when: {status: actioned}
      required: [addressed_by]
computed: [severity]
body:
  required: ["## Pattern", "## History"]
  optional: ["## Proposal"]
fields:
  type: |
    required; `insight`. Page category.
  pattern: |
    required; one line. The shared root cause, stated once. The index line of the category is built from it.
  status: |
    required; `open` | `actioned` | `archived`. `actioned` when a ratified decision has addressed it. Not terminal — a new Lesson with the same root cause reopens it, unless its entry carries `addressed_by`: a decision of its own session closed its cause, and the Insight stays `actioned` (case 284.4); an Insight made from a lesson whose entry carries `addressed_by` is set `actioned` right after its `create`, by the librarian's `update` (case 302.2). `archived` when the cascade of `generate` finds an `open` Insight with no live child (case 104.3); an `actioned` Insight is never archived by the cascade, it is kept for the recurrence.
  children: |
    required; list of quoted wikilinks `"[[slug]]"`. The Lessons clustered here. Unordered. The scripts read the slug through the brackets; a slug without a category prefix stays bare (case 148.2). The field is the link; no body section repeats it (case 166.1).
  severity: |
    required; integer. `count(children where status != archived)`. Recomputed by the cascade of `generate` (case 104.3), a child read in `wiki/lessons/` or in the archive (case 110), never written by hand (case 110.1).
  addressed_by: |
    required on `actioned`; decision quoted wikilink `"[[slug]]"`. The ratified decision that fixed the pattern, or rejected it (case 124) — one, the latest; a list is not a shape of this field, and of two Cases of one plan only one actions the Insight (case 361). The field is the link; no body section repeats it (case 166.1).
  deferred_by: |
    optional; list of decision quoted wikilinks `"[[slug]]"`. The `defer` decisions that postponed it; set by `generate`, cleared by a `supersedes` (case 124.2).
  origin: |
    required; date + session. When the librarian first clustered it. Unlike every other category this does not point at a ledger line — no decision created it.
  sprint: |
    required; the sprint id.
  created: |
    required; date.
  tags: |
    required; list.
sections:
  "## Pattern": |
    required. Expands the property: what the clustered lessons have in common, stated as a mechanism rather than a list of symptoms.
  "## Proposal": |
    optional. What the librarian suggests doing about it. A suggestion, not a decision — it is ratified, rejected or reshaped in a later Case.
  "## History": |
    required. Appended by hook, never by an agent. Always the last section. Reopening is visible here.
examples:
  "actioned": |
    ---
    type: insight
    pattern: Hooks were assumed to gate execution without checking which events can block
    status: actioned
    children: [lesson-hooks-sessionstart-cannot-block, lesson-hooks-subagentstart-no-gate]
    severity: 2
    addressed_by: decision-hook-capability-table
    origin: 2026-09-15 · session-2026-09-15
    sprint: 2026-Q3-s4
    created: 2026-09-15
    tags: [hooks, session]
    ---

    ## Pattern
    Both failures came from placing a guard on an event that cannot block. The events were
    chosen by when they fire, without checking whether a non-zero exit there actually stops
    anything. The shape recurs because the two properties are independent and only one is
    obvious from the event name.

    ## Proposal
    A capability table in the session-start rule: for each hook event, whether exit 2 blocks.
    Consult it before placing any guard.

    ## History
    - 2026-09-15 created · clustered from 2 lessons
    - 2026-09-19 status: open → actioned · decision-hook-capability-table
<!-- /rule-insights-schema -->

## History

- 2026-09-22 created · [[decision-case-304.6]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-23 updated: addressed_by listed under properties.single (case 362.2) · [[decision-case-362.2]]
- 2026-09-23 updated: addressed_by is one link, the latest; a list is not its shape (case 361) · [[decision-case-361]]
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 status: draft → built · cascade
- 2026-09-24 updated: the move of addressed_by only to a later case (case 385) · [[decision-case-385]]
- 2026-09-27 updated: an open Insight stands in backlog.md, a Case when the person brings it onto a Frontier (case 451.4) · [[decision-case-451.4]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 status: draft → built · cascade
