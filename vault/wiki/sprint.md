# Sprint

## migration

Open since 2026-09-09. The repository works by the model of its rule pages: Phase 1
(the harness built by its own rules) and Phase 2 (the surviving pages brought into
conformance) of `docs/migration/migration-plan.md` are closed. Done when every
Estimate of this page passes: lint clean, the leftovers gone, the branch merged, the
Rule-class files dissolved, `index.md` gone, the `file` route out of the scripts.

**Done when**

- [ ] make lint exits 0 at the close of the sprint, unmigrated included, but for the unread of the sprint page's own Estimates · pending
- [ ] vault/parked/, the 2026-08 documents, the old archive root and the empty raw date folders are gone by decision at the close of the sprint · pending
- [ ] make test green on the last commit of migration and the branch merged into main · pending
- [ ] No Rule-class file at the close of Slice 3f — the schemas rendered from rule pages, the glossary from entity-glossary, index.md gone, the file route out of the scripts · pending
- [ ] index.md is gone and no live page, harness file or script docstring points at a §N of it or at the file as a source · pending
- [x] The file route is out of the scripts — no RULE_CLASS, rule_class, applied by hand or prose_names in guppi/; an update item with file is a pre-spec finding; a slug without a prefix lands category unknown; tests green and lint clean on the schemas · passed

## Milestones

### [ ] Slice 3b — Work Mode

- [ ] [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; the sentence of [[insight-workflow-code-live-before-the-page-it-reads]] on a check that reads a page the same Spec changes; cases 183, 206, 238 · draft · decision-case-183, decision-case-206, decision-case-218, decision-case-231, decision-case-242, decision-case-248, decision-case-252, decision-case-254, decision-case-260, decision-case-263, decision-case-269, decision-case-276, decision-case-281, decision-case-285, decision-case-289, decision-case-293, decision-case-303, decision-case-307, decision-case-322
- [ ] [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206 · draft · decision-case-183, decision-case-206, decision-case-218, decision-case-231, decision-case-242, decision-case-248, decision-case-252, decision-case-254, decision-case-260, decision-case-263, decision-case-269, decision-case-276, decision-case-281, decision-case-285, decision-case-289, decision-case-293, decision-case-303, decision-case-307, decision-case-322

### [ ] Slice 4 — conversion of the parked pages by group — 1 item: [[estimate-sprint-migration-leftovers-gone]]
### [ ] Slice 5 — closing — 4 items: [[estimate-sprint-migration-lint-clean]], [[estimate-sprint-migration-merges]], [[rule-spec-box]], [[rule-morph]]

## Backlog

- [ ] the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)
- [ ] reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319)
- [ ] reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319)
- [ ] reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319)
- [ ] a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301)

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
