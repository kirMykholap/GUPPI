---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi or at a stop of Work Mode, takes the question shape of grill-me, the exceptions kept in their own form
method: by hand at the close of a later session, each question of the main agent's own read in the transcript
checked: 2026-10-03
origin: raw/2026-09-30/2356/ledger.md#case-561.13
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
The main agent puts a question to the person itself, outside a round of `case-guppi`: a decision it needs in the report of `/pre-spec`, a question at `/hi`, or a question at a stop of Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
**＋** It stands in Russian, and its labels may stand translated.
**－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.

## Result

2026-10-03, by hand in the transcript of session 2300: the main agent's own questions of the three kinds the Criterion names were Q1 and Q2 of the /pre-spec report, each with its numbered title line, a Now line, Options, 🔹 options with After items and the ➡️ line, in Russian; no A line at /hi and no stop in Work Mode; the forks the main agent wrote in answer to the person's questions on C7 and C4 before any dispatch stood as plain lists, outside the three kinds

## History

- 2026-10-01 created · [[decision-case-561.13]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1441/ledger.md#L35
- 2026-10-02 renamed from `estimate-case-protocol-asks-in-the-grill-me-shape` · [[decision-case-595.13]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the question shape as orchestration.md sets it (case 595.13) · [[decision-case-595.13]]
- 2026-10-03 status: pending → passed · raw/2026-10-02/2300/ledger.md#L25
