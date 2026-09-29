---
type: estimate
kind: QA
status: pending
target: "[[rule-skill-wait-what]]"
purpose: Whether the skill wait-what writes the agent's last text again in plain words in the chat language, with the open question asked again and no option changed
method: uv run guppi render --check; by hand, in a session after the render, one run of the skill read in the chat, on the person's /wait-what or on a request in words
checked: 2026-09-28
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
**＋** The main agent writes its last text again — a round, the short text on a Case or a reply — in the language of `chat_lang`. It uses short active sentences with one idea each and opens with a little background.
**＋** It shows the mechanism on one real example: a line of a page, a file, a ledger or the Case, which the main agent reads itself and quotes as it stands, with its path. For a line it cannot find, it asks the `case-guppi` of the Case by `SendMessage` for the file and the line, then reads the file and quotes the line.
**＋** When it finds no real example, it says so in one sentence and gives the mechanism without one.
**＋** Each question of a round it explains, and the options of a short text on a Case or of a reply, take the question shape of `.claude/skills/grill-me/SKILL.md`.
**＋** Its own sentences hold no case number and no history of a slug. They use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.
**＋** It ends with the open question asked again.
**－** No example is made up, whether it is marked as made up or not.
**－** A quoted line keeps its case numbers as written.
**－** A label of the shape translated into the language of `chat_lang` counts as the label of the template.
**－** The question shape itself is read by `estimate-skill-grill-me-asks-in-rounds`, not here.
**－** No other fact of a Case that the main agent does not hold is guessed: it comes from the `case-guppi` of that Case.
**－** No option and no recommendation of the last text changes.
**－** The skill starts no Case and writes no ledger line.

## Result

2026-09-28, uv run guppi render --check exit 0; by hand, the wait-what run on round 2 Q1 of Case 485: Russian, short sentences, background first, no case number, option and recommendation unchanged, the open question asked again; but it showed the mechanism on a made-up example ("guppi cleanup prints one line per moved file", marked as a made-up example) instead of a real case, and it did not ask the case-guppi of the Case for a real line

## History

- 2026-09-28 created · [[decision-case-477.2]]
- 2026-09-28 status: pending → failed · raw/2026-09-28/2000/ledger.md#L26
- 2026-09-29 updated: the Criterion replaced whole — a real quoted example or a plain word that none was found, and options in the question shape of the grill-me template (case 502) · [[decision-case-502]]
