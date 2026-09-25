---
type: decision
case: "391.2"
status: current
create: ["[[estimate-case-protocol-shows-the-built-case]]"]
update: ["[[rule-case-protocol]]", "[[insight-workflow-case-written-without-reading-the-pages-it-changes]]"]
origin: raw/2026-09-24/1303/ledger.md#case-391.2
sprint: migration
created: 2026-09-24
tags: [session, workflow, ledger, harness]
---

## Context

The agent writes a Case from what it has in view: the dialogue, the rule page, the code. The pages the Case changes or runs beside are not read against it before the showing. A contradiction is found only by pre-spec, after the ratification, and its fix costs a showing again. It happened in sessions 1809 (Cases 175 and 164) and 1859 (eight contradictions in Case 387): the two lessons of `insight-workflow-case-written-without-reading-the-pages-it-changes`, `open`, severity 2. If the main agent reads the frame itself, that is 20–25 thousand tokens of Opus per Case, measured in this session from its transcript, and they stay in the context to the end of the session. `ask-guppi` does not fit: it searches by meaning, opens every dispatch with the Grep of the index lines of all rules and runs on Opus; over its 59 past dispatches before a `create` the median input is 205 772 tokens a dispatch. So the frame is read by a separate narrow agent on Sonnet. It gets the draft of the Case in the prompt of the call, not from the chat: `transcript_texts` in `guppi/ledger.py` takes only the text blocks, so the call is not a showing. State: `rule-plan-mode` `built`, its Estimates speak of the vault's answer before a `create` and of naming the Estimates; `rule-case-protocol` `draft`; `rule-ask` `built`, its Purpose is one entry point of the search by meaning, and the new agent does not search. `estimate-plan-mode-verified` is not touched: its Criterion speaks of the answer before a `create`. `estimate-case-protocol-case-form` speaks of what `context` closes with, which 391.2 extends; it is not touched here, since the one pass of Slice 3g rewrites it whole (378.1), and it is not read before that. No vault query: every `create` line of the ledger carries a `ref`. The four new names are free: a grep over the repository found none. Read against the Case: `rule-ask`, `rule-plan-mode`, `estimate-plan-mode-verified`, `estimate-ask-finds`, `rule-rules-schema` (the fields of a rule with `enforcement: render`) and `rule-render-harness`. One contradiction, taken in: an agent written by `guppi render` is available from the next session (case 139.1), so its reading is in the next session.

## Problem

A Case is shown without being read against its frame, and reading the frame in the main agent fills its context. Is a narrow, cheap agent needed that reads the frame before the showing, and a rule for when to call it?

## Given

`rule-case-protocol` — the section on the vault before a `create` in its Render.
**＋** `vault/wiki/case-schema.md` — the Render, written by `uv run guppi render`.
**＋** `rule-frame-check` — the agent `frame-guppi` the sentence names.
**＋** `estimate-case-protocol-shows-the-built-case` — the new Estimate of the check.
**＋** `insight-workflow-case-written-without-reading-the-pages-it-changes` — the Insight the Case sets `actioned`.

## History

- 2026-09-24 created · raw/2026-09-24/1303/ledger.md#case-391.2
