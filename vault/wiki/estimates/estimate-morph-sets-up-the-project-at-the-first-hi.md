---
type: estimate
kind: QA
status: pending
target: "[[rule-morph]]"
purpose: Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the setup as done, puts one setup Case first, before the opening of the first sprint, with the values it finds and the values the person gives, and whether the settings change only by the copy, the render of /hi and the render after that Case is ratified
method: "by hand, after the session whose Work Mode builds the setup skill of rule-morph, its step in /hi and in /sprint-open and the pass of the ledger hook for the setup Case: in an empty project, the plugin guppi installed, /guppi:install typed, Claude Code reopened and /hi typed; the transcript of that session, its ledger and the files its Work Mode writes read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-13/1753/ledger.md#case-802
sprint: plugin
created: 2026-10-13
tags: [session, harness, plugin]
---

## Criterion

When:
In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` does not mark the setup of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

Then:
`/hi` opens the session as `rule-skill-hi` sets it, and puts the setup Case first, before the opening Case of `rule-skill-sprint-open` and before the Frontier.
**＋** Once the person ratifies the setup Case, `/hi` starts `/sprint-open` in the same session, and the ledger hook of `rule-ledger-write` writes the decision lines of the setup Case though no sprint is open.
**＋** The setup step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
**＋** It asks the person only for the values it cannot find, such as `documentation_lang`, `chat_lang`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
**＋** Every value stands in that one setup Case, which the person ratifies or corrects.
**＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config`, the description of the project in `CLAUDE.md` from `rule-claude-md` and the read rules of the saved transcripts from `rule-permissions`, and `guppi.toml` then marks the setup as done.
**－** `/guppi:install` is no Case, and the person ratifies nothing at it.
**－** Between `/guppi:install` and the ratified setup Case, no settings file changes but by the copy of `/guppi:install` and the render that `/hi` runs.
**－** The setup step is no skill named `install`.
**－** The setup step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
**－** The setup step reads no code of the project and creates no page for it.
**－** A project whose `guppi.toml` marks the setup as done gets no setup Case at `/hi`.

## History

- 2026-10-13 created · [[decision-case-802]]
- 2026-10-15 updated: the Criterion replaced whole — the install Case comes at the first /hi after /guppi:install, while guppi.toml does not mark the install as done · [[decision-case-817]]
- 2026-10-15 updated: the Criterion replaced whole — the setup Case comes first at the first /hi and /sprint-open follows it in the same session; /guppi:install is no Case · [[decision-case-825]]
