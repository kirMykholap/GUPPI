---
type: entity
kind: MOC
purpose: The repository works by the model in wiki/index.md — Phase 1 and Phase 2 of docs/migration/migration-plan.md closed
status: draft
children: []
estimates: ["[[estimate-sprint-migration-lint-clean]]", "[[estimate-sprint-migration-leftovers-gone]]", "[[estimate-sprint-migration-merges]]"]
origin: raw/2026-09-16/2238/ledger.md#case-209.2
sprint: migration
created: 2026-09-16
tags: [sprint, workflow]
---

## Purpose

Open since 2026-09-09. The repository works by the model in `wiki/index.md`: Phase 1
(the harness built by its own rules) and Phase 2 (the surviving pages brought into
conformance) of `docs/migration/migration-plan.md` are closed. Done when the three
Estimates of this page pass: lint clean, the leftovers gone, the branch merged.

## Milestones

### Slice 3b — Work Mode

- [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; cases 183, 206
- [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206

### Slice 4 — conversion of the parked pages by group

- [[estimate-sprint-migration-leftovers-gone]] — every page of `vault/parked/` and every document of 2026-08 under `docs/` converted, archived or deleted by a decision

### Slice 5 — closing

- [[estimate-sprint-migration-lint-clean]] — `make lint` exit 0: the 31 Decision pages of Cases 1–28 decided, `unmigrated` at zero
- [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`
- [[rule-spec-box]] — the Spec box, case 207, after Slice 3b

## Backlog

- the categories as data of the project: `generate`, `lint`, `materialize` and `ask-guppi` read the category set from `wiki/<category>/schema.yaml`; the development set — entity, rule, estimate — is the default (session 1119)
- the product model: `applies_to` on a Rule and `rules` on an Entity, `kind: test | measurement | reading`, `ask-guppi` through Entities, the pre-task questions before a product's records (session 1119)

## Closed

Slices 0–2 closed by 2026-09-10: layout; ledger, event log, `/hi`; renderer, lint,
indexes, `/ask`, pre-task. Slice 3 (materialize, generate, cleanup, librarian, retro,
handoff) built 2026-09-10, closed 2026-09-12. Slice 3c (the raw lifecycle: the archive
of an applied session, the tail, one archive root, the ledger of a session, the status
cascades, the slug checked against the archive) built 2026-09-13. Slice 3d (the
Estimate model, case 182) opened and closed 2026-09-16: Cases 187–190 ratified in
session 1034 and conserved, repaired by 193–198 and built in session 1651, case 191
taken up by 201–203 and built in session 1955 — `generate`, `lint`, `pre-task` by the
model. The recut of each old Estimate at its first touch runs on past the Slice: lint
counts the remainder as `unmigrated` (42 at the close of 3d) and the old shape is
removed when it reaches zero. Kept without a page: `/grill-me`; `git pull` in `/hi`
without an upstream (decision 11.1); `gh` not logged in, no GitHub remote (11.2) —
both decided again at the close (`estimate-sprint-migration-leftovers-gone`).

## History

- 2026-09-17 created · [[decision-case-209.2]]
- 2026-09-17 estimate estimate-sprint-migration-lint-clean added · [[decision-case-209.2]]
- 2026-09-17 estimate estimate-sprint-migration-leftovers-gone added · [[decision-case-209.3]]
- 2026-09-17 estimate estimate-sprint-migration-merges added · [[decision-case-209.4]]
- 2026-09-18 updated: the Slices under Milestones, a Backlog of two plain lines without a page (case 229.1) · [[decision-case-229.1]]
