---
type: decision
case: "324"
status: archived
update: ["[[rule-atomicity]]", "[[rule-case-protocol]]"]
origin: raw/2026-09-22/1724/ledger.md#case-324
sprint: migration
created: 2026-09-22
tags: [harness, workflow, session, ledger]
---

## Context

`rule-atomicity` is a page with `render_mode: partial`: its `## Render` is spliced into `case-schema.md`, and `own_text` in `guppi/render.py` takes the text between the page's own markers `<!-- rule-atomicity -->` … `<!-- /rule-atomicity -->`, while the parent `full` page carries one marker line per child, which the renderer replaces with the child's text and its markers. Case 317 wrote `sections.Render` from the heading, with no marker pair, and put both lines into the Render of the parent `rule-case-protocol`. `plan()` raised before the first write, so `guppi render` in the librarian's run of session 1121 wrote no governed file: `CLAUDE.md`, `case-schema.md`, three `schema.yaml` and the three harness files stayed at the text of the previous session. Commit `94277ea` fixed this by hand, outside the librarian's run: the markers added to `rule-atomicity`, the extra closing line removed from `rule-case-protocol`.
Both pages stand `draft`; `render --check`, `sprint --check` and `glossary --check` exit 0. `estimate-atomicity-rendered` stands `pending`, and its Criterion already states this state — "`rule-case-protocol` is a MOC with the child `rule-atomicity` and a marker line in its Render"; the Case touches neither it nor the four Estimates of `rule-case-protocol`.

## Problem

The text on disk is right, but nothing is signed under it. The fix went past `materialize` and `generate`, so neither page carries a History line and no Decision page exists for `origin` and History to reach. The gap closes either by signing the text as it stands, or by a change that makes `render` place a partial's markers itself.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-324
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
