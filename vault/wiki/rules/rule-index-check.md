---
type: rule
kind: Leaf
purpose: Prevents a page from being born twice under two names
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, workflow, librarian]
core: true
---

## Purpose

Prevents a page from being born twice under two names. The vault query before the Case asked
once; this asks once more, with the finished content, before the page is
written. It is the one judgment the librarian acts on. Catching a duplicate here
avoids a page created and merged in the same session.

## Render

<!-- rule-index-check -->
Index check. Do what `handoff.md` asks first. Then, for each `create` entry in `materialize.yaml` other than an estimate — an Estimate is born with its Leaf and has no index — run the Grep of its category yourself — `^(purpose|deferred_by):` over `vault/wiki/<category>/`, `root_cause` for lessons, `pattern` for insights — and compare the entry's `purpose` (`root_cause` for a lesson) with every index line it returns; name the Grep and the number of lines in the report. Compare meanings, not words. Never compare across categories.
- The same thing already has a page: change the entry to `kind: update` of that
  slug, add `change: "merged by librarian: <why>"` and `librarian: merged`. Keep
  every other field of the entry as it is.
- A page is close but not the same: keep the entry and add `near: <slug>`.
When the index line does not settle same or near, open the page and name it in the report.
<!-- /rule-index-check -->

## History

- 2026-10-14 shipped with GUPPI
