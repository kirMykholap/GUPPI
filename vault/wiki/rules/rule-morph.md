---
type: rule
kind: Leaf
purpose: "Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi of a project with no answers in its settings, one install Case that the person ratifies sets them"
status: draft
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, harness, plugin]
core: true
---

## Purpose

Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` of a project with no answers in its settings, one install Case that the person ratifies sets them. Some settings name one machine or one project until then: the read rules of [[rule-permissions]] name the folder of this repository's saved transcripts under `~/.claude/projects`, and the code takes the main branch to be `main`.

The install step is a skill. `/hi` opens the session as always and, while the settings hold no answers of the install, puts the install Case first, before the Frontier: a Case lives only inside a session that `/hi` opened. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml` and [[rule-permissions]] for the read rules. No settings file changes outside that Case ([[rule-ratification]]).

The install step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of `entity-sprint-plugin`. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The skill is built in the milestone The plugin of `entity-sprint-plugin`.

## History

- 2026-10-14 shipped with GUPPI
