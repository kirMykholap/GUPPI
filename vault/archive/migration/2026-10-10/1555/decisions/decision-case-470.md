---
type: decision
case: "470"
status: archived
update: ["[[estimate-skill-grill-me-asks-in-rounds]]"]
origin: raw/2026-09-28/0000/ledger.md#case-470
sprint: migration
created: 2026-09-28
tags: [harness, workflow]
---

## Context

`.claude/skills/grill-me/SKILL.md` is the text of `rule-skill-grill-me`. It reaches an agent in two ways: the person types `/grill-me`, or `case-guppi` loads it through `skills: [grill-me]` and asks the rounds of Plan Mode with it. The `When` of `estimate-skill-grill-me-asks-in-rounds` names only the person's typed command. So no round of `case-guppi` counts toward a reading. The handoff of session 2050 counts 14 such rounds in that session. The person seldom types `/grill-me`, so the reading may never come and `rule-skill-grill-me` stays in `draft`.
In the round, the person chose to widen the trigger to both paths. For `case-guppi`, the instructions that started the grill name the confirmation: the showing of the Case and its ratification (`rule-case-build`). The line on confirmation therefore holds as written. The `－` line on dispatching a sub-agent stays true on both paths.
At pre-spec, `ask-guppi` found that the new `When` would sign the form of a round of `case-guppi` twice. `estimate-case-build-writes-the-case` already signs "a round of questions in the form of `.claude/skills/grill-me/SKILL.md`", so one bad round would fail two Estimates. The person agreed to this fix: the form line reads only the person's `/grill-me`. On a round of `case-guppi`, this Estimate reads the frontier rule, finding facts and the confirmation, and a `－` line leaves the form to `estimate-case-build-writes-the-case`. That Estimate's Criterion is not touched.
This Case does not fix the two rounds that broke the frontier rule, in 465 and in the fourth round of 467. That fix is a separate promise on `rule-case-build`. Under this Case, a round that breaks the rule again counts as a `failed` reading of this Estimate. The Context of case 466 says this Estimate does not change. It stands in the Spec of session 2050 and on the live pages `decision-case-466.1` and `decision-case-466.2`. A Decision page records what held when it was written, so that sentence does not become false. The Purpose of `rule-skill-grill-me` still holds. The Case has no `create`, so no vault query ran.

## Problem

The promise of the grill-me skill can be read only on a command the person seldom types. The path where the skill is actually used, the rounds of `case-guppi`, gives no reading. The Estimate may stay `pending`, and its rule `draft`, with no end.

## Given

`estimate-skill-grill-me-asks-in-rounds` — the promise of the skill, its Criterion replaced whole and its method changed
**＋** `rule-skill-grill-me` — the rule the Estimate reads, unchanged
**＋** `.claude/skills/grill-me/SKILL.md` — the skill text both paths load
**＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by its `skills` field and names the confirmation of its rounds
**＋** `estimate-case-build-writes-the-case` — the promise of the form of a round of `case-guppi`, unchanged

## History

- 2026-09-28 created · raw/2026-09-28/0000/ledger.md#case-470
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
