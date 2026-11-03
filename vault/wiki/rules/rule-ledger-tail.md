---
type: rule
kind: Leaf
purpose: Shows at /hi every ledger line that no vault page holds yet, so a reading or a lesson written after the librarian's commit reaches the next session's Frontier
status: built
enforcement: render
implementation_ref: [.guppi/guppi/tail.py, .guppi/tests/test_tail.py]
governs: .claude/skills/hi/SKILL.md
render_mode: partial
parent: "[[rule-skill-hi]]"
estimates: ["[[estimate-ledger-tail]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness, ledger]
core: true
---

## Purpose

Shows at `/hi` and at `/retro` every ledger line that no vault page holds yet. The readings of the
librarian's own run and the lessons of the close are written after its commit and
after its brief, so the next `/hi`, which reads the brief, would not see them until
the librarian after next. The tail closes that gap for the Frontier: the page of a
reading comes with the next librarian, the fact that it failed comes at once.

## Render

<!-- rule-ledger-tail -->
Tail: !`uv run --project .guppi guppi tail`
<!-- /rule-ledger-tail -->

## History

- 2026-11-03 shipped with GUPPI
