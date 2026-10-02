---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether a question of the person to discuss an item goes to its case-guppi and comes back under Fact, with no reading of the main agent's own
method: by hand in a later session, the first such question, the SendMessage call, the tool calls of the main agent and the answer read in the transcript
checked: 2026-10-03
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
**＋** The main agent shows the answer translated into Russian, then asks again the question that stood open: the open question of the round, or the sign-off of the shown Case.
**－** A request for a plain explanation of a round, of the short text on a Case or of a reply stays with `.claude/skills/wait-what/SKILL.md`.
**－** A `**Fact:**` answer changes nothing of the round or of the Case, and the hook of `rule-case-check` reads it as no Case.

## Result

2026-10-03, by hand in the transcript of session 2300: the person's question on the round of Case 603 ("А почему вообще появляется такая ситуация…") went to its case-guppi by SendMessage verbatim and untranslated, with no Read, Grep or Glob call of the main agent; case-guppi answered with a round (Q5) as the question opened a fork; the main agent showed it translated and asked the open questions again; the question on the librarian came back as a `**Fact:**` answer, shown translated

## History

- 2026-10-01 created · [[decision-case-561.12]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L32
- 2026-10-02 renamed from `estimate-case-protocol-forwards-a-discussion-question` · [[decision-case-595.12]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the forwarding as orchestration.md sets it (case 595.12) · [[decision-case-595.12]]
- 2026-10-03 status: pending → passed · raw/2026-10-02/2300/ledger.md#L26
