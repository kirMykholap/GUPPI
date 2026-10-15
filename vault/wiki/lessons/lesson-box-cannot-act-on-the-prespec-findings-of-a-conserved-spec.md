---
type: lesson
kind: error
root_cause: /pre-spec dispatches ask-guppi over a conserved Spec, but rule-spec-box neither checks nor builds a Case of that Spec again and its check refuses a session that ratified a Case of its own, so a finding has no way to a fix before Work Mode
status: new
origin: raw/2026-10-15/1739/ledger.md#L16
sprint: plugin
created: 2026-10-15
tags: [prespec, workflow, box]
---

## Trigger

in session 1739 the ask-guppi run of /pre-spec over the conserved Spec of raw/2026-10-15/0553/ found 13 findings, among them that guppi ship --allow-draft needs a tag the stop task places only after Work Mode and that the passed Estimates it ships carry pointers outside a bracket so prod cannot build; the person chose to run /box as is

## Root cause

/pre-spec dispatches ask-guppi over a conserved Spec, but rule-spec-box neither checks nor builds a Case of that Spec again and its check refuses a session that ratified a Case of its own, so a finding has no way to a fix before Work Mode

## History

- 2026-10-15 created · raw/2026-10-15/1739/ledger.md#L16
- 2026-10-15 updated: tagged box, the tag the ledger hook refused at the Retro of session 1739 · [[decision-case-826]]
