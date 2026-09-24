---
type: entity
kind: Leaf
purpose: The repository works by the model of its rule pages — Phase 1 and Phase 2 of docs/migration/migration-plan.md closed
status: draft
parent: "[[entity-sprint]]"
estimates: ["[[estimate-sprint-migration-lint-clean]]", "[[estimate-sprint-migration-leftovers-gone]]", "[[estimate-sprint-migration-merges]]", "[[estimate-sprint-migration-rule-class-files-dissolved]]", "[[estimate-sprint-migration-index-dissolved]]", "[[estimate-sprint-migration-file-route-gone]]"]
origin: raw/2026-09-16/2238/ledger.md#case-209.2
sprint: migration
created: 2026-09-16
tags: [sprint, workflow]
---

## Purpose

Open since 2026-09-09. The repository works by the model of its rule pages: Phase 1
(the harness built by its own rules) and Phase 2 (the surviving pages brought into
conformance) of `docs/migration/migration-plan.md` are closed. Done when every
Estimate of this page passes: lint clean, the leftovers gone, the branch merged, the
Rule-class files dissolved, `index.md` gone, the `file` route out of the scripts.

## Milestones

### Slice 3g — the model of the Criterion, one pass over the Estimates

- every other Estimate: `Given:` out, the input of the scenario into `When:`, the `－` lines on the bounds of an edit out, each Criterion replaced whole
- the old shape recut: every Estimate whose Criterion still holds `### case N` blocks brought to one Criterion, until lint counts no `unmigrated` page

### Slice 4 — conversion of the parked pages by group

- [[estimate-sprint-migration-leftovers-gone]] — every page of `vault/parked/` and every document of 2026-08 under `docs/` converted, archived or deleted by a decision

### Slice 5 — closing

- [[estimate-sprint-migration-lint-clean]] — `make lint` exit 0: the 31 Decision pages of Cases 1–28 decided, `unmigrated` at zero
- [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`; at the close [[rule-git-context]] and [[rule-github-issues]] — the upstream of the branch and the GitHub remote, decisions 11.1, 11.2, defers 220, 243 — read by [[estimate-sprint-migration-leftovers-gone]]
- [[rule-spec-box]] — the Spec box, case 207, after Slice 3b
- [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239

## Backlog

- the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)
- reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319)
- reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319)
- reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319)
- a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301)
- [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; the sentence of [[insight-workflow-code-live-before-the-page-it-reads]] on a check that reads a page the same Spec changes; cases 183, 206, 238
- [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206

## Closed

Slices 0–2 closed by 2026-09-10: layout; ledger, event log, `/hi`; renderer, lint,
indexes, `/ask`, pre-spec (then `/pre-task`). Slice 3 (materialize, generate, cleanup, librarian, retro,
handoff) built 2026-09-10, closed 2026-09-12. Slice 3c (the raw lifecycle: the archive
of an applied session, the tail, one archive root, the ledger of a session, the status
cascades, the slug checked against the archive) built 2026-09-13. Slice 3d (the
Estimate model, case 182) opened and closed 2026-09-16: Cases 187–190 ratified in
session 1034 and conserved, repaired by 193–198 and built in session 1651, case 191
taken up by 201–203 and built in session 1955 — `generate`, `lint`, `pre-spec` by the
model. The recut of each old Estimate at its first touch runs on past the Slice: lint
counts the remainder as `unmigrated` (42 at the close of 3d) and the old shape is
removed when it reaches zero. Kept without a page: `/grill-me`; `git pull` in `/hi`
without an upstream (decision 11.1); `gh` not logged in, no GitHub remote (11.2) —
both decided again at the close (`estimate-sprint-migration-leftovers-gone`).

Slice 3f (the Rule-class files into the graph, case 301) opened 2026-09-22 and closed
the same day: the six schemas as rule pages under `rule-page-schemas` (304), the edge
Rule → Entity (305), the glossary as `entity-glossary` under `rule-glossary` (306);
then `rule-vault-layout` (315), `rule-session` over the five phases (316),
`rule-atomicity` rendered into the Case schema (317), `index.md` and its thirty
pointers gone (318), the `file` route out of the scripts (320), the term "Rule-class"
retired (321). A sprint item is a page and a note is a task not yet cut (310, 313).
No file of `vault/wiki/` is written by hand.

## History

- 2026-09-17 created · [[decision-case-209.2]]
- 2026-09-17 estimate estimate-sprint-migration-lint-clean added · [[decision-case-209.2]]
- 2026-09-17 estimate estimate-sprint-migration-leftovers-gone added · [[decision-case-209.3]]
- 2026-09-17 estimate estimate-sprint-migration-merges added · [[decision-case-209.4]]
- 2026-09-18 updated: the Slices under Milestones, a Backlog of two plain lines without a page (case 229.1) · [[decision-case-229.1]]
- 2026-09-18 updated: the morph mechanism as rule-morph in Slice 5; the Backlog line on the categories as data folded into it (case 239) · [[decision-case-239]]
- 2026-09-18 updated: a Leaf under entity-sprint — the sprint by id is a thing with no parts named (cases 240.1, 241) · [[decision-case-241]]
- 2026-09-18 updated: the item rule-work-mode of Slice 3b names the Insight deferred to it by case 238 (case 245) · [[decision-case-245]]
- 2026-09-18 updated: the item estimate-sprint-migration-merges of Slice 5 names rule-git-context and rule-github-issues, read by estimate-sprint-migration-leftovers-gone at the close (case 249, supersedes 247) · [[decision-case-249]]
- 2026-09-20 updated: the Backlog line — pre-task → the vault query (case 277.4) · [[decision-case-277.4]]
- 2026-09-22 updated: Slice 3f — the Rule-class files into the graph — the current milestone, with its Estimate and six themes; applies_to moved from the Backlog into the Slice, the template engine added to it (case 301) · [[decision-case-301]]
- 2026-09-22 estimate estimate-sprint-migration-rule-class-files-dissolved added · [[decision-case-301]]
- 2026-09-22 updated: Slice 3f as page items — themes 1–3 by the pages of 304–306, themes 4–5 by their Estimates, theme 6 into the description; the Estimate line and the Purpose reworded (case 310.2) · [[decision-case-310.2]]
- 2026-09-22 estimate estimate-sprint-migration-index-dissolved added · [[decision-case-310.3]]
- 2026-09-22 updated: theme 4 done — the § covered by pages, the file and its pointers gone (case 318) · [[decision-case-318]]
- 2026-09-22 updated: three notes of the reuse model in the Backlog — the edge, the question, the hook (case 319) · [[decision-case-319]]
- 2026-09-22 estimate estimate-sprint-migration-file-route-gone added · [[decision-case-320]]
- 2026-09-22 updated: theme 5 done — the file route out of the scripts (case 320) · [[decision-case-320]]
- 2026-09-22 updated: Slice 3f closed — out of Milestones, named in Closed with its cases (case 321) · [[decision-case-321]]
- 2026-09-22 updated: the Purpose off index.md and off a count of Estimates (case 323) · [[decision-case-323]]
- 2026-09-23 moved to the Backlog: rule-work-mode passed over in 29 sessions in a row — 0034, 2046, 1121, 0014, 1853, 1315, 0019, 2106, 1749, 1308, 0958, 0740, 0527, 2253, 2054, 1957, 1252, 1119, 2238, 1955, 2225, 1809, 1448, 1110, 1633, 1229, 1029, 0747, 0652 · generate
- 2026-09-23 moved to the Backlog: rule-subagent-guppi passed over in 29 sessions in a row — 0034, 2046, 1121, 0014, 1853, 1315, 0019, 2106, 1749, 1308, 0958, 0740, 0527, 2253, 2054, 1957, 1252, 1119, 2238, 1955, 2225, 1809, 1448, 1110, 1633, 1229, 1029, 0747, 0652 · generate
- 2026-09-23 milestone Slice 3b — Work Mode left the Milestones: its items moved to the Backlog · generate
- 2026-09-23 updated: Slice 3g, the one pass over the Estimates, ahead of Slice 4 (case 381) · [[decision-case-381]]
- 2026-09-25 updated: Slice 3g cut into four notes — the eleven, the journals, Given: out of the rest, the old shape (case 395) · [[decision-case-395]]
- 2026-09-25 updated: Slice 3g: the note of the eleven Estimates done — cases 396 to 400, 388 for estimate-prespec-reconciles (case 400.2) · [[decision-case-400.2]]
- 2026-09-25 updated: Slice 3g: the note of the journals done (case 401) · [[decision-case-401.8]]
