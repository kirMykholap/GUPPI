# Sprint

## migration

Open since 2026-09-09. The repository works by the model of its rule pages: Phase 1
(the harness built by its own rules) and Phase 2 (the surviving pages brought into
conformance) of `docs/migration/migration-plan.md` are closed. Done when every
Estimate of this page passes: lint clean, the leftovers gone, `make test` green on the last commit of `migration`, the
Rule-class files dissolved, `index.md` gone, the `file` route out of the scripts. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (`rule-sprint-close`, case 632.3).

**Done when**

- [ ] make lint in the Work Mode of the session that closes the sprint, before the librarian's run, shows no finding, unmigrated included, but the unread of the sprint page's own Estimates and of the Estimates read only at or after the closing librarian's run, which the close line carries · pending
- [ ] vault/parked/, the 2026-08 documents and the old archive root are gone, git tracks no raw date folder without a session, and the repository has no remote, each by a decision named in the reading, read in the Work Mode of the session that closes the sprint · pending
- [ ] make test green on the last commit of migration, read in the Work Mode of the session that closes it · pending
- [x] No Rule-class file at the close of Slice 3f — the schemas rendered from rule pages, the glossary from entity-glossary, index.md gone, the file route out of the scripts · passed
- [x] index.md is gone and no live page, harness file or script docstring points at a §N of it or at the file as a source · passed
- [x] The file route is out of the scripts — no RULE_CLASS, rule_class, applied by hand or prose_names in guppi/; an update item with file is a pre-spec finding; a slug without a prefix lands category unknown; tests green and no lint finding on the schema.yaml of a category folder · passed

## Milestones

### [ ] Slice 5 — closing

- [ ] [[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (cases 612.1, 627) · draft
- [ ] the close of migration — a session of its own: the pending readings taken in groups, `make test`, `make lint` and the tree read in its Work Mode, then `uv run guppi sprint-close --sprint migration --apply` in the librarian's run (case 628.9)

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
