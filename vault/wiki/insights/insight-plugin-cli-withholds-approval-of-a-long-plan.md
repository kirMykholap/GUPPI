---
type: insight
pattern: The Claude Code CLI withholds the approval of a plan above the size it can show, whatever the terminal window and with no hook of GUPPI before the dialog, while the VS Code extension approves the same size; GUPPI writes each ratified Case whole into the plan file, so a Spec of a few Cases cannot be approved in the CLI.
status: open
children: ["[[lesson-plugin-cli-withholds-approval-of-a-long-plan]]", "[[lesson-plugin-cli-withholds-approval-in-every-window]]"]
severity: 2
deferred_by: ["[[decision-case-957]]"]
origin: raw/2026-10-31/0128/ledger.md#L16
sprint: plugin
created: 2026-10-31
tags: [plugin, harness]
---

## Pattern

Two lessons record the same fault of the Claude Code CLI. In install A of session 2026-10-29/0327 the CLI withheld the approval of a plan file of 15347 bytes, while the VS Code extension approved a larger plan. The by-hand test of Case 953 in session 2026-10-31/0128 ran the same plan text in an empty folder with no GUPPI, in a standalone PowerShell window of 120 by 30 and in the terminal of VS Code of 330 by 16; the approval was withheld in both. The cause lies in the CLI, not in the window and not in a hook of GUPPI.

## Proposal

A suggestion for a Case, not a decision. Options named in the handoff of session 2026-10-31/0128 are a shorter plan file, an approval in the chat, or the VS Code extension as the way to approve a Spec.

## History

- 2026-10-31 created · raw/2026-10-31/0128/ledger.md#L16
- 2026-10-31 deferred · [[decision-case-957]]
