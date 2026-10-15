---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A Case of case-guppi that names the page of an open backlog line, where no Case among it and its sub-cases both names the page and supersedes every Decision of its deferred_by, goes back to case-guppi
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k backlog, then by hand the first answer of case-guppi on an item taken from the backlog
checked: 2026-10-05
origin: raw/2026-09-27/2050/ledger.md#case-467.2
sprint: migration
created: 2026-09-27
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of that file, the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, and the pages of the vault.

Then:
For each open line of the Frontier whose source is `backlog`, each page that its title names in a code span and that carries `deferred_by` is checked against each top-level Case N of the file that, itself or through a sub-case, names that page on a decision line other than a `defer`.
**＋** Case N gets a finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases in the file both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and the missing mark. The hook exits 2, and `case-guppi` fixes the file.
**＋** The judgment is the function of `.guppi/guppi/prespec.py` that the pre-spec check runs, imported, not copied.
**－** A Case of the file that names no such page, a file while no open line of the source `backlog` stands, and a page without `deferred_by` get no finding of this check.

## Result

2026-10-05, Plan Mode of session 1831, case 669: set passed by the person's decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-09-28, `uv run pytest tests/test_casecheck.py -k backlog` 6 passed; by hand, session 0000: the first answers of case-guppi on items taken from the backlog — C5 (`insight-case-build-promise-lines-compared-by-no-check`, no `deferred_by`) and C6 (`insight-workflow-code-live-before-the-page-it-reads`, `deferred_by` 238), C6 answered with `{supersedes:case 238}` on 473.2, the line that names the page; the store holds both Cases with no finding, as the Criterion says

## History

- 2026-09-27 created · [[decision-case-467.2]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/0000/ledger.md#L30
- 2026-10-05 updated: the Criterion replaced whole — the Cases are read from the file case-guppi wrote (case 645.14) · [[decision-case-645.14]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.4]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
