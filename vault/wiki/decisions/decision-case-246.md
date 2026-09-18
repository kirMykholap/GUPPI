---
type: decision
case: "246"
status: current
update: ["[[insight-hi-skill-substitution-checked-by-a-model-call]]"]
origin: raw/2026-09-18/1957/ledger.md#case-246
sprint: migration
created: 2026-09-18
tags: [harness, session, hooks]
---

## Context

`insight-hi-skill-substitution-checked-by-a-model-call` — an Insight `open`, severity 2, made by the librarian of the 1252 run over `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable` (session 1119: the cause named as the classifier's model, `render --check` by hand as the fallback) and `lesson-hi-substitution-fails-when-the-login-has-lapsed` (session 1252: the cause is a lapsed login, the cure is `/login` and `/hi` again; the first lesson was wrong). No Case touched it; session 1252 closed the question with the lesson. Its Proposal is one sentence in `rule-skill-hi`. `rule-skill-hi` is `built`, its Render is `.claude/skills/hi/SKILL.md`; its Estimate `estimate-hi-no-read-calls` is in the shape before case 193, so a change of the Render would bring a recut and a reading that only a live lapsed login can take. The Case touches no Estimate.

## Problem

The Insight asks to write the cure into the rule. The check of a `!` command is the client's, not the harness's: the harness has nothing to refuse and nothing to guard, and the lesson of 1252 already holds the cause and the cure. The question: accept the Proposal, reject it or defer.

## History

- 2026-09-18 created · raw/2026-09-18/1957/ledger.md#case-246
