---
type: entity
kind: Leaf
purpose: The repository works by the model of its rule pages — Phase 1 and Phase 2 of docs/migration/migration-plan.md closed
status: archived
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
Estimate of this page passes: lint clean, the leftovers gone, `make test` green on the last commit of `migration`, the
Rule-class files dissolved, `index.md` gone, the `file` route out of the scripts. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (`rule-sprint-close`, case 632.3).

## Milestones

### Slice 5 — closing

- the close of `migration` — `/sprint-close`, a session of its own

## Backlog

- [[rule-work-mode]] — the rest of Work Mode past the skill `/work` of case 479.2: the test of each Estimate written first and turned green, and the full model the person plans; cases 183, 206
- [[rule-spec-box]] — the Spec box, its second part: a conserved Spec checked against the pages changed after it was conserved, a Case on such a page built again, ratified again and written into the folder of the conserved Spec, and a conserved Spec taken after other Cases of its session (case 591)
- [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239

## Closed

Slices 0–2 closed by 2026-09-10: layout; ledger, event log, `/hi`; renderer, lint,
indexes, `/ask`, pre-spec (then `/pre-task`). Slice 3 (materialize, generate, cleanup, librarian, retro,
handoff) built 2026-09-10, closed 2026-09-12. Slice 3c (the raw lifecycle: the archive
of an applied session, the tail, one archive root, the ledger of a session, the status
cascades, the slug checked against the archive) built 2026-09-13. Slice 3d (the
Estimate model, case 182) opened and closed 2026-09-16: Cases 187–190 ratified in
session 1034 and conserved, repaired by 193–198 and built in session 1651, case 191
taken up by 201–203 and built in session 1955 — `generate`, `lint`, `pre-spec` by the
model. The recut of each old Estimate ran on past the Slice, 42 pages at the close of 3d; Slice 3g recut the last of them (cases 484-500) and closed with case 506, which took the checks of the old shape out of the scripts. `/grill-me` has its page since case 443.1, `rule-skill-grill-me`. `git pull` and `gh` left `/hi` with the remote of the product repository, kept since decisions 11.1 and 11.2 (case 528).

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
- 2026-09-27 updated: /grill-me has its rule page (case 443.1) · [[decision-case-443.1]]
- 2026-09-28 updated: a note in Slice 5: the sprint page and its Estimates go to the archive together at the close of a sprint, once each has passed (case 478.2) · [[decision-case-478.2]]
- 2026-09-28 updated: the Backlog entry of rule-work-mode names what is left past the skill /work; the sentence on a red check stands in rule-retro (case 479.2) · [[decision-case-479.2]]
- 2026-09-28 updated: Slice 3g: the Estimates of rule-prespec recut to When and Then; the note on every other Estimate stands (case 484) · [[decision-case-484.7]]
- 2026-09-28 updated: Slice 3g: the old-layout Estimates of session start and /hi recut to one Criterion; the note on the old layout stands (case 485) · [[decision-case-485.6]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-glossary, entity-glossary and entity-guppi recut to When and Then; the note on every other Estimate stands (case 488) · [[decision-case-488.6]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-page-generation and rule-materialize recut to When and Then, the two texts overwritten by case 211.3 restored; the note on every other Estimate stands (case 489) · [[decision-case-489.8]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-page-schemas, its five category schemas and rule-vault-layout recut to When and Then; the note on every other Estimate stands (case 490) · [[decision-case-490.8]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-sprint and the Spec tick of rule-render-harness recut to When and Then; the note on every other Estimate stands (case 491) · [[decision-case-491.5]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-claude-md, rule-atomicity and rule-one-judgment-one-implementation recut to When and Then; the note on every other Estimate stands (case 492) · [[decision-case-492.4]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-compact-recall, rule-plan-mode, rule-retro-commit, rule-session and rule-prespec-hook recut to When and Then; the note on every other Estimate stands (case 493) · [[decision-case-493.6]]
- 2026-09-29 updated: Slice 3g: the note on every other Estimate removed, its last group recut (cases 484, 488-494); the note on the old shape stands · [[decision-case-494.6]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-render-harness, rule-settings, rule-default-mode and rule-governed-files-hook recut to one Criterion (case 498) · [[decision-case-498.6]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-end-of-work and rule-handoff recut to one Criterion, the dispatch of the handoff by its path (case 499) · [[decision-case-499.3]]
- 2026-09-29 updated: Slice 3g: the Estimates of rule-ask, rule-index-check, rule-cleanup, rule-raw-archive and rule-tests-clock-pinned recut to one Criterion; the recut of the old shape done (cases 498-500), its note replaced by the note on removing the checks of the old shape · [[decision-case-500.6]]
- 2026-09-29 updated: Slice 3g closed: the checks of the old shape left the scripts, the schema and lint (case 506) · [[decision-case-506.7]]
- 2026-09-29 updated: Slice 4 done: the parked pages and the documents of 2026-08 deleted, the item moved to Slice 5 for its reading at the close; Slice 4 removed (case 510) · [[decision-case-510]]
- 2026-09-30 moved to the Backlog: estimate-sprint-migration-lint-clean passed over in 3 sessions in a row — 0138, 2024, 1753 · generate
- 2026-09-30 moved to the Backlog: estimate-sprint-migration-merges passed over in 3 sessions in a row — 0138, 2024, 1753 · generate
- 2026-09-30 moved to the Backlog: rule-spec-box passed over in 3 sessions in a row — 0138, 2024, 1753 · generate
- 2026-09-30 moved to the Backlog: rule-morph passed over in 3 sessions in a row — 0138, 2024, 1753 · generate
- 2026-09-30 updated: Slice 5: the raw date folders, git pull and gh decided; the remote removed; the merge item no longer names the two rules (case 528.5) · [[decision-case-528.5]]
- 2026-09-30 updated: the finish conditions lint-clean, merges and leftovers-gone stand only under Done when: off Slice 5 and the Backlog (case 539.3) · [[decision-case-539.3]]
- 2026-10-02 updated: the Backlog line of rule-spec-box names its second part (case 593.2) · [[decision-case-593.2]]
- 2026-10-03 updated: Slice 5: the close of a sprint is the item rule-sprint-close, and where the close runs is a note, not decided (case 612.1) · [[decision-case-612.1]]
- 2026-10-03 deferred · [[decision-case-615]]
- 2026-10-04 defer by decision-case-615 superseded · [[decision-case-627.1]]
- 2026-10-04 updated: Slice 5: the item rule-sprint-close names case 627, which builds the command of the close; the question put off by case 615 closed (case 627.1) · [[decision-case-627.1]]
- 2026-10-04 updated: the Slice 5 note on where the close runs cut into the close of migration; make test in the Purpose for the branch merged; the merge a Backlog line for the next sprint; the question put off by case 615 closed (case 628.9) · [[decision-case-628.9]]
- 2026-10-04 updated: each Estimate of the page is read before the close; one not passed is archived with the page (case 632.3) · [[decision-case-632.3]]
- 2026-10-05 deferred · [[decision-case-642]]
- 2026-10-06 defer by decision-case-642 superseded · [[decision-case-680]]
- 2026-10-06 updated: the five plain notes of the Backlog — the product model, reuse three times, the template engine — and the line of rule-subagent-guppi leave; the defer of the close of migration is retired, and the close stays the milestone of Slice 5 · [[decision-case-680]]
- 2026-10-09 updated: the close line takes the form that starts /sprint-close; the merge into main leaves the Backlog for the closing Case of /sprint-close (case 743.8) · [[decision-case-743.8]]
- 2026-10-10 updated: Slice 5 holds the close line alone: rule-sprint-close left the milestone, its pending Estimates settled by the closing Case (case 753) · [[decision-case-753]]
- 2026-10-10 updated: the close of the sprint, case 755: its readings taken in the closing session, the close line run by the librarian · [[decision-case-755]]
- 2026-10-10 status: draft → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
