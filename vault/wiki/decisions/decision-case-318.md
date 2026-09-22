---
type: decision
case: "318"
status: current
update: ["[[rule-ask]]", "[[rule-materialize]]", "[[rule-skill-hi]]", "[[rule-case-protocol]]", "[[rule-claude-md]]", "[[rule-prespec]]", "[[entity-glossary]]", "[[entity-sprint-migration]]", "[[estimate-case-protocol-ledger-line-form]]", "[[estimate-glossary-terms-defined]]", "[[estimate-synthesis-keeps-actioned-by-the-mark]]", "[[estimate-sprint-migration-merges]]", "[[estimate-raw-archive]]"]
delete: [index]
origin: raw/2026-09-22/1121/ledger.md#case-318
sprint: migration
created: 2026-09-22
tags: [session, workflow, harness, ledger, render, sprint, librarian, git, tests]
---

## Context

`index.md` is the map of the vault in thirteen §. After 315, 316 and 317 every § is covered by a page: §0, §2, §3 and §12 by `rule-case-protocol`; §1 by `rule-vault-layout` and `rule-raw-archive`; §4 by `rule-ledger-write`; §5 by `rule-materialize`; §6 by `rule-atomicity`; §7 by `rule-estimates-schema`; §8 by `rule-lessons-schema`, `rule-insights-schema` and `rule-synthesis`; §9 by `rule-session`; §10 by `rule-documentation`; §11 by `rule-ask`. What is left is the file and its pointers: a live `§N` or a mention of the file stands on six rule pages (`rule-ask`, `rule-materialize`, `rule-skill-hi`, `rule-case-protocol`, `rule-claude-md`, `rule-prespec`), on `entity-glossary` in two rows, on five Estimates and in `RULE_CLASS` of `guppi/materialize.py`; four harness files — `CLAUDE.md`, `ask-guppi.md`, the `/hi` and `/pre-spec` skills — are repaired by the render of their rules, and `entities/schema.yaml` by the render of `rule-entities-schema`. Estimates: `estimate-sprint-migration-index-dissolved` (created by 310.3) is the promise of this work and is read here; of the five carrying a pointer four are `pending` already (`estimate-glossary-terms-defined`, `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-sprint-migration-merges`, `estimate-sprint-migration-rule-class-files-dissolved`), `estimate-raw-archive` is changed in its `## Context` and keeps its status (case 296), and `estimate-case-protocol-ledger-line-form` is the one `passed` page whose Criterion is touched: it goes `pending` and is read again. The rest of the `file` route in the scripts is theme 5.

## Problem

How the file and its thirty pointers go without leaving a live page that sends a reader to a § that no longer exists.

## History

- 2026-09-22 created · raw/2026-09-22/1121/ledger.md#case-318
