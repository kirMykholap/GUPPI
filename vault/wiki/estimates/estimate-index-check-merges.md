---
type: estimate
kind: QA
status: pending
target: "[[rule-index-check]]"
purpose: The librarian's index check turns a create whose thing already has a page into an update of that page and marks a near one, comparing within one category by the Grep of its index lines
method: by hand on the report of a later librarian's run, against its materialize.yaml
origin: raw/2026-09-10/ledger.md#case-35.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Criterion

When:
The librarian's run does the index check of `.claude/agents/librarian-guppi.md`, as rendered from `rule-index-check`, over the `create` entries of each `materialize.yaml`.

Then:
For each `create` other than an Estimate, the librarian runs the Grep of its category under `vault/wiki/`: `^(purpose|deferred_by):`, `root_cause` for lessons, `pattern` for insights. It compares the entry's `purpose`, or `root_cause` for a lesson, with every line the Grep returns.
**＋** The report names each Grep and the number of lines compared.
**＋** A `create` whose thing already has a page becomes an `update` of that slug with `change: "merged by librarian: <why>"` and `librarian: merged`, every other field of the entry as it was.
**＋** A page that is close but not the same keeps the entry and adds `near: <slug>`.
**＋** Every page opened is named in the report, with the index line that did not settle same or near.
**－** No comparison crosses categories.

## Result

live 2026-09-15, the librarian's run of session Q read against the brief: four lesson creates compared against the Grep `^(root_cause|deferred_by):` over `wiki/lessons/`, 27 lines named with their count; 0 merged and none was due; 1 near (`lesson-retro-typed-still-bypasses-the-skill-tool-after-150` near `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate`) settled on the index line with the reason; no page opened; no create in another category, the Greps of `rules/` and `entities/` not run; no comparison crossed categories

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L90
- 2026-09-10 updated: an opened page is named in the report with the index line that did not settle it · raw/2026-09-10/ledger.md#case-49
- 2026-09-11 status: passed → passed · raw/2026-09-10/ledger.md#L125
- 2026-09-14 criterion: case 147.3 added · [[decision-case-147.3]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1448/ledger.md#L1
- 2026-09-29 updated: the Criterion replaced whole — the head and the block 147.3 into one When and Then, the bound on the rule's name out; purpose and method set, Context and Method out (case 500.2) · [[decision-case-500.2]]
