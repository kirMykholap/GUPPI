---
type: rule
kind: Leaf
purpose: Prevents a Rule page and the harness file it governs from becoming two copies of one text
status: draft
enforcement: check
implementation_ref: [guppi/render.py, tests/test_render.py, .claude/settings.json]
parent: rule-harness
estimates: [estimate-render-harness-reproduces, estimate-render-sync-reports]
origin: raw/2026-09-09/ledger.md#case-18.1
sprint: migration
created: 2026-09-09
tags: [harness, render]
---

## Purpose

Prevents a Rule page and the harness file it governs from becoming two copies of one
text. Without a renderer `enforcement: render` is a label: the skill and `CLAUDE.md` are
edited by hand, the page follows or does not, and the vault stops being the source.

`parent: rule-harness` names the MOC of the harness tools: the renderer runs with lint and the indexes, in no phase of the session.

## How it works

`uv run guppi render` writes every governed file from its Rule page; `--check`
renders in memory and names the files that differ, for `make lint`; `--sync`, the
`SessionStart` hook, prints a unified diff for each differing file — the file as it
is, then the rendered text — and writes it, so the agent's first turn shows what
the render changed: the pages the librarian updated, or a hand edit that is now
gone and may deserve a Case. It exits 0 always; `SessionStart` cannot block, and a
render error goes to stderr. The rendered files are committed at Retro.

## Estimates

- [[estimate-render-harness-reproduces]]
- [[estimate-render-sync-reports]]

## Parent

- [[rule-documentation]]

## Implementation

- `guppi/render.py`
- `tests/test_render.py`
- `.claude/settings.json`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.1
- 2026-09-10 updated: a child without enforcement render contributes nothing to a full render; a marker line for it is an error · raw/2026-09-10/ledger.md#case-36.2
- 2026-09-10 updated: parent is rule-harness · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: render --sync at SessionStart — diff on stdout, then the write; enforcement hook (case 59.7) · [[decision-case-59.7]]
- 2026-09-12 status: built → draft · cascade
