---
type: rule
kind: Leaf
purpose: Prevents a page from being born twice under two names
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: ["[[estimate-index-check-merges]]"]
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
Index check. Do what `handoff.md` asks first. Then, for each `create` entry in `materialize.yaml` other than an estimate — an Estimate is born with its Leaf and has no index — run the Grep of its category yourself — `^(purpose|deferred_by):` over `vault/wiki/<category>/`, `root_cause` for lessons, `pattern` for insights — and compare the entry's `purpose` (`root_cause` for a lesson) with every index line it returns; name the Grep and the number of lines in the report (case 147.3). Compare meanings, not words. Never compare across categories.
- The same thing already has a page: change the entry to `kind: update` of that
  slug, add `change: "merged by librarian: <why>"` and `librarian: merged`. Keep
  every other field of the entry as it is.
- A page is close but not the same: keep the entry and add `near: <slug>`.
When the index line does not settle same or near, open the page and name it in the report.
<!-- /rule-index-check -->

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.1
- 2026-09-10 estimate estimate-index-check-merges added · raw/2026-09-10/ledger.md#case-35.1
- 2026-09-10 updated: the read is for same-or-near only and is named in the report · raw/2026-09-10/ledger.md#case-44
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: estimate creates are not compared; four categories · [[decision-case-53.4]]
- 2026-09-14 updated: the index lines come from the librarian's own Grep of the category, not a file (case 147.3) · [[decision-case-147.3]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 status: draft → built · cascade
