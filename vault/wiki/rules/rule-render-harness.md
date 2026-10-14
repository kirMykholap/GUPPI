---
type: rule
kind: Leaf
purpose: Prevents a Rule page and the harness file it governs from becoming two copies of one text
status: built
enforcement: check
implementation_ref: [guppi/render.py, guppi/config.py, tests/test_render.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, render]
core: true
---

## Purpose

Prevents a Rule page and the harness file it governs from becoming two copies of one
text. Without a renderer `enforcement: render` is a label: the skill and `CLAUDE.md` are
edited by hand, the page follows or does not, and the vault stops being the source.

`parent: rule-harness` names the MOC of the harness tools: the renderer runs with lint and as the librarian's step after `cleanup`, and its tick of the render lines of the Spec belongs to that step.

## History

- 2026-10-14 shipped with GUPPI
