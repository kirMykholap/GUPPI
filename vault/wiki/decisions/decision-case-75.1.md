---
type: decision
case: "75.1"
status: current
update: [case-schema, index, rule-case-protocol]
supersedes: [decision-case-67]
origin: raw/2026-09-12/ledger.md#case-75.1
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger]
---

## Context

Every decision line of session I up to 10:09 was written `decision[58][update][slug]`;
`materialize.parse_line` reads `decision[case 58][update][slug]` only. The agent took
the placeholder `decision[case_id][kind][slug]` of the table "What a Case produces" in
`case-schema.md` literally; the Render of `rule-case-protocol` shows the line only as
`- decision[...]`. Deferred as Case 67; the 30 wrong lines stand under `unparsed`
(`lesson-ledger-decision-line-written-without-the-case-word`). The Insight over it:
nothing between the reply and `materialize` holds a written line against the grammar.

## Problem

What the agent reads at session start does not show a decision line as the ledger
holds it; and nothing in the session reports a line that will not parse.

## Given

`case-schema.md` table: `- decision[case_id][kind][slug]{ref}{source}{supersedes}{tags:a,b}`.
`index.md` §4: line 158 shows `decision[case 3][create][entity-x]`, line 179
`decision[case_id][kind][slug]{ref:parent}{source:external_id}{tags:a,b}`, line 203
`{supersedes:case1}` without the space. `rule-case-protocol` Render: "A record is a
`- decision[...]`, `- estimate[...]` or `- lesson[...]` line"; `deferred_by:
[decision-case-67]`.
**＋** `materialize.parse_line`: `RECORD` then brackets; a decision needs three heads
and `heads[0]` starting with `case `; `supersedes` goes through `_case_of`.
**＋** `guppi pretask --check` already reads the ledgers of the window for the
then-item comparison (59.1); `parse_line` is importable from `guppi.materialize`.
**＋** 72.5, 73.4 and 74 update the Render of `rule-pretask` this session; 72.1 and
73.9 the Render of `rule-case-protocol`; each `replace` its own sentence.
**－** The 30 unparsed lines of 2026-09-12 stay as the trace; nothing rewrites them.

## Criterion

- [[estimate-case-protocol-loaded]] § case 75.1

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-75.1
