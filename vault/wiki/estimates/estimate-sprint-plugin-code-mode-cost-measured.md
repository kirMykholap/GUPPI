---
type: estimate
kind: Research
status: passed
target: "[[entity-sprint-plugin]]"
purpose: What Code Mode of Claude Code saves or adds in calls, tokens and seconds of the main agent on one read-only task in a clone of the project, and whether it gives the same answer
method: "by hand, after the person's word that the two measured sessions in the clone C:/PROJECTS/guppi-codemode-trial ran: the output of uv run --project .guppi guppi agents over the transcript of each, in the folder of the clone under ~/.claude/projects/, and the list of links each session gave read against the Criterion, the numbers and the transcripts in the estimate line"
origin: raw/2026-11-27/0947/ledger.md#case-1079.1
sprint: plugin
created: 2026-11-27
tags: [sprint, harness]
once: true
---

## Criterion

When:
The person runs two sessions of `claude --permission-mode default` in a terminal in `C:/PROJECTS/guppi-codemode-trial`, the first without Code Mode and the second with `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE` set to `1` in its terminal, each on the same read-only prompt that lists the links of the Markdown files that point to missing local files.
**＋** The agent runs `uv run --project .guppi guppi agents` of `.guppi/guppi/agents.py` over the transcript of each session.

Then:
Determine how many calls, tokens and seconds of the main agent Code Mode saves or adds on that prompt.
**＋** Determine whether the two sessions give the same list of links.
**－** The variable stands only in the terminal of the second session, so no other session of `claude` starts in Code Mode.
**－** No page, rule or harness file of this repository changes for Code Mode in this session: a Case of a later session does, by the finding.

## Result

2026-11-27, after the person's word, uv run --project .guppi guppi agents over the two transcripts in ~/.claude/projects/C--PROJECTS-guppi-codemode-trial/, Claude Code 2.1.332: without Code Mode (0bb1cae1, no REPL call) calls 9, tokens 510430, tools 10, seconds 641; with Code Mode (248087da, 15 REPL calls) calls 2589, tokens 258586, tools 2588, seconds 1027 — Code Mode used about half the tokens and about 60% more seconds, and guppi agents counts each call made inside the code as a call (about 2576 Reads); both sessions gave the same 54 broken wikilinks, the same targets named in both answers; the two sessions ran at the same time (first prompts at 11:19:15 and 11:19:50 UTC), so the seconds hold that overlap and the permission prompts; the variable stood only in the second terminal

## History

- 2026-11-27 created · [[decision-case-1079.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/0947/ledger.md#L33
