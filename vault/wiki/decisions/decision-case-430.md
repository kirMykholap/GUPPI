---
type: decision
case: "430"
status: current
update: ["[[rule-context-size]]", "[[estimate-context-size-warns-past-the-limit]]"]
supersedes: ["[[decision-case-404]]", "[[decision-case-409]]", "[[decision-case-418]]", "[[decision-case-422]]"]
origin: raw/2026-09-25/1654/ledger.md#case-430
sprint: migration
created: 2026-09-25
tags: [hooks, harness, session]
---

## Context

Two hooks count the size of the context from the transcript. The hook `uv run guppi context` on `Stop` shows the person a line with the size after each reply. Past 400 000 tokens it appends `— past 400 000: close the session` to it. The hook `uv run guppi context --prompt` on `UserPromptSubmit` prints an order to the agent past the limit: open the reply by saying that the session must be closed by /retro, then /handoff, before the next Case. Below the limit it is silent.
In session 1228 the limit was passed at 456 635 tokens. The hook printed the order, but the person had just asked for /retro, and the agent called /retro at once without opening its reply with the recommendation. So the reading of `estimate-context-size-warns-past-the-limit` is recorded `failed`. Its Criterion promises an order the agent obeys.
The person said that past 400 000 the hook must not demand to finish at once, but inform: the session is already costly, taking on new work is not recommended, and when the Frontier holds open items, deferring them is better. That is an informative note, not a direct instruction. The limit of 400 000 stays: in the person's words, the rest works, with no complaints. This also answers the question of Cases 404, 409, 418 and 422. Case 404 deferred the limit, and Cases 409, 418 and 422 the limit and the text of the hook past it, to a session that reaches the limit. Case 409 already recorded that the person reads the note as "take no more work", not as an order to go to Retro at once. Case 429 allowed several `{supersedes:case N}` on one decision line. So the line of `rule-context-size` retires all four deferred decisions at once.
C5 and C9 are one Case without sub-cases. Both items are about the text past the limit, and it lies in one promise, `estimate-context-size-warns-past-the-limit`. Its Criterion is replaced whole. The line of the hook on `Stop` changes its end with it: `close the session` is the same kind of order, and in the same Criterion. Otherwise the person's words would stay true only in half. If the end of the line must stay, that is a change of this Case.
What the frame check showed. How it works of `rule-context-size` has a sentence on the order. It becomes false, so the Case changes it by one `replace` pair. The Purpose of `rule-context-size`, that the person sees how full the context is, stays true. The field `purpose` of `estimate-context-size-warns-past-the-limit` says that the agent tells the person to close the session. That becomes false, so it is replaced together with the Criterion. The Criterion of `estimate-context-size-shown-after-each-reply` promises only the start of the line on `Stop`, so the Case does not touch it. Two more hooks run on `UserPromptSubmit` beside `guppi context --prompt`. `guppi event prompt` writes the `hi` line on `/hi` (`rule-event-log`). `guppi gate` refuses a typed `/pre-spec`, `/retro`, `/handoff` by the rules `rule-retro-commit` and `rule-ledger-write`. None of them reads the output of `guppi context`, and the note contradicts none of them. The commands in `.claude/settings.json` and the Render of `rule-hook-registry` do not change. The docstrings of `guppi/context.py` and `tests/test_context.py`, and the test of the limit, name the old order; the tasks edit them. The decision pages of 392.2 and of the earlier defers are history, and the Case does not edit them. There is no `create`, so no vault query is due. By Case 428.1 the next session measures the new Criterion, at the first prompt past 400 000 tokens.

## Problem

Past 400 000 tokens the hook gives the agent an order to close the session, and the person wants only an informative note. The Criterion promises that the agent obeys the order, and the reading of that promise failed. It must be decided what both hooks say past the limit and what the Estimate promises.

## Given

`rule-context-size` — the rule of the context-size hooks; its How it works states what they print past the limit
**＋** `estimate-context-size-warns-past-the-limit` — the promise past 400 000 tokens
**＋** `guppi/context.py` — `prompt_text` and `stop_line`, the texts past the limit
**＋** `tests/test_context.py` — the tests of the limit
**＋** `.claude/settings.json` — the `UserPromptSubmit` hook `uv run guppi context --prompt` and the `Stop` hook `uv run guppi context`

## History

- 2026-09-25 created · raw/2026-09-25/1654/ledger.md#case-430
