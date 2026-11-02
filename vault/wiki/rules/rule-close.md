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
origin: raw/2026-09-10/ledger.md#case-36.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, git, librarian]
core: true
---

## Purpose

Prevents the librarian's writes from landing in the session's own commit, or from
ending without a commit at all. The Retro commit is the baseline. What the librarian
changed must be readable as one separate diff, six months on.

## Render

<!-- rule-close -->
Close. Run `uv run --project .guppi guppi check` and keep its output for the report. The report gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags you raised, the lint total, and each part that another step of this frame sends to the report. Nothing else: no test result and no list of files (as set in case 913). Commit the vault with the files the render wrote, by the Bash tool, since the command is written for a POSIX shell: `git add vault $(uv run --project .guppi guppi render --paths) && git commit -m "docs(vault): librarian, <date>"`, never `--amend`, never a path that neither `vault` nor that list names. After the commit, no file the render wrote stands modified or untracked. Then give the report back once, as your last output: as the message of your handback where you have the tool `SubagentHandback`, and as your last text where you have no such tool, since Claude Code gives that tool only in auto mode; write no text after it, since the hook copies your last output, a text after the handback included (as set in case 994). The hook of `rule-librarian-report-copy` copies that report into `report.md` in the session's folder, the folder of the `handoff.md` your dispatch names, and `/handoff` or `/box` commits it; write no `report.md` yourself (as set in case 956).
<!-- /rule-close -->

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.1
- 2026-09-10 estimate estimate-close-commits added · raw/2026-09-10/ledger.md#case-36.1
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: the commit takes the governed files the render wrote, beside vault/ (case 89.2) · [[decision-case-89.2]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
- 2026-09-28 updated: the commit takes guppi.toml, the settings file rendered at the root (case 482) · [[decision-case-482]]
- 2026-09-28 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-16 updated: the commit takes vault and each file that guppi render --paths prints, in place of four fixed paths · [[decision-case-857]]
- 2026-10-16 status: built → draft · cascade
- 2026-10-17 updated: the close command is run by the Bash tool · [[decision-case-866]]
- 2026-10-29 estimate estimate-close-reports-in-twenty-lines added · [[decision-case-903.2]]
- 2026-10-30 updated: the report gives each part another step of the frame sends to it, no test result and no list of files, and has no limit of lines · [[decision-case-913]]
- 2026-10-30 ref `estimate-close-reports-in-twenty-lines` → `estimate-close-reports-the-run` · [[decision-case-913]]
- 2026-10-31 updated: the librarian writes its report into report.md of the session folder before its commit and returns that text · [[decision-case-944]]
- 2026-10-31 updated: the librarian returns its report as text and writes no report.md; a hook copies the text into the file · [[decision-case-956.2]]
- 2026-11-01 status: draft → built · cascade
- 2026-11-02 updated: the librarian gives its report back once, as its last output: the handback where it has the tool, else its last text · [[decision-case-994]]
- 2026-11-02 status: built → draft · cascade
- 2026-11-02 status: draft → built · cascade
