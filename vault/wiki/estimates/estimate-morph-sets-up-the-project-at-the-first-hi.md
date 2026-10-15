---
type: estimate
kind: QA
status: pending
target: "[[rule-morph]]"
purpose: Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the install as done, puts one install Case first with the values it finds and the values the person gives, and whether the settings change only by the copy, the render of /hi and the render after that Case is ratified
method: "by hand, after the session whose Work Mode builds the install skill of rule-morph and its step in /hi: in an empty project, the plugin guppi installed, /guppi:install typed, Claude Code reopened and /hi typed; the transcript of that session and the files its Work Mode writes read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-13/1753/ledger.md#case-802
sprint: plugin
created: 2026-10-13
tags: [session, harness, plugin]
---

## Criterion

When:
In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` does not mark the install step of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

Then:
`/hi` opens the session as `rule-skill-hi` sets it, and puts the install Case first, before the items of `raw/<date>/<hi HHMM>/frontier.md`.
**＋** The install step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
**＋** It asks the person only for the values it cannot find, such as `documentation_lang`, `chat_lang`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
**＋** Every value stands in that one install Case, which the person ratifies or corrects.
**＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config`, the description of the project in `CLAUDE.md` from `rule-claude-md` and the read rules of the saved transcripts from `rule-permissions`, and `guppi.toml` then marks the install as done.
**－** Between `/guppi:install` and the ratified install Case, no settings file changes but by the copy of `/guppi:install` and the render that `/hi` runs.
**－** The install step is no skill named `install`.
**－** The install step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
**－** The install step reads no code of the project and creates no page for it.
**－** A project whose `guppi.toml` marks the install as done gets no install Case at `/hi`.

## History

- 2026-10-13 created · [[decision-case-802]]
- 2026-10-15 updated: the Criterion replaced whole — the install Case comes at the first /hi after /guppi:install, while guppi.toml does not mark the install as done · [[decision-case-817]]
