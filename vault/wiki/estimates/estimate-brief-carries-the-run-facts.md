---
type: estimate
kind: QA
status: passed
target: "[[rule-brief]]"
purpose: Whether the brief ends the Readings due line of each pending Estimate read at the librarian's run with the facts its method and Criterion name, the stdout of guppi archive included, with no comparison or verdict, one line per Estimate
method: "by hand, after a librarian's run: vault/wiki/brief.md read against the run's report in the transcript of that run, recorded in the estimate line"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, librarian]
core: true
---

## Criterion

When:
The librarian `librarian-guppi` writes `vault/wiki/brief.md` in its run, and then runs `uv run --project .guppi guppi archive`.

Then:
For each `pending` Estimate whose `method` names the librarian's run, its line under Readings due of `vault/wiki/brief.md` ends with the facts that its `method` and `## Criterion` name, as the steps of the run before the brief printed or left them.
**＋** After `uv run --project .guppi guppi archive`, the librarian adds its stdout lines at the end of the Readings due line of each `pending` Estimate whose `method` names the archive step, and the close of `rule-close` commits the brief with them.
**＋** Each Estimate keeps one line under Readings due, with the Estimate, its `draft` rule and where it is read.
**－** The line compares nothing and carries no passed or failed, and the librarian writes no ledger line.
**－** The order of the steps does not change: the brief, then `uv run --project .guppi guppi archive`, then the close.
**－** No line of the brief names the commit of the close.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
