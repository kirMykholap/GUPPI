---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether a question of the person to discuss an item goes to its case-guppi and comes back under Fact, with no reading of the main agent's own
method: "by hand, at the Retro of a session that holds a question of the person in the chat to discuss an item whose case-guppi is building its Case or has shown it: the SendMessage call, the tool calls of the main agent and the answer, read in that session"
checked: 2026-10-29
origin: raw/2026-09-30/2356/ledger.md#case-561.12
sprint: migration
created: 2026-09-30
tags: [session, workflow]
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

2026-10-29, Retro of session 1930, read in this session: the person asked how the installer handles a project with its own settings, CLAUDE.md and hooks while the round of Case 905 stood open; the main agent sent the question verbatim and untranslated to the case-guppi of Case 905 by SendMessage and made no Read, Grep or Glob of its own to answer it; case-guppi answered under a first line **Fact:** with no Case heading and no round; the main agent showed it translated into the language of the chat and asked the open question of the round again; the round stood unchanged and was answered next

## History

- 2026-10-01 created · [[decision-case-561.12]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L32
- 2026-10-02 renamed from `estimate-case-protocol-forwards-a-discussion-question` · [[decision-case-595.12]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the forwarding as orchestration.md sets it (case 595.12) · [[decision-case-595.12]]
- 2026-10-03 status: pending → passed · raw/2026-10-02/2300/ledger.md#L26
- 2026-10-29 updated: the Criterion replaced whole — the answer is shown in the language of the chat, not named as Russian; the method is read at the Retro of a session that holds such a question, from its own tool calls, not in the transcript of a later session · [[decision-case-908.2]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/1930/ledger.md#L25
