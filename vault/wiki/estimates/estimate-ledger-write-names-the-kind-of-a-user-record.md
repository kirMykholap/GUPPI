---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: One function of .guppi/guppi/ledger.py says whether a user record of a transcript is the person's message or a returned answer, and the case check, the ledger hook, the onward hook and the token counter judge by it, so the turn and the stretch cannot drift apart
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py -k kind; by hand, a Grep of task-notification|"human" over .guppi/guppi/ that prints .guppi/guppi/ledger.py alone
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, ledger]
core: true
---

## Criterion

When:
The `Stop` hooks `uv run --project .guppi guppi casecheck`, `uv run --project .guppi guppi ledger`, `uv run --project .guppi guppi onward` and `uv run --project .guppi guppi context` run after a reply and read the transcript at `transcript_path`.

Then:
One function of `.guppi/guppi/ledger.py` names the kind of a `user` record of the transcript: the person's message when its `origin.kind` is `human`, a returned answer when its `origin.kind` is `task-notification`, and neither for any other record.
**＋** The turn of the reply, which `.guppi/guppi/casecheck.py` reads for a sending and for a round, is the records after the last record that is the person's message or a returned answer.
**＋** The stretch, which `.guppi/guppi/ledger.py` and `.guppi/guppi/onward.py` read for their own refusals, is the records after the last person's message, and a returned answer does not end it.
**＋** `.guppi/guppi/casecheck.py` and `.guppi/guppi/context.py` import that function, `.guppi/guppi/onward.py` reaches it through `own_refusals`, and no other module of `.guppi/guppi/` judges `origin.kind` of a `user` record.
**＋** One test runs `turn_of_reply`, `own_refusals` and the count of `.guppi/guppi/context.py` over one transcript that holds a person's message, a returned answer, a local command with no `origin`, a `peer` message, a refusal marked `isMeta` and a tool result, and asserts where each one starts.
**－** A record with no `origin.kind`, such as that of the local command that clears the session, a record of another kind, a record marked `isMeta` and a tool result open no turn and end no stretch.
**－** A transcript that holds neither kind of record gives the whole transcript as the turn and as the stretch.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
