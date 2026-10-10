---
type: decision
case: "299.2"
status: archived
create: ["[[estimate-prespec-catches-a-superseded-case]]"]
update: ["[[rule-prespec]]"]
supersedes: ["[[decision-case-298]]"]
origin: raw/2026-09-21/1853/ledger.md#case-299.2
sprint: migration
created: 2026-09-21
tags: [harness, workflow, session]
---

## Context

The Spec is the plan the person approves at the end of Plan Mode. In session 1315 Case 296 superseded 291.1 before the approval, and the Spec of 1315 still holds 291.1 whole: its sections, its `then` block, its five task lines. Nothing ticks or removes them: `generate` neither applies nor ticks the entries of a superseded Case (151, 286), Retro does not count them (282). The lines stay `[ ]` for good and read like debt. The sentence of the schema, "the replaced text stays in the Spec of its session and in History", is right for a supersede from a later session, whose Spec is archived history; inside one session the superseded Case was never the plan. Three scripts lean on the Case being in the Spec: `prespec --check` (`check_lines`) prints "no Case N heading in the plan" for a ledger line whose Case left the plan — so today removing 291.1 from the plan would be a finding; `materialize` without the Case in the Spec marks the entry `incomplete: [then]` and the `decisions` record `incomplete: [context, problem, given, when]`; `generate` writes the body of the Decision page from `case_text` — without it, a page with no `## Context` and no `## Problem`. The defect of the librarian's run of 1315: the `then` block of Case 298 is not YAML (a colon in `no incomplete: [then]`, line 384 of Spec 1315), so the three entries of 298 are `incomplete` and `decision-case-298` has no `## Deferred`; the `deferred_by` on the three pages stand.
The pages: `rule-case-protocol` `draft`, `rule-prespec` `built`, `rule-materialize` `draft`, `rule-page-generation` `draft`, the last three with `deferred_by: decision-case-298`; `index.md` §7 a Rule-class file, by hand. The Estimates the Case touches: `estimate-case-protocol-loaded` (the live reading of the Render), the new `estimate-prespec-catches-a-superseded-case`, `estimate-materialize-marks-superseded` (in the shape before case 193, no `Given`), `estimate-generate-writes-the-decision-page`; the other Estimates of these rules are not touched. The slug of the new Estimate is free, in `wiki/` and in the archive.

## Problem

Where the rule stands and what the three scripts do, so that the agent removes a superseded Case from the plan, pre-spec catches one left there, and `materialize` and `generate` invent no debt from its absence. And how `decision-case-298` is repaired.

## History

- 2026-09-22 created · raw/2026-09-21/1853/ledger.md#case-299.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
