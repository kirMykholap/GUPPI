---
type: decision
case: "306.3"
status: current
create: ["[[entity-glossary]]", "[[estimate-glossary-terms-defined]]"]
origin: raw/2026-09-22/0014/ledger.md#case-306.3
sprint: migration
created: 2026-09-22
tags: [session, harness]
---

## Context

`glossary.md` — 50 rows in eight groups and a table of retired terms: `where` names a page on 28 rows, a `§N` of `index.md` on 19, `here` on 3. The file is changed by hand; `/hi` loads it through `rule-internal-context`. The pattern is the sprint: `entity-sprint-migration` holds its content in `## Milestones`, `rule-sprint` is its guard, writes `sprint.md`, `--check` in `make lint`, ticks its Spec lines through `render.tick_command_lines`. The librarian runs `sprint` as step 5 of the frame of `rule-documentation`; `estimate-documentation-completes` names the step in its Criterion. The Case schema names three tickers of the Spec. By the Entity schema a Leaf carries `parent`; a MOC is a thing whose parts the person named as built (240.1) — a term is a row, not a part, so the glossary is a Leaf. No root stands over the Entities: `entity-sprint` is a MOC without a parent (241). `rule-harness` keeps the code of the harness equal to the pages that describe it; `make test` is the Makefile target over the whole suite, `estimate-harness-pipeline` covers `make test-harness` (render and lint). Vault: `entity-guppi`, `entity-glossary`, `rule-glossary` and the five Estimate slugs are free; `entity-sprint` `draft`, `rule-harness` `built`, `rule-documentation` `built`, `rule-lint` `built`, `rule-case-protocol` `draft`. The Render of `rule-entities-schema` was ratified in 305.2 and the page does not exist — 306.1 supersedes 305.2 (the section `## Terms`); `rule-rules-schema` is not touched. The Estimates touched: `estimate-documentation-completes` (step 6), `estimate-case-protocol-loaded` (the fourth ticker), `estimate-sprint-migration-rule-class-files-dissolved` ("the glossary from `terms`") — one `replace` pair each, `pending`; `estimate-harness-pipeline`, the Estimates of `rule-lint`, `rule-sprint` and `entity-sprint-migration` but the one named — not. The decisions of this session: the glossary is an Entity, not a `terms` field on the pages; the glossary carries no tick — the tick of 306.6 marks a Spec line, never a term; `rule-work-mode`, a placeholder, is a live page and the `where` of Work Mode.
The rows on `§N` and `here` go to the page whose meaning they name — after 304 the defining pages exist: the six schemas and `rule-page-schemas` take Entity, Rule, Estimate, Lesson, Insight, MOC, Leaf, Vault and the fields; `rule-page-generation` takes `origin`, `deferred_by` and the statuses; `rule-case-protocol` Ratification, Contract, Case, the ledger grammar and the agents. C4 model and Delegate — rejected ideas — and the four retired terms — retired — are not rows; the History of `entity-glossary` names them, their decisions stand in the archived ledgers of 2026-09-08 and 2026-09-09.

## Problem

How the glossary enters the graph as a thing: who its parent is and how the root earns its place; what its section and Estimate are; which rule guards it, how a term is added and how the file is rendered; who runs and checks the script; and where the 19 rows on `§N` and the 3 on `here` go, so that no row is lost.

## History

- 2026-09-22 created · raw/2026-09-22/0014/ledger.md#case-306.3
