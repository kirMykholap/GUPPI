---
type: decision
case: "99"
status: archived
update: ["[[estimate-hook-registry-rendered]]", "[[rule-prespec]]", "[[rule-materialize]]", "[[rule-harness]]"]
origin: raw/2026-09-12/ledger.md#case-99
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render, session, workflow, ledger]
---

## Context

Four wordings in the vault say what cases 85, 86 and 90 stop being true. It is the class
case 88 repaired on the two render Estimates: the contract moves and the derived text
stays. Here it moves in this session, so the repair belongs in it and not one session
later.

## Problem

Left standing, the next readings fail on the words and not on the code — exactly how two
render readings failed today.

## Given

`estimate-hook-registry-rendered` (`passed`) asks the render to leave
`.claude/settings.json` "byte-identical to the ratified Render body" of that page. After
85.3 the page renders the `"hooks"` key alone, and the clause is false by construction;
85.3 appends a block and does not touch the prose.
**＋** `rule-prespec` (line 37) and `rule-materialize` (line 47) name the item's key
`slug` where the code reads `estimate_slug`. Case 86 ratifies the prefixed names; the two
texts are left from the earlier wording. `estimate-prespec-reconciles` does not carry the
phrase — checked.
**＋** The Purpose of `rule-harness` names its four children "the renderer, the hook
registry, lint and the indexes". After 85.2 the hook registry is a child of
`rule-settings`, which takes that slot.
**＋** `estimate-harness-pipeline` reads the steps of `make lint`, not the children list,
so the slot swap leaves it alone — checked.
**－** No contract moves here: all four bring the words to what is already signed. Hence
`contract: same` on the two Leaf pages and no new criterion block.
**－** The anchor of the `rule-prespec` pair is the text 90.2 leaves behind, so it matches
only after that entry applies.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-99
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
