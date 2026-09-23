---
type: decision
case: "375"
status: archived
defer: ["[[rule-retro]]"]
superseded_by: ["[[decision-case-376]]"]
origin: raw/2026-09-23/1126/ledger.md#case-375
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness, render]
---

## Context

The Render of `rule-retro` asks the Retro to open with the frontier — what was ratified, the lines of the Tail grouped by Case, one line per Case, and the unticked boxes of the Spec per Case — and to close with three lists: every ratification of the session, what got done, what did not. In session 1126 the report followed it and the person found two defects: the ratifications stand twice, once at the opening by the Tail and once in the closing list; and the unticked boxes of the Spec stand apart from "what did not get done", though they are part of it.
`rule-retro` is not changed in this session; a Retro ratifies no `create`, `update` or `delete`.

## Problem

The report of `/retro` names the same ratifications twice and splits what is not done into two places, so the person reads more and finds the open work in two lists.

## Deferred

### [[rule-retro]]

The report of /retro holds each fact once — the ratifications in one list, the person proposing to drop the opening list by the Tail and keep the closing one; and the unticked boxes of the Spec, those waiting for the librarian and those that are debt, inside the list of what is not done rather than a list of their own

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-375
- 2026-09-23 superseded by decision-case-376 · [[decision-case-376]]
- 2026-09-23 archived · superseded
- 2026-09-23 archived · cleanup
