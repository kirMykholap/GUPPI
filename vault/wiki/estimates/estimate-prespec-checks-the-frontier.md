---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: The Frontier of the session exists and every closed line has a box and a closer that agree with its source
method: uv run --project .guppi pytest .guppi/tests/test_prespec.py
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`, and the title line of `<plan>` may name the `vault/raw/<date>/<HHMM>/spec.md` of a folder that holds `carry.md`.
**＋** The check reads the decision lines of the session's window, the decision lines of the `vault/raw/<date>/<HHMM>/ledger.md` of that folder when the title line names one, and the pages of the vault.

Then:
A missing file is the finding `frontier: <path> is missing`.
**＋** An open line under `## Cases` is a finding. An open line under `## Work` or `## Ask` is not.
**＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `defer`, `kept` and `defer case N` is a finding.
**＋** These pairings of box and closer are findings: `[x]` with `defer`, `kept` or `defer case N`, and `[-]` with `case N` or `work`.
**＋** `defer` is clean only after the source segment `sprint`, the segment before the closer. `kept` is clean only after the source `backlog`. After any other source, each one is a finding.
**＋** `defer case N` after the source `sprint` is a finding. After the source `backlog`, it is a finding when no `defer` line of Case N or of its sub-cases names a slug that the title, the text before the first ` · `, names in a code span. It is also a finding for each Case M of the `deferred_by` of such a page when no Case among Case N and its sub-cases both names the page on a `defer` line and carries `{supersedes:case M}`. The lines of Case N are those of the session's window and, for a Case of the conserved Spec, those of the `ledger.md` of its folder.
**＋** After another source, `defer case N` is a finding when there is no `defer` item under Case N in the plan, and none under Case N of the `spec.md` that the title line of the plan names.
**＋** A line closed `case N` is a finding when the plan has no heading of Case N.
**－** A title line that names no folder holding `carry.md` adds no Case and no ledger: `defer case N` after the source `backlog` is then judged against the session's window alone, and after a source other than `sprint` or `backlog` against the plan alone.
**－** A line that is not a box line, such as `Backlog: N items` or an indented `- near` line, is not read. No line of another session's Frontier file is read.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
