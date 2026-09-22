---
type: decision
case: "315"
status: current
create: ["[[rule-vault-layout]]", "[[estimate-vault-layout-holds]]"]
update: ["[[rule-harness]]"]
origin: raw/2026-09-22/1121/ledger.md#case-315
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Context

The layout of the vault lives in §1 of `index.md`: the trees of `raw/`, `archive/` and `wiki/`, "the filename is the slug", the table "System files are Rule-class" and the line "`brief.md`, `sprint.md`, `tags.md` and `log.md` are not pages". Part of it stands on pages already: `raw/` and the archive in `rule-raw-archive`, the shape of a page per category in the six schema rules, History and `log.md` in `rule-page-generation`. The Rule-class table is retired by themes 5 and 6, and the "not pages" line is stale: `sprint.md` and `glossary.md` are Renders of pages, `case-schema.md` too. Nothing holds the layout of `wiki/` itself, the equality of slug and filename, or the rule that no file lands in `wiki/` without a decision — `read_vault` takes `*.md` of a category folder but `schema`, and does not read a file at the root at all. Pages: `rule-harness` a `draft` MOC of eight children; `rule-lint` `built`, the Case touches no Estimate of it — `estimate-lint-catches` keeps its Criterion; the slugs `rule-vault-layout` and `estimate-vault-layout-holds` are free by the Grep over `rules/` and `estimates/`, the nearest are `rule-page-schemas` (the shape of a page, not its place) and `rule-raw-archive` (the layout of `raw/`, not of `wiki/`).

## Problem

Where the layout of `wiki/` lives once `index.md` is gone, and what checks that no file nobody ratified appeared in `wiki/`.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-315
