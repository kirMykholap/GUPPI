---
type: lesson
kind: knowledge
root_cause: The Claude Code CLI withholds the approval of a plan above the size it can show whatever the terminal window, its width or its height, and with no hook of GUPPI before the dialog; the fault lies in the CLI, not in the window, and the VS Code extension approves the same size.
status: archived
source: "by-hand test of session 2026-10-31/0128 (Case 953): the Claude Code CLI started by claude --permission-mode plan in the empty folder C:\\tmp\\plan-approval-test, with the text of C:\\Users\\kir\\.claude\\plans\\resilient-munching-peacock.md, 15347 bytes"
insight: "[[insight-plugin-cli-withholds-approval-of-a-long-plan]]"
origin: raw/2026-10-31/0128/ledger.md#L16
sprint: plugin
created: 2026-10-31
tags: [plugin, harness]
---

## Trigger

In an empty folder with no GUPPI and so no hook of it, the Claude Code CLI withheld the approval of the plan text of resilient-munching-peacock.md both in a standalone PowerShell window of 120 columns by 30 rows and in the terminal of VS Code of 330 columns by 16 rows, each time with "the plan is too large to be shown in full — approval is withheld; send feedback asking for a shorter plan, or press Esc"; the plan of this session, approved by ExitPlanMode in the VS Code extension, was larger.

## Root cause

The Claude Code CLI withholds the approval of a plan above the size it can show whatever the terminal window, its width or its height, and with no hook of GUPPI before the dialog; the fault lies in the CLI, not in the window, and the VS Code extension approves the same size.

## History

- 2026-10-31 created · raw/2026-10-31/0128/ledger.md#L16
- 2026-10-31 updated: clustered under insight-plugin-cli-withholds-approval-of-a-long-plan (synthesis) · raw/2026-10-31/0128/ledger.md#L16
- 2026-11-01 archived · insight actioned
- 2026-11-01 archived · cleanup
