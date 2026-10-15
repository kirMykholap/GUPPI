---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-onward]]"
purpose: Whether guppi onward --plan, after /pre-spec, refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode and sends the agent to the check and the exit or on with the loop after its findings, once a stretch and once more after each reply the ledger hook sent back, an answer with no LEDGER block included, judged by the refusals in the transcript whatever stop_hook_active says; silent before /pre-spec, on a reply that opens with STOP:, and otherwise
method: uv run --project .guppi pytest .guppi/tests/test_onward.py .guppi/tests/test_ledger.py, which cover a refusal of the ledger hook
checked: 2026-10-07
origin: raw/2026-09-30/2356/ledger.md#case-561.5
sprint: migration
created: 2026-09-30
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi onward --plan` receives the payload of the end of a reply of the main agent.

Then:
It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session and, after it, a `prespec` line of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block, or a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it; no Case is still out, as `rule-prespec-onward` judges it; its own refusal is not spent; and the reply does not open with `STOP:`.
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run --project .guppi guppi onward --plan`, and the command of the ledger hook is `uv run --project .guppi guppi ledger`.
**＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `refusals` of `.guppi/guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply: the one that writes a line again, or an answer with no `LEDGER` block, such as the answer that no Case fixed the cause of the lesson.
**＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
**＋** Its reason on stderr sends the agent to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
**＋** Each reason adds that, when only the person can go on — a Case still out with its `case-guppi`, or a question the person must answer — the agent opens its reply with `STOP:` and asks the person instead.
**＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
**＋** `.claude/settings.json` registers it on `Stop`, after `uv run --project .guppi guppi onward`.
**－** With no `prespec` line of this session after its `hi` in the event log, it exits 0 and prints nothing, and its reason never tells the agent to call `/pre-spec`.
**－** A reply with no `LEDGER` block after a reply that the ledger hook did not send back gets no reason.
**－** An error of its own after it has read the payload, when a `prespec` line of this session stands after its `hi`, exits 2 with `onward: not checked: <error>` on stderr and the advice, when no Case is left out, to go on with the loop after the findings of `/pre-spec` or to run the check and exit Plan Mode; the advice does not name a call of `/pre-spec`. It does so at most once a stretch, judged by its own refusal in the stretch alone. Before `/pre-spec`, or when it cannot read the `prespec` line, an error of its own exits 0 and does not send the reply back. An empty payload exits 0.
**－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
**－** `uv run --project .guppi guppi onward` without `--plan` keeps its own judgment.

## Result

2026-10-07, uv run pytest tests/test_onward.py tests/test_ledger.py: 188 passed; silent before /pre-spec, the answer with no LEDGER block to a reply the ledger hook sent back exits 2, the reply after its own reason at that answer exits 0, its own error exits 0 before /pre-spec and 2 after it with advice that names no /pre-spec

## History

- 2026-10-01 created · [[decision-case-561.5]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L39
- 2026-10-02 updated: the Criterion replaced whole — the run speaks again after each reply the ledger hook refused (case 597.1) · [[decision-case-597.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L14
- 2026-10-04 updated: method names no Plan Mode at which the ledger hook refuses a line, a moment no one brings on; the tests cover the refusal (case 625) · [[decision-case-625]]
- 2026-10-06 updated: the Criterion replaced whole — after /pre-spec the reason sends the agent to the check and the exit, or on with the loop, as estimate-prespec-onward-tells-the-loop-from-its-end sets it; purpose and method set anew (case 686.2) · [[decision-case-686.2]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L36
- 2026-10-07 updated: the Criterion replaced whole — silent before /pre-spec, and the answer with no LEDGER block to a reply the ledger hook sent back is sent on too; purpose set anew · [[decision-case-696.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L35
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
