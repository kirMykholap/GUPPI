---
type: rule
kind: Leaf
purpose: "Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi after /guppi:install, while guppi.toml does not mark the setup as done, one setup Case that the person ratifies sets them, before the first sprint opens"
status: draft
estimates: ["[[estimate-morph-sets-up-the-project-at-the-first-hi]]"]
origin: raw/2026-09-18/1252/ledger.md#case-239
sprint: migration
created: 2026-09-18
tags: [session, harness, plugin]
core: true
---

## Purpose

Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` after `/guppi:install`, while `guppi.toml` does not mark the setup as done, one setup Case that the person ratifies sets them, before the first sprint opens. The plugin `guppi` installs GUPPI by its skill `/guppi:install`, which copies the files of the clean version into the project, the settings among them, as `rule-plugin-install` sets it. Until the setup Case, those settings name another project: `guppi.toml` holds the languages and the commands of the keys `test` and `style` of the repository of GUPPI, `CLAUDE.md` holds a blank description of the project, the read rules of [[rule-permissions]] name the folder of the saved transcripts of the repository of GUPPI under `~/.claude/projects`, and the code takes the main branch to be `main` (as set in case 693).

A new project starts in this order. The install is no Case; the setup and the opening of the first sprint are Cases.

1. The person installs the plugin `guppi`, which the catalogue `guppi-marketplace` lists, as [[rule-plugin-install]] sets it.
2. The person types `/guppi:install` in the project. It copies the files of GUPPI and builds its Python environment. It decides nothing, so it is no Case, and the person ratifies nothing at it.
3. The person reopens Claude Code in the project and types `/hi`, which opens the session as [[rule-skill-hi]] sets it: a Case lives only inside a session that `/hi` opened.
4. While `guppi.toml` does not mark the setup as done, `/hi` puts the setup Case first, before the opening of a sprint and before the Frontier. The person ratifies or corrects it.
5. Once the setup Case is ratified, `/hi` starts `/sprint-open` in the same session, since the clean version holds the sprint `guppi` closed ([[rule-clean-branch]]). The opening Case of [[rule-skill-sprint-open]] opens the first sprint of the project, and the Frontier comes after it.
6. The Work Mode of that session writes the settings of the setup Case and runs the tasks of the opening Case.

The ledger hook of [[rule-ledger-write]] refuses each decision line but a `defer` while no sprint is open. While `guppi.toml` does not mark the setup as done, it writes the decision lines of the setup Case all the same, so that the setup Case is ratified before the opening Case.

A key of `guppi.toml`, which [[rule-guppi-config]] renders, marks the setup as done: the setup Case sets it, and the clean version holds it unset. The setup step is a skill of the project whose name is not `install`, so that a project never holds both `/install` and `/guppi:install`. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml`, [[rule-claude-md]] for the description of the project in `CLAUDE.md` and [[rule-permissions]] for the read rules, and so sets the key. No settings file changes outside that Case but by the copy of `/guppi:install` and the render that `/hi` runs, which take the values as the clean version holds them ([[rule-ratification]]).

The setup step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The key, the setup skill, its step in `/hi` and in `/sprint-open`, the pass of the ledger hook for the setup Case and the clean version that holds the key unset are built in the milestone The plugin of [[entity-sprint-plugin]]; until then [[rule-skill-hi]], [[rule-skill-sprint-open]] and [[rule-ledger-write]] put the opening Case first in every project (as set in cases 802, 817 and 825).

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
- 2026-10-15 updated: the Purpose names the repository of GUPPI where it meant it by this repository · [[decision-case-824]]
- 2026-10-15 updated: the Purpose tells the start of a new project in order: /guppi:install is no Case, the setup Case comes first at the first /hi, and /sprint-open follows it in the same session; the install Case is named the setup Case · [[decision-case-825]]
