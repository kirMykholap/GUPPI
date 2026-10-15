---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
method: "pytest in .guppi/tests/test_ledger.py and .guppi/tests/test_gate.py with piped payloads against a temp vault; by hand once, the ledger of a session whose reply that ends Retro follows a refusal of a Stop hook in the same stretch: its lines written at that Stop, with its time"
checked: 2026-10-03
origin: raw/2026-09-09/ledger.md#case-10
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` fires at the end of a reply of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

Then:
In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
**＋** With `stop_hook_active` set, the hook writes and judges the lines as without it.
**＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
**＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
**＋** For each refused line of the reply just finished, the hook prints its stderr line only when that stderr line does not already stand in its own refusals of the stretch, and exits 2 when it prints one; a repeat of a line already told stays silent.
**＋** No `hi`, and an error of its own after it read the payload, exit 2 only when no refusal of its own stands in the stretch; otherwise the hook exits 0 and prints nothing.
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. Its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run --project .guppi guppi ledger]: `; one function of `.guppi/guppi/ledger.py` judges both, and `.guppi/guppi/onward.py` calls it with its own command.
**－** A line that a refusal of `rule-ledger-write` refuses does not land while that refusal holds.
**－** Without a `hi`, the ledger is untouched.
**－** With `stop_hook_active` set and a transcript it cannot read, it writes the lines of `last_assistant_message` and exits 0.
**－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

## Result

2026-10-03, at the /hi of session 1341: `uv run pytest tests/test_ledger.py tests/test_gate.py` 105 passed; by hand, session 0317 (transcript 5b311f89): in the stretch after the person's message at 04:51:52 the hook `uv run guppi onward --plan` refused the reply at 04:52:16; the reply that ends Retro at 05:05:59 carried 4 lines in its LEDGER block, and ledger lines 52-55 hold each once with 05:06:02, the time of that Stop

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
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L30
- 2026-09-27 updated: the Criterion replaced whole — a lesson line refused for its slug does not land (case 460.4) · [[decision-case-460.4]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L21
- 2026-09-29 updated: the Criterion replaced whole — a lesson line refused for its mark does not land while the refusal holds (case 497.2) · [[decision-case-497.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L46
- 2026-09-30 updated: the Criterion replaced whole — a line the hook cannot read does not land (case 552.3) · [[decision-case-552.3]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/2042/ledger.md#L32
- 2026-10-01 updated: the Criterion replaced whole — the hook writes whatever stop_hook_active says, tells each refused line once a stretch, and tells no hi and its own error once a stretch (case 577.3) · [[decision-case-577.3]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1341/ledger.md#L3
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
