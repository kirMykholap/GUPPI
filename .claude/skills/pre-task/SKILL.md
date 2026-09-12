---
name: pre-task
description: Check this Plan Mode's ratified decisions against each other and the vault before the Spec is approved.
---
Recorded: !`uv run guppi event pretask --session "${CLAUDE_SESSION_ID:-}"`

Run `uv run guppi pretask --check <the plan file of this Plan Mode>`. It prints one line
for every decision line of this session that has no item under its own Case in the plan,
for every item that has no line, for every line of `raw/<date>/frontier.md` still
open or closed by a Case the plan does not hold, for every ratified Case without a
`tasks` block, for every Estimate a `then` block creates or sets `pending` that no
task names, and for every `file` item on a path a Rule page governs. Fix the plan or the frontier for each,
then run it again until it prints nothing.

List every decision ratified in this Plan Mode, one line each: slug — decision type — purpose; for an `update` that changes a page's contract, add the page's `estimates` and whether the Case updates their criterion — an Estimate whose criterion quotes the changed wording and has no update line is a finding. Dispatch the `ask-guppi` agent once with that list and the question: which of
these contradict a page of the vault, a rule of `index.md`, or each other. Raise each
finding as a Case, or say in one line why it is already known. Then exit Plan Mode again.
