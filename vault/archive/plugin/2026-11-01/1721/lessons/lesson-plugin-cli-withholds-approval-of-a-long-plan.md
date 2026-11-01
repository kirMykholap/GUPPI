---
type: lesson
kind: knowledge
root_cause: The Claude Code CLI shows a plan whole before approval and withholds approval of a plan above the size it can show, while GUPPI writes each ratified Case whole into the plan file, so a Spec of two Cases already passes that size in the CLI.
status: archived
source: Claude Code CLI, transcript ~/.claude/projects/C--tmp-guppi-0327-a/bc61060a-010e-461d-8872-4071ea6c0f1e.jsonl
insight: "[[insight-plugin-cli-withholds-approval-of-a-long-plan]]"
origin: raw/2026-10-29/0327/ledger.md#L42
sprint: plugin
created: 2026-10-29
tags: [plugin, harness]
---

## Trigger

In install A of session 0327, ExitPlanMode in the Claude Code CLI withheld the approval of the plan file resilient-munching-peacock.md, 15347 bytes and 183 lines, with "the plan is too large to be shown in full — approval is withheld", leaving only Esc or a reason to refuse; the plan of session 0327, 58861 bytes, was approved in the VS Code extension.

## Root cause

The Claude Code CLI shows a plan whole before approval and withholds approval of a plan above the size it can show, while GUPPI writes each ratified Case whole into the plan file, so a Spec of two Cases already passes that size in the CLI.

## History

- 2026-10-29 created · raw/2026-10-29/0327/ledger.md#L42
- 2026-10-31 updated: clustered under insight-plugin-cli-withholds-approval-of-a-long-plan (synthesis) · raw/2026-10-31/0128/ledger.md#L16
- 2026-11-01 archived · insight actioned
- 2026-11-01 archived · cleanup
