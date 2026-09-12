---
type: decision
case: "62"
status: current
update: [rule-case-protocol, case-schema]
origin: raw/2026-09-12/ledger.md#case-62
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger]
---

## Context

Three habits the owner set in sessions G to I live only in the agent's memory files: the
owner answers a Case in plain chat and rejected the AskUserQuestion picker twice (session
G); when the owner changes a Case's conditions or verdict, the Case is shown again with
the sections that changed and without `recommend`, since the variant is theirs (today,
Case 58); a Frontier item with no decision in it is one line in the Work Mode order
(today, `lesson-plan-mode-exited-per-frontier-item`). Memory is for personal notes; a
rule of the dialogue belongs in the Render every session reads.

## Problem

The Case protocol names the `ratification` section and its ledger preview, and nothing of
how the sign-off is asked for, nor what happens when the owner answers with a variant.

## Given

`rule-case-protocol` Render: "The `ratification` section ends with a preview of the ledger
lines in an untagged fence."; `case-schema.md` row `ratification`: "The human's sign-off,
question, or their own alternative. Ends with a preview of the ledger lines in an untagged
fence."
**＋** The memory files `feedback-no-askuserquestion-in-cases`,
`feedback-one-plan-per-plan-mode`, `bash-heredoc-escapes-interpreted` and
`session-f-unmaterialized-tail` sit in the agent's memory directory outside the
repository; two of them are now lessons in the ledger.
**－** `recommend` is still required in the first showing of a Case; the schema table is
not changed on that.

## When

The agent ends a Case turn; the owner answers with a change.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-62
