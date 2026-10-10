---
type: lesson
kind: error
root_cause: the vault is open in an editor during a session and a keystroke lands in a page; nothing guards wiki/ against a hand edit outside the librarian, and the tree is checked only by guppi gate at /handoff
status: archived
origin: raw/2026-09-15/1110/ledger.md#L28
sprint: migration
created: 2026-09-15
tags: [workflow, librarian]
---

## Trigger

decision-case-140 was modified in the working tree at 13:43 while the owner checked the page in Obsidian, four characters gone from its quoted wikilink; pre-task's ask-guppi noticed it through git status and the file was reverted with git checkout

## Root cause

the vault is open in an editor during a session and a keystroke lands in a page; nothing guards wiki/ against a hand edit outside the librarian, and the tree is checked only by guppi gate at /handoff

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#L28
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
