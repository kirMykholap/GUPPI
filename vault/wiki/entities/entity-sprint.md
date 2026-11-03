---
type: entity
kind: MOC
purpose: The sprint as a kind — a unit of work over the project with a Definition of done and milestones; its children the sprints, one Leaf per id
status: built
parent: "[[entity-guppi]]"
estimates: ["[[estimate-sprint-keeps-one-live-page]]"]
rules: ["[[rule-sprint]]", "[[rule-sprint-close]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow]
core: true
---

## Purpose

The sprint as a kind. A sprint is a unit of work over the project: its Estimates are its Definition of done, read before its close, and one that has not passed by then goes to the archive with the sprint page, its status kept in the record of the close, as `rule-sprint-close` sets it; its `## Milestones` the Slices in order, its `## Backlog` the items without a turn. Each sprint is a Leaf under this page, `entity-sprint-<id>`, one live at a time; `guppi sprint` renders `vault/wiki/sprint.md` from the live one, and `rule-sprint` is its guard. Its Estimate is a measure over all sprints, which no single sprint owns: at most one sprint page is live, and each other one stands in the archive.

## History

- 2026-11-03 shipped with GUPPI
