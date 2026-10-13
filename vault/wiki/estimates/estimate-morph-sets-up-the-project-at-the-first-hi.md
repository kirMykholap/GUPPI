---
type: estimate
kind: QA
status: pending
target: "[[rule-morph]]"
purpose: Whether the first /hi of a project with no answers in its settings puts one install Case first, with the values it finds and the values the person gives, and whether the settings change only by the render after that Case is ratified
method: "by hand, after the session whose Work Mode builds the install skill of rule-morph: /hi typed in an empty project with GUPPI installed and no answers in its settings, the transcript of that session and the files its Work Mode writes read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-13/1753/ledger.md#case-802
sprint: plugin
created: 2026-10-13
tags: [session, harness, plugin]
---

## Criterion

When:
In a project with GUPPI installed, whose settings hold no answers of the install step of `rule-morph`, the person types `/hi`.

Then:
`/hi` opens the session as `rule-skill-hi` sets it, and puts the install Case first, before the items of `raw/<date>/<hi HHMM>/frontier.md`.
**＋** The install step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
**＋** It asks the person only for the values it cannot find, such as `documentation_lang` and `chat_lang`.
**＋** Every value stands in that one install Case, which the person ratifies or corrects.
**＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config` and the read rules of the saved transcripts from `rule-permissions`.
**－** No settings file changes before the person ratifies the install Case.
**－** The install step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
**－** The install step reads no code of the project and creates no page for it.
**－** A project whose settings hold the answers gets no install Case at `/hi`.

## History

- 2026-10-13 created · [[decision-case-802]]
