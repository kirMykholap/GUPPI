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
origin: raw/2026-09-13/ledger.md#case-101.2
sprint: migration
created: 2026-09-10
tags: [session, harness, ledger]
core: true
---

## Purpose

Shows at `/hi` and at `/retro` (since case 126) every ledger line that no vault page holds yet. The readings of the
librarian's own run and the lessons of the close are written after its commit and
after its brief, so the next `/hi`, which reads the brief, would not see them until
the librarian after next. The tail closes that gap for the Frontier: the page of a
reading comes with the next librarian, the fact that it failed comes at once.

## Render

<!-- rule-ledger-tail -->
Tail: !`uv run --project .guppi guppi tail`
<!-- /rule-ledger-tail -->

## History

- 2026-09-10 deferred, placeholder · raw/2026-09-10/ledger.md#case-45
- 2026-09-11 deferred_by decision-case-45 set · [[decision-case-52.3]]
- 2026-09-12 defer by decision-case-45 superseded · [[decision-case-63]]
- 2026-09-12 deferred · [[decision-case-63]]
- 2026-09-12 defer by decision-case-63 superseded · [[decision-case-79]]
- 2026-09-12 deferred · [[decision-case-79]]
- 2026-09-12 defer by decision-case-79 superseded · [[decision-case-95]]
- 2026-09-12 deferred · [[decision-case-95]]
- 2026-09-13 defer by decision-case-95 superseded · [[decision-case-100.1]]
- 2026-09-13 created over placeholder · [[decision-case-101.2]]
- 2026-09-13 estimate estimate-ledger-tail added · [[decision-case-101.2]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: the second caller of guppi tail, the retro skill, named (case 132) · [[decision-case-132]]
- 2026-09-28 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-09-30 updated: the Tail line follows the git lines: rule-github-issues left the harness (case 528.2) · [[decision-case-528.2]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the pointer stands in a bracket of its own · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/tail.py · [[decision-case-942.1]]
