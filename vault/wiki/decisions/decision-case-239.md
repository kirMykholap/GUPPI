---
type: decision
case: "239"
status: current
update: ["[[entity-sprint-migration]]"]
defer: ["[[rule-morph]]"]
origin: raw/2026-09-18/1252/ledger.md#case-239
sprint: migration
created: 2026-09-18
tags: [sprint, workflow]
---

## Context

The sprint page `entity-sprint-migration` holds three Slices under `## Milestones` and two plain lines without a page under `## Backlog`: "the categories as data of the project" and "the product model" (case 229.1). The question of the universality of the categories — objection F of `categories-discussion.md` — stands in the first Backlog line as "some day". The person decided: it is a question of Slice 5, the close, in the form of a morph mechanism — at install the person goes through an initiation in which the category set may change, and the architecture has to hold that without a rewrite of the rules. The Case touches the sprint page and creates the placeholder `rule-morph` by a `defer`; it touches no Estimate of the sprint.

## Problem

A Backlog line is "without a turn", and the question got a turn and a name. An item of a milestone without a page is never ticked, and Slice 5 with one would never close; the item needs a page to point at, and the rule does not exist yet.

## Deferred

### [[rule-morph]]

The initiation at install: the person sets the category set of the project — the development set entity, rule, estimate by default — and the harness holds it as data, so a changed set rewrites no rule; the categories discussion of session 1119, raw/2026-09-17/1119/categories-discussion.md; Slice 5

## History

- 2026-09-18 created · raw/2026-09-18/1252/ledger.md#case-239
