---
type: decision
case: "59.4"
status: current
update: [decisions-schema-yaml, decisions-schema, "[[rule-page-generation]]", "[[estimate-generate-writes]]", "[[rule-lint]]", "[[estimate-lint-catches]]", index, glossary]
origin: raw/2026-09-12/ledger.md#case-59.4
sprint: migration
created: 2026-09-12
tags: [harness, workflow, ledger]
---

## Context

Plan Mode leaves four things behind: the Frontier it opened with, the ledger lines the
Stop hook wrote at each ratification, the Spec the human approved, and the Decision pages
the librarian generates from both. In sessions G and H the four drifted: three decision
lines had no item under their Case in the Spec (`lesson-spec-then-items-unchecked-against-
ledger-lines`); the Frontier lived in the agent's memory and a plan was closed on one item
of it (`lesson-plan-mode-exited-per-frontier-item`); a Decision page shows its targets as
two lists aligned by position, unreadable; the items left over at the end of a session are
carried by the brief's counter, not by a decision.

## Problem

Each drift has a mechanical check or a form that removes it, and none is written. The
sub-cases below fix one each; they share this context and are ratified apart. In Work
Mode a fork is not a return to Plan Mode: the subagent stops, the fork is written as a
Case in the short form, shown at Retro, appended to the Spec with a `defer`, and the plan
stays unfinished until the next session (the owner, 2026-09-12; a clause of
`rule-work-mode`, Slice 3b).

## Given

`decisions/schema.yaml` requires `kind` and `target_slug`, "two lists aligned by position,
one position per ledger line of the Case" (case 52.1); `schema.md` shows the example
`kind: [create, create]` / `target_slug: [entity-cart, estimate-cart-render-time]`.
**＋** `rule-page-generation` (`draft`, `guppi/generate.py`) writes the two lists in
`decision()` and reads them in `clear_deferred_by()` to find the `defer` targets of a
superseded decision; `estimate-generate-writes` (`pending`) says "kind and target_slug
aligned by position".
**＋** `rule-lint` (`built`, `guppi/lint.py`) checks "kind and target_slug of equal length;
every target_slug with a category prefix an existing page" in `check_decision`;
`estimate-lint-catches` (`passed`) seeds "decision lists of unequal length, a target_slug
naming no page". `check_decision` looks a slug up among live pages only; the fix outside
any Case (the lesson of 2026-09-11) folds into this rewrite.
**＋** `index.md` §5 and the glossary row "Routing Table, Decision page" describe the two
lists.
**＋** 78 live decision pages carry the two lists, 9 of them `superseded`; no decision page
is archived.
**＋** A Rule-class file is named by its slug in a list, as in a ledger line: `index`,
`glossary`, `case-schema`, `decisions-schema-yaml`.
**－** `deferred_by` on target pages, `superseded_by`, `source`, `supersedes` and the body
sections do not change.
**－** `materialize.yaml` does not change: its `targets` already carry `kind` and `slug`
per line; `generate` regroups them.

## When

`guppi generate` writes a Decision page; `guppi lint` reads one; the migration runs once.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-59.4
