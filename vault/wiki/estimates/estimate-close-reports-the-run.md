---
type: estimate
kind: QA
status: pending
target: "[[rule-close]]"
purpose: Whether the librarian gives its report back once at its close, as its last output, by its handback where it has the tool or as its last text, and report.md of the session folder holds that report and gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to the report, with no test result and no list of files
method: "by hand, after the librarian's run of a session whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close that gives the report back once as the last output: the agent reads report.md of the session folder of that run, as the commit of /handoff or /box holds it by git show, beside every output of the librarian, its texts and the message of each SubagentHandback call, read in its agent transcript under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line"
checked: 2026-11-01
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
**＋** The librarian gives the report once, as its last output: the `message` of its `SubagentHandback` call where it has that tool, else its last text, with no output after it.
**＋** The file gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags the run raised and the lint total.
**＋** The file gives each part that another step of `.claude/agents/librarian-guppi.md` sends to the report.
**－** The file holds no test result and no list of files.
**－** No limit of lines binds the file.

## Result

2026-11-01, Work reading of session 2038, git show 994ade11:vault/raw/2026-11-01/0141/report.md beside the handback of the librarian in ~/.claude/projects/c--PROJECTS-GUPPI/b91d8531-1bea-46ba-a54a-0282b108e453/subagents/agent-a4bd75adff6d794e7.jsonl, record 205: report.md equals the returned report byte for byte but its last newline, 62 lines; it gives pages created and updated per category, entries incomplete or failed (none), pages archived, flags, the lint total and each part the frame at ce0231ab sends to the report; no test result, no list of files; the frame held the libreport hook in settings.json and the Render of rule-close; the librarian's last plain text was one line before its commit, the report stood only in its handback

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
- 2026-10-31 deferred · [[decision-case-971]]
- 2026-11-01 defer by decision-case-971 superseded · [[decision-case-982.3]]
- 2026-11-01 updated: the defer of decision-case-971, archived as superseded, retired; the reading waits for its event · [[decision-case-982.3]]
- 2026-11-01 status: pending → passed · raw/2026-11-01/2038/ledger.md#L15
- 2026-11-02 updated: the Criterion replaced whole — the librarian gives the report once, as its last output, by its handback or its last text · [[decision-case-994]]
