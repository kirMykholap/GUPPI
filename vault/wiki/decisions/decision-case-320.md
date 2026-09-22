---
type: decision
case: "320"
status: current
create: ["[[estimate-sprint-migration-file-route-gone]]"]
update: ["[[rule-case-protocol]]", "[[rule-lint]]", "[[rule-decisions-schema]]", "[[rule-prespec]]", "[[estimate-case-protocol-case-form]]", "[[estimate-generate-fails-alone]]", "[[estimate-generate-ticks-the-spec]]", "[[estimate-prespec-checks-the-plan]]", "[[entity-sprint-migration]]"]
delete: ["[[estimate-materialize-finds-a-rule-class-item]]"]
supersedes: ["[[decision-case-310.4]]"]
origin: raw/2026-09-22/1121/ledger.md#case-320
sprint: migration
created: 2026-09-22
tags: [sprint, workflow, harness, ledger, session, render, schema, tests]
---

## Context

A Rule-class file changed by a route of its own: `RULE_CLASS` and `rule_class_path` in `materialize.py` give an entry `category: file` with its `path`, `generate` prints "a Rule-class file, applied by hand" and marks it applied, `prespec` matches an item by `file` in `line_has_item` and `item_has_line`, and `check_governed` refuses a `file` on a path a live rule governs. After 304 (the schemas as Renders of rules), 306 (the glossary) and 318 (`index.md` deleted) no file of that class is left; `prose_names` left lint with 304. The route is described on four pages (`rule-case-protocol`, `rule-lint`, `rule-decisions-schema`, `rule-prespec`) and in the Criteria of four Estimates; `estimate-materialize-finds-a-rule-class-item` (`passed`) promises the route itself. Case 310.4 of this session created the Estimate of theme 5 with the line "a ledger line with `file` is `unparsed`" — wrong: `file` is a key of a `then` item, not part of a ledger line, and a slug without a prefix lands `category: unknown`. This Case is written whole in its place. `rule-morph` (defer 239, Slice 5) does not touch the route — it is about the category set of a project, and its compatibility with the six schema rules is already held by 304.

## Problem

The route is dead but alive in four scripts, on four pages and in four promises; and the promise of theme 5 is worded wrong.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-320
