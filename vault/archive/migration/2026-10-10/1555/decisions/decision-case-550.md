---
type: decision
case: "550"
status: archived
update: ["[[decision-case-534]]", "[[decision-case-538]]", "[[decision-case-539]]"]
origin: raw/2026-09-30/1736/ledger.md#case-550
sprint: migration
created: 2026-09-30
tags: [harness, session, render, hooks, workflow, librarian, sprint, ledger]
---

## Problem

The librarian run of session 1306 wrote parent Decision pages for Cases 534, 538 and 539 of session 0248, and no Case decided that for Cases ratified before case 544. The question was whether to keep these pages, change them or remove them, and whether to limit the code that wrote them.

## Recommend

- **What to do with the three parent pages**
  Recommended: (a) keep them as they are; their sub-case pages keep no link back.
  Answer: (a) keep them as they are.
- **Should `materialize` be limited so that it adds no parent record to an older folder**
  Recommended: (a) no code change; after the two older folders are archived, the case cannot happen again.
  Answer: (a) no code change.
- **Should `rule-decisions-schema` say how sub-case pages written before the new rule look**
  Recommended: (a) add one sentence: a sub-case page written before case 544 keeps its `## Problem` and carries no `parent`.
  Answer: (b) leave the text as it is. Decision pages move to the archive over time, and the added sentence would stay behind and describe pages that are already archived.

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-550
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
