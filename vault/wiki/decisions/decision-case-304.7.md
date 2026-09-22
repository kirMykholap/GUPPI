---
type: decision
case: "304.7"
status: current
create: ["[[rule-decisions-schema]]", "[[estimate-decisions-schema-checked]]"]
origin: raw/2026-09-22/0014/ledger.md#case-304.7
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Context

The shape of a page category lives in two files outside the graph: `schema.yaml`, which lint reads, and `schema.md`, the same schema as prose with tables and examples; lint checks that the names of the two agree (`schema-prose`). Both change by hand by an `update` with `file`; neither has a `purpose`, a History or an Estimate. The mechanism of the replacement exists: `render_mode: full` writes the text of a `## Render` section whole into `governs` — `case-schema.md` is born that way from `rule-case-protocol`; `guppi/guard.py` refuses a hand edit of any file a live rule governs; `split_sections` in `guppi/pages.py` keeps everything between the markers inside the section, so yaml in `## Render` does not break the page. Lint reads from the yaml only `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; other keys it ignores — room for the descriptions as data.
Out of this theme: `index.md` §1 and its Rule-class map stay stale until theme 4; the sentence "A Rule-class file (`index.md`, `glossary.md`, a schema)" of `case-schema.md` until theme 6; `rule_class_path` and `RULE_CLASS` in `materialize.py` and `prespec.py` until theme 5 (the slug `rule-rules-schema` does not match their pattern, no collision). `rule-morph` (Slice 5, defer 239) wants the category set as data — six pages fix it; theme 5 keeps the two compatible. No `applies_to` on a schema rule: a schema applies to a category of pages, not to a page; `applies_to` is the edge Rule → Entity alone, theme 2 (the person's decision of this session).
Vault: the slugs `rule-page-schemas`, `rule-rules-schema`, `rule-entities-schema`, `rule-estimates-schema`, `rule-lessons-schema`, `rule-insights-schema`, `rule-decisions-schema` and the seven Estimates are free, live and archived; the nearest pages are `rule-render-harness` (built), `rule-governed-files-hook` (built), `rule-lint` (built), `rule-case-protocol` (draft, the one precedent of a vault file rendered from a page). A MOC under a MOC exists three times (`rule-harness` → `rule-settings`, `rule-claude-md`; `rule-session-start` → `rule-skill-hi`); an intermediate MOC earns its place by a cross-cutting Estimate. The tags `harness` and `render` exist; `schema` is new. The Estimates touched: `estimate-lint-catches` (its Criterion names `schema-prose`), one `replace` pair; `estimate-case-protocol-loaded` is not touched — the sentence of the Case schema waits for theme 6. `rule-harness` gets `rule-page-schemas` in `children`, a field alone, no Estimate touched (296). Cases 304.2 and 304.3 of this session were superseded by 305.1 and 305.2 before the approval and left the Spec (299.1).

## Problem

How the six schemas enter the graph: one rule page per category whose Render is `schema.yaml`; where the prose of `schema.md` goes; what the parent of the six is, so that six Leaves are no orphans; what each Leaf promises and what the MOC promises, so that one promise is not signed six times; and what lint does once `schema.md` is gone.

## History

- 2026-09-22 created · raw/2026-09-22/0014/ledger.md#case-304.7
