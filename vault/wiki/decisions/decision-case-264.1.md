---
type: decision
case: "264.1"
status: current
update: ["[[estimate-generate-renames]]"]
origin: raw/2026-09-20/0958/ledger.md#case-264.1
sprint: migration
created: 2026-09-20
tags: [harness, workflow, tests]
---

## Context

`estimate-generate-renames` is a QA Estimate under `rule-page-generation`, `pending`; its reading — the librarian's run on Case 261 — stands as the line of 09:38:37 in the ledger of `raw/2026-09-20/0740`, not yet applied, and the next walk applies it before the entries of this session (F2). Case 262 took the two bare `[[decision-case-N]]` out of the Criterion, but the `change` text of the same Case carried the placeholder without a code span, and `generate` wrote it into History verbatim — lint raises `ref: body names decision-case-N` again. `generate.replace` does not touch History, so the line cannot be repaired through `replace`; the precedent is 130.1 — the History line edited by hand as a one-off migration, recorded by an `update` with `change`. An `update` of an Estimate replaces its Criterion with the Case's text unless the item writes `sections: Criterion` itself, and sets `pending` unless the item writes a status (case 204). `rule-prespec` stands `draft`; its Estimates are `estimate-prespec-checks-the-plan` (`passed`, pytest) and `estimate-prespec-reconciles` (`pending`, its first live reading is F3 of this session, before Work Mode). The same class of finding was cured three times on Decision pages and on a lesson (130.1, 140, 160); there is no guard before the Spec — `prespec --check` checks the form of the items, not the text of the strings. `lint` and `rule-page-generation` are not touched.

## Problem

The finding stands until the History line changes; and nothing stops a fifth time — a bare `[[slug]]` in any text of the Spec (`change`, `purpose`, `sections`, the blockquotes) reaches a page unchecked.

## History

- 2026-09-20 created · raw/2026-09-20/0958/ledger.md#case-264.1
