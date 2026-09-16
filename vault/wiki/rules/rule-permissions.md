---
type: rule
kind: Leaf
purpose: Lets the session write its own working files without asking, and nothing else
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: ["[[estimate-permissions]]"]
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Purpose

Lets the session write its own working files without asking, and nothing else. The Frontier, the Spec, the handoff, the carry mark and the brief of `/carry` are the session's own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec, `/handoff` writes the note, `/carry` writes `carry.md` and rewrites `brief.md` (case 200.5). A question before each of those writes buys
nothing — the content is the agent's own, and the person reads it in the reply
anyway.

What stays outside the list is the point of the list. `ledger.md` and
`event_log.md` are written by hooks, `materialize.yaml` by a script, and a harness
file rendered from a Rule page is refused by `guppi guard`: none of them is the
agent's to write, so none of them is allowed here. `deny` and `ask` stay empty:
a refusal that matters has a hook behind it (case 85.5).

## Render

<!-- rule-permissions -->
    "allow": [
      "Edit(vault/raw/**/frontier.md)",
      "Write(vault/raw/**/frontier.md)",
      "Edit(vault/raw/**/spec.md)",
      "Write(vault/raw/**/spec.md)",
      "Edit(vault/raw/**/handoff.md)",
      "Write(vault/raw/**/handoff.md)",
      "Write(vault/raw/**/carry.md)",
      "Edit(vault/wiki/brief.md)",
      "Write(vault/wiki/brief.md)"
    ]
<!-- /rule-permissions -->

## History

- 2026-09-12 created · [[decision-case-85.5]]
- 2026-09-12 estimate estimate-permissions added · [[decision-case-85.5]]
- 2026-09-13 status: draft → built · cascade
- 2026-09-16 updated: carry.md and brief.md join the allow list for /carry (case 200.5) · [[decision-case-200.5]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 status: draft → built · cascade
