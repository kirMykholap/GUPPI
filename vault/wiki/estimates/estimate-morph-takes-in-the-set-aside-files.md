---
type: estimate
kind: QA
status: passed
target: "[[rule-morph]]"
purpose: Whether the setup Case of the first /hi shows what each file that /guppi:install set aside holds, lets the person keep or drop each part, puts a kept part into the page that writes its file or, where none does, into the file by a task, creates no page and deletes guppi-set-aside/
method: "by hand, after the session whose Work Mode builds the skill /setup of rule-skill-setup and its step in /hi: in a git project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, with a tag prod-x.y.z in the history of HEAD, the plugin guppi installed from a local copy written by uv run --project .guppi guppi ship --allow-draft, /guppi:install typed, Claude Code reopened and /hi typed, one part of each set-aside file kept and one dropped in the setup Case; the transcript of that session under ~/.claude/projects, its ledger and the files written in it read against the Criterion, recorded in the estimate line"
checked: 2026-11-04
origin: raw/2026-10-30/1713/ledger.md#case-932.2
sprint: plugin
created: 2026-10-30
tags: [session, harness, plugin]
---

## Criterion

When:
In a project where `/guppi:install`, as `rule-plugin-install` sets it, set aside files of the project under `guppi-set-aside/`, and whose `guppi.toml` holds `setup_done = false`, the person reopens Claude Code and types `/hi`.

Then:
The setup Case of `rule-morph` that `/setup` of `rule-skill-setup` builds shows what each file under `guppi-set-aside/` holds, by its old path.
**＋** In that one setup Case, the person keeps or drops each part of each file, such as an instruction, a hook or a permission.
**＋** A kept part goes into the page that writes its file, and the render at the librarian's run of that session writes it into the file.
**＋** For a file that no page writes, a task of the setup Case writes the kept part into that file, and the Work Mode of the same session runs it.
**＋** A task of the setup Case deletes `guppi-set-aside/` in that Work Mode.
**－** A dropped part reaches no file of the project.
**－** The setup Case creates no page for a kept part.

## Result

2026-11-04, Work Mode of session 0358, ~/.claude/projects/C--PROJECTS-guppi-trial-0358-own-files/36b6e39b-7323-4638-8d29-7608d3856ae2.jsonl and the folder C:/PROJECTS/guppi-trial-0358/own-files: the setup Case showed CLAUDE.md, .claude/settings.json and .gitattributes by their old paths (round at L98, Q6, Q8, Q9); CLAUDE.md: the heading and line kept as the description through rule-claude-md, the instruction dropped; .claude/settings.json: its one hook kept through rule-hook-registry and rendered by the librarian (my-own-hook stands in .claude/settings.json), the file held no second part to drop; .gitattributes, which no page writes: `*.png binary` kept and written by a task of Work Mode (commit fcf3e8c), `* text=auto` dropped; guppi-set-aside/ deleted by a task in that Work Mode; no page created for a kept part

## History

- 2026-10-30 created · [[decision-case-932.2]]
- 2026-11-03 updated: the Criterion replaced whole — the setup Case is built by /setup, and a kept part reaches its file at the render of the librarian's run · [[decision-case-1017.5]]
- 2026-11-04 updated: the put-off retired before it was applied; the reading taken at the install stop of Work Mode · [[decision-case-1026.2]]
- 2026-11-04 status: pending → passed · raw/2026-11-04/0358/ledger.md#L26
