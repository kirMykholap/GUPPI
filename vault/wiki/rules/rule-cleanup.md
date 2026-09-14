---
type: rule
kind: Leaf
purpose: Prevents an archived page from staying among the live ones, or the indexes from lagging behind the vault
status: built
enforcement: check
implementation_ref: [guppi/cleanup.py, tests/test_cleanup.py]
parent: rule-documentation
estimates: [estimate-cleanup-moves]
origin: raw/2026-09-10/ledger.md#case-33
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Purpose

Prevents an archived page from staying among the live ones, or the indexes from
lagging behind the vault. `archived` is a status the generator sets. The file move
is this script's, so a page never disappears by an agent's hand. `raw/<date>/` is not
this script's: `guppi archive` moves an applied session ([[rule-raw-archive]]).

## How it works

`uv run guppi cleanup` moves every live page with `status: archived` to
`vault/archive/<sprint>/<date>/<HHMM>/<category>/<slug>.md`. `sprint` is the first
`## <id>` heading of `sprint.md`, `date` the day of the run, `HHMM` the session of the
run: the latest `<HHMM>/` folder under `raw/<date>/`, and without one the latest of the
nearest date back (case 102.2). The moved page gets the History
line `archived · cleanup`; `log.md` gets the same. The slug is removed from the `children` lists of live pages and from the `estimates` lists of entities and rules, their sections are rebuilt and they get a History line; an Insight's `children` keep archived lessons, since `severity`
counts the live ones. `[[slug]]` links in page bodies are not changed: Obsidian
resolves a name in any folder, and lint counts archived slugs as known. A live page
whose `parent` or `target` went to the archive is reported on stderr and left.

A page under `vault/archive/`, at any depth, whose status is no longer `archived` moves back to
`wiki/<category>/` with the History line `restored · cleanup`. Then the four indexes are rewritten with the writer of `guppi index`; an archived Estimate leaves no line, since estimates have none. A rerun moves nothing and exits 0. A
file that cannot be moved, or a name already taken in the archive, is reported on
stderr with exit 1; the other pages still move.

## Estimates

- [[estimate-cleanup-moves]]

## Parent

- [[rule-documentation]]

## Implementation

- `guppi/cleanup.py`
- `tests/test_cleanup.py`

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-33
- 2026-09-10 estimate estimate-cleanup-moves added · raw/2026-09-10/ledger.md#case-33
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: four indexes; estimates lists of entities and rules only · [[decision-case-57]]
- 2026-09-13 updated: raw/ is guppi archive's, not cleanup's (case 100.4) · [[decision-case-100.4]]
- 2026-09-13 updated: the root is vault/archive/, the page lands under the session of the run (case 102.2) · [[decision-case-102.2]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
