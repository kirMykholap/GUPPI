---
type: estimate
kind: QA
status: passed
target: "[[rule-pretask]]"
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Context

The skill is a short instruction plus one recorded line. What has to hold is that the line
lands where the hook looks, that the agent is dispatched once with the whole set rather
than per decision, and that nothing it returns is dropped on the floor.

## Criterion

Unit: `guppi pretask --check <plan>` against a temp vault — a decision line with its item
under its own Case passes; a line without an item, an item without a line, and an item
under another sub-case's heading are each one finding, exit 1; a `defer` line matches a
`defer` item and a `file` line an item with that `file`; no `hi`, exit 0 with a line on
stderr; the frontier of the `hi` date: a missing file, an open line, a `case N` without
its heading and a `defer case N` without its item are each one finding; a Case with decision lines and
no `tasks` block, and an Estimate created or set `pending` by a `then` block that no
task names, and a `file` item on a path a Rule page governs, a Leaf `create` item without `method`, a Leaf `update` item without `contract`, a Case with two or more Leaf items that create or say `contract: changed`, and a derived Estimate slug naming an existing page with no `slug` on the item, are each one finding; a Leaf's Estimate without a line of its own is none. One live run before a plan approval: the check runs first and its findings are
fixed in the plan; the event log gains a `pretask` line, the `ask-guppi`
agent is dispatched once with the list of this Plan Mode's decisions, and every finding it
returns is either raised as a Case or named as already known in the reply.

### case 73.4

When:
`guppi pretask --check <plan>` runs.

Then:
The frontier it checks is `raw/<hi date>/<hi HHMM>/frontier.md`; a missing file is one
finding, as before.

### case 74

When:
`guppi pretask --check <plan>` reads a ratified Case.

Then:
A Case with a line of a kind other than `defer` and no fenced block tagged `tasks` is
one finding; a Case whose lines are all `defer` is none.
**＋** The Render of `rule-pretask` says so in those words.
**－** The code does not change; the unit test of the exemption is the reading.

### case 75.2

When:
`guppi pretask --check <plan>` runs.

Then:
Every record line of the session's window — the ledgers of the window's dates, on the
`hi` date from the `hi` time on — goes through `materialize.parse_line`; each that
returns none is one finding with its date and line number, exit 1.
**－** Lines before the `hi` are not read; a preview outside a LEDGER block is not a
record and is not checked.

### case 90.2

When:
`guppi pretask --check` runs against the plan of this Plan Mode.

Then:
It prints one line for every `update` with `contract: changed` whose page carries no
Estimate or more than one while the item names no `estimate_slug`.
**＋** The line names the Case, the page and the page's Estimates, so the person can see
the choice.
**－** A page with exactly one Estimate is no finding.

### case 103.4

When:
`uv run guppi pretask --check` gathers the lines of the window.

Then:
The window is `raw/<hi date>/<hi HHMM>/ledger.md` whole, plus the date-level ledgers from the `hi` date to today from the `hi` time on, as today, while any exist.
**＋** A grammar finding names the file: `raw/<date>/<HHMM>/ledger.md:<n>` or `raw/<date>/ledger.md:<n>`.
**＋** `estimate-pretask-reconciles` gets a `### case 103.4` block, `pending`.

### case 128

When:
The person invokes `/pre-task` and the agent assembles the dispatch for `ask-guppi`.

Then:
The Render of `rule-pretask`: "Dispatch the `ask-guppi` agent once with that list and the question" → "Dispatch the `ask-guppi` agent once with that list, the absolute path of the plan file, the instruction to read for every Case there its `when` and `then` sections and its `then` block — `replace` old and new, `set`, `sections` — before judging a page, so that a finding can name a wrong wording or a wrong place, and the question".
**＋** `estimate-pretask-reconciles` gets a `### case 128` block, `pending`; read at this session's `/pre-task`: the dispatch carries the path and the instruction on `when`, `then` and the blocks, and no finding answers what the plan already does.
**－** `{supersedes:case 121}`: `decision-case-121` is superseded, `rule-pretask` loses `deferred_by`.

## Method

One reading by hand, written into the estimate line — the exception the Method rule
allows.

## Result

block 128 at the /pre-task of session N: the dispatch carried the plan file's absolute path and the instruction to read every Case's when, then and then block; ask-guppi returned ten findings, each naming a page and a sentence, and none answered what a then block already does; four were wrong places or absent old texts in the blocks themselves, which a summary would not have shown

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.2
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L75
- 2026-09-12 updated: the mechanical check of the plan against the session's decision lines joins the criterion; pending for the reading at this session's pre-task (case 59.1) · [[decision-case-59.1]]
- 2026-09-12 updated: the frontier findings join the criterion (case 59.2) · [[decision-case-59.2]]
- 2026-09-12 updated: the tasks findings join the criterion (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: the governed-file finding joins the criterion (case 59.6) · [[decision-case-59.6]]
- 2026-09-12 updated: the findings of case 72.5 join the criterion; pending until the unit reading · [[decision-case-72.5]]
- 2026-09-12 criterion: case 73.4 added · [[decision-case-73.4]]
- 2026-09-12 criterion: case 74 added · [[decision-case-74]]
- 2026-09-12 criterion: case 75.2 added · [[decision-case-75.2]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L158
- 2026-09-12 criterion: case 90.2 added · [[decision-case-90.2]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L208
- 2026-09-13 criterion: case 103.4 added · [[decision-case-103.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L38
- 2026-09-14 criterion: case 128 added · [[decision-case-128]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L25
