---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check judges a reply after a refusal of any Stop hook as before it, gives a reason of one Case at most three times since the person's last message, and then lets the reply through with a line on stderr
method: uv run pytest tests/test_casecheck.py — piped payloads and transcripts with refusals of the hook in a temp vault
origin: raw/2026-10-06/0104/ledger.md#case-688.1
sprint: migration
created: 2026-10-06
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi casecheck` of `guppi/casecheck.py` fires at the end of a reply of the main agent in a session with a `hi`, and finds a reason to refuse it: a shown Case that differs from `<plan>.checked.json`, whose file was not sent or differs from the store, a text of the agent's own outside the list of a showing or before a round, or an error of its own after it read the payload.

Then:
The hook judges the reply the same whether `stop_hook_active` is set or not.
**＋** It gives a reason that names a Case, opening with `case <id>:`, while fewer than three of its own refusals in the stretch hold a reason of that Case, and any other reason while fewer than three of them hold the same reason.
**＋** It exits 2 while a reason is left to give, with those reasons on stderr.
**＋** When no reason is left to give, it exits 0 and prints on stderr one line per Case it let through: "casecheck: case <id> shown unchecked after three refusals; the Spec hook compares it at ratification".
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`; its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run guppi casecheck]: `, judged by the function of `guppi/ledger.py` that `guppi onward` calls.
**－** With `stop_hook_active` set and a transcript it cannot read, it exits 0 and prints nothing.
**－** The run `uv run guppi casecheck --subagent` keeps its own guard, the store.

## Result

2026-10-06, uv run pytest tests/test_casecheck.py: 157 passed; a showing after another hook's refusal with the flag is refused, the same wrong showing is refused three times and the fourth passes with the line "casecheck: case 7 shown unchecked after three refusals", two Cases are counted apart, a reason with no Case is counted by its text, the flag with an unreadable transcript passes silently

## History

- 2026-10-06 created · [[decision-case-688.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L37
