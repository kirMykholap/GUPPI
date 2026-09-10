---
type: rule
kind: Leaf
purpose: Prevents a page from being born twice under two names
status: draft
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: rule-documentation
estimates: [estimate-index-check-merges]
origin: raw/2026-09-10/ledger.md#case-35.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Purpose

Prevents a page from being born twice under two names. Pre-task asked the vault
before the Case; this asks once more, with the finished content, before the page is
written. It is the one judgment the librarian acts on. Catching a duplicate here
avoids a page created and merged in the same session.

## Render

<!-- rule-index-check -->
Index check. Do what `handoff.md` asks first. Then, for each `create` entry in
`materialize.yaml`, compare its `purpose` (`criterion` for an estimate, `root_cause`
for a lesson) with every line of `vault/wiki/<category>-index.md` of the same
category. Compare meanings, not words. Never compare across categories.
- The same thing already has a page: change the entry to `kind: update` of that
  slug, add `change: "merged by librarian: <why>"` and `librarian: merged`. Keep
  every other field of the entry as it is.
- A page is close but not the same: keep the entry and add `near: <slug>`.
Open a page only when its index line is not enough to judge.
<!-- /rule-index-check -->

## Estimates

- [[estimate-index-check-merges]]

## Parent

- [[rule-documentation]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.1
- 2026-09-10 estimate estimate-index-check-merges added · raw/2026-09-10/ledger.md#case-35.1
