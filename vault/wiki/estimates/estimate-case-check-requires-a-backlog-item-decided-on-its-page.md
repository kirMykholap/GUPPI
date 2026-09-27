---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: A Case of case-guppi that names the page of an open backlog line, where no Case among it and its sub-cases both names the page and supersedes every Decision of its deferred_by, goes back to case-guppi
method: uv run pytest tests/test_casecheck.py -k backlog, then by hand the first answer of case-guppi on an item taken from the backlog
origin: raw/2026-09-27/2050/ledger.md#case-467.2
sprint: migration
created: 2026-09-27
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, and the pages of the vault.

Then:
For each open line of the Frontier whose source is `backlog`, each page that its title names in a code span and that carries `deferred_by` is checked against each top-level Case N of the answer that, itself or through a sub-case, names that page on a decision line other than a `defer`.
**＋** Case N gets a finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases in the answer both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and the missing mark. The hook exits 2, and `case-guppi` answers again.
**＋** The judgment is the function of `guppi/prespec.py` that the pre-spec check runs, imported, not copied.
**－** A Case of the answer that names no such page, an answer while no open line of the source `backlog` stands, and a page without `deferred_by` get no finding of this check.

## History

- 2026-09-27 created · [[decision-case-467.2]]
