---
type: decision
case: "883"
status: current
update: ["[[rule-page-generation]]", "[[estimate-generate-writes-the-decision-page]]", "[[rule-decisions-schema]]", "[[entity-glossary]]"]
origin: raw/2026-10-17/2307/ledger.md#case-883
sprint: plugin
created: 2026-10-17
tags: [harness, workflow, ledger, render, schema, session]
---

## Problem

`guppi generate` carries out the `supersedes` of a Case that a later Case retired, so a Case that never applied sets an earlier decision superseded, clears a put-off and writes its name into History and `log.md`.

## Recommend

- **How far does the fix go?**
  - Recommended: (a) page writing only; the tags in `materialize.yaml` stay, and the case where they skip a Case not yet applied is left for a later Case.
  - Answer: agreed, (a).
- **What happens to the lines already written?**
  - Recommended: (a) leave them as a true record of that run.
  - Answer: agreed, (a).
- **Does the page of a retired Case still list what it meant to replace?**
  - Recommended: (a) keep the list; its status shows that nothing of it applied.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, make the field `status` of `rule-decisions-schema` and the row `Decision (status)` of `entity-glossary` carry the same condition as the rule, a later Case retired before its entries applied, and say that the earlier Decision page ends `archived` after the cascade.
  - Taken: both new texts say that a page does not go `superseded` when another Case retired the naming Case before its entries applied, and `context` says that the cascade archived `decision-case-875`.

## History

- 2026-10-26 created · raw/2026-10-17/2307/ledger.md#case-883
