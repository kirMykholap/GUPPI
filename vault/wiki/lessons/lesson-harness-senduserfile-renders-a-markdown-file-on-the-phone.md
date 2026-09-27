---
type: lesson
kind: knowledge
root_cause: SendUserFile with display render puts a local markdown file into the conversation as a rendered card that the person reads on the phone, and the call carries only the path, so the content costs no output tokens
status: new
source: SendUserFile tool of Claude Code, test in session 1255 on 2026-09-27 with the plan file and display render
origin: raw/2026-09-27/1255/ledger.md#L54
sprint: migration
created: 2026-09-27
tags: [harness, session]
---

## Trigger

the person works from a phone and cannot open a file of the project, so each built Case was retyped whole into the chat

## Root cause

SendUserFile with display render puts a local markdown file into the conversation as a rendered card that the person reads on the phone, and the call carries only the path, so the content costs no output tokens

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#L54
- 2026-09-27 renamed from `harness-senduserfile-renders-a-markdown-file-on-the-phone` · [[decision-case-460.1]]
- 2026-09-27 updated: the lesson- prefix added to the slug (case 460.1) · [[decision-case-460.1]]
