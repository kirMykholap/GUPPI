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
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
core: true
---

## Purpose

Lets the session write its own working files and read this project's saved transcripts without asking, and nothing else. The Frontier, the Spec, the work file, the handoff, the carry mark and the brief of `/carry` are the session's own record of itself: `/hi` writes the Frontier, every closed item edits it, Work Mode ticks the boxes of the Spec and writes `work.md` (case 479.5), `/handoff` writes the note, `/carry` writes `carry.md` and rewrites `brief.md` (case 200.5). A question before each of those writes buys
nothing — the content is the agent's own, and the person reads it in the reply
anyway. The list states that intent; in Plan Mode the client asks before every edit of the main agent outside the plan file all the same, the person approves, and whether it asked is the person's word, never the agent's, which cannot see the prompt (case 237). The file of a built Case under `cases/` is not on the list: in Plan Mode Claude Code keeps a subagent in plan mode whatever its `permissionMode` and asks before its edit, allow list or not, so the guard of `rule-spec-reconcile` writes the file of `case-guppi` itself, stops its call so that nothing is asked unless the guard fails to write, and keeps it inside `cases/` (as set in case 894.2). The saved transcripts of the project, under a folder of `~/.claude/projects/` named after the path of the project outside the repository, are on the list for reading only: `case-guppi` checks a past reading in them, and a prompt on each of its searches buys nothing; the rule covers every agent of the project, and Claude Code applies a `Read` rule to Grep and Glob best-effort, and whether a search there still asks is the person's word (the folder of the repository of GUPPI is `c--PROJECTS-GUPPI`, case 656). A call of `case-guppi` that these rules do not match is judged by the mode of the session, and by its own `permissionMode: auto` only while the session runs in `default` or `dontAsk` mode, so a read outside the project that no rule names may ask the person, in Plan Mode too; a call the rules match needs no verdict of the classifier of Claude Code, which refuses a call when its server gives none (as set in case 894.2). A second rule names the folder itself beside the rule for what lies inside it, since a Grep whose path was that folder itself asked all the same (in session 1448, case 693). Until the setup Case of [[rule-morph]] sets the folder name of the project, the read rules name the transcripts folder of the repository of GUPPI, as the clean version brings them (that folder is named after where that repository sits on the person's disk, case 693).

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
      "Write(vault/wiki/brief.md)",
      "Read(~/.claude/projects/c--PROJECTS-GUPPI)",
      "Read(~/.claude/projects/c--PROJECTS-GUPPI/**)"
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
- 2026-10-05 updated: this project's saved transcripts under ~/.claude/projects join the allow list for reading, so a search of case-guppi there does not ask (case 656) · [[decision-case-656]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-07 updated: the folder of the saved transcripts itself joins the allow list for reading, beside what lies inside it; another install needs its own folder name, left to rule-morph · [[decision-case-693]]
- 2026-10-07 status: built → draft · cascade
- 2026-10-07 updated: case-guppi runs in permissionMode auto; the read rules of the saved transcripts stay, and a call they do not match is judged by that mode (case 698) · [[decision-case-698.2]]
- 2026-10-07 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the session stands in the bracket of its pointer · [[decision-case-809]]
- 2026-10-15 updated: the Purpose names the folder of saved transcripts by how it is named, and the repository of GUPPI where it meant it by this repository · [[decision-case-824]]
- 2026-10-15 updated: the Purpose names the setup Case of rule-morph as the step that sets the folder name · [[decision-case-825]]
- 2026-10-26 updated: the folder of the saved transcripts said by its role, the folder of the repository of GUPPI in brackets · [[decision-case-881.6]]
- 2026-10-28 updated: case-guppi stays in plan mode in Plan Mode whatever its permissionMode; the guard of rule-spec-reconcile writes its Case file, and a read outside the project that no rule names may ask (case 894.2) · [[decision-case-894.2]]
- 2026-10-28 status: built → draft · cascade
- 2026-10-29 status: draft → built · cascade
