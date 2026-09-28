---
type: insight
pattern: The agent writes its chat reply in the language of the English text it has just read — the Render of a skill, the file of a Case, ledger lines — instead of the language of the chat; rule-language stands in CLAUDE.md with no guard, since no hook or check reads the language of a reply, so the rule holds by the agent alone and a long English text outweighs it.
status: open
children: ["[[lesson-retro-answered-in-the-skills-language]]", "[[lesson-chat-language-follows-the-last-english-file-read]]"]
severity: 2
origin: raw/2026-09-28/0000/ledger.md#L33
sprint: migration
created: 2026-09-28
tags: [session, workflow]
---

## Pattern

Two sessions, one cause. The Retro of session 1315 was written in English after the English Render of rule-retro (lesson-retro-answered-in-the-skills-language); the reply that acknowledged Case 471 in session 0000 was written in English after the English file of the Case and its ledger lines (lesson-chat-language-follows-the-last-english-file-read). In both, the person asked why. The reply took the language of the text read just before it, and rule-language, which stands only in CLAUDE.md, has no guard that reads a reply.

## Proposal

A suggestion for a Case, not a decision. Either a cue on the language of the reply where the agent reads a long English text and then answers in the chat — the Renders of skills that end in a chat reply, the showing of a Case and its ratification — or a check on Stop that reads the prose of a reply outside code spans and ledger blocks and warns when it holds no Cyrillic; the second would be the first guard of rule-language that is not the agent's own reading.

## History

- 2026-09-28 created · raw/2026-09-28/0000/ledger.md#L33
