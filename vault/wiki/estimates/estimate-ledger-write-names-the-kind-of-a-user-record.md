---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: One function of guppi/ledger.py says whether a user record of a transcript is the person's message or a returned answer, and the case check, the ledger hook, the onward hook and the token counter judge by it, so the turn and the stretch cannot drift apart
method: uv run pytest tests/test_ledger.py -k kind; by hand, a Grep of task-notification|"human" over guppi/ that prints guppi/ledger.py alone
checked: 2026-10-02
origin: raw/2026-10-02/1202/ledger.md#case-592
sprint: migration
created: 2026-10-02
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hooks `uv run guppi casecheck`, `uv run guppi ledger`, `uv run guppi onward` and `uv run guppi context` run after a reply and read the transcript at `transcript_path`.

Then:
One function of `guppi/ledger.py` names the kind of a `user` record of the transcript: the person's message when its `origin.kind` is `human`, a returned answer when its `origin.kind` is `task-notification`, and neither for any other record.
**＋** The turn of the reply, which `guppi/casecheck.py` reads for a sending and for a round, is the records after the last record that is the person's message or a returned answer.
**＋** The stretch, which `guppi/ledger.py` and `guppi/onward.py` read for their own refusals, is the records after the last person's message, and a returned answer does not end it.
**＋** `guppi/casecheck.py` and `guppi/context.py` import that function, `guppi/onward.py` reaches it through `own_refusals`, and no other module of `guppi/` judges `origin.kind` of a `user` record.
**＋** One test runs `turn_of_reply`, `own_refusals` and the count of `guppi/context.py` over one transcript that holds a person's message, a returned answer, a local command with no `origin`, a `peer` message, a refusal marked `isMeta` and a tool result, and asserts where each one starts.
**－** A record with no `origin.kind`, such as that of the local command that clears the session, a record of another kind, a record marked `isMeta` and a tool result open no turn and end no stretch.
**－** A transcript that holds neither kind of record gives the whole transcript as the turn and as the stretch.

## Result

2026-10-02, uv run pytest tests/test_ledger.py -k kind: 1 passed; Grep task-notification|"human" over guppi/ printed guppi/ledger.py (HUMAN, NOTIFICATION, user_kind) and guppi/casecheck.py, whose three hits are docstring lines naming user_kind of guppi/ledger.py; no other module judges origin.kind in code

## History

- 2026-10-02 created · [[decision-case-592]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1834/ledger.md#L37
