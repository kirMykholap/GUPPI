---
type: decision
case: "548"
status: archived
update: ["[[estimate-decisions-schema-checked]]"]
origin: raw/2026-09-30/1736/ledger.md#case-548
sprint: migration
created: 2026-09-30
tags: [harness, render, schema]
---

## Problem

A test of the Decision schema fails on its own setup after the schema made `## Problem` optional, although the schema and its promise are right. Three tests still skip on text that the schema files no longer hold. The method of the schema's promise names neither the page without `## Problem` nor a command that runs the Decision-page tests, and it expects lint findings that are gone.

## Recommend

- **How should the out-of-date test be fixed?**
  - Recommended: add `## Problem` to the page in the test, remove `## Context`, and expect no finding.
  - Answer: agreed.
- **Should the "skip until the file is rewritten" lines be removed?**
  - Recommended: remove the skip from all three tests.
  - Answer: agreed.
- **Should the method line of the schema's promise be fixed too?**
  - Recommended: rewrite the method line so that it names a page without `## Context` and a page without `## Problem`, and expects no schema finding on `wiki/decisions/`.
  - Answer: agreed.
- **Fix the method line now, or read the promise today?**
  - Recommended: fix the method line now, and read the promise in a later session.
  - Answer: fix the method line now; the reading waits for a later session.
- **Change**
  - Asked: correct the claim of `context` about the Grep for `estimate-decisions-schema-checked`, so that it states what the Grep printed.
  - Taken: `context` names the hits `brief.md`, `log.md`, the `estimates` field of `rule-decisions-schema` and Decision pages, and says why none of them repeats the method.

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-548
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
