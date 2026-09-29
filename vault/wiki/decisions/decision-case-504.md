---
type: decision
case: "504"
status: current
defer: ["[[rule-complaint-becomes-a-lesson]]"]
origin: raw/2026-09-29/0137/ledger.md#case-504
sprint: migration
created: 2026-09-29
tags: []
---

## Context

A complaint of the person about the agent's text or work is a lesson: what is worth keeping is a `lesson` line or a Case. In session 0137 the person complained that the numbering of the report after pre-spec was unreadable. The agent fixed the report and wrote no lesson, because nothing in the flow asks it whether a reply of the person is a complaint.

## Problem

Whether a hook should, after each reply of the person, raise the question "does this reply hold a complaint?", so that a complaint becomes a lesson line.

## Deferred

### [[rule-complaint-becomes-a-lesson]]

After each reply of the person a hook raises the question whether it holds a complaint about the agent's text or work, and a complaint becomes a lesson line; an idea of session 0137, not yet decided

## History

- 2026-09-29 created · raw/2026-09-29/0137/ledger.md#case-504
