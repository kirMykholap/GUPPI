---
type: lesson
kind: error
root_cause: the agent took the ratification preview for the record and moved on to the Spec-writing tool calls without a LEDGER block; the hook dropped nothing, and lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn names a hook fault that did not happen; the case belongs with insight-ledger-line-written-unchecked, since nothing between the reply and guppi pretask --check holds the written lines against the Spec at the moment of writing
status: archived
insight: "[[insight-ledger-line-written-unchecked]]"
origin: raw/2026-09-12/ledger.md#L107
sprint: migration
created: 2026-09-12
tags: [ledger, workflow]
---

## Trigger

F24 of session J read guppi/ledger.py against the transcript of session I (763dd08e): 324 assistant records, none isSidechain; transcript_texts collects 46 texts, 15 hold a LEDGER fence, every one of the 15 is the last text of its turn, and all 106 lines they hold stand in ledger.md; the decision lines of Cases 59.1, 59.2, 59.4, 60, 63, 64, 65 and 66 appear in the transcript only as "> - decision[...]" inside the ratification blockquote of the acknowledging reply, never inside a fenced block

## Root cause

the agent took the ratification preview for the record and moved on to the Spec-writing tool calls without a LEDGER block; the hook dropped nothing, and lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn names a hook fault that did not happen; the case belongs with insight-ledger-line-written-unchecked, since nothing between the reply and guppi pretask --check holds the written lines against the Spec at the moment of writing

## Insight

- [[insight-ledger-line-written-unchecked]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L107
- 2026-09-12 updated: clustered by librarian: a ledger line is unchecked until materialize, with lesson-spec-then-items-unchecked-against-ledger-lines · raw/2026-09-12/ledger.md#L107
- 2026-09-14 insight section derived
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
