---
type: decision
case: "135"
status: current
update: ["[[insight-ledger-line-written-unchecked]]"]
origin: raw/2026-09-14/1229/ledger.md#case-135
sprint: migration
created: 2026-09-14
tags: [harness, ledger, workflow]
---

## Context

An Insight of severity 4, `open` since 2026-09-12, four children. Pattern: a ledger line is written verbatim and nothing reads it back until `materialize`, so a line that does not parse or does not match the Spec costs a session. The page's Proposal: (a) `guppi pretask --check` already reads the ledger for the `then`-item comparison (59.1) — put every line through `materialize.parse_line` in the same pass; (b) the table of `case-schema.md` should show `decision[case N]`, not `decision[case_id]` (Case 67 deferred it).

## Problem

Both halves of the Proposal were ratified on the day the Insight was created — session I, 2026-09-12: 75.2 (the grammar of the lines at pre-task) and 75.1 (the table of `case-schema.md`, `index.md`, `rule-case-protocol`). The Insight was not updated because an Insight could not be a Decision target then (124 made it one). The other children were closed on the way: 59.1 (every line to its `then` item and back), 72.5 (no nested Estimates any more — the Estimate is derived from a Leaf `create`, pre-task checks `method` and the slug), 122 (`guppi gate` refuses a Skill call while a `then` item has no line — a preview in `ratification` no longer passes for the record). Decide: is the Insight actioned.

## Given

`insight-ledger-line-written-unchecked`: `open`, `severity: 4`, children `lesson-spec-then-items-unchecked-against-ledger-lines`, `lesson-ledger-decision-line-written-without-the-case-word`, `lesson-ledger-preview-in-ratification-taken-for-the-record`, `lesson-pretask-nested-estimate-exempt-from-the-line-check`; all `clustered`.
**＋** `rule-prespec` `built`, `estimate-prespec-reconciles` `passed`: the `### case 75.2` block — every record line of the window through `materialize.parse_line`, one that does not read is a finding with its date and line number, exit 1; `check_grammar` in `guppi/pretask.py`; the blocks of 59.1 and 72.5 on the same page.
**＋** `case-schema.md`, the table "What a Case produces": `- decision[case 12][update][rule-x]{ref:rule-x}`; "The id is `case N` — the word and a space … (case 75.1)".
**＋** `rule-ledger-write` `built`, `estimate-ledger-write-lifts` `passed` with the block of 122: `guppi gate` on `PreToolUse Skill` refuses while a `then` item of the Spec has no decision line.
**＋** `CLAUDE.md` (Case protocol): a line outside a `LEDGER` fence is a preview, never a record.
**＋** The cascade of 104.2: the four children go `archived`, `cleanup` moves them; `actioned` is not an end state.
**－** An Insight is not a Leaf: no `contract`, no Estimate.
**－** The `Stop` moment stays verbatim: the hook does not validate the grammar — signed so in 75.2, not changed here.

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#case-135
