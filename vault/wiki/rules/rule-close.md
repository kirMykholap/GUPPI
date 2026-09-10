---
type: rule
kind: Leaf
purpose: Prevents the librarian's writes from landing in the session's own commit, or from ending without a commit at all
status: draft
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: rule-documentation
estimates: [estimate-close-commits]
origin: raw/2026-09-10/ledger.md#case-36.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, git, librarian]
---

## Purpose

Prevents the librarian's writes from landing in the session's own commit, or from
ending without a commit at all. The Retro commit is the baseline. What the librarian
changed must be readable as one separate diff, six months on.

## Render

<!-- rule-close -->
Close. Run `make lint` and keep its output for the report. Commit only paths under
`vault/`: `git add vault && git commit -m "docs(vault): librarian, <date>"`, never
`--amend`, never anything outside `vault/`. Then return a report of at most twenty
lines: pages created and updated per category, entries marked incomplete or failed,
pages archived, the flags you raised, the lint total. Nothing else.
<!-- /rule-close -->

## Estimates

- [[estimate-close-commits]]

## Parent

- [[rule-documentation]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.1
- 2026-09-10 estimate estimate-close-commits added · raw/2026-09-10/ledger.md#case-36.1
