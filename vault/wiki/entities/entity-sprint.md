---
type: entity
kind: MOC
purpose: The sprint as a kind — a unit of work over the project with a Definition of done and milestones; its children the sprints, one Leaf per id
status: draft
children: ["[[entity-sprint-migration]]"]
estimates: []
origin: raw/2026-09-18/1252/ledger.md#case-241
sprint: migration
created: 2026-09-18
tags: [sprint, workflow]
---

## Purpose

The sprint as a kind. A sprint is a unit of work over the project: its Estimates are its Definition of done, its `## Milestones` the Slices in order, its `## Backlog` the items without a turn. Each sprint is a Leaf under this page, `entity-sprint-<id>`, one live at a time; `guppi sprint` renders `vault/wiki/sprint.md` from the live one, and `rule-sprint` is its guard. This page carries no Estimate yet — the person named none; a measure over all sprints, which no single sprint owns, goes here when one is named (case 241).

## History

- 2026-09-18 created · [[decision-case-241]]
