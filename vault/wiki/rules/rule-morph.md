---
type: rule
kind: Leaf
purpose: "Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi of a project with no answers in its settings, one install Case that the person ratifies sets them"
status: draft
estimates: ["[[estimate-morph-sets-up-the-project-at-the-first-hi]]"]
origin: raw/2026-09-18/1252/ledger.md#case-239
sprint: migration
created: 2026-09-18
tags: [session, harness, plugin]
core: true
---

## Purpose

Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` of a project with no answers in its settings, one install Case that the person ratifies sets them. Some settings name one machine or one project until then: the read rules of [[rule-permissions]] name the folder of this repository's saved transcripts under `~/.claude/projects`, and the code takes the main branch to be `main` (case 693).

The install step is a skill. `/hi` opens the session as always and, while the settings hold no answers of the install, puts the install Case first, before the Frontier: a Case lives only inside a session that `/hi` opened. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml` and [[rule-permissions]] for the read rules. No settings file changes outside that Case ([[rule-ratification]]).

The install step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The skill is built in the milestone The plugin of [[entity-sprint-plugin]] (case 802).

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
