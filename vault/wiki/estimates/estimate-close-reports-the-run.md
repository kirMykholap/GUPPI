---
type: estimate
kind: QA
status: passed
target: "[[rule-close]]"
purpose: Whether the librarian gives its report back once at its close, as its last output, by its handback where it has the tool or as its last text, and report.md of the session folder holds that report and gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to the report, with no test result and no list of files
method: "by hand, after the librarian's run of a session whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close that gives the report back once as the last output: the agent reads report.md of the session folder of that run, as the commit of /handoff or /box holds it by git show, beside every output of the librarian, its texts and the message of each SubagentHandback call, read in its agent transcript under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line"
checked: 2026-11-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, librarian]
core: true
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

2026-11-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
