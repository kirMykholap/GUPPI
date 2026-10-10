---
type: decision
case: "683"
status: archived
update: ["[[rule-page-generation]]", "[[estimate-generate-writes-the-decision-page]]", "[[rule-decisions-schema]]", "[[entity-glossary]]"]
supersedes: ["[[decision-case-469]]"]
origin: raw/2026-10-05/2249/ledger.md#case-683
sprint: migration
created: 2026-10-05
tags: [harness, workflow, ledger, render, schema, session]
---

## Problem

A later Case that supersedes a Decision already in the archive sets it `superseded` again, so `cleanup` brings it back to the live vault and the next run archives it again, with History lines that change no meaning.

## Recommend

- Recommended: an archived Decision that a later Case supersedes stays `archived` where it lies and only takes the later Decision into `superseded_by`, with one History line; the code of `generate.decision`, its test, the Criterion of `estimate-generate-writes-the-decision-page`, and the exception written into `rule-decisions-schema` and `entity-glossary`.
  Answer: ratified as built
- **Change**
  - Asked: the person agreed to the fixes of the pre-spec report: the new line of the Criterion narrows the defers it clears to the targets a decision line of the superseding Case names, and `context` counts the archived Decisions of Case 676.
  - Taken: the new line of the Criterion of `estimate-generate-writes-the-decision-page` names the same condition as the line after it; `context` says that all 19 Decisions that Case 676 supersedes stand in the archive, by a Glob over the 19.

## History

- 2026-10-06 created · raw/2026-10-05/2249/ledger.md#case-683
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
