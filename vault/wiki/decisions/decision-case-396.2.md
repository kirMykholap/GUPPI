---
type: decision
case: "396.2"
status: current
update: ["[[estimate-case-protocol-loaded]]"]
origin: raw/2026-09-24/1916/ledger.md#case-396.2
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Context

Two Estimates of `rule-case-protocol` describe a model of the Criterion that no longer stands. Both open with `Given:`, while Case 378 left `given` in the Case and on the Decision page. `estimate-case-protocol-case-form` also says that `given`, `when` and `then` together are copied into the Criterion; now only `when` and `then` are. `estimate-case-protocol-loaded` has grown into a journal of 13 `＋` lines, each retelling one paragraph of the Render. By Case 378.5 the reading of a Render promises one thing: the file equals the Render and is loaded; the behaviour a paragraph describes is promised by the Estimate of that behaviour. Most lines of the journal already have such a home:
- the lines of 355.1, 355.2, 368 and 370 repeat `estimate-case-protocol-case-form`;
- 356.1 and 356.2 stand in `estimate-hi-writes-frontier`;
- 299.1 stands in `estimate-prespec-catches-a-superseded-case`;
- 306.6 stands in `estimate-glossary-ticks-the-spec`;
- 373 stands in `estimate-spec-reconcile-refuses-an-edit-of-the-plan`;
- "a session without `/hi` holds no Case" stands in `estimate-ledger-write-lifts`;
- the line of 294 and 296 is out of date: since Case 378.4 a pair inside the Criterion is refused, as `estimate-prespec-refuses-a-pair-inside-a-criterion` promises.

The line of 353 stands only in the journal: a `replace` or `reword` pair is signed after the sentence around each match is read, and a Case that changes a page reads its `estimates`. It moves to `estimate-case-protocol-case-form`. The first paragraph, "The one rule", has no Estimate of its behaviour, and this Case creates none. The language of the sections of a Case in the chat is promised by `estimate-language-followed`, the report of `frame-guppi` in `context` by `estimate-case-protocol-shows-the-built-case`, so neither enters the form of a Case. Both Estimates stand `pending`, `rule-case-protocol` `draft`. The three other Estimates of the rule (`-acknowledging-reply`, `-ledger-line-form`, `-checks-its-frame`) are written in the new model already and are not touched. An `update` with a `ref`, no vault query; `frame-guppi` was not dispatched: the behaviour of the rule does not change. The agent read the Render itself; it is loaded by the `/hi` of this session.

## Problem

The Criteria of two Estimates promise a model that no longer stands; one of them is also a journal that repeats the promises of others and breaks at every edit of the Render.

## Given

`estimate-case-protocol-loaded` — the Estimate whose Criterion and `method` are replaced.
**＋** `rule-case-protocol` — the page whose Render is `vault/wiki/case-schema.md`.
**＋** `guppi/render.py` — `uv run guppi render` writes the Render, `--check` compares the file with it.
**＋** `.claude/skills/hi/SKILL.md` — `/hi`, which loads `vault/wiki/case-schema.md` with `sprint.md`, `brief.md` and `glossary.md`.
**＋** `CLAUDE.md` — the system prompt, which does not carry the schema.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-396.2
