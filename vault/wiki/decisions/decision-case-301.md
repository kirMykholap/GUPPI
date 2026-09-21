---
type: decision
case: "301"
status: current
create: ["[[estimate-sprint-migration-rule-class-files-dissolved]]"]
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-09-21/1853/ledger.md#case-301
sprint: migration
created: 2026-09-21
tags: [sprint, workflow, harness]
---

## Context

The vault is a tree of pages: one `parent` per page, `children` on a MOC, the other edges wikilinks — `estimates`, `deferred_by`, History. Fourteen files stand outside that tree — `index.md`, `glossary.md`, six `schema.md` and six `schema.yaml`: "Rule-class" by §1 of `index.md`, changed only by a ratified `update` with `file`, by hand in Work Mode. No `purpose`, no History, no Estimates; `ask-guppi` finds them by grep, not by the index lines; pre-spec corrects them with a guard of their own (`check_governed`, `file` against `slug`). The scripts keep a route of their own for them: `RULE_CLASS` and `category: file` in `materialize.py`, "a Rule-class file, applied by hand" in `generate.py`, `rule_class_path` in `prespec.py`, `prose_names` in `lint.py` — the check that the md tables and the yaml agree, a guard on two records of one condition not drifting apart. What the files are: `schema.yaml` is the input of lint, a condition with a guard, a Rule without a page; `schema.md` its prose; `glossary.md` a fast map of the terms, 28 rows pointing at a page and 23 at a `§N` of `index.md` — the count of what has not migrated; `index.md` (438 lines, 13 §) the document the rules migrated from, so every change of a rule is made twice, on the page and in its §; its own §11 says the index of a category is computed by its reader, written by nobody (147.8) — the map file stands outside that rule. The mechanisms of the replacement exist: `render_mode: full` writes any text into `governs`, yaml included (273, `render.py`); `guppi sprint` writes `sprint.md` from the fields of a page under a Rule with `governs`, `implementation_ref` and `--check` (209, 229). The product — a developer's vault on their own codebase — must have no "by hand" route: without it there is no History and no guard; the `file` route is a crutch of the migration. Rejected in the discussion: two rules per category (yaml and md) — one condition signed twice (72.1, 188); a render of `schema.md` — a Leaf has no section for prose, the mechanism lives in the Render or the docstring; a rule per glossary term — a term is no condition with a guard, ~50 pages with a required `estimates`; `replace` pairs written into the file by the script (Case 300 of this session, not ratified) — leaves the files outside the graph; a notes folder under `raw/` — ratification by pointer, a second memory nobody signed; a template engine for the renders — two shapes are not yet a pattern, Backlog. The edge Rule → Entity does not exist in the model: `rule-sprint` names `entity-sprint` in a code span, not a wikilink; it is the Backlog item "`applies_to` on a Rule, `rules` on an Entity" (session 1119) — taken into the Slice. The pages: `entity-sprint-migration` `draft`, an `update` with a `ref`; its three Estimates (lint clean, leftovers gone, merges) the Case does not touch — it creates a fourth; the `purpose` of the entity ("the model in `wiki/index.md`") changes in theme 4, not here. The slug of the new Estimate is free.

## Problem

How these files become vertices of the graph with edges, a `purpose` and Estimates, and whether the "by hand" route leaves the scripts — a programme the size of a Slice, to be fixed as the current milestone of the sprint with a Definition of done, and done from the next session on.

## History

- 2026-09-22 created · raw/2026-09-21/1853/ledger.md#case-301
