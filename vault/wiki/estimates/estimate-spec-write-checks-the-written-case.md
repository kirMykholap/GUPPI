---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-write]]"
purpose: Each Case the Stop hook writes into the plan is checked at once, and a finding comes back to the agent
method: uv run pytest tests/test_ratified.py -k checks_the_written; by hand, the first ratification of a session after the change
origin: raw/2026-09-25/0051/ledger.md#case-414.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` has written Case N into the plan file and its ratified copy after a reply whose `LEDGER` block holds the decision lines of Case N.

Then:
The hook runs the checks of `prespec --check`, imported from `guppi/prespec.py`, on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
**＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
**＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan and in its ratified copy.
**＋** A finding of a Case not written in this run is not reported.
**－** On the re-fire (`stop_hook_active`) nothing is checked: exit 0.
**－** A Case not written in this run — a last showing that is a `DIFF` block — and a defer-only Case, which the hook writes under `## Deferred`, are not checked.
**－** The Frontier `raw/<hi date>/<hi HHMM>/frontier.md` is not read.
**－** The plan is not compared with its ratified copy, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
**－** A ledger line of the window that does not parse is no finding of this check.

## History

- 2026-09-25 created · [[decision-case-414.1]]
- 2026-09-25 updated: the Criterion replaced whole — a defer-only Case is written by the hook and not checked (case 421.1) · [[decision-case-421.1]]
