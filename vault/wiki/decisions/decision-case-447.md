---
type: decision
case: "447"
status: current
defer: ["[[rule-work-mode]]"]
origin: raw/2026-09-26/2300/ledger.md#case-447
sprint: migration
created: 2026-09-26
tags: []
---

## Context

Today the approved plan is copied to `raw/<date>/<hi HHMM>/spec.md`, and the same file holds the state of the work. The agent ticks its boxes in Work Mode, `generate` ticks the page and `read` lines, `render`, `sprint` and `glossary` tick their command lines, and the Spec hook keeps the ticks of unchanged task lines when a Case is ratified again. Retro, the librarian and `/carry` read the unticked boxes of `spec.md` as open work. So the Spec is at once the signed record and a working file, and the guard of Case 445.1 cannot cover it. The person wants the Spec written by the hook alone and the ticks moved to a separate work file, `raw/<date>/<hi HHMM>/work.md`, the seed of the implementation plan of `rule-work-mode`. The change touches eight promises and a one-off migration of every session under `raw/`.

## Problem

Where the ticks of Work Mode live, and whether the Spec may change during the work other than by the hook. The person defers the decision until the sprint reaches Work Mode; until then the ticks stay in `spec.md` as they are.

## Deferred

### [[rule-work-mode]]

The ticks of Work Mode move out of the Spec into a work file made at approval, the seed of the implementation plan; spec.md is then written by the hook alone and guarded like the plan

## History

- 2026-09-27 created · raw/2026-09-26/2300/ledger.md#case-447
