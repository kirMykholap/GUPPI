---
type: rule
kind: Leaf
purpose: Lets the session write its own working files without asking, and nothing else
status: draft
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

Lets the session write its own working files without asking, and nothing else. The Frontier, the Spec, the work file, the handoff, the carry mark and the brief of `/carry` are the session's own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec and writes `work.md` (case 479.5), `/handoff` writes the note, `/carry` writes `carry.md` and rewrites `brief.md` (case 200.5). A question before each of those writes buys
nothing — the content is the agent's own, and the person reads it in the reply
anyway. The list states that intent; in Plan Mode the client asks before every edit of the main agent outside the plan file all the same, the person approves, and whether it asked is the person's word, never the agent's, which cannot see the prompt (case 237). The file of a built Case under `cases/` is not on the list: `case-guppi` writes it in the mode `permissionMode: acceptEdits` of its agent file, which Claude Code keeps for a subagent while the session is in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/` (case 645.16).

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
      "Edit(vault/raw/**/work.md)",
      "Write(vault/raw/**/work.md)",
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
- 2026-09-18 updated: the allow list as intent; in Plan Mode the client asks all the same, and the prompt is read by the person (case 237) · [[decision-case-237]]
- 2026-09-28 updated: work.md, the baseline and the marks of an expected red, joins the allow list (case 479.5) · [[decision-case-479.5]]
- 2026-09-28 status: built → draft · cascade
- 2026-09-30 status: draft → built · cascade
- 2026-10-05 updated: the prompt in Plan Mode binds the main agent; case-guppi writes its Case file in permissionMode acceptEdits, with no allow rule (case 645.16) · [[decision-case-645.16]]
- 2026-10-05 status: built → draft · cascade
