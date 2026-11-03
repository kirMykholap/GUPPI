---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check judges a reply after a refusal of any Stop hook as before it, gives a reason of one Case at most three times since the person's last message, and then lets the reply through with a line on stderr
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py — piped payloads and transcripts with refusals of the hook in a temp vault
checked: 2026-10-07
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi casecheck` of `.guppi/guppi/casecheck.py` fires at the end of a reply of the main agent in a session with a `hi`, and finds a reason to refuse it: a shown Case that differs from `<plan>.checked.json`, a shown Case whose file was not sent or differs from the store, or an error of its own after it read the payload.

Then:
The hook judges the reply the same whether `stop_hook_active` is set or not.
**＋** It gives a reason that names a Case, opening with `case <id>:`, while fewer than three of its own refusals in the stretch hold a reason of that Case, and any other reason while fewer than three of them hold the same reason.
**＋** It exits 2 while a reason is left to give, with those reasons on stderr.
**＋** When no reason is left to give, it exits 0 and prints on stderr one line per Case it let through: "casecheck: case <id> shown unchecked after three refusals; the Spec hook compares it at ratification".
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`; its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run --project .guppi guppi casecheck]: `, judged by `refusals` of `.guppi/guppi/ledger.py`, the function that `guppi onward` calls.
**－** A text of the main agent's own before a round of `case-guppi` or outside the list of a showing is no reason of the `Stop` run. `uv run --project .guppi guppi casecheck --prompt` refuses nothing, so it counts nothing.
**－** With `stop_hook_active` set and a transcript it cannot read, it exits 0 and prints nothing.
**－** The run `uv run --project .guppi guppi casecheck --subagent` keeps its own guard, the store.

## Result

2026-10-07, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
