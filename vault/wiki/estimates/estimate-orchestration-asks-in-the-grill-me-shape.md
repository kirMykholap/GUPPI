---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi, at a stop of Work Mode, in Work Mode after a clash on whether another Case changes, or at pre-spec on whether a finding of ask-guppi not closed is fixed or left, takes the question shape of grill-me, the exceptions kept in their own form
method: "by hand at the Retro of a session that changes this Criterion or the Render of rule-orchestration: vault/wiki/orchestration.md as rendered, or the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-10-26
origin: raw/2026-09-30/2356/ledger.md#case-561.13
sprint: migration
created: 2026-09-30
tags: [session, workflow]
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

2026-10-26, Retro, by hand: vault/wiki/orchestration.md as rendered has each question the main agent puts itself (the report of /pre-spec, a question at /hi, a stop of Work Mode, the question after a clash in Work Mode, the question after the ask-guppi confirmation) take the shape of .claude/skills/grill-me/SKILL.md "in Russian, the labels translated or not", Russian being the language of the chat of this repository; the question of the next item, of an A line, of a sign-off, of going on to /pre-spec and the /work or /carry choice keep their own form

## History

- 2026-10-01 created · [[decision-case-561.13]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1441/ledger.md#L35
- 2026-10-02 renamed from `estimate-case-protocol-asks-in-the-grill-me-shape` · [[decision-case-595.13]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the question shape as orchestration.md sets it (case 595.13) · [[decision-case-595.13]]
- 2026-10-03 status: pending → passed · raw/2026-10-02/2300/ledger.md#L25
- 2026-10-04 updated: the Criterion replaced whole — the When names the question after a clash and the question on a finding not closed (case 632.10) · [[decision-case-632.10]]
- 2026-10-05 status: pending → passed · raw/2026-10-04/2245/ledger.md#L14
- 2026-10-07 updated: the Criterion replaced whole — the question whether to go on to /pre-spec keeps its own form · [[decision-case-697.4]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L39
- 2026-10-17 updated: the Criterion replaced whole — the question on another Case after a clash stands in Work Mode only · [[decision-case-872.6]]
- 2026-10-17 status: pending → passed · raw/2026-10-16/2104/ledger.md#L49
- 2026-10-26 updated: the Criterion replaced whole — the question stands in the language of the chat, not in Russian; the method reads at the Retro of a session that changes the Criterion too · [[decision-case-882.2]]
- 2026-10-26 status: pending → passed · raw/2026-10-17/2307/ledger.md#L51
