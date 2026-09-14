---
type: insight
pattern: A ledger line is written verbatim and nothing reads it back until materialize, so a line that does not parse or does not match the Spec costs a session.
status: actioned
children: ["[[lesson-spec-then-items-unchecked-against-ledger-lines]]", "[[lesson-ledger-decision-line-written-without-the-case-word]]", "[[lesson-ledger-preview-in-ratification-taken-for-the-record]]", "[[lesson-pretask-nested-estimate-exempt-from-the-line-check]]"]
severity: 0
addressed_by: "[[decision-case-135]]"
origin: raw/2026-09-12/ledger.md#L100
sprint: migration
created: 2026-09-12
tags: [harness, ledger, workflow]
---

## Pattern

Four lessons on the gap between the reply that writes a ledger line and the librarian that
reads it.

`lesson-spec-then-items-unchecked-against-ledger-lines` (session H): three ratified decision
lines had no item in their Case's `then` block - 53.3 wrote none, and the two lines of 55.1
sat under 55.2. The mismatch would have shown as `incomplete: then` in the yaml, one session
later.

`lesson-ledger-decision-line-written-without-the-case-word` (session I): the decision lines
up to 10:09 were written as `decision[58][update][slug]`, and `materialize.parse_line`
accepts `decision[case 58]` only; 30 lines stand under `unparsed` in the yaml of 2026-09-12.
The check of Case 59.1 found them while comparing the plan with the ledger; nothing found
them at the moment of writing.

`lesson-ledger-preview-in-ratification-taken-for-the-record` (session J): the lines of Cases
59.1, 59.2, 59.4, 60, 63, 64, 65 and 66 stand in the transcript of session I only as the
preview inside the `ratification` blockquote, never in a LEDGER fence; the agent took the
preview for the record. The read-back of `guppi/ledger.py` against that transcript found the
hook dropped nothing.

`lesson-pretask-nested-estimate-exempt-from-the-line-check` (session J): `pretask.items_of`
marks an Estimate nested under a Leaf create as covered by its parent's line, so the missing
create lines of `estimate-governed-files-hook-refuses` and `estimate-claude-md-rendered` were
reported by nothing; both were signed in the Spec of session I and never logged.

The `Stop` hook writes verbatim by design. Between the reply and `materialize` no step holds
a written line against the grammar or against the Spec, and a line that was never written is
harder still to see.

## Proposal

A suggestion, not a decision. `guppi pretask --check` already reads the day's ledger for the
`then`-item comparison Case 59.1 added; the same pass can put every line through
`materialize.parse_line` and report the ones that do not parse. Case 67 defers the other
half: the table of `case-schema.md` shows `decision[case_id][kind][slug]`, a placeholder read
literally, and should show `decision[case N]`.

## Children

- [[lesson-spec-then-items-unchecked-against-ledger-lines]]
- [[lesson-ledger-decision-line-written-without-the-case-word]]
- [[lesson-ledger-preview-in-ratification-taken-for-the-record]]
- [[lesson-pretask-nested-estimate-exempt-from-the-line-check]]

## Addressed by

- [[decision-case-135]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L100
- 2026-09-12 updated: clustered by librarian: two more lessons on a ledger line unchecked at the moment of writing · raw/2026-09-12/ledger.md#L107
- 2026-09-14 updated: actioned: the Proposal was done by 75.2 (line grammar at pre-task) and 75.1 (the case N form in case-schema.md); the children closed by 59.1, 72.5 and 122 (case 135) · [[decision-case-135]]
