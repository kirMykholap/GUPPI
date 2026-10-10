---
type: decision
case: "549"
status: archived
update: ["[[entity-glossary]]", "[[rule-rules-schema]]", "[[rule-entities-schema]]", "[[rule-insights-schema]]", "[[rule-prespec]]", "[[rule-backlog]]"]
origin: raw/2026-09-30/1736/ledger.md#case-549
sprint: migration
created: 2026-09-30
tags: [session, harness, render, schema, workflow, librarian, sprint]
---

## Problem

The rule for when a supersede clears a defer is written in full on several pages. Some copies leave out the condition that the superseding Case names the page, so they contradict `rule-case-protocol` and the code. The fix must remove the copies that repeat the rule, so that the condition stands in one place and the other texts point to it.

## Recommend

- **Which texts change**
  - Recommended: the three pages the item names and the Insight schema too, so that every live text that describes clearing `deferred_by` is covered.
  - Answer: agreed.
- **How the texts state the condition**
  - Recommended: each text states the condition in its own words.
  - Answer: the person asked why the texts should not point to one place instead. One judgment written in several places is several implementations of it. The next question settled this.
- **Where the condition stands, and what the other texts say**
  - Recommended: the condition stands on `rule-case-protocol`, and the texts point to it.
  - Answer: agreed. The person also asked to take in two remarks. First, the glossary row `ref`, `slug`, `supersedes`, which states the condition in full, also becomes a pointer. Second, the other full copies are checked: each vault text either points to `rule-case-protocol` or stands with a reason given in `context`.

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-549
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
