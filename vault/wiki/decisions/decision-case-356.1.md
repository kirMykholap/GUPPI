---
type: decision
case: "356.1"
status: current
update: ["[[rule-skill-hi]]", "[[rule-prespec]]", "[[estimate-hi-writes-frontier]]", "[[estimate-prespec-checks-the-plan]]", "[[rule-case-protocol]]", "[[estimate-case-protocol-loaded]]"]
supersedes: ["[[decision-case-352]]"]
origin: raw/2026-09-23/0034/ledger.md#case-356.1
sprint: migration
created: 2026-09-23
tags: [session, harness, workflow, tests, ledger]
---

## Context

As the page `decision-case-352` stands: Case 346 of plan 2046 deferred `rule-skill-hi` and `rule-prespec` with one question — what a Frontier closer must tell apart. Case 351 of the same plan changed the Render of `rule-prespec`, and by case 186.2 a Case that changes a page another Case of the same plan defers is a finding; so 352 deferred `rule-skill-hi` alone. The questions of the defer: whether a Work line closes in a second moment of its own; whether pre-spec requires closed lines under `Cases` alone; whether `· sprint` and `· defer case N` stay two closers or become one; and whether a session that passes over an item of the sprint leaves any trace. The trace is answered by 354.1: `guppi archive` keeps every `frontier.md`, and `generate` counts the passes from it; no page changes for it. `rule-prespec` is changed by this Case itself and needs no defer.
`rule-skill-hi` stands `draft` with `deferred_by` 352; `rule-prespec` stands `draft`, with no defer; `rule-case-protocol` stands `draft`, and its Plan Mode paragraph says Plan Mode does not end while a line is open and lists the closers without `· sprint`; in this plan 354.3 changes `rule-skill-hi` and 355 `rule-case-protocol` too, and no defer stands in this plan, so 186.2 does not fire. `estimate-hi-writes-frontier` of `rule-skill-hi`, `estimate-prespec-checks-the-plan` of `rule-prespec` and `estimate-case-protocol-loaded`, the live reading of the Render of `rule-case-protocol`, are touched; `estimate-prespec-binds-a-sprint-line` speaks of the closer `case N` alone and `estimate-prespec-reconciles` of no kind of Frontier line — neither is touched.

## Problem

The defer of a page and the change of that page stand in one plan. Either the question loses its second page, or the change waits a session.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-356.1
