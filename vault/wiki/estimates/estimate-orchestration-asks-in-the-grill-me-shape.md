---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi, at a stop of Work Mode, after a clash on whether another Case is built again, or at pre-spec on whether a finding of ask-guppi not closed is fixed or left, takes the question shape of grill-me, the exceptions kept in their own form
method: by hand at the close of a later session, each question of the main agent's own read in the transcript
checked: 2026-10-04
origin: raw/2026-09-30/2356/ledger.md#case-561.13
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
The main agent puts a question to the person itself, outside a round of `case-guppi`. The question is one of these:
- a decision it needs in the report of `/pre-spec`;
- a question at `/hi`;
- a question at a stop of Work Mode;
- the question whether another Case of the session is built again after a Case was bounded around a clash with it;
- at `/pre-spec`, after the `ask-guppi` runs confirm their findings, the question whether each finding not closed is fixed or left.

This is with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
**＋** It stands in Russian, and its labels may stand translated.
**－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.

## Result

2026-10-04, at the close of session 2245, by hand from its transcript: the main agent's own questions of the kinds the Criterion lists — the two decisions of the /pre-spec report (the lesson of Case 620 inside the Insight of Case 636; what case-guppi does after a clash) and the question after the confirmation whether finding 3.1 of Case 636 is fixed or left — each stood in Russian with its numbered ❓ **Qn** - **<title>**: line, one **Сейчас:** text with its quotation as a blockquote, the label **Варианты:**, each option on a 🔹 line with one **После:** item, and the ➡️ line; the question which Frontier item is next, the sign-off questions of shown Cases and the choice between /work and /carry (by AskUserQuestion, as the hook of rule-spec-capture asked) kept their own form

## History

- 2026-10-01 created · [[decision-case-561.13]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1441/ledger.md#L35
- 2026-10-02 renamed from `estimate-case-protocol-asks-in-the-grill-me-shape` · [[decision-case-595.13]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the question shape as orchestration.md sets it (case 595.13) · [[decision-case-595.13]]
- 2026-10-03 status: pending → passed · raw/2026-10-02/2300/ledger.md#L25
- 2026-10-04 updated: the Criterion replaced whole — the When names the question after a clash and the question on a finding not closed (case 632.10) · [[decision-case-632.10]]
- 2026-10-05 status: pending → passed · raw/2026-10-04/2245/ledger.md#L14
