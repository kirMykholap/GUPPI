---
type: decision
case: "381"
status: current
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-09-23/1355/ledger.md#case-381
sprint: migration
created: 2026-09-23
tags: [sprint, workflow]
---

## Context

Case 378 changed the model of the Criterion; the 104 Estimates come to it in one pass: `Given:` out, the input of the scenario into `When:`, the `－` lines on the bounds of an edit out, the journals split, and the eleven Estimates of the old model named by Case 378 rewritten whole. It is the work of a session of its own. A defer does not fit: a defer stands on a Rule or an Insight, and `rule-estimates-schema` is changed by Case 378 already. A task without a page goes to the sprint page; the Frontier takes the first milestone with an open item, so a milestone ahead of Slice 4 is the agenda of the next `/hi`. It is named Slice 3g: the Criterion of `estimate-sprint-migration-lint-clean` reads `## Milestones` as the Slices in order, and 3g follows the closed 3c, 3d and 3f. The item is a plain line with no wikilink — no page closes the pass — so it never ticks and leaves by the `update` of the sprint page that closes the pass. `entity-sprint-migration` stands `draft`; its Estimates speak of the build, lint and the merge and are not touched.

## Problem

The one pass over the Estimates has no place that brings it to the next session as its first item.

## Given

`entity-sprint-migration` — the section `## Milestones`.
**＋** `vault/wiki/sprint.md` — its render, `uv run guppi sprint`.
**＋** `/hi` — the skill that assembles the Frontier from `vault/wiki/sprint.md`.

## History

- 2026-09-23 created · raw/2026-09-23/1355/ledger.md#case-381
