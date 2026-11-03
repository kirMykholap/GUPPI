---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Each Case the Stop hook writes into the plan is checked at once, and a finding comes back to the agent
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k checks_the_written; by hand, a ratification of a session
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` has written Case N into the plan file after a reply whose `LEDGER` block holds the decision lines of Case N.

Then:
The hook runs the checks of `prespec --check` on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
**＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
**＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan file.
**＋** A finding of a Case not written in this run is not reported.
**＋** With `stop_hook_active` set, the hook checks as without it, as `estimate-spec-write-answers-a-refusal` sets it, and a finding it already gave in the stretch is not given again, as `estimate-spec-write-tells-each-reason-once` sets it.
**－** A Case not written in this run, and a Case whose lines are all `defer` and that the reply shows in the short form, which the hook writes under `## Deferred`, are not checked.
**－** The Frontier is not read, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
**－** A ledger line of the window that does not parse is no finding of this check.
**－** The plan is compared with no other file, and no ratified copy `<plan>.ratified.md` is written.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
