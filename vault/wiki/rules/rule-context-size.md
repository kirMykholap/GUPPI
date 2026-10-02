---
type: rule
kind: Leaf
purpose: Prevents a session from running on while the person cannot see how full the context window is
status: draft
enforcement: hook
implementation_ref: [guppi/context.py, tests/test_context.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-context-size-shown-after-each-reply]]", "[[estimate-context-size-warns-past-the-limit]]", "[[estimate-context-size-shows-its-error]]"]
origin: raw/2026-09-24/1303/ledger.md#case-392.1
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session]
---

## Purpose

Prevents a session from running on while the person cannot see how full the context window is. In the VS Code extension the context indicator shows only past half of the window, and `/context` is typed by hand; no hook payload carries the size, only `transcript_path`. The size is counted from the transcript, where every API call of the model carries its `usage`.

## History

- 2026-09-24 created · [[decision-case-392.1]]
- 2026-09-24 estimate estimate-context-size-shown-after-each-reply added · [[decision-case-392.1]]
- 2026-09-24 updated: the warning past 400 000 tokens (case 392.2) · [[decision-case-392.2]]
- 2026-09-24 estimate estimate-context-size-warns-past-the-limit added · [[decision-case-392.2]]
- 2026-09-25 deferred · [[decision-case-404]]
- 2026-09-25 deferred · [[decision-case-409]]
- 2026-09-25 deferred · [[decision-case-418]]
- 2026-09-25 deferred · [[decision-case-422]]
- 2026-09-25 defer by decision-case-404 superseded · [[decision-case-430]]
- 2026-09-25 defer by decision-case-409 superseded · [[decision-case-430]]
- 2026-09-25 defer by decision-case-418 superseded · [[decision-case-430]]
- 2026-09-25 defer by decision-case-422 superseded · [[decision-case-430]]
- 2026-09-25 updated: past 400 000 tokens both hooks give a note, not an order to close the session; the limit stays (case 430) · [[decision-case-430]]
- 2026-09-30 status: draft → built · cascade
- 2026-09-30 updated: the Stop run shows its own error to the person as the systemMessage and still exits 0 (case 555.2) · [[decision-case-555.2]]
- 2026-09-30 estimate estimate-context-size-shows-its-error added · [[decision-case-555.2]]
- 2026-09-30 status: built → draft · cascade
- 2026-10-01 status: draft → built · cascade
- 2026-10-02 updated: ## How it works left the Leaf, its mechanism in the docstring of guppi/context.py; D counts from the start of the turn, named by the function of guppi/ledger.py (case 590.2) · [[decision-case-590.2]]
- 2026-10-02 status: built → draft · cascade
