---
type: decision
case: "454"
status: archived
defer: ["[[rule-claude-md]]"]
superseded_by: ["[[decision-case-459]]"]
origin: raw/2026-09-27/1255/ledger.md#case-454
sprint: migration
created: 2026-09-27
tags: [harness, render]
---

## Context

`make lint` reports a contradiction: the `method` of `estimate-claude-md-rendered` says the reading is by hand, while `estimate-language-spec-prose-in-english`, an Estimate of `rule-language`, whose Render sits in `CLAUDE.md`, names a test file.

## Problem

Whether the method of `estimate-claude-md-rendered` changes, or the lint finding is wrong. The person defers it to a later session.

## Deferred

### [[rule-claude-md]]

The method of estimate-claude-md-rendered says by hand while estimate-language-spec-prose-in-english names a test file; lint reports the pair as a contradiction

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#case-454
- 2026-09-27 superseded by decision-case-459 · [[decision-case-459]]
- 2026-09-27 archived · superseded
- 2026-09-27 archived · cleanup
