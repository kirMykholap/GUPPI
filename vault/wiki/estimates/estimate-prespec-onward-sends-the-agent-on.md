---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-onward]]"
purpose: Whether guppi onward --plan, after /pre-spec, refuses the end of a reply that leaves no Case open in the Frontier and sends the agent on with the Cases still out, to the check and the exit or on with the loop after its findings, once a stretch and once more after each reply the ledger hook sent back, an answer with no LEDGER block included, judged by the refusals in the transcript whatever stop_hook_active says; silent before /pre-spec, on a reply that opens with STOP:, and otherwise
method: uv run --project .guppi pytest .guppi/tests/test_onward.py .guppi/tests/test_ledger.py, which cover a refusal of the ledger hook
checked: 2026-11-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, hooks, harness]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi onward --plan` receives the payload of the end of a reply of the main agent.

Then:
It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session and, after it, a `prespec` line of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block, or a refusal of the ledger hook in the stretch follows the reply of the main agent that ended just before it; its own refusal is not spent; and the reply does not open with `STOP:`.
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run --project .guppi guppi onward --plan`, and the command of the ledger hook is `uv run --project .guppi guppi ledger`.
**＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `refusals` of `.guppi/guppi/ledger.py`. So after a reply that the ledger hook sent back — a line it refused or held, or its reminder of a lesson with no mark — it sends the agent on again at the end of the next reply: the one that writes a line again, or an answer with no `LEDGER` block, such as the answer that no Case fixed the cause of the lesson.
**＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
**＋** Its reason on stderr sends the agent on with the Cases still out, to the check and the exit, or on with the loop after the findings of `/pre-spec`, as `estimate-prespec-onward-tells-the-loop-from-its-end` sets it.
**＋** Each reason adds that, when only the person can go on — a question the person must answer, or a Case that waits only for the person's word — the agent opens with `STOP:` a reply that carries a `LEDGER` block, or that answers a reply the ledger hook sent back, and asks the person instead; that a reply that shows a Case or a round of `case-guppi` carries no `LEDGER` block and opens with no `STOP:` line, in the layout `vault/wiki/orchestration.md` sets; and that while a `case-guppi` has not answered the agent ends the turn as `vault/wiki/orchestration.md` sets it for a Case out and goes on in the turn that the answer opens.
**＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript. `.claude/settings.json` registers it on `Stop`, after `uv run --project .guppi guppi onward`.
**－** A Case still out, as `rule-prespec-onward` judges it, does not keep it silent: it changes only its reason.
**－** With no `prespec` line of this session after its `hi` in the event log, it exits 0 and prints nothing, and its reason never tells the agent to call `/pre-spec`.
**－** A reply with no `LEDGER` block after a reply that the ledger hook did not send back gets no reason, a reply that shows a Case with no line before its first Case heading among them.
**－** An error of its own after it has read the payload, when a `prespec` line of this session stands after its `hi`, exits 2 with `onward: not checked: <error>` on stderr and the advice, when no Case is left out, to go on with the loop after the findings of `/pre-spec` or to run the check and exit Plan Mode; the advice does not name a call of `/pre-spec`. It does so at most once a stretch, judged by its own refusal in the stretch alone. Before `/pre-spec`, or when it cannot read the `prespec` line, an error of its own exits 0 and does not send the reply back. An empty payload exits 0.
**－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
**－** `uv run --project .guppi guppi onward` without `--plan` keeps its own judgment.

## Result

2026-11-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
