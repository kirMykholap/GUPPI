---
type: decision
case: "721"
status: current
defer: ["[[rule-orchestration]]", "[[rule-case-protocol]]"]
origin: raw/2026-10-07/1804/ledger.md#case-721
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness, ledger]
---

## Context

At the `/pre-spec` of session 1804 `ask-guppi` found five faults in Case 713, the take-back of a ratified Case, which stays ratified as it was: the take-back stands under the short-form paragraph of `rule-orchestration` whose closer is `[-] … · defer case N` (F2); the same sentence says the `defer` lines add to the source and that the source stays as it is (F3); a take-back of a Case whose only targets are existing Estimates leaves nothing in `backlog.md`, against `rule-backlog` (F4); `rule-case-protocol` says a Frontier line is closed again by the superseding Case, which the closer of a sprint or backlog item does not name (F5); the Criterion of `estimate-orchestration-defers-in-one-reply` says a sprint or backlog item takes no short Case (F6). Case 719, built to fix them by superseding 713, was dropped: the store of the Case-file check kept stale sub-cases 713.1 and 713.2 and refused its showing (Case 720). The person put the fixes off to the next session. `estimate-orchestration-defers-in-one-reply` is an Estimate, which a `defer` does not mark; its fault is named here.

## Problem

No Case of this session fixes the faults the pre-spec found in the take-back of a ratified Case.

## Deferred

### [[rule-orchestration]]

The take-back of a ratified Case as Case 713 sets it holds the pre-spec faults F2–F6 of session 1804: two closers for one reply, a sentence that contradicts itself, a take-back that leaves nothing in backlog.md, and the Criterion of estimate-orchestration-defers-in-one-reply left unchanged

### [[rule-case-protocol]]

A Frontier line closed again by the superseding Case does not hold for a sprint or backlog item whose Case is taken back (pre-spec F5 of session 1804)

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#case-721
