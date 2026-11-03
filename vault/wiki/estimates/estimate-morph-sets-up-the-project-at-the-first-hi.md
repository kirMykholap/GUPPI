---
type: estimate
kind: QA
status: pending
target: "[[rule-morph]]"
purpose: Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the setup as done, puts one setup Case first, before the opening of the first sprint, with the values it finds and the values the person gives, and whether the settings change only by the copy and the setting aside of /guppi:install, the render of /hi and the render after that Case is ratified
method: "by hand, after the session whose Work Mode builds the skill /setup of rule-skill-setup, its step in /hi and in /sprint-open and the pass of the ledger hook for the setup Case: in an empty git project, the plugin guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, /guppi:install typed, Claude Code reopened and /hi typed; the transcript of that session under ~/.claude/projects, its ledger and the files written in it read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-13/1753/ledger.md#case-802
sprint: plugin
created: 2026-10-13
tags: [session, harness, plugin]
---

## Criterion

When:
In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` holds `setup_done = false`, the person reopens Claude Code and types `/hi`.

Then:
`/hi` opens the session and starts `/setup` of `rule-skill-setup`, which puts the setup Case of `rule-morph` first, before the opening Case of the first sprint and before the Frontier.
**＋** The setup Case takes the name of the project's folder of saved transcripts from the path of the project.
**＋** It asks the person only for the values it cannot find: the language of the repository, the language of the chat, the commands of the keys `test` and `style` of `guppi.toml` and the description of the project.
**＋** Every value stands in that one setup Case, which the person ratifies or corrects, and the ledger hook of `rule-ledger-write` writes its decision lines though no sprint is open.
**＋** The reply that acknowledges the setup Case shows no Frontier and ends with the open question on what the first sprint is to build, and on the person's answer `/sprint-open` starts in the same session with that answer.
**＋** The librarian's run of that session writes the settings by the render of the rule pages that hold them, `guppi.toml`, the description of the project in `CLAUDE.md` and the read rules of the saved transcripts, and `guppi.toml` then holds `setup_done = true`.
**－** `/guppi:install` is no Case, and the person ratifies nothing at it.
**－** Between `/guppi:install` and that librarian's run, no settings file changes but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs.
**－** The setup step asks for no category set, no name of the main branch and no git remote, reads no code of the project and creates no page for it.
**－** A project whose `guppi.toml` does not hold `setup_done = false` gets no setup Case at `/hi`.

## History

- 2026-10-13 created · [[decision-case-802]]
- 2026-10-15 updated: the Criterion replaced whole — the install Case comes at the first /hi after /guppi:install, while guppi.toml does not mark the install as done · [[decision-case-817]]
- 2026-10-15 updated: the Criterion replaced whole — the setup Case comes first at the first /hi and /sprint-open follows it in the same session; /guppi:install is no Case · [[decision-case-825]]
- 2026-10-30 updated: the Criterion replaced whole — the files that /guppi:install sets aside count beside its copy among the changes before the setup Case · [[decision-case-932.5]]
- 2026-11-03 updated: the Criterion replaced whole — /setup builds the setup Case, the reply that acknowledges it asks what the first sprint is to build, the settings land at the librarian's run, and no main branch or git remote is taken · [[decision-case-1017.4]]
