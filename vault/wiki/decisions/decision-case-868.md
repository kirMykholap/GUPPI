---
type: decision
case: "868"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-keeps-the-old-form-until-the-writer-is-live]]", "[[insight-workflow-code-live-before-the-page-it-reads]]"]
origin: raw/2026-10-16/2104/ledger.md#case-868
sprint: plugin
created: 2026-10-16
tags: [session, workflow, harness, hooks, ledger]
---

## Problem

A Case may change a test that reads a live file which the same session changes. The test is red from Work Mode until the librarian's run, while `rule-retro` lets no red test stand. `rule-case-build` still calls that red a note for the handoff.

## Recommend

- **What should happen to this Insight?**
  - Recommended: (a) action it: a test that reads a live file which the same session changes accepts both the old and the new text until the text lands, and a Case of a later session removes the old form.
  - Answer: agreed, (a).

## History

- 2026-10-17 created · raw/2026-10-16/2104/ledger.md#case-868
