---
type: decision
case: "461"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-defers-in-one-reply]]"]
origin: raw/2026-09-27/1819/ledger.md#case-461
sprint: migration
created: 2026-09-27
tags: [session, workflow, ledger]
---

## Context

When the person asks to put off an item, the main agent writes the short Case and its `LEDGER` line in one reply. The `Stop` hook of `rule-spec-write` then writes the short Case under `## Deferred`. `estimate-case-protocol-defers-in-one-reply` promises that in Plan Mode "the reply ends with the Frontier". It failed on the reading of session 1745 and failed again on the reading of session 1255. In 1255, the defer reply for Cases 454–456 was right in every other part. But the defers came at the close of Plan Mode, when no line was open, and a paragraph that proposed `/pre-spec` with a question followed the Frontier. The edit of the plan file seen in 1745 is now refused by the hook of Case 445.1.
The Render of `rule-case-protocol` says only that the agent "asks nothing about it", meaning the defer. The acknowledging reply ends with "the question which item is next". So the defer reply is the only reply that must end with no question, even when `/pre-spec` is the only next step. In the rounds the person chose these points. The promise changes, not the reply: the defer reply ends as the acknowledging reply does, and no hook is added. `rule-orchestration` stays in `backlog.md` as it stands. The acknowledging reply is not changed. It has the same gap when the Case closes the last open line, and that is left not done: its reading (Frontier W8) can show whether it matters.
Of the other Estimates of the rule, `estimate-case-protocol-loaded` promises only that the file equals the Render (case 378.5). `estimate-case-protocol-shows-the-built-case` speaks of the short form only as written by the main agent in English. `estimate-case-protocol-acknowledging-reply` speaks of the acknowledging reply. None of them is touched. The `replace` pair of this Case is in the paragraph "The short form — deferred decisions". The pairs of Case 458 are in "Who builds a Case" and "Language", so the anchors do not meet. No `create`, so no vault query ran.

## Problem

The Criterion forbids any text after the Frontier in a defer reply. At the close of Plan Mode no line is open, and the person needs to know what comes next. So the agent writes a question after the Frontier, and the Estimate fails on a reply that did what the person needed. The wording that fails is the promise, and a stricter Render would fail again for the same reason.

## Given

`rule-case-protocol` — its Render, the paragraph "The short form — deferred decisions", where the defer reply is described
**＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
**＋** `estimate-case-protocol-defers-in-one-reply` — the promise of the defer reply, its Criterion replaced whole
**＋** `rule-spec-write` — the `Stop` hook that writes the short Case into the plan file and `spec.md`
**＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose line the defer reply closes
**＋** `rule-prespec` — `/pre-spec`, the next step when no line under `## Cases` is open

## History

- 2026-09-27 created · raw/2026-09-27/1819/ledger.md#case-461
