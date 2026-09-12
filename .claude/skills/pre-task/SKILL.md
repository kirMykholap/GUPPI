---
name: pre-task
description: Check this Plan Mode's ratified decisions against each other and the vault before the Spec is approved.
---
Recorded: !`uv run guppi event pretask --session "${CLAUDE_SESSION_ID:-}"`

List every decision ratified in this Plan Mode, one line each: slug — decision type — purpose; for an `update` that changes a page's contract, add the page's `estimates` and whether the Case updates their criterion — an Estimate whose criterion quotes the changed wording and has no update line is a finding. Dispatch the `ask-guppi` agent once with that list and the question: which of
these contradict a page of the vault, a rule of `index.md`, or each other. Raise each
finding as a Case, or say in one line why it is already known. Then exit Plan Mode again.
