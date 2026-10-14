---
type: entity
kind: MOC
purpose: The sprint as a kind — a unit of work over the project with a Definition of done and milestones; its children the sprints, one Leaf per id
status: draft
parent: "[[entity-guppi]]"
estimates: []
rules: ["[[rule-sprint]]", "[[rule-sprint-close]]"]
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [sprint, workflow]
core: true
---

## Purpose

The sprint as a kind. A sprint is a unit of work over the project: its Estimates are its Definition of done, read before its close, and one that has not passed by then goes to the archive with the sprint page, its status kept in the record of the close, as `rule-sprint-close` sets it; its `## Milestones` the Slices in order, its `## Backlog` the items without a turn. Each sprint is a Leaf under this page, `entity-sprint-<id>`, one live at a time; `guppi sprint` renders `vault/wiki/sprint.md` from the live one, and `rule-sprint` is its guard. This page carries no Estimate yet — the person named none; a measure over all sprints, which no single sprint owns, goes here when one is named.

## History

- 2026-10-14 shipped with GUPPI
