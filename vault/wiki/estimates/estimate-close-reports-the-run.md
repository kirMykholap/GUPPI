---
type: estimate
kind: QA
status: pending
target: "[[rule-close]]"
purpose: Whether the librarian's report, as /handoff or /box shows it, gives the counts, the marks, the archived pages, the flags, the lint total and each part another step of its frame sends to it, with no test result and no list of files
method: "by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close with no limit of lines: the person's answer on whether the report that /handoff, or /box in a session that /box runs, showed after that run gave each part the Criterion names and no test result and no list of files, the exit code of guppi test that /box adds beside the report not counted as a part of it"
checked: 2026-10-30
origin: raw/2026-10-29/1930/ledger.md#case-903.2
sprint: plugin
created: 2026-10-29
tags: [harness, workflow, librarian]
---

## Criterion

When:
The librarian's run that `/handoff` of `.claude/skills/handoff/SKILL.md` dispatches ends, and `/handoff` shows its report to the person.
**＋** In a session that `/box` runs, `/box` of `.claude/skills/box/SKILL.md` dispatches that run and shows its report to the person instead.

Then:
The report gives the pages created and updated per category, the entries marked incomplete or failed, the pages archived, the flags the run raised and the lint total.
**＋** The report gives each part that another step of `.claude/agents/librarian-guppi.md` sends to the report.
**－** The report holds no test result and no list of files.
**－** No limit of lines binds the report.
**－** The exit code of `uv run --project .guppi guppi test` that `/box` shows beside the report is a line of `/box`, not a part of the report.

## Result

2026-10-30, at the /hi of session 2341, the person's reading of the report that /handoff showed after the librarian's run of session 1930, quoted by case-guppi from the last message of that session: it gives the counts (Created 24, Updated 23), the marks and flags (incomplete L11 of Case 905; stale defer of rule-clean-branch) and the lint total (guppi check exit 1, 11 lines), in 19 lines; the person: "да, я смотрел другой отчёт" — the failed reading of this session rested on another text

## History

- 2026-10-29 created · [[decision-case-903.2]]
- 2026-10-30 status: pending → failed · raw/2026-10-29/2341/ledger.md#L3
- 2026-10-30 status: failed → passed · raw/2026-10-29/2341/ledger.md#L5
- 2026-10-30 renamed from `estimate-close-reports-in-twenty-lines` · [[decision-case-913]]
- 2026-10-30 updated: the Criterion replaced whole — the report gives each part its frame sends to it, no test result and no list of files, and has no limit of lines; renamed from estimate-close-reports-in-twenty-lines · [[decision-case-913]]
