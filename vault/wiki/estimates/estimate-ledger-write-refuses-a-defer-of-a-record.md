---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a defer line of a Lesson or a Decision page, so that no defer lands where no list shows it
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py -k record
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, ledger]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds, in a `LEDGER` block of a session with a `hi`, a `defer` decision line that no ledger holds yet.

Then:
A `defer` line whose slug names a Lesson or a Decision page, by `defers_a_record` of `.guppi/guppi/materialize.py`, whether its page stands or not, does not land in `raw/<hi date>/<hi HHMM>/ledger.md`, whatever text of the transcript holds it.
**＋** When the line stands in the reply just finished, the hook prints `ledger: line not written — <line>: a Lesson or a Decision page carries no deferred_by, so no list shows its defer — defer the rule or entity page whose change settles it` on stderr, once a stretch, and exits 2.
**＋** The other lines of the same block land as without it.
**＋** The hook of `rule-spec-write` refuses the short Case of the same line by the same judgment, so neither the plan nor the ledger holds it.
**－** A `defer` line of a rule, an entity, an Insight or an Estimate is not refused by `defers_a_record`.
**－** A refused line of an earlier text of the transcript prints no stderr line.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
