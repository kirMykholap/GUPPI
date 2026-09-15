---
type: decision
case: "166.4"
status: current
update: ["[[rule-cleanup]]"]
origin: raw/2026-09-15/1448/ledger.md#case-166.4
sprint: migration
created: 2026-09-15
tags: [harness, workflow]
---

## Context

Seven body sections repeat a ref field of the frontmatter: on a Rule and an Entity `## Estimates`, `## Children`, `## Parent`, `## Implementation`, `## Code`; on a Lesson `## Insight`; on an Insight `## Children`, `## Addressed by`. `generate` writes them at `create`, rebuilds two on `update`, derives two on every write and fills one by the cascade; `cleanup` rebuilds two when an archived page leaves the lists; four schemas require them; `lint` requires what the schema requires and checks `schema.md` against `schema.yaml`. The sections were born when the fields were bare slugs Obsidian did not see. Since 148.1 the fields are `"[[slug]]"`, and the graph, backlinks and Bases see them on their own; `target` of an Estimate has lived without a section from birth. Five live pages show a section that differs from its field. Case 165.2 deferred the removal; this Case takes it up.

## Problem

A copy of a field in prose drifts, needs code in three scripts and lines in four schemas, and gives the reader nothing since 148.1; the removal touches four schemas, `generate`, `cleanup`, the tests and every live and archived page, and lifts parts of the contracts of 114 and 164.

## Given

`rules/schema.yaml` and `entities/schema.yaml`: `## Estimates` required, `## Children`/`## Parent` conditional on `kind`, `## Implementation` conditional on `enforcement`, `## Code` optional; `lessons/schema.yaml`: `## Insight` conditional on `status: clustered`; `insights/schema.yaml`: `## Children` required, `## Addressed by` optional; `estimates/` and `decisions/` have no derived section.
**＋** The `schema.md` of the four categories carry the rows of these sections in the Body table and in the examples; `lint` compares the section names of `schema.md` and `schema.yaml` and requires only the required sections — it does not name a section a page carries beyond the schema.
**＋** `generate`: `SECTION_ORDER` lists the seven sections; `create` writes five from the fields; an `update` with `set` on `children`/`estimates` rebuilds the section; `save` derives `## Insight` and `## Addressed by`; the cascade walks the live lessons and writes `## Insight` with History `insight section derived` (114).
**＋** `estimate-generate-writes`: block 114 — `## Insight` from the field and the cascade; block 164 (`pending`, this session) — the librarian's `create`, `defer` on an Insight, `addressed_by` and the `## Addressed by` section, `actioned` with the cascade, the refusals.
**＋** `cleanup.unlink`: removes an archived slug from `children`/`estimates` of the live pages, rebuilds the section, writes History `child <slug> archived` / `estimate <slug> archived`; `rule-cleanup` (`built`, `estimates: [estimate-cleanup-moves]`, `passed`) says "their sections are rebuilt".
**＋** The migration of 148.1: a script from the scratchpad, `read_page` → `write_page` over `wiki/**` and `archive/**`, no History lines, checked by `lint`, `render --check`, `git diff --stat`.
**＋** Tests that name the sections: `test_generate.py` 11 places, `test_lint.py` 9, `test_cleanup.py` 2, `test_render.py` 1.
**－** `## Purpose`, the `## Criterion` of a Decision page, `## History` and the History lines about fields are not touched; `docs/migration/rule-*.md` are drafts, their fate in Slice 5; `lint`, `materialize`, `ask-guppi`, `index` read no section — their contracts do not change.

## Criterion

- [[estimate-cleanup-moves]] § case 166.4

## History

- 2026-09-15 created · raw/2026-09-15/1448/ledger.md#case-166.4
