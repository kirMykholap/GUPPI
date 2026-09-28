---
type: lesson
kind: error
root_cause: the Render of rule-retro is an English instruction with no cue on the language of the reply, and the agent answered in the language of the instruction instead of the language of the chat; rule-language stands in CLAUDE.md with no guard — no hook or check can read the language of a reply, so the rule holds by the agent alone and a long English instruction outweighed it
status: archived
insight: "[[insight-session-reply-language-follows-the-english-text-read]]"
origin: raw/2026-09-21/1315/ledger.md#L21
sprint: migration
created: 2026-09-21
tags: [session, workflow]
---

## Trigger

the Retro of session 1315 was written in English; the owner asked why, the chat is Russian by rule-language

## Root cause

the Render of rule-retro is an English instruction with no cue on the language of the reply, and the agent answered in the language of the instruction instead of the language of the chat; rule-language stands in CLAUDE.md with no guard — no hook or check can read the language of a reply, so the rule holds by the agent alone and a long English instruction outweighed it

## History

- 2026-09-21 created · raw/2026-09-21/1315/ledger.md#L21
- 2026-09-28 updated: clustered under insight-session-reply-language-follows-the-english-text-read (synthesis) · raw/2026-09-28/0000/ledger.md#L33
- 2026-09-28 archived · insight actioned
- 2026-09-28 archived · cleanup
