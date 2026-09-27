---
type: decision
case: "466.2"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-shows-the-built-case]]"]
origin: raw/2026-09-27/2050/ledger.md#case-466.2
sprint: migration
created: 2026-09-27
tags: [session, workflow, ledger]
---

## Context

When an item has an open fork, `case-guppi` answers with a round of questions in the form of `.claude/skills/grill-me/SKILL.md`. The main agent translates the round into Russian and shows it line by line. The Render of `rule-case-build` makes the round "its numbered questions ... with no Case heading and nothing else". The Render of `rule-case-protocol` has the main agent add nothing between the questions and put its own text only after the last question. So the round opens straight with `❓ **Q1**`. In session 2050 the first rounds for Cases 464 and 465 did this, and the person saw the questions with nothing to explain the item.
In the rounds, the person chose these answers. `case-guppi` writes the context, because it has read the frame before it asks, and the main agent has not. Only the first round on an item carries it. The person's own `/grill-me` stays as it is, so `rule-skill-grill-me`, its Render and `estimate-skill-grill-me-asks-in-rounds` do not change. The context is one prose paragraph under the label `**Context:**`, with no fixed limit. Its parts follow the Language paragraph of `case-schema.md` (case 449): a sentence per part where one is enough, and a part with nothing to say left out, such as "where it goes wrong" for an item that is not a defect. The person judges its length.
The change touches two promises, so there are two sub-cases (`rule-atomicity`). 466.1 covers the round `case-guppi` writes. 466.2 covers how the main agent shows it. `rule-case-check` neither checks nor stores an answer with no Case heading, and its `Stop` comparison reads only Cases. So a round with a context passes both hooks unchanged, if the context carries no Case heading. `.claude/settings.json` and `guppi/casecheck.py` do not change, and no code judges the form of a round. `estimate-language-followed` says a round of `case-guppi` is shown "translated from the answer". The context is part of the answer, so that line stays true. `estimate-case-protocol-loaded` promises three things: `case-schema.md` equals the Render, it stands in the context after `/hi`, and `CLAUDE.md` repeats no paragraph of it. None of these speaks of a round, so it is not touched (case 378.5). The Language paragraph of `case-schema.md` still holds. The Case has no `create`, so no vault query ran.

## Problem

The first round on an item reaches the person with no framing. The person reads questions about a mechanism before being told what the item is, what goes wrong today, or what the round decides. No sentence of the vault lets `case-guppi` or the main agent put a context before the first question, and two sentences forbid it.

## Given

`rule-case-protocol` — its Render, the paragraph "Who builds a Case", where a round is shown
**＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
**＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing, its Criterion replaced whole
**＋** `.claude/agents/case-guppi.md` — the agent that writes the round and its context
**＋** `.claude/skills/grill-me/SKILL.md` — the form of a question in a round
**＋** `rule-case-check` — the hooks that write the file of a Case and compare its showing
**＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a Case that the main agent sends
**＋** `.claude/agents/ask-guppi.md` — the vault query the main agent dispatches at pre-spec

## History

- 2026-09-27 created · raw/2026-09-27/2050/ledger.md#case-466.2
