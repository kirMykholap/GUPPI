---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook writes the decision lines of a reply that follow an unmarked lesson of the session with no reminder of the addresses mark, and lands a decision line that carries it
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py — piped payloads and a session ledger in a temp vault; by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, ledger]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` writes fresh decision lines of the reply just finished, and a `lesson[<slug>]` line of the session stands before them, in the session's ledger or among the lines of the same `Stop`, with no `{addressed_by:...}` and no decision line after it that carries `{addresses:<slug>}`.

Then:
The hook writes every line of the `Stop` and prints no line about the lesson.
**＋** When no other refusal of the hook stands at that `Stop`, it exits 0.
**＋** A decision line that carries `{addresses:<slug>}` lands in the session's ledger as any decision line of its Case does.
**＋** `.guppi/guppi/ledger.py` holds no question about a lesson before a Case, and the new Render of `rule-orchestration` in the Spec names no reply that answers one.
**－** The hook holds back no decision line because it lacks `{addresses:...}`.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
