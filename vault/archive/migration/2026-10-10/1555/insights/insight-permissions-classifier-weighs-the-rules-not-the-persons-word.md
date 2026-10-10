---
type: insight
pattern: The auto mode classifier judges an action against the permission rules of the settings, not against the person's word in the chat, so a task the person asked for, such as a change of a git remote or of a check's own state file, is refused to the agent and can be done only by the person or under a permission rule.
status: archived
children: ["[[lesson-permissions-auto-mode-refuses-a-remote-change-despite-the-chat]]", "[[lesson-permissions-auto-mode-refuses-editing-the-case-check-store]]"]
severity: 0
addressed_by: "[[decision-case-741]]"
origin: raw/2026-10-07/1804/ledger.md#L30
sprint: migration
created: 2026-10-07
tags: [harness, workflow]
---

## Pattern

In session 0138 of 2026-09-30 the classifier refused git remote remove origin twice, the second time after the person allowed it in the chat, and the person ran it by hand. In session 1804 of 2026-10-07 the person chose to remove the stale entries 713.1 and 713.2 from the store of the Case-file check, and the script was refused as Logging/Audit Tampering; the entries stand.

## Proposal

A suggestion, not a decision. When a Case or a choice of the person sets a task that changes a git remote, the state file of a check or another record the classifier guards, let the Case name who runs it, the person by ! in the prompt or a permission rule of rule-permissions, before Work Mode reaches it.

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#L30
- 2026-10-08 updated: actioned: a refusal of the auto mode classifier is a stop of where-to-stop.md, and the person runs the command after ! (case 741) · [[decision-case-741]]
- 2026-10-10 status: actioned → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
