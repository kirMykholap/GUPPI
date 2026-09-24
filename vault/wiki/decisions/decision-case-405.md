---
type: decision
case: "405"
status: current
create: ["[[estimate-case-protocol-defers-in-one-reply]]"]
update: ["[[rule-case-protocol]]"]
origin: raw/2026-09-24/1916/ledger.md#case-405
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger]
---

## Context

Today a deferred decision is shown in the short form and waits for the person's "ratify" like any Case; only then does the acknowledging reply write its `LEDGER` line. The decision to defer, though, is the person's own words ("keep it", "defer it"); the second question checks only the wording of `purpose`. In this session C3 and C4 took one round more for it. `frame-guppi` found three contradictions, all taken in:
1. The one rule, "nothing changes without a Decision ratified by the human": it now says outright that the person's words asking for the defer are its ratification.
2. The `ratification` row of the Sections table is required of every Case: the short form now names it among the sections it does not hold.
3. Retro has no Frontier: the closing of a Frontier line stays with Plan Mode alone.

`estimate-case-protocol-acknowledging-reply` speaks of the reply after a ratification; a defer no longer has one, so it is not touched. The slug of the new Estimate is free. `rule-case-protocol` stands `draft`.

## Problem

Does a defer need a round of ratification of its own when the person asked for it?

## Given

`rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the section on the short form.
**＋** `estimate-case-protocol-defers-in-one-reply` — the new promise.
**＋** `rule-retro` — its Render `.claude/skills/retro/SKILL.md`: a short defer at Retro, which closes with three lists and no Frontier.
**＋** `raw/<date>/<hi HHMM>/spec.md` and the plan file — where the short Case is appended.
**＋** `rule-ledger-write` — writes the `LEDGER` lines of a reply.
**＋** `estimate-case-protocol-acknowledging-reply` — the reply after a ratification; a defer has none.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-405
