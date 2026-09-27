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
- [x] No Rule-class file at the close of Slice 3f — the schemas rendered from rule pages, the glossary from entity-glossary, index.md gone, the file route out of the scripts · passed
- [x] index.md is gone and no live page, harness file or script docstring points at a §N of it or at the file as a source · passed
- [ ] The file route is out of the scripts — no RULE_CLASS, rule_class, applied by hand or prose_names in guppi/; an update item with file is a pre-spec finding; a slug without a prefix lands category unknown; tests green and lint clean on the schemas · pending

## Milestones

### [ ] Slice 3g — the model of the Criterion, one pass over the Estimates

- [ ] every other Estimate: `Given:` out, the input of the scenario into `When:`, the `－` lines on the bounds of an edit out, each Criterion replaced whole
- [ ] the old shape recut: every Estimate whose Criterion still holds `### case N` blocks brought to one Criterion, until lint counts no `unmigrated` page

### [ ] Slice 4 — conversion of the parked pages by group — 1 item: [[estimate-sprint-migration-leftovers-gone]]

### [ ] Slice 5 — closing — 4 items: [[estimate-sprint-migration-lint-clean]], [[estimate-sprint-migration-merges]], [[rule-spec-box]], [[rule-morph]]

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
removed when it reaches zero. `/grill-me` has its page since case 443.1, `rule-skill-grill-me`. Kept without a page: `git pull` in `/hi`
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
