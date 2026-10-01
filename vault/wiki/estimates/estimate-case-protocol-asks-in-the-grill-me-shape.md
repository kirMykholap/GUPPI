---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi or at a stop of Work Mode, takes the question shape of grill-me, the exceptions kept in their own form
method: by hand at the close of a later session, each question of the main agent's own read in the transcript
origin: raw/2026-09-30/2356/ledger.md#case-561.13
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
The main agent puts a question to the person itself, outside a round of `case-guppi`: a decision it needs in the report of `/pre-spec`, a question at `/hi`, or a question at a stop of Work Mode.

Then:
Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
**＋** It stands in Russian, and its labels may stand translated.
**－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.

## History

- 2026-10-01 created · [[decision-case-561.13]]
