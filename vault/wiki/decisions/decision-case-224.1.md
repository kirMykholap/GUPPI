---
type: decision
case: "224.1"
status: current
update: ["[[rule-ledger-write]]", "[[estimate-ledger-write-lifts]]"]
origin: raw/2026-09-17/1119/ledger.md#case-224.1
sprint: migration
created: 2026-09-17
tags: [session, hooks, harness, ledger]
---

## Context

`insight-ledger-hook-reads-only-the-final-text` is the Insight over five lessons on the ledger hook: a `LEDGER` block that is not the last text of its turn "is lost". It was `actioned` by case 137 and reopened by the librarian of 2238 on the fifth lesson, `lesson-ledger-block-followed-by-a-tool-call` (the reply to case 222 ended in a ToolSearch call). Its Proposal asks one thing: read `guppi/ledger.py` against a transcript and settle whether an intermediate assistant text is in the transcript at all. Today `rule-ledger-write` and `CLAUDE.md` (the Render of `rule-case-protocol`) say the text before a tool call is never kept, not in the transcript, not in `last_assistant_message`; the refusal of `guppi gate` prints the same sentence. The Case touches `estimate-ledger-write-lifts` (the old shape, no `method` field — a recut by case 211) and `estimate-case-protocol-loaded` (no `method` field either); it does not touch `estimate-hook-registry-rendered`. No page is created; the lesson is a line the hook writes, `knowledge`, with a `source`.

## Problem

`transcript_texts` has collected every text of the main agent from the transcript since case 55.2, and `tests/test_ledger.py` fixes the case of a text with a block followed by a `tool_use` record — it passes. The transcripts hold the intermediate texts: session 2238 (Claude Code 2.1.272) — 19 of 19 texts followed by a tool call in the same turn, the block of case 222 among them; session 0747 of 2026-09-14 (2.1.270) — the block of case 117, written by the hook 13 seconds later at the `Stop` of the same turn; the session of 2026-09-13 (2.1.269) — the block of case 101, written at the next `Stop` 22 minutes later. The one measured loss is the block of case 109 in that same session: it is absent from the transcript, and nothing explains it. The lines of case 222 are in the ledger (01:25:46), written by the `Stop` at the end of the same turn; "the Stop hook read nothing" was a wrong diagnosis: the agent checked `ledger.md` before the turn had ended. The claim "never kept" in the rule, in `CLAUDE.md` and in the gate's advice is false; one gap is real: a turn that ends in a tool call has no `Stop`, its lines wait for the next `Stop` of the same session, and the last turn of a session has none.

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#case-224.1
