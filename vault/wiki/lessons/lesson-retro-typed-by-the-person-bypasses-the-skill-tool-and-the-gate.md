---
type: lesson
kind: knowledge
root_cause: "retro's SKILL.md carries `disable-model-invocation: true`, so the client expands a typed /retro as a prompt and never calls the Skill tool; the PreToolUse Skill hook of 136.1 cannot see it, and once the render drops the Recorded line the retro mark disappears — no reader in code needs it today; a Case when one does"
status: new
source: ".claude/skills/retro/SKILL.md, disable-model-invocation: true"
origin: raw/2026-09-14/1229/ledger.md#L31
sprint: migration
created: 2026-09-14
tags: [hooks, session, harness]
---

## Trigger

the /retro of session O typed by the person left `- 14:45:16 -------- retro` from the skill's Recorded line and no `tool Skill: retro` line and no stamped mark from guppi gate, while the typed /handoff of session N and the /pre-task calls went through the Skill tool and got their PostToolUse lines

## Root cause

retro's SKILL.md carries `disable-model-invocation: true`, so the client expands a typed /retro as a prompt and never calls the Skill tool; the PreToolUse Skill hook of 136.1 cannot see it, and once the render drops the Recorded line the retro mark disappears — no reader in code needs it today; a Case when one does

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#L31
- 2026-09-14 updated: source added (case 144.2) · [[decision-case-144.2]]
