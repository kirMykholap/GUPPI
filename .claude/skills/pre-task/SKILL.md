---
name: pre-task
description: Check this Plan Mode's ratified decisions against each other and the vault before the Spec is approved.
---
Recorded: !`uv run guppi event pretask --session "${CLAUDE_SESSION_ID:-}"`

Run `uv run guppi pretask --check <the plan file of this Plan Mode>`. It prints one line
for every decision line of this session that has no item under its own Case in the plan,
for every item that has no line, for every line of `raw/<hi date>/<hi HHMM>/frontier.md` (the session's folder, case 73) still open or closed by a Case the plan does not hold, for every ratified Case with a line of a kind other than `defer` and no `tasks` block (a defer-only Case has no work, case 74), for every Estimate a `then` block creates or sets `pending` that no
task names, for every `file` item on a path a Rule page governs, for every Leaf `create` item without `method`, for every Leaf `update` item without `contract`, for every Case with two or more Leaf items that create or say `contract: changed` (split the Case), and for every derived Estimate slug that names an existing page while the item has no `slug`; an Estimate has no line of its own (case 72.5). It also runs every record line of the session's window through `materialize.parse_line` and prints one line for each that does not parse, with its date and line number (case 75.2). Fix the plan, the frontier or the line for each, then run it again until it prints nothing.

List every decision ratified in this Plan Mode, one line each: slug — decision type — purpose; for an `update` that changes a page's contract, add the page's `estimates` and whether the Case updates their criterion — an Estimate whose criterion quotes the changed wording and has no update line is a finding. Dispatch the `ask-guppi` agent once with that list and the question: which of
these contradict a page of the vault, a rule of `index.md`, or each other. Raise each
finding as a Case, or say in one line why it is already known. Then exit Plan Mode again.
