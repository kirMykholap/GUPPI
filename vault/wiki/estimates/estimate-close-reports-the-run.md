---
type: estimate
kind: QA
status: pending
target: "[[rule-close]]"
purpose: Whether report.md of the session folder holds the report the librarian returned last at its close, and gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to the report, with no test result and no list of files
method: "by hand, after the librarian's run of a session that starts with the hook of rule-librarian-report-copy in .claude/settings.json and whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close that returns the report as text: the agent reads report.md of the session folder of that run, as the commit of /handoff or /box holds it by git show, beside the last output of the librarian read in its agent transcript under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line"
checked: 2026-10-31
origin: raw/2026-10-29/1930/ledger.md#case-903.2
sprint: plugin
created: 2026-10-29
tags: [harness, workflow, librarian]
---

## Criterion

When:
The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches, or that `/box` of `.claude/skills/box/SKILL.md` dispatches in a session that `/box` runs, reaches the close of `.claude/agents/librarian-guppi.md` and ends, and the hook of `rule-librarian-report-copy` fires.

Then:
`vault/raw/<date>/<hi HHMM>/report.md`, the folder of the `handoff.md` the dispatch names, holds the report that the librarian returned last.
**＋** The file gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags the run raised and the lint total.
**＋** The file gives each part that another step of `.claude/agents/librarian-guppi.md` sends to the report.
**－** The file holds no test result and no list of files.
**－** No limit of lines binds the file.

## Result

2026-10-31, /hi of session 0431, git show e71f98bc:.claude/agents/librarian-guppi.md, ls vault/raw/2026-10-31/0128/, git show --stat c7e796eb and git ls-files: the frame at the start of the librarian's run of session 0128 holds the Close step that writes report.md (line 129), and the run reached its commit c7e796eb; no report.md stands in vault/raw/2026-10-31/0128/, c7e796eb takes none, and git ls-files lists no report.md in the repository

## History

- 2026-10-29 created · [[decision-case-903.2]]
- 2026-10-30 status: pending → failed · raw/2026-10-29/2341/ledger.md#L3
- 2026-10-30 status: failed → passed · raw/2026-10-29/2341/ledger.md#L5
- 2026-10-30 renamed from `estimate-close-reports-in-twenty-lines` · [[decision-case-913]]
- 2026-10-30 updated: the Criterion replaced whole — the report gives each part its frame sends to it, no test result and no list of files, and has no limit of lines; renamed from estimate-close-reports-in-twenty-lines · [[decision-case-913]]
- 2026-10-31 status: pending → passed · raw/2026-10-30/2345/ledger.md#L3
- 2026-10-31 updated: the Criterion replaced whole — the report is written into report.md of the session folder and the agent reads that file · [[decision-case-944]]
- 2026-10-31 status: pending → failed · raw/2026-10-31/0431/ledger.md#L2
- 2026-10-31 updated: the Criterion replaced whole — the hook writes report.md from the report the librarian returns · [[decision-case-956.2]]
