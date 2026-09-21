---
type: decision
case: "298"
status: current
defer: ["[[rule-prespec]]", "[[rule-materialize]]", "[[rule-page-generation]]"]
origin: raw/2026-09-21/1315/ledger.md#case-298
sprint: migration
created: 2026-09-21
tags: [session, workflow, harness, ledger]
---

## Context

296 superseded 291.1 before the Spec was approved. The Spec of 1315 still holds 291.1 whole — its sections, its `then` block, its five task lines — and nothing ticks or removes them: `generate` neither applies nor ticks the entries of a superseded Case (151, 200.2), `tick_read` skips its `read` lines (286), Retro does not count its lines (282). The lines stay `[ ]` for good, and an open box that nobody will close reads like debt. The rule that the replaced text stays in the Spec of its session (index §7, the Case schema) is right for a supersede from a later session, whose Spec is archived history; inside one session the Spec is the plan the person approves, and a Case superseded before the approval was never the plan.

## Problem

The Spec should hold what the session is going to do. A Case superseded in the same session is removed by the agent and the superseding Case is written whole — as the schema already asks of a taken-up defer — and pre-spec catches a superseded Case still in the plan. Two scripts lean on the Case being there: `materialize` takes the decision entry's text and `then` from the Spec and would mark the entry `incomplete: [then]`; `generate` writes the Decision page of the superseded Case from that text.

## Deferred

### [[rule-prespec]]

prespec --check reads every {supersedes:case N} of the session's ledger and prints a line when ## Case N or ### Case N still stands in the plan — the superseded Case leaves the Spec, the superseding one is written whole; the check runs to a clean output like the others (owner, Retro of 1315)

### [[rule-materialize]]

a decision entry marked superseded_by with no Case of its number in the Spec is complete by the mark alone — no incomplete: [then], no case_text; the replaced text is the ledger lines and the Decision page of the superseding Case

### [[rule-page-generation]]

the Decision page of a Case superseded in its own session is written with status superseded and a one-line body — superseded by case N before the Spec was approved — so origin and deferred_by resolve as before; the supersede from a later session keeps the text of the archived Spec as today

## History

- 2026-09-21 created · raw/2026-09-21/1315/ledger.md#case-298
- 2026-09-21 ## Deferred written by hand from Spec 1315 lines 379–387 — the then block of 298 was not YAML · one-off migration · raw/2026-09-21/1853/spec.md#case-299.4
