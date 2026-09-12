---
type: insight
pattern: A ledger line is written verbatim and nothing reads it back until materialize, so a line that does not parse or does not match the Spec costs a session.
status: open
children: [lesson-spec-then-items-unchecked-against-ledger-lines, lesson-ledger-decision-line-written-without-the-case-word]
severity: 2
origin: raw/2026-09-12/ledger.md#L100
sprint: migration
created: 2026-09-12
tags: [harness, ledger, workflow]
---

## Pattern

Two lessons on the gap between the reply that writes a ledger line and the librarian that
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

The `Stop` hook writes verbatim by design. Between the reply and `materialize` no step holds
a written line against the grammar or against the Spec.

## Proposal

A suggestion, not a decision. `guppi pretask --check` already reads the day's ledger for the
`then`-item comparison Case 59.1 added; the same pass can put every line through
`materialize.parse_line` and report the ones that do not parse. Case 67 defers the other
half: the table of `case-schema.md` shows `decision[case_id][kind][slug]`, a placeholder read
literally, and should show `decision[case N]`.

## Children

- [[lesson-spec-then-items-unchecked-against-ledger-lines]]
- [[lesson-ledger-decision-line-written-without-the-case-word]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L100
