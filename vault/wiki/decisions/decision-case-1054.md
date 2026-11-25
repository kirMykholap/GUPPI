---
type: decision
case: "1054"
status: current
children: ["[[decision-case-1054.1]]", "[[decision-case-1054.2]]"]
origin: raw/2026-11-25/0816/ledger.md#case-1054
sprint: plugin
created: 2026-11-25
tags: [session, workflow, harness]
---

## Problem

The level of a dispatch is judged from the item, but its check judges it against the built Case, so a Case that grows past its item fails the check. A sentence of the agent's text also still invites a question on how a Case is checked, so `case-guppi` asked the person choices of form that it should settle itself.

## Recommend

- **How is the level of a dispatch judged when the built Case changes more than the item asked?**
  - Recommended: (a) the rule and the check judge the level once, at the dispatch, from the item and the person's words, and the level stands where the built Case changes more.
  - Answer: (a), as recommended.
- **What changes so that `case-guppi` stops asking a choice of form?**
  - Recommended: (a) narrow the sentence of the agent's text: a question on how a Case is checked comes only where the Case can give no check, or where the options differ in behaviour, in cost or in what they block; the check gains that line and is read again.
  - Answer: (a), as recommended.

## History

- 2026-11-25 created · raw/2026-11-25/0816/ledger.md#case-1054
