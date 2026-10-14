---
type: rule
kind: Leaf
purpose: Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, session]
core: true
---

## Purpose

Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else. The Frontier, the Spec, the work file, the handoff, the carry mark and the brief of `/carry` are the session's own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec and writes `work.md`, `/handoff` writes the note, `/carry` writes `carry.md` and rewrites `brief.md`. A question before each of those writes buys
nothing — the content is the agent's own, and the person reads it in the reply
anyway. The list states that intent; in Plan Mode the client asks before every edit of the main agent outside the plan file all the same, the person approves, and whether it asked is the person's word, never the agent's, which cannot see the prompt. The file of a built Case under `cases/` is not on the list: `case-guppi` writes it in the mode `permissionMode: auto` of its agent file, which Claude Code keeps for a subagent while the session is in Plan Mode, and the guard of `rule-spec-reconcile` keeps it inside `cases/`. The saved transcripts of this project, under `~/.claude/projects/c--PROJECTS-GUPPI/` outside the repository, are on the list for reading only: `case-guppi` checks a past reading in them, and a prompt on each of its searches buys nothing; the rule covers every agent of the project, and Claude Code applies a `Read` rule to Grep and Glob best-effort, and whether a search there still asks is the person's word. A call of `case-guppi` that these rules do not match is judged by its mode `permissionMode: auto`, with no prompt to the person, and a call they match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none. A second rule names the folder itself beside the rule for what lies inside it, since a Grep whose path was that folder itself asked all the same. The folder name follows where this repository sits on the person's disk: another install needs its own name in both rules, and that is not done here; it waits for [[rule-morph]], whose initiation at install sets the folder name.

What stays outside the list is the point of the list. `ledger.md` and
`event_log.md` are written by hooks, `materialize.yaml` by a script, and a harness
file rendered from a Rule page is refused by `guppi guard`: none of them is the
agent's to write, so none of them is allowed here. `deny` and `ask` stay empty:
a refusal that matters has a hook behind it.

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
      "Write(vault/wiki/brief.md)",
      "Read(~/.claude/projects/c--PROJECTS-GUPPI)",
      "Read(~/.claude/projects/c--PROJECTS-GUPPI/**)"
    ]
<!-- /rule-permissions -->

## History

- 2026-10-14 shipped with GUPPI
