---
type: rule
kind: MOC
purpose: Prevents the shape of a page category from living in a file nobody ratified — each schema is a rule page and its yaml the Render
status: built
parent: "[[rule-harness]]"
children: ["[[rule-entities-schema]]", "[[rule-rules-schema]]", "[[rule-estimates-schema]]", "[[rule-lessons-schema]]", "[[rule-insights-schema]]", "[[rule-decisions-schema]]"]
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, render, schema]
core: true
---

## Purpose

Prevents the shape of a page category from living in a file nobody ratified. Each child renders one `vault/wiki/<category>/schema.yaml`: the lists lint reads, the prose of the former `schema.md` as data under `description`, `fields`, `sections` and `examples`. Lint reads the file, the governed-files hook refuses a hand edit of it. The schemas are read in every phase — the agent's `then` block in Plan Mode, `materialize` and `generate` in Documentation, lint with the renderer — so the MOC sits under `rule-harness`, as `rule-lint` does. The order of the children is the order of `CATEGORIES` in `materialize.py`. No `applies_to` on a schema rule: a schema applies to a category of pages, not to a page.

## History

- 2026-10-14 shipped with GUPPI
