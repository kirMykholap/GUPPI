---
type: rule
kind: Leaf
purpose: Prevents the librarian's writes from landing in the session's own commit, or from ending without a commit at all
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: ["[[estimate-close-commits]]", "[[estimate-close-reports-the-run]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, git, librarian]
core: true
---

## Purpose

Prevents the librarian's writes from landing in the session's own commit, or from
ending without a commit at all. The Retro commit is the baseline. What the librarian
changed must be readable as one separate diff, six months on.

## Render

<!-- rule-close -->
Close. Run `uv run --project .guppi guppi check` and keep its output for the report. The report gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags you raised, the lint total, and each part that another step of this frame sends to the report. Nothing else: no test result and no list of files. Commit the vault with the files the render wrote, by the Bash tool, since the command is written for a POSIX shell: `git add vault $(uv run --project .guppi guppi render --paths) && git commit -m "docs(vault): librarian, <date>"`, never `--amend`, never a path that neither `vault` nor that list names. After the commit, no file the render wrote stands modified or untracked. Then give the report back once, as your last output: as the message of your handback where you have the tool `SubagentHandback`, and as your last text where you have no such tool, since Claude Code gives that tool only in auto mode; write no text after it, since the hook copies your last output, a text after the handback included. The hook of `rule-librarian-report-copy` copies that report into `report.md` in the session's folder, the folder of the `handoff.md` your dispatch names, and `/handoff` or `/box` commits it; write no `report.md` yourself.
<!-- /rule-close -->

## History

- 2026-11-03 shipped with GUPPI
