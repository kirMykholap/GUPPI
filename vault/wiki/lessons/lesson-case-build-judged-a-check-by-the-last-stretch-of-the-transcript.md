---
type: lesson
kind: error
root_cause: case-guppi described the behaviour of written_case_files from its name and docstring without following what its loop over agent_transcript_path collects, and did not search for an existing judgment of the name of a Case file before adding one
status: clustered
insight: "[[insight-case-build-claims-what-code-does-without-reading-it]]"
origin: raw/2026-10-28/2312/ledger.md#L29
sprint: plugin
created: 2026-10-28
tags: [case-build, prespec]
---

## Trigger

Case 896.4 as first ratified said that a round of case-guppi that wrote only its note is judged as an answer with no file written, and its task added a new name test for the note; ask-guppi at /pre-spec found that written_case_files reads every Write and Edit of the whole transcript, and that case_number already judges the name of a Case file

## Root cause

case-guppi described the behaviour of written_case_files from its name and docstring without following what its loop over agent_transcript_path collects, and did not search for an existing judgment of the name of a Case file before adding one

## History

- 2026-10-29 created · raw/2026-10-28/2312/ledger.md#L29
- 2026-10-29 updated: clustered under insight-case-build-claims-what-code-does-without-reading-it (synthesis) · raw/2026-10-28/2312/ledger.md#L29
