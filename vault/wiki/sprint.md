# Sprint

## migration

Open since 2026-09-09. The repository works by the model in `wiki/index.md`: Phase 1
(the harness built by its own rules) and Phase 2 (the surviving pages brought into
conformance) of `docs/migration/migration-plan.md` are closed. Done when the three
Estimates of this page pass: lint clean, the leftovers gone, the branch merged.

**Done when**

- [ ] make lint exits 0 at the close of the sprint, unmigrated included, but for the unread of the sprint page's own Estimates · pending
- [ ] vault/parked/, the 2026-08 documents, the old archive root and the empty raw date folders are gone by decision at the close of the sprint · pending
- [ ] make test green on the last commit of migration and the branch merged into main · pending
- [ ] No Rule-class file at the close of Slice 3f — the schemas rendered from rule pages, the glossary from terms, index.md gone, the file route out of the scripts · pending

## Milestones

### [ ] Slice 3f — the Rule-class files into the graph

The vault is a graph of pages; fourteen files stand outside it — `index.md`, `glossary.md`, six `schema.md` and six `schema.yaml` — changed by hand, without `purpose`, History or Estimates, and kept by a route of their own in the scripts. The Slice brings each into the graph by its nature and removes the "by hand" route: a developer's vault changes only by the scripts, from decisions (case 301).
- [ ] [[estimate-sprint-migration-rule-class-files-dissolved]] — no Rule-class file: the schemas rendered from rule pages, the glossary from `terms`, `index.md` gone, the `file` route out of the scripts · pending
- [ ] 1. schemas — six Leaves `rule-<category>-schema`, `enforcement: render`, the Render the `schema.yaml` with the description of its fields as yaml data; `schema.md` gone; one rule per category, never two
- [ ] 2. audit of the rules — the parent of every rule: under a category's MOC a rule that holds for that category alone, the MOC made at two or more such rules, else the schemas under `rule-page-schemas`; `applies_to` on a Rule and `rules` on an Entity, the edge Rule → Entity, `rule-sprint` → `entity-sprint` the first (from the Backlog, session 1119)
- [ ] 3. glossary — `terms` on the page that defines a term; `guppi glossary` writes `glossary.md`, grouped by the parent MOC, under `rule-glossary` with `governs`, `implementation_ref` and `--check`, the pattern of `rule-sprint`; the rows on `§N` resolved as the index dissolves, "Retired terms" into the history of decisions
- [ ] 4. `index.md` — one Case per §: covered by a rule page, the § leaves; not covered, a rule is made; the last Case removes the file and every `§N` pointer in the vault
- [ ] 5. scripts — the audit "script — what it assumes — what changes"; the `file` route and "applied by hand" removed from `materialize`, `generate`, `prespec`, `lint`; the grep of `index.md` out of `rule-ask`; `rule-morph` (Slice 5) kept compatible with six schema rules
- [ ] 6. close — "Rule-class" retired in the Case schema and the glossary; the Estimate read; the Slice moved to Closed

### [ ] Slice 3b — Work Mode — 2 items: [[rule-work-mode]], [[rule-subagent-guppi]]
### [ ] Slice 4 — conversion of the parked pages by group — 1 item: [[estimate-sprint-migration-leftovers-gone]]
### [ ] Slice 5 — closing — 4 items: [[estimate-sprint-migration-lint-clean]], [[estimate-sprint-migration-merges]], [[rule-spec-box]], [[rule-morph]]

## Backlog

- [ ] the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)
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
