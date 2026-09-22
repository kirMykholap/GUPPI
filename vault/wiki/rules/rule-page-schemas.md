---
type: rule
kind: MOC
purpose: Prevents the shape of a page category from living in a file nobody ratified — each schema is a rule page and its yaml the Render
status: draft
parent: "[[rule-harness]]"
children: ["[[rule-entities-schema]]", "[[rule-rules-schema]]", "[[rule-estimates-schema]]", "[[rule-lessons-schema]]", "[[rule-insights-schema]]", "[[rule-decisions-schema]]"]
estimates: ["[[estimate-page-schemas-one-file-per-rule]]"]
origin: raw/2026-09-22/0014/ledger.md#case-304.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Purpose

Prevents the shape of a page category from living in a file nobody ratified. Until case 304 the six `schema.yaml` and their `schema.md` stood outside the graph — no `purpose`, no History, no Estimate, changed by hand by an `update` with `file`. Each child renders one `vault/wiki/<category>/schema.yaml`: the lists lint reads, the prose of the former `schema.md` as data under `description`, `fields`, `sections` and `examples`. Lint reads the file, the governed-files hook refuses a hand edit of it. The schemas are read in every phase — the agent's `then` block in Plan Mode, `materialize` and `generate` in Documentation, lint with the renderer — so the MOC sits under `rule-harness`, as `rule-lint` does. The order of the children is the order of `CATEGORIES` in `materialize.py`. No `applies_to` on a schema rule: a schema applies to a category of pages, not to a page (case 304).

## History

- 2026-09-22 created · [[decision-case-304.1]]
