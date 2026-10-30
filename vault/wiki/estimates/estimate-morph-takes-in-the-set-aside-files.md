---
type: estimate
kind: QA
status: pending
target: "[[rule-morph]]"
purpose: Whether the setup Case of the first /hi shows what each file that /guppi:install set aside holds, lets the person keep or drop each part, puts a kept part into the page that writes its file or, where none does, into the file by a task, creates no page and deletes guppi-set-aside/
method: "by hand, after the session whose Work Mode builds the setup skill of rule-morph and its step in /hi: in a project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, with a tag prod-x.y.z in the history of HEAD, the plugin guppi installed from a local copy written by uv run --project .guppi guppi ship --allow-draft, /guppi:install typed, Claude Code reopened and /hi typed, one part of each set-aside file kept and one dropped in the setup Case; the transcript of that session, its ledger and the files its Work Mode writes read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-30/1713/ledger.md#case-932.2
sprint: plugin
created: 2026-10-30
tags: [session, harness, plugin]
---

## Criterion

When:
In a project where `/guppi:install`, as `rule-plugin-install` sets it, set aside files of the project under `guppi-set-aside/`, and whose `guppi.toml` does not mark the setup of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

Then:
The setup Case of `rule-morph` shows what each file under `guppi-set-aside/` holds, by its old path.
**＋** In that one setup Case, the person keeps or drops each part of each file, such as an instruction, a hook or a permission.
**＋** A kept part goes into the page that writes its file, such as `rule-claude-md` for an instruction of `CLAUDE.md`, and the render of the Work Mode of that session writes it into the file.
**＋** For a file that no page writes, such as `.gitattributes` or `.github/workflows/checks.yml`, a task of the setup Case writes the kept part into that file, and the Work Mode of the same session runs it.
**＋** A task of the setup Case deletes `guppi-set-aside/` in that Work Mode.
**－** A dropped part reaches no file of the project.
**－** The setup Case creates no page for a kept part.

## History

- 2026-10-30 created · [[decision-case-932.2]]
