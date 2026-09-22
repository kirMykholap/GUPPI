---
type: lesson
kind: error
root_cause: the agent read the shape of the record as the completeness of the record — the question it put to the file was "does this field exist", while the claim it was about to sign was "every line is here"; the second question costs one more command and was not asked.
status: archived
insight: "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"
origin: raw/2026-09-22/2046/ledger.md#L21
sprint: migration
created: 2026-09-22
tags: [workflow, ledger]
---

## Trigger

Case 348 was ratified on the claim that every ledger line stands in `materialize.yaml` with its `line`, `text` and `origin`; the agent had checked that those fields exist on the entries it looked at, never that an entry exists for every line. `vault/raw/2026-09-22/0014/materialize.yaml` holds entries for lines 1–51, 58 and 60 of a 64-line ledger, and `unparsed` is empty.

## Root cause

the agent read the shape of the record as the completeness of the record — the question it put to the file was "does this field exist", while the claim it was about to sign was "every line is here"; the second question costs one more command and was not asked.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#L21
- 2026-09-23 updated: clustered by librarian: a fact signed on a check that does not cover it, with lesson-ledger-estimate-line-carried-a-count-not-read · raw/2026-09-22/2046/ledger.md#L21
- 2026-09-23 archived · insight actioned
- 2026-09-23 archived · cleanup
