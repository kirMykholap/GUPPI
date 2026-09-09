---
type: rule
kind: Leaf
purpose: Prevents a Rule page and the harness file it governs from becoming two copies of one text
status: draft
enforcement: check
implementation_ref: [guppi/render.py, tests/test_render.py]
parent: rule-documentation
estimates: [estimate-render-harness-reproduces]
origin: raw/2026-09-09/ledger.md#case-18.1
sprint: migration
created: 2026-09-09
tags: [harness, render]
---

## Purpose

Prevents a Rule page and the harness file it governs from becoming two copies of one
text. Without a renderer `enforcement: render` is a label: the skill and `CLAUDE.md` are
edited by hand, the page follows or does not, and the vault stops being the source.

`parent: rule-documentation` names the Documentation MOC of Slice 3, which does not exist
yet as a page; the reference dangles until then, on purpose.

## Estimates

- [[estimate-render-harness-reproduces]]

## Parent

- [[rule-documentation]]

## Implementation

- `guppi/render.py`
- `tests/test_render.py`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.1
