---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi, at a stop of Work Mode, in Work Mode after a clash on whether another Case changes, or at pre-spec on whether a finding of ask-guppi not closed is fixed or left, takes the question shape of grill-me, the exceptions kept in their own form
method: "by hand at the Retro of a session that changes this Criterion or the Render of rule-orchestration: vault/wiki/orchestration.md as rendered, or the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-10-26
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
The main agent puts a question to the person itself, outside a round of `case-guppi`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
**＋** The question is a decision it needs in the report of `/pre-spec`, a question at `/hi` or a question at a stop of Work Mode.
**＋** Or, in Work Mode, it is the question whether another Case of the session changes after a Case was bounded around a clash with it.
**＋** Or, at `/pre-spec`, after the `ask-guppi` runs confirm their findings, it is the question whether each finding not closed is fixed or left.

Then:
Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
**＋** It stands in the language of the chat, and its labels may stand translated.
**－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, the question whether to go on to `/pre-spec` when no line under `## Cases` is open, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.
**－** In Plan Mode the main agent puts no question whether another Case is built again after a clash.

## Result

2026-10-26, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
