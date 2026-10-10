---
type: decision
case: "316"
status: archived
create: ["[[rule-session]]", "[[estimate-session-phases-in-order]]"]
update: ["[[rule-session-start]]", "[[rule-plan-mode]]", "[[rule-work-mode]]", "[[rule-end-of-work]]", "[[rule-documentation]]"]
origin: raw/2026-09-22/1121/ledger.md#case-316
sprint: migration
created: 2026-09-22
tags: [session, workflow, hooks, harness, librarian, render]
---

## Context

The five phases of a session — `rule-session-start`, `rule-plan-mode`, `rule-work-mode`, `rule-end-of-work`, `rule-documentation` — stand as root MOCs with no parent, and their order lives only in the table of §9 of `index.md`. By the rule "a Rule MOC is a workflow" the order of the children is the content, and the MOC's Estimate promises it. Each phase holds its own cross-cutting Estimate inside itself: `estimate-session-start-context` the difference between an ordinary and a working session, `estimate-end-of-work-order` the order Retro → commit → handoff → librarian. Nobody holds the chain whole: that all five left their marks in the session folder, and in that order. Pages: of the five, `rule-session-start`, `rule-plan-mode` and `rule-end-of-work` are `built`, `rule-work-mode` and `rule-documentation` `draft`; the slugs `rule-session` and `estimate-session-phases-in-order` are free by the Grep over `rules/` and `estimates/`, the nearest are `rule-session-start` (the first phase, not the chain) and `rule-harness` (the tools outside the phases). The Estimates of the phases are untouched: a parent is a field, not a promise (case 296).

## Problem

Where the order of the phases lives once `index.md` is gone, and what promises that the chain ran whole.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-316
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
