---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether a question of the person to discuss an item goes to its case-guppi and comes back under Fact, with no reading of the main agent's own
method: "by hand, at the Retro of a session that holds a question of the person in the chat to discuss an item whose case-guppi is building its Case or has shown it: the SendMessage call, the tool calls of the main agent and the answer, read in that session"
checked: 2026-10-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
In Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to discuss an item whose `case-guppi` is building its Case or has shown it, or to learn something of that item, and the question is no request for a plain explanation of the agent's text.

Then:
The main agent sends the question to that `case-guppi` by `SendMessage`, verbatim and untranslated, and makes no `Read`, `Grep` or `Glob` call of its own to answer it.
**＋** `case-guppi` answers in plain words under a first line `**Fact:**`, with no Case heading and no round, from the pages it read, or with a round when the question opens a fork.
**＋** The main agent shows the answer translated into the language of the chat, then asks again the question that stood open: the open question of the round, or the sign-off of the shown Case.
**－** A request for a plain explanation of a round, of the short text on a Case or of a reply stays with `.claude/skills/wait-what/SKILL.md`.
**－** A `**Fact:**` answer changes nothing of the round or of the Case, and the hook of `rule-case-check` reads it as no Case.

## Result

2026-10-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
