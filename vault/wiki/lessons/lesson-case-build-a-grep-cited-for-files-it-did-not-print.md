---
type: lesson
kind: error
root_cause: case-guppi names the files of a search in its context from the files it read during the build, not from the output of the command it names, so a claim stands on a search that does not print it
status: clustered
insight: "[[insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]]"
origin: raw/2026-10-04/2041/ledger.md#L38
sprint: migration
created: 2026-10-04
tags: [workflow, session]
---

## Trigger

at the /pre-spec of session 2041 ask-guppi found that the context of Case 632 cites a Grep of ``Backlog` of the sprint page|Backlog of the sprint page`` as printing brief.md, .claude/agents/librarian-guppi.md and rule-documentation.md, while that pattern, the backtick standing before ## in the text, prints only brief.md; case-guppi ran a corrected Grep when built again

## Root cause

case-guppi names the files of a search in its context from the files it read during the build, not from the output of the command it names, so a claim stands on a search that does not print it

## History

- 2026-10-04 created · raw/2026-10-04/2041/ledger.md#L38
- 2026-10-04 updated: clustered under insight-workflow-fact-signed-from-a-check-that-does-not-cover-it (synthesis) · raw/2026-10-04/2041/ledger.md#L38
