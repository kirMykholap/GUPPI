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
is this script's, so a page never disappears by an agent's hand. `raw/<date>/` stays
where it is: every `origin` points into it and lint checks that path.

## How it works

`uv run guppi cleanup` moves every live page with `status: archived` to
`vault/archived/<sprint>/<date>/<category>/<slug>.md`. `sprint` is the first `## <id>`
heading of `sprint.md`, `date` the day of the run. The moved page gets the History
line `archived · cleanup`; `log.md` gets the same. The slug is removed from the
`children` and `estimates` lists of live pages, their sections are rebuilt and they
get a History line; an Insight's `children` keep archived lessons, since `severity`
counts the live ones. `[[slug]]` links in page bodies are not changed: Obsidian
resolves a name in any folder, and lint counts archived slugs as known. A live page
whose `parent` or `target` went to the archive is reported on stderr and left.

A page under `vault/archived/` whose status is no longer `archived` moves back to
`wiki/<category>/` with the History line `restored · cleanup`. Then the indexes are
rewritten with the writer of `guppi index`. A rerun moves nothing and exits 0. A
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
