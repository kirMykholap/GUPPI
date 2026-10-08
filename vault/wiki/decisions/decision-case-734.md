---
type: decision
case: "734"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-checks-the-finished-case]]", "[[insight-workflow-case-written-without-reading-the-pages-it-changes]]"]
origin: raw/2026-10-08/0213/ledger.md#case-734
sprint: migration
created: 2026-10-08
tags: [session, workflow, harness]
---

## Problem

Inside a page it changes, `case-guppi` finds the sentences to fix by the words of the one sentence it changes. A sentence that states the same rule in other words stays false until `/pre-spec` finds it, and the Case is built and ratified again.

## Recommend

- **How the agent finds the sentences a change touches**
  - Recommended: (a) read each changed page by meaning: list every sentence that states the behaviour the change touches, judged by what it says, not found by a word search; each enters the Case or `context` says why it stands.
  - Answer: agreed, (a).
- **Which pages the reading by meaning covers**
  - Recommended: (a) only the pages the Case changes; other pages are still reached by the slug and moment searches and read around each hit.
  - Answer: agreed, (a).
- **Which Estimate checks the fix**
  - Recommended: (a) add it to `estimate-case-build-checks-the-finished-case`: its Criterion replaced whole with one more line, and its purpose and method gain this kind of miss.
  - Answer: agreed, (a).
- **The open Insight**
  - Recommended: (a) set `insight-workflow-case-written-without-reading-the-pages-it-changes` `actioned`, as the last session did.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/0213/ledger.md#case-734
