---
type: insight
pattern: A slash command typed by the person is expanded by the client into the prompt and is never a Skill tool call, so a hook on the Skill tool sees only the agent's own calls; a cure aimed at the skill's settings changes the agent's path and leaves the typed one as it was.
status: archived
children: ["[[lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate]]", "[[lesson-retro-typed-still-bypasses-the-skill-tool-after-150]]"]
severity: 0
addressed_by: "[[decision-case-173]]"
origin: raw/2026-09-15/1110/ledger.md#L27
sprint: migration
created: 2026-09-15
tags: [hooks, session, harness]
---

## Pattern

Two lessons on one path.

`lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate` (session O): the
typed `/retro` left the skill's Recorded line in the event log and no `tool Skill: retro`
line; the PreToolUse Skill hook of 136.1 and `guppi gate` never saw it. The cause was read as
`disable-model-invocation: true` in the skill's frontmatter.

`lesson-retro-typed-still-bypasses-the-skill-tool-after-150` (session Q): case 150 removed
`disable-model-invocation`; the agent's own call now goes through the Skill tool and the gate,
the typed `/retro` still does not. The reading of `estimate-retro-loads` is `failed`.

In both, the client expands a typed slash command into the prompt and makes no tool call, so
no PreToolUse hook and no gate on the Skill tool can see it. The skill's frontmatter decides
only whether the agent may call it.

## Proposal

A suggestion, not a decision. Treat the two paths as two: the agent's call is gated on the
Skill tool, the person's typed command on the event it does produce — `UserPromptSubmit`, where
the stamped `hi` of 111 already reads the prompt. A `then` on a slash command names which path it
covers, and its reading takes both. The cure of 150 is a Case of the next Plan Mode; `rule-retro`
is `draft` by the cascade until `estimate-retro-loads` passes.

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#L27
- 2026-09-15 updated: actioned: the two paths of a slash command are two since 169.1–169.3, and case-schema.md now asks a when on a slash command to name its path and a then covering both to be read on both (case 173) · [[decision-case-173]]
- 2026-10-10 status: actioned → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
