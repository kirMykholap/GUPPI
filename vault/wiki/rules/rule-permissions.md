---
type: rule
kind: Leaf
purpose: Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: ["[[estimate-permissions]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, session]
core: true
---

## Purpose

Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else. The Frontier, the Spec, the work file, the handoff, the carry mark and the brief of `/carry` are the session's own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec and writes `work.md`, `/handoff` writes the note, `/carry` writes `carry.md` and rewrites `brief.md`. A question before each of those writes buys
nothing — the content is the agent's own, and the person reads it in the reply
anyway. The list states that intent; in Plan Mode the client asks before every edit of the main agent outside the plan file all the same, the person approves, and whether it asked is the person's word, never the agent's, which cannot see the prompt. The file of a built Case under `cases/` is not on the list: in Plan Mode Claude Code keeps a subagent in plan mode whatever its `permissionMode` and asks before its edit, allow list or not, so the guard of `rule-spec-reconcile` writes the file of `case-guppi` itself, stops its call so that nothing is asked unless the guard fails to write, and keeps it inside `cases/`. The saved transcripts of the project, under a folder of `~/.claude/projects/` named after the path of the project outside the repository, are on the list for reading only: `case-guppi` checks a past reading in them, and a prompt on each of its searches buys nothing; the rule covers every agent of the project, and Claude Code applies a `Read` rule to Grep and Glob best-effort, and whether a search there still asks is the person's word. A call of `case-guppi` that these rules do not match is judged by the mode of the session, and by its own `permissionMode: auto` only while the session runs in `default` or `dontAsk` mode, so a read outside the project that no rule names may ask the person, in Plan Mode too; a call the rules match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none. A second rule names the folder itself beside the rule for what lies inside it, since a Grep whose path was that folder itself asked all the same. Until the setup Case of a project sets its folder name, the read rules name the transcripts folder of the repository of GUPPI, as the clean version brings them.

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

- 2026-11-03 shipped with GUPPI
