---
type: estimate
kind: QA
status: passed
target: "[[rule-morph]]"
purpose: Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the setup as done, puts one setup Case first, before the opening of the first sprint, with the values it finds and the values the person gives, and whether the settings change only by the copy and the setting aside of /guppi:install, the render of /hi and the render after that Case is ratified
method: "by hand, after the install stop of the Work Mode that sets this method: the plugin guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, in a git project made by git init -b main after the install that holds a CLAUDE.md and a code file of its own, and in a git project that holds only a LICENSE of its own, /guppi:install typed, Claude Code reopened, /hi typed and that session taken to its librarian's run, the transcript of each of those sessions under ~/.claude/projects, its ledger and the files written in it read against the Criterion, recorded in the estimate line"
checked: 2026-11-25
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
**＋** It asks the person only for the values it cannot find: the language of the repository, the language of the chat and the description of the project.
**＋** Where the file paths of the project show a file of a programming language outside `.guppi/`, `vault/`, `.claude/` and `guppi-set-aside/`, one plain question says that GUPPI's own tests and style check keep running in the project, says why it asks, and asks how the project's own tests and style check run beside them, and the commands the person gives stand after GUPPI's commands in the keys `test` and `style` of `guppi.toml`.
**＋** Every value stands in that one setup Case, which the person ratifies or corrects, and the ledger hook of `rule-ledger-write` writes its decision lines though no sprint is open.
**＋** The reply that acknowledges the setup Case shows no Frontier and ends with the open question on what the first sprint is to build, and on the person's answer `/sprint-open` starts in the same session with that answer.
**＋** The librarian's run of that session writes the settings by the render of the rule pages that hold them, `guppi.toml`, the description of the project in `CLAUDE.md` and the read rules of the saved transcripts, and `guppi.toml` then holds `setup_done = true`.
**－** `/guppi:install` is no Case, and the person ratifies nothing at it.
**－** Between `/guppi:install` and that librarian's run, no settings file changes but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs.
**－** The setup step asks for no category set, no name of the main branch and no git remote, reads no code of the project and creates no page for it.
**－** Where the file paths show no such file, it asks nothing on tests or style, and the keys `test` and `style` stay as they are.
**－** The question names no key of `guppi.toml`, GUPPI's commands leave no key, and no key becomes an empty list.
**－** It asks no question on how the setup Case splits or how it is checked.
**－** A project whose `guppi.toml` does not hold `setup_done = false` gets no setup Case at `/hi`.

## Result

2026-11-25, Retro of session 0816, the install stop of its Work Mode, ~/.claude/projects/C--tmp-guppi-1055-p1-code/e3d24d1f-917e-441b-b0ff-4f7de6f018ec.jsonl (code app.py, git init -b main after the install) and C--tmp-guppi-1055-p2-license/4b3495da-b569-431c-860c-6b95cdee18f0.jsonl (only a LICENSE): /hi started /setup first in both, before the opening Case and the Frontier; the setup Case asked the languages and the description, and showed the transcripts folder taken from the path for correction as the setup skill sets it (p1 Q5 C--tmp-guppi-1055-p1-code; p2 Q4 c--tmp-guppi-1055-p2-license, made C-- by a Glob before the Case was written); p1 asked one plain question on tests and style naming no key of guppi.toml, answered none, so test and style stayed GUPPI's; p2 asked nothing on tests; no subagent and no main call read app.py; the decision lines stood in each ledger before the sprint page (p1 18:12:13, p2 18:25:34); each acknowledging reply showed no Frontier and ended with the question on the first sprint, and /sprint-open followed with that answer; the commits before the librarian's run (p1 9d8618a, p2 1af3d22) held setup_done = false and a CLAUDE.md and .claude/settings.json equal to the copy, and after the run (p1 5d5ec49, p2 5dba49c) guppi.toml held setup_done = true, CLAUDE.md the description and settings.json the read rules of the folder

## History

- 2026-10-13 created · [[decision-case-802]]
- 2026-10-15 updated: the Criterion replaced whole — the install Case comes at the first /hi after /guppi:install, while guppi.toml does not mark the install as done · [[decision-case-817]]
- 2026-10-15 updated: the Criterion replaced whole — the setup Case comes first at the first /hi and /sprint-open follows it in the same session; /guppi:install is no Case · [[decision-case-825]]
- 2026-10-30 updated: the Criterion replaced whole — the files that /guppi:install sets aside count beside its copy among the changes before the setup Case · [[decision-case-932.5]]
- 2026-11-03 updated: the Criterion replaced whole — /setup builds the setup Case, the reply that acknowledges it asks what the first sprint is to build, the settings land at the librarian's run, and no main branch or git remote is taken · [[decision-case-1017.4]]
- 2026-11-04 updated: the put-off retired before it was applied; the reading taken at the install stop of Work Mode · [[decision-case-1026.1]]
- 2026-11-04 status: pending → failed · raw/2026-11-04/0358/ledger.md#L25
- 2026-11-20 updated: the Criterion replaced whole — the setup asks on tests and style only where the project holds code of its own · [[decision-case-1031.3]]
- 2026-11-25 updated: the method set anew — the project with code is the one of the git init offer, the project with no code the one that holds only a LICENSE, at the install stop of Work Mode · [[decision-case-1055.2]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0816/ledger.md#L26
