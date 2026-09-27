---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: A Case that decides an item taken from the backlog names its page and supersedes every Decision of its deferred_by, or pre-spec reports it
method: uv run pytest tests/test_prespec.py -k backlog
origin: raw/2026-09-27/2050/ledger.md#case-467.1
sprint: migration
created: 2026-09-27
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, the decision lines of the session's window, and the pages of the vault.

Then:
For each line of the Frontier closed `[x] … · backlog · case N`, each page that its title names in a code span and that carries `deferred_by` is checked against Case N and its sub-cases.
**＋** A finding when no decision line of Case N or of its sub-cases, other than a `defer`, names that page.
**＋** A finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and `{supersedes:case M}`.
**－** A line of another source, an open line, a line closed `work` or put off, and a page without `deferred_by`, such as an open Insight or a note of the sprint page's `## Backlog`, give no finding of this check.

## History

- 2026-09-27 created · [[decision-case-467.1]]
