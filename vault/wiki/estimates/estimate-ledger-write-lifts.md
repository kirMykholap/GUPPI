---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
method: "pytest in .guppi/tests/test_ledger.py and .guppi/tests/test_gate.py with piped payloads against a temp vault; by hand once, the ledger of a session whose reply that ends Retro follows a refusal of a Stop hook in the same stretch: its lines written at that Stop, with its time"
checked: 2026-10-03
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, ledger]
core: true
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

2026-10-03, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
