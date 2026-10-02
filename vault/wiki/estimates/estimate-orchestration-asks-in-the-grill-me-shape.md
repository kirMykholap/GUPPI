---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi or at a stop of Work Mode, takes the question shape of grill-me, the exceptions kept in their own form
method: by hand at the close of a later session, each question of the main agent's own read in the transcript
checked: 2026-10-01
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

2026-10-01, by hand at the close of session 1441, the main agent's own questions read in the transcript: at /pre-spec one question, on the silent loss of a second faulty ledger line, shown in the report as 1.Q1 and in the gathered list as 577.Q1, each with the numbered title line, one Now line, Options with one After item per option and the recommended answer on the arrow line, in Russian with the labels kept; at /hi only the question which item is next; the choice between /work and /carry by its picker; the sign-off questions of shown Cases in their own form; no stop in Work Mode

## History

- 2026-10-01 created · [[decision-case-561.13]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1441/ledger.md#L35
- 2026-10-02 renamed from `estimate-case-protocol-asks-in-the-grill-me-shape` · [[decision-case-595.13]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the question shape as orchestration.md sets it (case 595.13) · [[decision-case-595.13]]
