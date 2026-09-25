---
type: estimate
kind: QA
status: pending
target: "[[rule-ledger-write]]"
method: pytest in tests/test_ledger.py and tests/test_gate.py with piped payloads against a temp vault; the live reading once by hand — the lines of the Case in the session's ledger.md, written by the hook
checked: 2026-09-17
origin: raw/2026-09-09/ledger.md#case-10
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` fires at the end of a turn of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

Then:
In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
**＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
**＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
**－** An `estimate[...]` line the hook refuses by `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` does not land.
**－** Without a `hi`: exit 2 with the reason, the ledger untouched; with `stop_hook_active`: exit 0, nothing written.
**－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

## Result

2026-09-17, `uv run pytest -q tests/test_ledger.py tests/test_gate.py` 67 passed; live: the six lines of Case 224 stand in raw/2026-09-17/1119/ledger.md at 11:35:29, written by the Stop hook from the reply that ended in its LEDGER block, each once with its time; the gate's advice now reads "The text before a tool call waits for the next Stop" (test_an_item_of_the_plan_without_its_line_refuses_the_skill)

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-10
- 2026-09-09 updated: criterion follows the LEDGER block and the time prefix · raw/2026-09-09/ledger.md#case-15.1
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-11 updated: the midnight window added to the criterion; pending until the reading · [[decision-case-55.1]]
- 2026-09-11 updated: the transcript read-back added to the criterion; pending until the live reading · [[decision-case-55.2]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L72
- 2026-09-13 criterion: case 103.1 added · [[decision-case-103.1]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/0652/ledger.md#L4
- 2026-09-14 criterion: case 111.3 added · [[decision-case-111.3]]
- 2026-09-14 criterion: case 111.6 added · [[decision-case-111.6]]
- 2026-09-14 criterion: case 122 added · [[decision-case-122]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L7
- 2026-09-14 status: passed → passed · raw/2026-09-14/1029/ledger.md#L32
- 2026-09-14 criterion: case 136.3 added · [[decision-case-136.3]]
- 2026-09-14 criterion: case 111.6 removed · [[decision-case-136.3]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L27
- 2026-09-16 criterion: case 184 added · [[decision-case-184]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L15
- 2026-09-18 updated: the Criterion replaced whole — the text before a tool call is read at the next Stop, the gate's advice reworded (case 224.1) · [[decision-case-224.1]]
- 2026-09-18 status: pending → passed · raw/2026-09-17/1119/ledger.md#L40
- 2026-09-25 updated: the Criterion replaced whole — a reading the hook refuses as a change of the session does not land; Given dropped, its input moved into When (case 428.2) · [[decision-case-428.2]]
