---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-wait-what]]"
purpose: Whether the skill wait-what writes the agent's last text again in plain words in the chat language, with the open question asked again and no option changed
method: uv run guppi render --check; by hand, in a session after the render, one run of the skill read in the chat, on the person's /wait-what or on a request in words
origin: raw/2026-09-28/1318/ledger.md#case-477.2
sprint: migration
created: 2026-09-28
tags: [harness, workflow]
---

## Criterion

When:
The person types `/wait-what` on `UserPromptSubmit`, or the main agent calls the skill on `PreToolUse Skill` when the person asks in words for a plain explanation of its last text, after `uv run guppi render` wrote `.claude/skills/wait-what/SKILL.md` from `rule-skill-wait-what`.

Then:
`uv run guppi render --check` exits 0: `.claude/skills/wait-what/SKILL.md` equals the Render of `rule-skill-wait-what`, with the name of the language that the `## Render` of `rule-guppi-config` sets for `chat_lang` in place of its placeholder.
**＋** The main agent writes its last text again — a round, the short text on a Case or a reply — in the language of `chat_lang`, in short active sentences with one idea each.
**＋** It opens with a little background, shows how the thing works on one real case, and names the effect of every choice the text offers.
**＋** It holds no case number and no history of a slug, uses the terms of `vault/wiki/glossary.md`, and explains a term in a few words where it first stands.
**＋** It takes a fact of a Case that the main agent does not hold from the `case-guppi` of that Case, never from a guess.
**＋** It ends with the open question asked again.
**－** No option and no recommendation of the last text changes.
**－** The skill starts no Case and writes no ledger line.

## History

- 2026-09-28 created · [[decision-case-477.2]]
