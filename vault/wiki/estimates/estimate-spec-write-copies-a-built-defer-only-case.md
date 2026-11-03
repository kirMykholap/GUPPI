---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-write]]"
purpose: Whether the Spec hook copies a Case that case-guppi built with only defer lines from its stored file, and keeps the short path for a Case the reply shows in the short form
method: uv run --project .guppi pytest .guppi/tests/test_ratified.py -k built_defer
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ratified` of `.guppi/guppi/ratified.py` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer`, and the same reply does not show Case N in the short form, by `is_short_form` of `.guppi/guppi/casecheck.py`: no `given`, no `when`, and a fence tagged `then` with `defer` items.

Then:
The hook takes Case N for a Case built by `case-guppi`: it reads the text stored for Case N and the sending of the file of Case N, as for a Case with lines of another kind.
**＋** It writes the stored text into the plan file, and into the approved Spec of the session once it stands, in the place of a ratified Case and not under `## Deferred`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, a block tagged `then` whose `defer` items it builds from the sub-points of `tasks`, and a block tagged `tasks`.
**＋** A store with no Case N: exit 2 with `case N: not built and checked by case-guppi — dispatch it` on stderr, and nothing of Case N is written.
**＋** A decision line of Case N that carries `{supersedes:case M}` removes Case M from the plan file and the approved Spec, as for any Case written in the run.
**－** A reply that shows Case N in the short form makes the hook write Case N under `## Deferred` from that reply, and the hook reads no stored text for it.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
