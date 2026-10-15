---
type: rule
kind: Leaf
purpose: "Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi after /guppi:install, while guppi.toml does not mark the install as done, one install Case that the person ratifies sets them"
status: draft
estimates: ["[[estimate-morph-sets-up-the-project-at-the-first-hi]]"]
origin: raw/2026-09-18/1252/ledger.md#case-239
sprint: migration
created: 2026-09-18
tags: [session, harness, plugin]
core: true
---

## Purpose

Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` after `/guppi:install`, while `guppi.toml` does not mark the install as done, one install Case that the person ratifies sets them. The plugin `guppi` installs GUPPI by its skill `/guppi:install`, which copies the files of the clean version into the project, the settings among them, as `rule-plugin-install` sets it. Until the install Case, those settings name another project: `guppi.toml` holds the languages and the commands of the keys `test` and `style` of this repository, `CLAUDE.md` holds a blank description of the project, the read rules of [[rule-permissions]] name the folder of this repository's saved transcripts under `~/.claude/projects`, and the code takes the main branch to be `main` (as set in case 693).

A key of `guppi.toml`, which [[rule-guppi-config]] renders, marks the install as done: the install Case sets it, and the clean version holds it unset. The install step is a skill of the project whose name is not `install`, so that a project never holds both `/install` and `/guppi:install`. After `/guppi:install`, the person reopens Claude Code in the project and types `/hi`. `/hi` opens the session as always and, while `guppi.toml` does not mark the install as done, puts the install Case first, before the Frontier: a Case lives only inside a session that `/hi` opened. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml`, [[rule-claude-md]] for the description of the project in `CLAUDE.md` and [[rule-permissions]] for the read rules, and so sets the key. No settings file changes outside that Case but by the copy of `/guppi:install` and the render that `/hi` runs, which take the values as the clean version holds them ([[rule-ratification]]).

The install step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The key, the skill, its step in `/hi` and the clean version that holds the key unset are built in the milestone The plugin of [[entity-sprint-plugin]] (as set in cases 802 and 817).

## History

- 2026-09-18 deferred, placeholder · [[decision-case-239]]
- 2026-10-07 updated: the initiation at install also sets the name of the transcripts folder in the read rules of rule-permissions · [[decision-case-693]]
- 2026-10-07 updated: the read rules of rule-permissions that its initiation at install names stay, beside the mode auto of case-guppi; no text changes (case 698) · [[decision-case-698.2]]
- 2026-10-09 deferred · [[decision-case-745]]
- 2026-10-09 deferred · [[decision-case-750]]
- 2026-10-10 deferred · [[decision-case-758]]
- 2026-10-13 defer by decision-case-239 superseded · [[decision-case-802]]
- 2026-10-13 defer by decision-case-745 superseded · [[decision-case-802]]
- 2026-10-13 defer by decision-case-750 superseded · [[decision-case-802]]
- 2026-10-13 defer by decision-case-758 superseded · [[decision-case-802]]
- 2026-10-13 updated: taken up: the install step is a skill at the first /hi whose answers become one ratified Case; the category set leaves for the Backlog of entity-sprint-plugin (case 802) · [[decision-case-802]]
- 2026-10-13 estimate estimate-morph-sets-up-the-project-at-the-first-hi added · [[decision-case-802]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-15 updated: the install Case comes at the first /hi after /guppi:install, while a key of guppi.toml does not mark the install as done; the install step is no skill named install · [[decision-case-817]]
